#!/usr/bin/env python3
"""Build a reproducible Mel Gibson acting + directing movie dataset from IMDb.

Large IMDb gzip files are streamed over HTTPS and never stored in the repo.
The analytical output keeps principal acting credits and feature-film directing
credits in one row-per-title dataset so the career lanes can be compared.
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
        except Exception as exc:
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


def normal(value):
    return "" if value in (None, "\\N") else value


def parse_characters(value):
    if value in ("", "\\N"):
        return []
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return [value]


def exact_person(person_name):
    matches = [
        row for row in stream_tsv(FILES["names"])
        if row["primaryName"].casefold() == person_name.casefold()
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
            f"Expected one exact match for {person_name!r}; candidates={candidates}"
        )
    return matches[0]


def directors_from_row(row):
    return [value for value in normal(row.get("directors")).split(",") if value]


def acquire(person_name):
    person = exact_person(person_name)

    principals = [
        row for row in stream_tsv(FILES["principals"])
        if row["nconst"] == person["nconst"]
    ]
    actor_rows = [
        row for row in principals
        if row["category"] in {"actor", "actress"}
    ]
    actor_ids = {row["tconst"] for row in actor_rows}

    crew_rows = []
    directed_ids = set()
    for row in stream_tsv(FILES["crew"]):
        row_directors = directors_from_row(row)
        is_directed_by_person = person["nconst"] in row_directors
        if row["tconst"] in actor_ids or is_directed_by_person:
            crew_rows.append(row)
        if is_directed_by_person:
            directed_ids.add(row["tconst"])

    career_ids = actor_ids | directed_ids

    basics = [
        row for row in stream_tsv(FILES["basics"])
        if row["tconst"] in career_ids
    ]
    ratings = [
        row for row in stream_tsv(FILES["ratings"])
        if row["tconst"] in career_ids
    ]

    director_ids = {
        director
        for row in crew_rows
        for director in directors_from_row(row)
    }
    director_names = [
        row for row in stream_tsv(FILES["names"])
        if row["nconst"] in director_ids
    ]

    return person, principals, actor_rows, directed_ids, basics, ratings, crew_rows, director_names


def write_csv(path, fieldnames, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_outputs(bundle, output_dir, min_votes):
    (
        person,
        principals,
        actor_rows,
        directed_ids,
        basics_rows,
        rating_rows,
        crew_rows,
        director_rows,
    ) = bundle

    basics = {row["tconst"]: row for row in basics_rows}
    ratings = {row["tconst"]: row for row in rating_rows}
    crew = {row["tconst"]: row for row in crew_rows}
    director_names = {row["nconst"]: row["primaryName"] for row in director_rows}

    actor_by_title = defaultdict(list)
    for row in actor_rows:
        actor_by_title[row["tconst"]].append(row)

    career_ids = set(actor_by_title) | set(directed_ids)
    joined = []
    audit = []

    for tconst in sorted(career_ids):
        title = basics.get(tconst)
        if title is None:
            audit.append({
                "tconst": tconst,
                "title": "",
                "title_type": "",
                "year": "",
                "rating": "",
                "votes": "",
                "acted": int(tconst in actor_by_title),
                "directed": int(tconst in directed_ids),
                "reason": "missing_title_join",
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

        acted = tconst in actor_by_title
        directed = tconst in directed_ids

        if reasons:
            audit.append({
                "tconst": tconst,
                "title": title["primaryTitle"],
                "title_type": title_type,
                "year": year,
                "rating": rating["averageRating"] if rating else "",
                "votes": rating["numVotes"] if rating else "",
                "acted": int(acted),
                "directed": int(directed),
                "reason": " | ".join(reasons),
            })
            continue

        characters = []
        principal_order = ""
        if acted:
            orders = []
            for row in actor_by_title[tconst]:
                orders.append(int(row["ordering"]))
                for character in parse_characters(row["characters"]):
                    if character not in characters:
                        characters.append(character)
            principal_order = min(orders)

        title_director_ids = directors_from_row(crew.get(tconst, {}))
        if acted and directed:
            career_lane = "acting + directing"
        elif directed:
            career_lane = "directing"
        else:
            career_lane = "acting"

        joined.append({
            "tconst": tconst,
            "title": title["primaryTitle"],
            "original_title": title["originalTitle"],
            "year": year,
            "runtime_minutes": normal(title["runtimeMinutes"]),
            "genres": normal(title["genres"]).replace(",", " | "),
            "average_rating": rating["averageRating"],
            "num_votes": rating["numVotes"],
            "acted": int(acted),
            "directed": int(directed),
            "career_lane": career_lane,
            "principal_order": principal_order,
            "directors": " | ".join(
                director_names.get(value, value) for value in title_director_ids
            ),
            "characters": " | ".join(characters),
        })

    joined.sort(key=lambda row: (int(row["year"]), row["title"]))
    audit.sort(key=lambda row: (row["tconst"], row["reason"]))

    data_fields = [
        "tconst", "title", "original_title", "year", "runtime_minutes", "genres",
        "average_rating", "num_votes", "acted", "directed", "career_lane",
        "principal_order", "directors", "characters",
    ]
    audit_fields = [
        "tconst", "title", "title_type", "year", "rating", "votes",
        "acted", "directed", "reason",
    ]

    write_csv(output_dir / "mel_gibson_imdb_career_movies.csv", data_fields, joined)
    write_csv(output_dir / "mel_gibson_imdb_exclusions.csv", audit_fields, audit)
    return joined, audit


def validation_report(bundle, joined, audit, min_votes):
    (
        person,
        principals,
        actor_rows,
        directed_ids,
        basics_rows,
        rating_rows,
        crew_rows,
        director_rows,
    ) = bundle

    actor_ids = {row["tconst"] for row in actor_rows}
    career_ids = actor_ids | set(directed_ids)
    basics_ids = {row["tconst"] for row in basics_rows}
    rating_ids = {row["tconst"] for row in rating_rows}
    crew_ids = {row["tconst"] for row in crew_rows}
    basics_by_id = {row["tconst"]: row for row in basics_rows}
    ratings_by_id = {row["tconst"]: row for row in rating_rows}

    movie_ids = {
        tconst for tconst in career_ids
        if tconst in basics_by_id and basics_by_id[tconst]["titleType"] == "movie"
    }
    released_movie_ids = {
        tconst for tconst in movie_ids
        if normal(basics_by_id[tconst]["startYear"])
    }
    rated_released_movie_ids = released_movie_ids & rating_ids
    vote_floor_ids = {
        tconst for tconst in rated_released_movie_ids
        if int(ratings_by_id[tconst]["numVotes"]) >= min_votes
    }

    return {
        "resolved_person": person,
        "minimum_votes_for_analysis": min_votes,
        "counts": {
            "all_person_principal_rows": len(principals),
            "principal_actor_rows": len(actor_rows),
            "distinct_principal_actor_titles": len(actor_ids),
            "distinct_directed_titles_all_types": len(directed_ids),
            "career_title_union": len(career_ids),
            "matched_title_basics": len(basics_ids & career_ids),
            "matched_ratings": len(rating_ids & career_ids),
            "matched_crew_rows": len(crew_ids & career_ids),
            "released_movie_titles": len(released_movie_ids),
            "rated_released_movie_titles": len(rated_released_movie_ids),
            "movies_meeting_vote_floor": len(vote_floor_ids),
            "analysis_rows": len(joined),
            "audit_rows": len(audit),
            "analysis_acting_rows": sum(row["acted"] == 1 for row in joined),
            "analysis_directing_rows": sum(row["directed"] == 1 for row in joined),
            "analysis_both_rows": sum(row["career_lane"] == "acting + directing" for row in joined),
            "analysis_missing_year": sum(not row["year"] for row in joined),
            "analysis_missing_runtime": sum(not row["runtime_minutes"] for row in joined),
            "analysis_missing_rating": sum(not row["average_rating"] for row in joined),
            "resolved_director_names": len(director_rows),
        },
        "coverage": {
            "title_basics_join_pct": round(
                100 * len(basics_ids & career_ids) / len(career_ids), 2
            ) if career_ids else None,
            "ratings_join_pct": round(
                100 * len(rating_ids & career_ids) / len(career_ids), 2
            ) if career_ids else None,
            "vote_floor_coverage_of_rated_released_movies_pct": round(
                100 * len(vote_floor_ids) / len(rated_released_movie_ids), 2
            ) if rated_released_movie_ids else None,
        },
        "duplicate_analysis_tconsts": len(joined) - len({row["tconst"] for row in joined}),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--person", default="Mel Gibson")
    parser.add_argument("--min-votes", type=int, default=1000)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "data",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    accessed_at = datetime.now(timezone.utc).isoformat()
    bundle = acquire(args.person)
    joined, audit = build_outputs(bundle, args.output_dir, args.min_votes)

    metadata = {
        "accessed_at_utc": accessed_at,
        "sources": {
            key: source_metadata(filename)
            for key, filename in FILES.items()
        },
        "validation": validation_report(bundle, joined, audit, args.min_votes),
        "scope_notes": [
            "Acting rows come from IMDb title.principals actor/actress credits, which are a principal-credit subset rather than a guaranteed complete filmography.",
            "Directing rows come from IMDb title.crew directors fields.",
            "The analytical set is restricted to titleType=movie, a release year, an IMDb rating, and the configured minimum vote floor.",
            "IMDb ratings describe titles, not Mel Gibson's individual acting or directing performance.",
            "All excluded, unrated, unreleased and non-movie career titles are preserved in the audit CSV.",
        ],
    }
    with (args.output_dir / "mel_gibson_imdb_source_metadata.json").open(
        "w", encoding="utf-8"
    ) as handle:
        json.dump(metadata, handle, indent=2)
        handle.write("\n")


if __name__ == "__main__":
    main()
