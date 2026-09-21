#!/usr/bin/env python3
"""Build a small actor-film dataset from IMDb's non-commercial TSV exports.

The default path streams the official gzip files and retains only matching rows.
Pass --staged-dir to assemble previously filtered TSVs without downloading them
again. Raw global IMDb files are never written into the repository.
"""

import argparse
import csv
import gzip
import io
import json
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


BASE_URL = "https://datasets.imdbws.com"
FILES = {
    "names": "name.basics.tsv.gz",
    "principals": "title.principals.tsv.gz",
    "basics": "title.basics.tsv.gz",
    "ratings": "title.ratings.tsv.gz",
    "crew": "title.crew.tsv.gz",
}


def stream_tsv(filename):
    response = urllib.request.urlopen(f"{BASE_URL}/{filename}", timeout=120)
    zipped = gzip.GzipFile(fileobj=response)
    text = io.TextIOWrapper(zipped, encoding="utf-8", newline="")
    yield from csv.DictReader(text, delimiter="\t")


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def source_metadata(filename):
    request = urllib.request.Request(f"{BASE_URL}/{filename}", method="HEAD")
    with urllib.request.urlopen(request, timeout=60) as response:
        return {
            "url": response.url,
            "run_date": response.headers.get("x-amz-meta-run-date"),
            "last_modified": response.headers.get("last-modified"),
            "content_length": int(response.headers.get("content-length", 0)),
            "etag": response.headers.get("etag"),
        }


def exact_person(actor_name, rows):
    matches = [row for row in rows if row["primaryName"].casefold() == actor_name.casefold()]
    if len(matches) != 1:
        candidates = [(row["nconst"], row["primaryName"]) for row in matches]
        raise ValueError(f"Expected one exact name match for {actor_name!r}; found {candidates}")
    return matches[0]


def normal(value):
    return "" if value == "\\N" else value


def parse_characters(value):
    if value in ("", "\\N"):
        return ""
    try:
        return " | ".join(json.loads(value))
    except json.JSONDecodeError:
        return value


def load_filtered(staged_dir, actor_name):
    name_rows = read_tsv(staged_dir / "taron_name.tsv")
    person = exact_person(actor_name, name_rows)
    return {
        "person": person,
        "principals": read_tsv(staged_dir / "taron_principals.tsv"),
        "basics": read_tsv(staged_dir / "taron_basics.tsv"),
        "ratings": read_tsv(staged_dir / "taron_actor_movies_ratings.tsv"),
        "crew": read_tsv(staged_dir / "taron_actor_movies_crew.tsv"),
        "director_names": read_tsv(staged_dir / "director_names.tsv"),
    }


def acquire(actor_name):
    person = exact_person(actor_name, stream_tsv(FILES["names"]))
    principals = [row for row in stream_tsv(FILES["principals"]) if row["nconst"] == person["nconst"]]
    credited_ids = {row["tconst"] for row in principals}
    basics = [row for row in stream_tsv(FILES["basics"]) if row["tconst"] in credited_ids]

    actor_ids = {row["tconst"] for row in principals if row["category"] in {"actor", "actress"}}
    movie_ids = {row["tconst"] for row in basics if row["tconst"] in actor_ids and row["titleType"] == "movie"}
    ratings = [row for row in stream_tsv(FILES["ratings"]) if row["tconst"] in movie_ids]
    crew = [row for row in stream_tsv(FILES["crew"]) if row["tconst"] in movie_ids]

    director_ids = {
        director
        for row in crew
        for director in normal(row["directors"]).split(",")
        if director
    }
    director_names = [row for row in stream_tsv(FILES["names"]) if row["nconst"] in director_ids]
    return {
        "person": person,
        "principals": principals,
        "basics": basics,
        "ratings": ratings,
        "crew": crew,
        "director_names": director_names,
    }


