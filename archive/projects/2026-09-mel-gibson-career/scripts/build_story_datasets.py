#!/usr/bin/env python3
"""Build the three Mel Gibson editorial chart datasets from the verified IMDb career file."""

import csv
from collections import Counter
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
SOURCE = DATA_DIR / "mel_gibson_imdb_career_movies.csv"


def read_rows():
    with SOURCE.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, fieldnames, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    rows = read_rows()
    acting = sorted(
        (row for row in rows if row["acted"] == "1"),
        key=lambda row: (int(row["year"]), row["title"]),
    )
    directing = sorted(
        (row for row in rows if row["directed"] == "1"),
        key=lambda row: (int(row["year"]), row["title"]),
    )

    chart_1_fields = [
        "year", "title", "average_rating", "num_votes", "principal_order"
    ]
    write_csv(
        DATA_DIR / "mel_gibson_chart_01_acting_ratings.csv",
        chart_1_fields,
        [{field: row[field] for field in chart_1_fields} for row in acting],
    )

    counts = Counter(int(row["year"]) for row in acting)
    years = range(min(counts), max(counts) + 1)
    write_csv(
        DATA_DIR / "mel_gibson_chart_02_annual_acting_count.csv",
        ["year", "acting_films"],
        [{"year": year, "acting_films": counts.get(year, 0)} for year in years],
    )

    award_notes = {
        "Braveheart": "Directing Oscar",
        "Hacksaw Ridge": "Directing nominee",
    }
    chart_3_rows = []
    previous_year = None
    for row in directing:
        year = int(row["year"])
        chart_3_rows.append({
            "year": year,
            "title": row["title"],
            "average_rating": row["average_rating"],
            "num_votes": row["num_votes"],
            "acted": row["acted"],
            "years_since_previous": "" if previous_year is None else year - previous_year,
            "award_note": award_notes.get(row["title"], ""),
        })
        previous_year = year

    write_csv(
        DATA_DIR / "mel_gibson_chart_03_directing_ratings.csv",
        [
            "year", "title", "average_rating", "num_votes", "acted",
            "years_since_previous", "award_note",
        ],
        chart_3_rows,
    )


if __name__ == "__main__":
    main()
