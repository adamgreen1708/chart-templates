#!/usr/bin/env python3
"""Validate live IMDb extraction; build *data-derived* chart research files.

No sample numbers, invented columns or hard-coded ratings are permitted.
Charts are not produced until this validation and editorial review pass.
"""
import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path

ACCEPTED_RELEASE = {"released_pre_2026", "released_2026_verified"}
REQUIRED = {"tconst", "title", "year", "rating", "num_votes", "release_status"}

def load_csv(path):
    if not path.is_file():
        raise ValueError(f"Missing source output: {path}")
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def write_csv(path, rows, fieldnames):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    args = parser.parse_args()
    root = args.data
    films = load_csv(root / "filmography.csv")
    bond_films = load_csv(root / "bond_films.csv")
    overlap = load_csv(root / "bond_overlap.csv")
    cast = load_csv(root / "cast_edges.csv")
    directors = load_csv(root / "director_edges.csv")
    if not films:
        raise ValueError("Empty filmography: no IMDb dataset ready")
    # The Bond catalogue must be exhaustive even when zero shared credits are found.
    bond_ids = [r["bond_tconst"] for r in bond_films]
    if len(bond_ids) != 27 or len(set(bond_ids)) != 27:
        raise ValueError(f"Expected 27 unique Bond feature IDs, found {len(bond_ids)}")
    bond_series = Counter(r["bond_series"] for r in bond_films)
    if bond_series != {"eon": 25, "non_eon": 2}:
        raise ValueError(f"Bond film type mismatch: {dict(bond_series)}")
    if {r["bond_actor"] for r in bond_films if r["bond_series"] == "eon"} != {
        "Sean Connery", "George Lazenby", "Roger Moore",
        "Timothy Dalton", "Pierce Brosnan", "Daniel Craig"
    }:
        raise ValueError("Official Bond era actor coverage incomplete")
    if any(int(row["principal_cast_count"]) < 1 for row in bond_films):
        raise ValueError("One or more Bond films lacks any IMDb principal acting credits")
    bond_by_id = {r["bond_tconst"]: r for r in bond_films}
    if not REQUIRED.issubset(films[0]):
        raise ValueError(f"Missing columns: {sorted(REQUIRED - set(films[0]))}")

    ids = [r["tconst"] for r in films]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate film tconst values")
    allowed_ids = set(ids)

    chart_rows = []
    excluded_status = Counter()
    missing_rating = 0
    for f in films:
        if f["release_status"] not in ACCEPTED_RELEASE:
            excluded_status[f["release_status"]] += 1
            continue
        if not f["rating"] or not f["num_votes"]:
            missing_rating += 1
            continue
        try:
            year, rating, votes = int(f["year"]), float(f["rating"]), int(f["num_votes"])
        except ValueError as exc:
            raise ValueError(f"Invalid IMDb value in {f['tconst']}: {f}") from exc
        if not (1900 <= year <= 2026 and 1 <= rating <= 10 and votes > 0):
            raise ValueError(f"Out-of-range IMDb values in {f['tconst']}")
        chart_rows.append({
            "tconst": f["tconst"], "title": f["title"], "year": year,
            "rating": rating, "num_votes": votes,
            "log10_votes": round(math.log10(votes), 6),
            "genres": f.get("genres", ""), "directors": f.get("directors", ""),
            "year_cohort": ("through_2012" if year <= 2012 else
                            "2013_to_2019" if year <= 2019 else "2020_to_2026"),
            "lower_vote_count": int(votes < 1000),
            "imdb_url": f["imdb_url"],
        })
    if not chart_rows:
        raise ValueError("No released, rated and voted films for chart analysis")
    chart_rows.sort(key=lambda r: (r["year"], r["title"], r["tconst"]))

    for collection, key in ((overlap, "pattinson_tconst"), (cast, "tconst"), (directors, "tconst")):
        unknown = sorted({r[key] for r in collection} - allowed_ids)
        if unknown:
            raise ValueError(f"Orphan tconst in {key}: {unknown[:5]}")
    for row in overlap:
        bond = bond_by_id.get(row["bond_tconst"])
        if bond is None:
            raise ValueError(f"Bond crossover references unregistered film: {row['bond_tconst']}")
        if row["bond_series"] != bond["bond_series"] or row["bond_actor"] != bond["bond_actor"]:
            raise ValueError(f"Bond series/lead mismatch in crossover: {row}")
    if len({(r["person_nconst"], r["pattinson_tconst"], r["bond_tconst"])
            for r in overlap}) != len(overlap):
        raise ValueError("Duplicate cast-to-cast film-pair links")

    # All 27 Bond films are represented in the register, even if a given film has
    # no intersection with Pattinson's principal-film cast. The connection table
    # contains edges only; do not infer that an absent edge proves no crossover.
    # Keep official and supplementary links separate for honest editorial display.
    chart_overlap = sorted(overlap, key=lambda r: (r["bond_series"] != "eon",
                        r["bond_year"], r["person"], r["pattinson_year"]))
    fields = ["tconst", "title", "year", "rating", "num_votes", "log10_votes",
              "genres", "directors", "year_cohort", "lower_vote_count", "imdb_url"]
    write_csv(root / "chart_01_film_rating_timeline.csv", chart_rows, fields)
    write_csv(root / "chart_02_rating_vs_votes.csv", chart_rows, fields)
    overlap_fields = ["person_nconst", "person", "pattinson_tconst", "pattinson_title",
                      "pattinson_year", "bond_tconst", "bond_title", "bond_year",
                      "bond_series", "bond_actor"]
    write_csv(root / "chart_03_all_bond_connections.csv", chart_overlap, overlap_fields)
    write_csv(root / "chart_03_official_bond_connections.csv",
              [r for r in chart_overlap if r["bond_series"] == "eon"], overlap_fields)

    cohort = {}
    for name in ("through_2012", "2013_to_2019", "2020_to_2026"):
        rows = [r for r in chart_rows if r["year_cohort"] == name]
        values = sorted(r["rating"] for r in rows)
        n = len(values)
        median = None if not n else (
            values[n // 2] if n % 2 else round((values[n // 2 - 1] + values[n // 2]) / 2, 3)
        )
        cohort[name] = {"film_count": n, "median_movie_imdb_rating": median,
                        "films_at_least_1000_votes": sum(r["num_votes"] >= 1000 for r in rows)}
    report = {
        "title": "Robert Pattinson IMDb research QA",
        "scope": "Pattinson principal acting films and 25 official Eon + 2 supplementary Bond theatrical films, as at 2026-11-18",
        "all_movie_rows": len(films),
        "chart_eligible_released_rated_movies": len(chart_rows),
        "excluded_release_status": dict(excluded_status),
        "released_but_missing_rating_or_votes": missing_rating,
        "films_below_1000_votes": sum(r["lower_vote_count"] for r in chart_rows),
        "official_eon_bond_films_checked": bond_series["eon"],
        "supplementary_non_eon_bond_films_checked": bond_series["non_eon"],
        "official_bond_actors_checked": sorted({r["bond_actor"] for r in bond_films if r["bond_series"] == "eon"}),
        "all_bond_unique_connected_people": len({r["person_nconst"] for r in overlap}),
        "official_bond_unique_connected_people": len({r["person_nconst"] for r in overlap if r["bond_series"] == "eon"}),
        "all_bond_film_pair_edges": len(overlap),
        "official_bond_film_pair_edges": sum(r["bond_series"] == "eon" for r in overlap),
        "non_eon_bond_film_pair_edges": sum(r["bond_series"] == "non_eon" for r in overlap),
        "bond_films_with_any_overlap": len({r["bond_tconst"] for r in overlap}),
        "cohorts": cohort,
        "warnings": [
            "No claim about actor's acting quality from film-level IMDb ratings",
            "IMDb principal credits are a limited cast sample",
            "Different films have different opportunities to accumulate votes",
            "Years define editorial cohorts, not genre/production category",
            "No causal claim about Bond casting from collaborator overlaps",
            "All 2026 non-audited titles omitted pending release verification",
            "Bond connections cover all six Eon-era leads and all 25 official films, with two non-Eon films flagged separately",
            "The 1954 television adaptation of Casino Royale is excluded from theatrical scope",
            "IMDb principal casts do not cover every supporting, uncredited or background performer",
            "A Bond film with no selected-principals crossover is not evidence that no real-world link exists",
        ]
    }
    (root / "qa_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