def write_csv(path, fieldnames, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_outputs(bundle, output_dir, min_votes):
    principal_groups = {}
    for row in bundle["principals"]:
        if row["category"] in {"actor", "actress"}:
            principal_groups.setdefault(row["tconst"], []).append(row)
    basics = {row["tconst"]: row for row in bundle["basics"]}
    ratings = {row["tconst"]: row for row in bundle["ratings"]}
    crew = {row["tconst"]: row for row in bundle["crew"]}
    names = {row["nconst"]: row["primaryName"] for row in bundle["director_names"]}

    joined = []
    excluded = []
    for tconst, principal_rows in principal_groups.items():
        principal_order = min(int(row["ordering"]) for row in principal_rows)
        characters = []
        for row in principal_rows:
            for character in parse_characters(row["characters"]).split(" | "):
                if character and character not in characters:
                    characters.append(character)
        title = basics.get(tconst)
        if title is None:
            excluded.append({"tconst": tconst, "title": "", "reason": "missing_title_metadata"})
            continue
        if title["titleType"] != "movie":
            excluded.append({"tconst": tconst, "title": title["primaryTitle"], "reason": f"title_type:{title['titleType']}"})
            continue

        rating = ratings.get(tconst)
        director_ids = normal(crew.get(tconst, {}).get("directors", ""))
        director_names = [names.get(item, item) for item in director_ids.split(",") if item]
        year = normal(title["startYear"])
        votes = int(rating["numVotes"]) if rating else None
        reasons = []
        if not year:
            reasons.append("missing_year")
        if not rating:
            reasons.append("missing_rating")
        elif votes < min_votes:
            reasons.append(f"votes_below_{min_votes}")

        joined.append(
            {
                "tconst": tconst,
                "title": title["primaryTitle"],
                "original_title": title["originalTitle"],
                "year": year,
                "runtime_minutes": normal(title["runtimeMinutes"]),
                "genres": normal(title["genres"]).replace(",", " | "),
                "rating": rating["averageRating"] if rating else "",
                "votes": rating["numVotes"] if rating else "",
                "principal_order": principal_order,
                "directors": " | ".join(director_names),
                "characters": " | ".join(characters),
                "analysis_eligible": "1" if not reasons else "0",
                "exclusion_reason": " | ".join(reasons),
            }
        )

    joined.sort(key=lambda row: (int(row["year"]) if row["year"] else 9999, row["title"]))
    for row in joined:
        if row["exclusion_reason"]:
            excluded.append({"tconst": row["tconst"], "title": row["title"], "reason": row["exclusion_reason"]})

    fields = [
        "tconst", "title", "original_title", "year", "runtime_minutes", "genres",
        "rating", "votes", "principal_order", "directors", "characters",
        "analysis_eligible", "exclusion_reason",
    ]
    write_csv(output_dir / "taron_egerton_imdb_principal_actor_movies.csv", fields, joined)
    write_csv(output_dir / "taron_egerton_imdb_exclusions.csv", ["tconst", "title", "reason"], excluded)
    return joined, excluded


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--actor", default="Taron Egerton")
    parser.add_argument("--min-votes", type=int, default=1000)
    parser.add_argument("--staged-dir", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent.parent / "data")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    bundle = load_filtered(args.staged_dir, args.actor) if args.staged_dir else acquire(args.actor)
    joined, excluded = build_outputs(bundle, args.output_dir, args.min_votes)
    actor_principals = [row for row in bundle["principals"] if row["category"] in {"actor", "actress"}]
    actor_title_counts = Counter(row["tconst"] for row in actor_principals)
    metadata = {
        "actor": bundle["person"],
        "accessed_at_utc": datetime.now(timezone.utc).isoformat(),
        "minimum_votes_for_analysis": args.min_votes,
        "counts": {
            "all_principal_credits": len(bundle["principals"]),
            "actor_or_actress_principal_rows": len(actor_principals),
            "distinct_actor_or_actress_titles": len(actor_title_counts),
            "titles_with_duplicate_principal_rows": sum(count > 1 for count in actor_title_counts.values()),
            "movie_records": len(joined),
            "analysis_eligible_movies": sum(row["analysis_eligible"] == "1" for row in joined),
            "excluded_records": len(excluded),
            "principal_categories": Counter(row["category"] for row in bundle["principals"]),
        },
        "sources": {key: source_metadata(filename) for key, filename in FILES.items()},
        "scope_note": "Principal actor/actress credits with IMDb titleType=movie. IMDb title ratings describe the title, not the actor's performance.",
    }
    with (args.output_dir / "taron_egerton_imdb_build_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2, default=dict)
        handle.write("\n")


if __name__ == "__main__":
    main()
