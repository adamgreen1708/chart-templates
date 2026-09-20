import csv
import statistics
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCE = PROJECT_ROOT / "data" / "tom_hanks_imdb_principal_actor_movies.csv"
DATA_DIR = PROJECT_ROOT / "data"

PEAK_START = 1992
PEAK_END = 2002
HIT_THRESHOLD = 7.5


def read_source():
    with SOURCE.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    for row in rows:
        row["year"] = int(row["year"])
        row["rating"] = float(row["rating"])
        row["votes"] = int(row["votes"])

    return [row for row in rows if "Documentary" not in row["genres"]]


def write_csv(filename, fieldnames, rows):
    with (DATA_DIR / filename).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_timeline(rows):
    output = []
    for row in rows:
        output.append(
            {
                "Year": row["year"],
                "Title": row["title"],
                "IMDb Rating": row["rating"],
                "Peak Run": 1 if PEAK_START <= row["year"] <= PEAK_END else 0,
            }
        )

    write_csv(
        "tom_hanks_chart_01_timeline.csv",
        ["Year", "Title", "IMDb Rating", "Peak Run"],
        sorted(output, key=lambda item: (item["Year"], item["Title"])),
    )


def build_period_comparison(rows):
    periods = [
        (1, "Before · 1980–91", 1980, 1991),
        (2, "Peak run · 1992–2002", 1992, 2002),
        (3, "After · 2003–26", 2003, 2026),
    ]
    output = []

    for order, label, start, end in periods:
        selected = [row for row in rows if start <= row["year"] <= end]
        hits = sum(row["rating"] >= HIT_THRESHOLD for row in selected)
        output.append(
            {
                "Order": order,
                "Period": label,
                "Film Count": len(selected),
                "Average IMDb Rating": round(statistics.mean(row["rating"] for row in selected), 2),
                "Median IMDb Rating": round(statistics.median(row["rating"] for row in selected), 2),
                "Films Rated 7.5+": hits,
                "Share Rated 7.5+": round(hits / len(selected), 4),
                "Detail Label": f"{hits} of {len(selected)}",
                "Peak Run": 1 if start == PEAK_START else 0,
            }
        )

    write_csv(
        "tom_hanks_chart_02_period_comparison.csv",
        [
            "Order",
            "Period",
            "Film Count",
            "Average IMDb Rating",
            "Median IMDb Rating",
            "Films Rated 7.5+",
            "Share Rated 7.5+",
            "Detail Label",
            "Peak Run",
        ],
        output,
    )


def build_toy_story(rows):
    selected = [row for row in rows if row["title"].startswith("Toy Story")]
    output = [
        {
            "Year": row["year"],
            "Title": row["title"],
            "IMDb Rating": row["rating"],
            "Latest Film": 1 if row["title"] == "Toy Story 5" else 0,
        }
        for row in sorted(selected, key=lambda item: item["year"])
    ]

    write_csv(
        "tom_hanks_chart_03_toy_story.csv",
        ["Year", "Title", "IMDb Rating", "Latest Film"],
        output,
    )


def main():
    rows = read_source()
    if len(rows) != 61:
        raise ValueError(f"Expected 61 rated narrative-film rows, found {len(rows)}")

    build_timeline(rows)
    build_period_comparison(rows)
    build_toy_story(rows)
    print("Built three Tom Hanks story datasets from 61 rated narrative-film rows.")


if __name__ == "__main__":
    main()
