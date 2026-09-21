#!/usr/bin/env python3
"""Stream-filter IMDb's official exports and build the Simon Pegg movie dataset.

The complete global gzip files are read over HTTPS and are never saved in the
repository. Outputs are deliberately small, reproducible project artefacts.
"""

import argparse
import csv
import gzip
import io
import json
import time
import urllib.request
from collections import Counter, defaultdict
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


def open_url(url, method=None, attempts=3):
    error = None
    for attempt in range(1, attempts + 1):
        try:
            request = urllib.request.Request(url, method=method)
            return urllib.request.urlopen(request, timeout=180)
        except Exception as exc:  # network failures need a bounded retry
            error = exc
            if attempt < attempts:
                time.sleep(attempt * 2)
    raise RuntimeError(f"Failed after {attempts} attempts: {url}") from error


def stream_tsv(filename):
    response = open_url(f"{BASE_URL}/{filename}")
    zipped = gzip.GzipFile(fileobj=response)
    text = io.TextIOWrapper(zipped, encoding="utf-8", newline="")
    yield from csv.DictReader(text, delimiter="\t")


def source_metadata(filename):
    with open_url(f"{BASE_URL}/{filename}", method="HEAD") as response:
        return {
            "url": response.url,
            "upstream_run_date": response.headers.get("x-amz-meta-run-date"),
            "last_modified": response.headers.get("last-modified"),
            "content_length": int(response.headers.get("content-length", 0)),
            "etag": response.headers.get("etag"),
        }


def exact_person(actor_name):
    matches = [
        row for row in stream_tsv(FILES["names"])
        if row["primaryName"].casefold() == actor_name.casefold()
    ]
    if len(matches) != 1:
        candidates = [
            {
                "nconst": row["nconst"],
                "primaryName": row["primaryName"],
                "birthYear": row["birthYear"],
                "primaryProfession": row["primaryProfession"],
                "knownForTitles": row["knownForTitles"],
            }
            for row in matches
        ]
        raise ValueError(
            f"Expected one exact match for {actor_name!r}; candidates={candidates}"
        )
    return matches[0]


def normal(value):
    return "" if value in (None, "\\N") else value


def parse_characters(value):
    if value in ("", "\\N"):
        return []
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return [value]


def acquire(actor_name):
    person = exact_person(actor_name)
    principals = [
        row for row in stream_tsv(FILES["principals"])
        if row["nconst"] == person["nconst"]
    ]
    credited_ids = {row["tconst"] for row in principals}
    basics = [
        row for row in stream_tsv(FILES["basics"])
        if row["tconst"] in credited_ids
    ]
    actor_ids = {
        row["tconst"] for row in principals
        if row["category"] in {"actor", "actress"}
    }
    ratings = [
        row for row in stream_tsv(FILES["ratings"])
        if row["tconst"] in actor_ids
    ]
    crew = [
        row for row in stream_tsv(FILES["crew"])
        if row["tconst"] in actor_ids
    ]
    director_ids = {
        director
        for row in crew
        for director in normal(row["directors"]).split(",")
        if director
    }
    director_names = [
        row for row in stream_tsv(FILES["names"])
        if row["nconst"] in director_ids
    ]
    return person, principals, basics, ratings, crew, director_names


