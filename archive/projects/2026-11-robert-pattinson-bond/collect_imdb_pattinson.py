#!/usr/bin/env python3
"""Stream IMDb official non-commercial TSV.gz sources; never store their global archives.

Scope: Robert Pattinson's IMDb principal acting movie credits and their overlap
with the five Daniel Craig-era Bond films. This is *principal* cast, not full cast.
Source: https://developer.imdb.com/non-commercial-datasets/
"""
from __future__ import annotations

import argparse
import csv
import gzip
import io
import json
import sys
from collections import defaultdict
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

ACTOR_NCONST = "nm1500155"
ROOT = "https://datasets.imdbws.com"
CRAIG_BOND = {
    "tt0381061": ("Casino Royale", 2006),
    "tt0830515": ("Quantum of Solace", 2008),
    "tt1074638": ("Skyfall", 2012),
    "tt2379713": ("Spectre", 2015),
    "tt2382320": ("No Time to Die", 2021),
}
# These two 2026 theatrical releases are independently confirmed by Amazon MGM
# (16 Nov 2026): https://www.aboutamazon.com/news/entertainment/james-bond-robert-pattinson-cast-amazon-mgm-film
AUDITED_2026 = {"tt33764258": "The Odyssey", "tt33071426": "The Drama"}
COLUMNS = {
    "filmography.csv": ["tconst", "title", "year", "genres", "runtime_minutes",
                        "character", "rating", "num_votes", "release_status",
                        "directors", "imdb_url"],
    "cast_edges.csv": ["tconst", "title", "year", "person_nconst", "person", "character"],
    "director_edges.csv": ["tconst", "title", "year", "person_nconst", "person"],
    "bond_overlap.csv": ["person_nconst", "person", "pattinson_tconst", "pattinson_title",
                         "pattinson_year", "bond_tconst", "bond_title", "bond_year"],
    "collaborators.csv": ["person_nconst", "person", "shared_movie_count"],
}

def clean(value):
    return "" if value is None or value == r"\N" else value

