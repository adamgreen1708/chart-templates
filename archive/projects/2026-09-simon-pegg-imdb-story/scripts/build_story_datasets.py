#!/usr/bin/env python3
"""Validate the approved Simon Pegg story and build three chart datasets."""

import csv
import statistics
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCE = PROJECT_ROOT / "data" / "simon_pegg_imdb_principal_actor_movies.csv"
DATA_DIR = PROJECT_ROOT / "data"


def read_source():
    with SOURCE.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["year"] = int(row["year"])
        row["average_rating"] = float(row["average_rating"])
        row["num_votes"] = int(row["num_votes"])
        row["principal_order"] = int(row["principal_order"])
    assert len(rows) == 33
    assert len({row["tconst"] for row in rows}) == 33
    assert all(row["num_votes"] >= 1000 for row in rows)
    return rows


def partnership_group(row):
    if row["title"].startswith("Mission: Impossible"):
        return "Mission: Impossible"
    if row["title"].startswith("Star Trek"):
        return "Star Trek"
    if row["directors"] == "Edgar Wright":
        return "Edgar Wright"
    return "Other eligible movies"


def write_csv(filename, fieldnames, rows):
    with (DATA_DIR / filename).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_timeline(rows):
    output = []
    for row in rows:
        group = partnership_group(row)
        output.append({
            "Year": row["year"],
            "Title": row["title"],
            "IMDb Rating": row["average_rating"],
            "Votes": row["num_votes"],
            "Partnership Group": group,
            "Partnership Film": 0 if group == "Other eligible movies" else 1,
        })
    assert sum(row["Partnership Film"] for row in output) == 12
    write_csv(
        "simon_pegg_chart_01_timeline.csv",
        ["Year", "Title", "IMDb Rating", "Votes", "Partnership Group", "Partnership Film"],
        sorted(output, key=lambda item: (item["Year"], item["Title"])),
    )


def build_group_comparison(rows):
    order = ["Star Trek", "Edgar Wright", "Mission: Impossible", "Other eligible movies"]
    grouped = {group: [] for group in order}
    for row in rows:
        grouped[partnership_group(row)].append(row)

    expected = {
        "Star Trek": (3, 7.53),
        "Edgar Wright": (3, 7.50),
        "Mission: Impossible": (6, 7.35),
        "Other eligible movies": (21, 6.09),
    }
    output = []
    for rank, group in enumerate(order, start=1):
        films = grouped[group]
        mean_rating = statistics.mean(row["average_rating"] for row in films)
        assert len(films) == expected[group][0]
        assert round(mean_rating, 2) == expected[group][1]
        output.append({
            "Order": rank,
            "Group": f"{group} (n={len(films)})",
            "Group Key": group,
            "Mean Rating": round(mean_rating, 2),
            "Median Rating": round(statistics.median(row["average_rating"] for row in films), 2),
            "Film Count": len(films),
            "Total Votes": sum(row["num_votes"] for row in films),
            "Partnership": 0 if group == "Other eligible movies" else 1,
            "Detail Label": f"{mean_rating:.2f}",
        })

    partnership_votes = sum(row["Total Votes"] for row in output if row["Partnership"] == 1)
    all_votes = sum(row["Total Votes"] for row in output)
    assert round(100 * partnership_votes / all_votes, 1) == 76.6
    write_csv(
        "simon_pegg_chart_02_groups.csv",
        [
            "Order", "Group", "Group Key", "Mean Rating", "Median Rating",
            "Film Count", "Total Votes", "Partnership", "Detail Label",
        ],
        output,
    )


def build_partnership_sequences(rows):
    grouped = {
        group: sorted(
            [row for row in rows if partnership_group(row) == group],
            key=lambda row: (row["year"], row["title"]),
        )
        for group in ("Mission: Impossible", "Star Trek", "Edgar Wright")
    }
    output = []
    for group, films in grouped.items():
        for sequence, row in enumerate(films, start=1):
            output.append({
                "Film Number": sequence,
                "Partnership": group,
                "Title": row["title"],
                "Year": row["year"],
                "IMDb Rating": row["average_rating"],
                "Principal Order": row["principal_order"],
            })
    assert len(output) == 12
    assert [row["IMDb Rating"] for row in output if row["Partnership"] == "Mission: Impossible"] == [6.9, 7.4, 7.4, 7.7, 7.6, 7.1]
    write_csv(
        "simon_pegg_chart_03_partnership_sequences.csv",
        ["Film Number", "Partnership", "Title", "Year", "IMDb Rating", "Principal Order"],
        output,
    )


def main():
    rows = read_source()
    build_timeline(rows)
    build_group_comparison(rows)
    build_partnership_sequences(rows)


if __name__ == "__main__":
    main()