def write_csv(path, fieldnames, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_outputs(bundle, output_dir, min_votes):
    person, principals, basics_rows, rating_rows, crew_rows, director_rows = bundle
    basics = {row["tconst"]: row for row in basics_rows}
    ratings = {row["tconst"]: row for row in rating_rows}
    crew = {row["tconst"]: row for row in crew_rows}
    director_names = {row["nconst"]: row["primaryName"] for row in director_rows}
    actor_principals = defaultdict(list)
    audit = []

    for row in principals:
        if row["category"] in {"actor", "actress"}:
            actor_principals[row["tconst"]].append(row)
        else:
            title = basics.get(row["tconst"], {})
            audit.append({
                "tconst": row["tconst"],
                "title": normal(title.get("primaryTitle")),
                "title_type": normal(title.get("titleType")),
                "category": row["category"],
                "year": normal(title.get("startYear")),
                "rating": "",
                "votes": "",
                "reason": f"principal_category:{row['category']}",
            })

    joined = []
    for tconst, principal_rows in actor_principals.items():
        title = basics.get(tconst)
        if title is None:
            audit.append({
                "tconst": tconst, "title": "", "title_type": "", "category": "actor",
                "year": "", "rating": "", "votes": "", "reason": "missing_title_join",
            })
            continue
        rating = ratings.get(tconst)
        year = normal(title["startYear"])
        title_type = title["titleType"]
        votes = int(rating["numVotes"]) if rating else None
        reasons = []
        if title_type != "movie":
            reasons.append(f"title_type:{title_type}")
        if not year:
            reasons.append("missing_year_or_unreleased")
        if not rating:
            reasons.append("missing_rating")
        elif votes < min_votes:
            reasons.append(f"votes_below_{min_votes}")

        if reasons:
            audit.append({
                "tconst": tconst,
                "title": title["primaryTitle"],
                "title_type": title_type,
                "category": "actor",
                "year": year,
                "rating": rating["averageRating"] if rating else "",
                "votes": rating["numVotes"] if rating else "",
                "reason": " | ".join(reasons),
            })
            continue

        characters = []
        for row in principal_rows:
            for character in parse_characters(row["characters"]):
                if character not in characters:
                    characters.append(character)
        director_ids = [
            value for value in normal(crew.get(tconst, {}).get("directors")).split(",")
            if value
        ]
        joined.append({
            "tconst": tconst,
            "title": title["primaryTitle"],
            "original_title": title["originalTitle"],
            "year": year,
            "runtime_minutes": normal(title["runtimeMinutes"]),
            "genres": normal(title["genres"]).replace(",", " | "),
            "average_rating": rating["averageRating"],
            "num_votes": rating["numVotes"],
            "principal_order": min(int(row["ordering"]) for row in principal_rows),
            "director_nconsts": " | ".join(director_ids),
            "directors": " | ".join(director_names.get(value, value) for value in director_ids),
            "characters": " | ".join(characters),
        })

    joined.sort(key=lambda row: (int(row["year"]), row["title"]))
    audit.sort(key=lambda row: (row["tconst"], row["reason"]))
    data_fields = [
        "tconst", "title", "original_title", "year", "runtime_minutes", "genres",
        "average_rating", "num_votes", "principal_order", "director_nconsts",
        "directors", "characters",
    ]
    audit_fields = [
        "tconst", "title", "title_type", "category", "year", "rating", "votes", "reason"
    ]
    write_csv(output_dir / "simon_pegg_imdb_principal_actor_movies.csv", data_fields, joined)
    write_csv(output_dir / "simon_pegg_imdb_exclusions.csv", audit_fields, audit)
    return joined, audit


def validation_report(bundle, joined, audit, min_votes):
    person, principals, basics, ratings, crew, director_rows = bundle
    actor_rows = [row for row in principals if row["category"] in {"actor", "actress"}]
    actor_ids = {row["tconst"] for row in actor_rows}
    basics_ids = {row["tconst"] for row in basics}
    rating_ids = {row["tconst"] for row in ratings}
    crew_ids = {row["tconst"] for row in crew}
    basics_by_id = {row["tconst"]: row for row in basics}
    ratings_by_id = {row["tconst"]: row for row in ratings}
    movie_ids = {
        tconst for tconst in actor_ids
        if basics_by_id[tconst]["titleType"] == "movie"
    }
    released_movie_ids = {
        tconst for tconst in movie_ids
        if normal(basics_by_id[tconst]["startYear"])
    }
    rated_released_movie_ids = released_movie_ids & rating_ids
    vote_floor_movie_ids = {
        tconst for tconst in rated_released_movie_ids
        if int(ratings_by_id[tconst]["numVotes"]) >= min_votes
    }
    requested_director_ids = {
        value
        for row in crew
        for value in normal(row["directors"]).split(",")
        if value
    }
    resolved_director_ids = {row["nconst"] for row in director_rows}
    title_counts = Counter(row["tconst"] for row in actor_rows)
    return {
        "resolved_person": person,
        "minimum_votes_for_analysis": min_votes,
        "counts": {
            "all_principal_rows": len(principals),
            "principal_category_counts": dict(Counter(row["category"] for row in principals)),
            "actor_or_actress_principal_rows": len(actor_rows),
            "distinct_actor_or_actress_tconsts": len(actor_ids),
            "duplicate_actor_principal_tconsts": sum(count > 1 for count in title_counts.values()),
            "matched_title_basics_rows": len(basics_ids & actor_ids),
            "matched_rating_rows": len(rating_ids & actor_ids),
            "matched_crew_rows": len(crew_ids & actor_ids),
            "principal_actor_title_type_counts": dict(Counter(
                basics_by_id[tconst]["titleType"] for tconst in actor_ids
            )),
            "principal_actor_movie_titles": len(movie_ids),
            "released_principal_actor_movies": len(released_movie_ids),
            "rated_released_principal_actor_movies": len(rated_released_movie_ids),
            "movies_meeting_vote_floor": len(vote_floor_movie_ids),
            "requested_director_ids": len(requested_director_ids),
            "resolved_director_names": len(resolved_director_ids),
            "unresolved_director_ids": sorted(requested_director_ids - resolved_director_ids),
            "analysis_rows": len(joined),
            "audit_rows": len(audit),
            "analysis_missing_year": sum(not row["year"] for row in joined),
            "analysis_missing_runtime": sum(not row["runtime_minutes"] for row in joined),
            "analysis_missing_rating": sum(not row["average_rating"] for row in joined),
        },
        "coverage": {
            "title_basics_join_pct": round(100 * len(basics_ids & actor_ids) / len(actor_ids), 2),
            "ratings_join_pct": round(100 * len(rating_ids & actor_ids) / len(actor_ids), 2),
            "crew_join_pct": round(100 * len(crew_ids & actor_ids) / len(actor_ids), 2),
            "rated_coverage_of_released_movies_pct": round(
                100 * len(rated_released_movie_ids) / len(released_movie_ids), 2
            ),
            "vote_floor_coverage_of_rated_released_movies_pct": round(
                100 * len(vote_floor_movie_ids) / len(rated_released_movie_ids), 2
            ),
            "analysis_coverage_of_all_actor_titles_pct": round(
                100 * len(joined) / len(actor_ids), 2
            ),
        },
        "duplicate_analysis_tconsts": len(joined) - len({row["tconst"] for row in joined}),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--actor", default="Simon Pegg")
    parser.add_argument("--min-votes", type=int, default=1000)
    parser.add_argument(
        "--output-dir", type=Path,
        default=Path(__file__).resolve().parent.parent / "data",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    accessed_at = datetime.now(timezone.utc).isoformat()
    bundle = acquire(args.actor)
    joined, audit = build_outputs(bundle, args.output_dir, args.min_votes)
    metadata = {
        "accessed_at_utc": accessed_at,
        "sources": {key: source_metadata(filename) for key, filename in FILES.items()},
        "validation": validation_report(bundle, joined, audit, args.min_votes),
        "scope_notes": [
            "The analytical data contains principal actor/actress credits with titleType=movie, a release year, an IMDb rating, and at least 1,000 votes.",
            "IMDb title.principals is a principal-credit subset, not a guaranteed complete filmography.",
            "IMDb ratings describe titles, not Simon Pegg's individual performance or critical acclaim.",
            "IMDb title.akas and title.episode were not used because regional titles and television episodes are outside scope.",
        ],
    }
    with (args.output_dir / "simon_pegg_imdb_source_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)
        handle.write("\n")


if __name__ == "__main__":
    main()