def number(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

@contextmanager
def imdb_rows(session: requests.Session, section: str):
    url = f"{ROOT}/{section}.tsv.gz"
    print(f"Streaming {url}", file=sys.stderr, flush=True)
    with session.get(url, stream=True, timeout=(35, 240)) as response:
        response.raise_for_status()
        response.raw.decode_content = False
        with gzip.GzipFile(fileobj=response.raw) as compressed:
            with io.TextIOWrapper(compressed, encoding="utf-8", newline="", errors="replace") as stream:
                yield csv.DictReader(stream, delimiter="\t")

def save_csv(destination: Path, name: str, rows: list[dict]):
    with (destination / name).open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=COLUMNS[name], extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {name}: {len(rows)} rows", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--as-of", default="2026-11-18")
    args = parser.parse_args()
    cutoff_year = int(args.as_of[:4])
    args.out.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": "coffeetableviz-pattinson-non-commercial-research/1.0"})
    retries = Retry(total=3, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))

    # Pass 1: identify Pattinson's principal acting credits and Craig-era Bond cast.
    pattinson_credits = {}
    bond_cast = defaultdict(list)
    with imdb_rows(session, "title.principals") as source:
        for row in source:
            tid, nid = row["tconst"], row["nconst"]
            if tid in CRAIG_BOND and row["category"] in ("actor", "actress"):
                bond_cast[nid].append(tid)
            if nid == ACTOR_NCONST and row["category"] in ("actor", "actress"):
                pattinson_credits[tid] = clean(row.get("characters"))
    if not pattinson_credits:
        raise RuntimeError("No Pattinson principal acting credits; check IMDb nconst and source")

    films = {}
    with imdb_rows(session, "title.basics") as source:
        for row in source:
            tid = row["tconst"]
            if tid not in pattinson_credits or row["titleType"] != "movie" or row["isAdult"] != "0":
                continue
            year = number(row["startYear"])
            if year is not None and year > cutoff_year:
                continue
            release_status = (
                "year_unknown_review" if year is None
                else "released_pre_2026" if year < 2026
                else "released_2026_verified" if (
                    tid in AUDITED_2026 and row["primaryTitle"] == AUDITED_2026[tid]
                ) else "2026_release_check"
            )
            films[tid] = {
                "tconst": tid, "title": row["primaryTitle"], "year": year or "",
                "genres": clean(row["genres"]), "runtime_minutes": clean(row["runtimeMinutes"]),
                "character": pattinson_credits[tid], "rating": "", "num_votes": "",
                "release_status": release_status, "directors": "",
                "imdb_url": f"https://www.imdb.com/title/{tid}/"
            }
    if not films:
        raise RuntimeError("No titleType=movie Pattinson films from title.basics")

    with imdb_rows(session, "title.ratings") as source:
        for row in source:
            if row["tconst"] in films:
                films[row["tconst"]]["rating"] = clean(row["averageRating"])
                films[row["tconst"]]["num_votes"] = clean(row["numVotes"])

    # Pass 2: selected principal cast for his movies only.
    raw_edges = []
    needed_people = {ACTOR_NCONST} | set(bond_cast)
    with imdb_rows(session, "title.principals") as source:
        for row in source:
            if row["tconst"] in films and row["category"] in ("actor", "actress"):
                nid = row["nconst"]
                if nid != ACTOR_NCONST:
                    raw_edges.append({
                        "tconst": row["tconst"], "person_nconst": nid,
                        "character": clean(row.get("characters"))
                    })
                    needed_people.add(nid)

    raw_directors = []
    with imdb_rows(session, "title.crew") as source:
        for row in source:
            if row["tconst"] in films:
                for nid in clean(row.get("directors")).split(","):
                    if nid:
                        raw_directors.append((row["tconst"], nid))
                        needed_people.add(nid)

    people = {}
    with imdb_rows(session, "name.basics") as source:
        for row in source:
            if row["nconst"] in needed_people:
                people[row["nconst"]] = row["primaryName"]
    if people.get(ACTOR_NCONST) != "Robert Pattinson":
        raise RuntimeError(f"Identity verification failed: {people.get(ACTOR_NCONST)!r}")

    directors = defaultdict(list)
    director_rows = []
    for tid, nid in raw_directors:
        person = people.get(nid, nid)
        directors[tid].append(person)
        director_rows.append({
            "tconst": tid, "title": films[tid]["title"], "year": films[tid]["year"],
            "person_nconst": nid, "person": person
        })

    for tid, film in films.items():
        film["directors"] = "; ".join(directors.get(tid, []))
    film_rows = sorted(films.values(), key=lambda f: (f["year"] or 9999, f["title"], f["tconst"]))

    cast_rows = []
    overlap_rows = []
    cofilms = defaultdict(set)
    for edge in raw_edges:
        tid, nid = edge["tconst"], edge["person_nconst"]
        film = films[tid]
        person = people.get(nid, nid)
        cast_rows.append({
            "tconst": tid, "title": film["title"], "year": film["year"],
            "person_nconst": nid, "person": person, "character": edge["character"]
        })
        cofilms[nid].add(tid)
        for bid in bond_cast.get(nid, []):
            bond_title, bond_year = CRAIG_BOND[bid]
            overlap_rows.append({
                "person_nconst": nid, "person": person,
                "pattinson_tconst": tid, "pattinson_title": film["title"],
                "pattinson_year": film["year"],
                "bond_tconst": bid, "bond_title": bond_title, "bond_year": bond_year
            })
    cast_rows.sort(key=lambda f: (f["year"] or 9999, f["title"], f["person"]))
    overlap_rows = list({(r["person_nconst"], r["pattinson_tconst"], r["bond_tconst"]): r
                         for r in overlap_rows}.values())
    overlap_rows.sort(key=lambda r: (r["person"], r["pattinson_year"] or 9999, r["bond_year"]))
    collaborators = sorted([
        {"person_nconst": nid, "person": people.get(nid, nid),
         "shared_movie_count": len(titles)}
        for nid, titles in cofilms.items()
    ], key=lambda r: (-r["shared_movie_count"], r["person"]))

    for filename, rows in [
        ("filmography.csv", film_rows), ("cast_edges.csv", cast_rows),
        ("director_edges.csv", director_rows), ("bond_overlap.csv", overlap_rows),
        ("collaborators.csv", collaborators),
    ]:
        save_csv(args.out, filename, rows)

    (args.out / "metadata.json").write_text(json.dumps({
        "source": "https://developer.imdb.com/non-commercial-datasets/",
        "actor_name": people[ACTOR_NCONST], "actor_nconst": ACTOR_NCONST,
        "editorial_as_of": args.as_of, "collected_utc": datetime.now(timezone.utc).isoformat(),
        "counts": {
            "principal_acting_credits_all_title_types": len(pattinson_credits),
            "movie_rows": len(film_rows),
            "movies_with_imdb_rating": sum(bool(r["rating"]) for r in film_rows),
            "movie_cast_edges": len(cast_rows), "craig_era_bond_overlap_rows": len(overlap_rows)
        },
        "important_limits": [
            "Only top principal credits, not an exhaustive cast or all filmography",
            "Only the five Craig-era Bond films, not all Bond instalments",
            "2026 films with unverified release dates must not enter ratings charts",
            "IMDb rating is a film rating, not an assessment of Pattinson's performance",
            "IMDb weighted averages cannot be recomputed from title summary counts",
            "IMDb non-commercial licensing must be assessed before public redistribution",
            "Producers not in title.crew; separately researched producer links required"
        ]
    }, indent=2), encoding="utf-8")
    print(f"IMDb collection complete: {len(film_rows)} films, {len(overlap_rows)} Bond links")

if __name__ == "__main__":
    main()
