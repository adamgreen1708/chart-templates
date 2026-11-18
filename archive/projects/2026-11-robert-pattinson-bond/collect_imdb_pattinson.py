#!/usr/bin/env python3
"""Stream IMDb official non-commercial TSV.gz sources; never store their global archives.

Scope: Robert Pattinson's IMDb principal acting movie credits and their overlap
with every official Eon James Bond film, plus two separately marked non-Eon
cinema films. These data only cover IMDb's top-listed principal cast.
Source: https://developer.imdb.com/non-commercial-datasets/
"""
from __future__ import annotations

import argparse
import csv
import gzip
import io
import json
import re
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
# Historical theatrical film register. Cross-check against IMDb title.basics at
# execution time: no silent skips or hand-entered ratings/cast members.
# Official catalogue: https://www.007.com/the-films/
# Eon: 25 films (1962-2021), six actors. Two non-Eon films are separate.
# Fields: IMDb tconst -> (film title, IMDb release year, series, Bond actor).
BOND_FILMS = {
    "tt0055928": ("Dr. No", 1962, "eon", "Sean Connery"),
    "tt0057076": ("From Russia with Love", 1963, "eon", "Sean Connery"),
    "tt0058150": ("Goldfinger", 1964, "eon", "Sean Connery"),
    "tt0059800": ("Thunderball", 1965, "eon", "Sean Connery"),
    "tt0062512": ("You Only Live Twice", 1967, "eon", "Sean Connery"),
    "tt0064757": ("On Her Majesty's Secret Service", 1969, "eon", "George Lazenby"),
    "tt0066995": ("Diamonds Are Forever", 1971, "eon", "Sean Connery"),
    "tt0070328": ("Live and Let Die", 1973, "eon", "Roger Moore"),
    "tt0071807": ("The Man with the Golden Gun", 1974, "eon", "Roger Moore"),
    "tt0076752": ("The Spy Who Loved Me", 1977, "eon", "Roger Moore"),
    "tt0079574": ("Moonraker", 1979, "eon", "Roger Moore"),
    "tt0082398": ("For Your Eyes Only", 1981, "eon", "Roger Moore"),
    "tt0086034": ("Octopussy", 1983, "eon", "Roger Moore"),
    "tt0090264": ("A View to a Kill", 1985, "eon", "Roger Moore"),
    "tt0093428": ("The Living Daylights", 1987, "eon", "Timothy Dalton"),
    "tt0097742": ("Licence to Kill", 1989, "eon", "Timothy Dalton"),
    "tt0113189": ("GoldenEye", 1995, "eon", "Pierce Brosnan"),
    "tt0120347": ("Tomorrow Never Dies", 1997, "eon", "Pierce Brosnan"),
    "tt0143145": ("The World Is Not Enough", 1999, "eon", "Pierce Brosnan"),
    "tt0246460": ("Die Another Day", 2002, "eon", "Pierce Brosnan"),
    "tt0381061": ("Casino Royale", 2006, "eon", "Daniel Craig"),
    "tt0830515": ("Quantum of Solace", 2008, "eon", "Daniel Craig"),
    "tt1074638": ("Skyfall", 2012, "eon", "Daniel Craig"),
    "tt2379713": ("Spectre", 2015, "eon", "Daniel Craig"),
    "tt2382320": ("No Time to Die", 2021, "eon", "Daniel Craig"),
    "tt0061452": ("Casino Royale", 1967, "non_eon", "David Niven"),
    "tt0086006": ("Never Say Never Again", 1983, "non_eon", "Sean Connery"),
}

# The register covers theatrical features, not the 1954 TV Casino Royale.
assert len(BOND_FILMS) == 27
assert sum(x[2] == "eon" for x in BOND_FILMS.values()) == 25
assert sum(x[2] == "non_eon" for x in BOND_FILMS.values()) == 2

def normalise_title(title):
    return re.sub(r"[^a-z0-9]", "", title.casefold())
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
                         "pattinson_year", "bond_tconst", "bond_title", "bond_year",
                         "bond_series", "bond_actor"],
    "bond_films.csv": ["bond_tconst", "bond_title", "bond_year", "bond_series",
                       "bond_actor", "principal_cast_count", "imdb_url"],
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

    # One streaming pass over the largest IMDb file. Its rows are grouped by
    # tconst; keep only a single title's principal actors in memory at a time.
    # This avoids downloading/parsing the enormous title.principals archive twice.
    pattinson_credits = {}
    bond_cast = defaultdict(list)
    all_pattinson_cast_edges = []

    def flush_principal_title(tid, acting_people):
        if tid is None:
            return
        if tid in BOND_FILMS:
            for nid, _character in acting_people:
                bond_cast[nid].append(tid)
        pattinson_rows = [character for nid, character in acting_people
                          if nid == ACTOR_NCONST]
        if pattinson_rows:
            pattinson_credits[tid] = pattinson_rows[0]
            for nid, character in acting_people:
                if nid != ACTOR_NCONST:
                    all_pattinson_cast_edges.append({
                        "tconst": tid, "person_nconst": nid,
                        "character": character
                    })

    with imdb_rows(session, "title.principals") as source:
        current_tid = None
        acting_people = []
        for row in source:
            tid = row["tconst"]
            if tid != current_tid:
                if current_tid is not None and tid < current_tid:
                    raise RuntimeError(
                        "IMDb title.principals no longer sorted by tconst: "
                        "cannot safely group principal casts in one pass"
                    )
                flush_principal_title(current_tid, acting_people)
                current_tid = tid
                acting_people = []
            if row["category"] in ("actor", "actress"):
                acting_people.append(
                    (row["nconst"], clean(row.get("characters")))
                )
        flush_principal_title(current_tid, acting_people)
    if not pattinson_credits:
        raise RuntimeError("No Pattinson principal acting credits; check IMDb nconst and source")

    films = {}
    observed_bond = set()
    with imdb_rows(session, "title.basics") as source:
        for row in source:
            tid = row["tconst"]
            if tid in BOND_FILMS:
                expected_title, expected_year, _series, _actor = BOND_FILMS[tid]
                if (row["titleType"] != "movie" or number(row["startYear"]) != expected_year
                    or normalise_title(row["primaryTitle"]) != normalise_title(expected_title)):
                    raise RuntimeError(
                        f"Bond register mismatch: {tid} expected {expected_title} ({expected_year}); "
                        f"IMDb lists {row['primaryTitle']} ({row['startYear']})"
                    )
                observed_bond.add(tid)
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
    if observed_bond != set(BOND_FILMS):
        missing = sorted(set(BOND_FILMS) - observed_bond)
        raise RuntimeError(f"IMDb Bond movie register incomplete: {missing}")
    if not films:
        raise RuntimeError("No titleType=movie Pattinson films from title.basics")

    with imdb_rows(session, "title.ratings") as source:
        for row in source:
            if row["tconst"] in films:
                films[row["tconst"]]["rating"] = clean(row["averageRating"])
                films[row["tconst"]]["num_votes"] = clean(row["numVotes"])

    # Keep the acting co-stars only from Pattinson's eligible movie titles.
    # Other title types are discarded before fetching colleague names.
    raw_edges = [
        edge for edge in all_pattinson_cast_edges
        if edge["tconst"] in films
    ]
    needed_people = {ACTOR_NCONST} | set(bond_cast)
    needed_people.update(edge["person_nconst"] for edge in raw_edges)

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
            bond_title, bond_year, bond_series, bond_actor = BOND_FILMS[bid]
            overlap_rows.append({
                "person_nconst": nid, "person": person,
                "pattinson_tconst": tid, "pattinson_title": film["title"],
                "pattinson_year": film["year"],
                "bond_tconst": bid, "bond_title": bond_title, "bond_year": bond_year,
                "bond_series": bond_series, "bond_actor": bond_actor
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

    bond_rows = [
        {"bond_tconst": tid, "bond_title": title, "bond_year": year,
         "bond_series": series, "bond_actor": actor,
         "principal_cast_count": sum(tid in bids for bids in bond_cast.values()),
         "imdb_url": f"https://www.imdb.com/title/{tid}/"}
        for tid, (title, year, series, actor) in BOND_FILMS.items()
    ]
    bond_rows.sort(key=lambda r: (r["bond_year"], r["bond_series"], r["bond_title"]))

    for filename, rows in [
        ("bond_films.csv", bond_rows), ("filmography.csv", film_rows), ("cast_edges.csv", cast_rows),
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
            "movie_cast_edges": len(cast_rows),
            "official_eon_bond_films": sum(r["bond_series"] == "eon" for r in bond_rows),
            "supplementary_non_eon_bond_films": sum(r["bond_series"] == "non_eon" for r in bond_rows),
            "bond_films_with_principal_cast": sum(r["principal_cast_count"] > 0 for r in bond_rows),
            "all_bond_overlap_rows": len(overlap_rows),
            "eon_bond_overlap_rows": sum(r["bond_series"] == "eon" for r in overlap_rows),
            "non_eon_bond_overlap_rows": sum(r["bond_series"] == "non_eon" for r in overlap_rows)
        },
        "important_limits": [
            "Only top principal credits, not an exhaustive cast or all filmography",
            "Coverage: all 25 Eon Bond films and two separately flagged non-Eon theatrical films",
            "The 1954 Casino Royale teleplay is outside theatrical movie scope",
            "Missing principal cast in a title does not prove there were no real-world crossovers",
            "2026 films with unverified release dates must not enter ratings charts",
            "IMDb rating is a film rating, not an assessment of Pattinson's performance",
            "IMDb weighted averages cannot be recomputed from title summary counts",
            "IMDb non-commercial licensing must be assessed before public redistribution",
            "Producers not in title.crew; separately researched producer links required"
        ]
    }, indent=2), encoding="utf-8")
    print(f"IMDb collection complete: {len(film_rows)} Pattinson films, 25 official + 2 independent Bond films, {len(overlap_rows)} potential Bond links")

if __name__ == "__main__":
    main()
