import csv
import statistics
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCE = PROJECT_ROOT / "data" / "taron_egerton_imdb_principal_actor_movies.csv"
DATA_DIR = PROJECT_ROOT / "data"


def read_source():
    with SOURCE.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    eligible = []
    for row in rows:
        if row["analysis_eligible"] != "1":
            continue
        row["year"] = int(row["year"])
        row["rating"] = float(row["rating"])
        row["votes"] = int(row["votes"])
        row["principal_order"] = int(row["principal_order"])
        eligible.append(row)

    assert len(rows) == 21
    assert len(eligible) == 14
    assert len({row["tconst"] for row in rows}) == len(rows)
    assert all(row["votes"] >= 1000 for row in eligible)
    return eligible


def write_csv(filename, fieldnames, rows):
    with (DATA_DIR / filename).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_timeline(rows):
    output = []
    for row in rows:
        biography_lead = row["principal_order"] == 1 and "Biography" in row["genres"]
        output.append(
            {
                "Year": row["year"],
                "Title": row["title"],
                "IMDb Rating": row["rating"],
                "Votes": row["votes"],
                "Top-billed Biography": 1 if biography_lead else 0,
                "Breakout": 1 if row["title"] == "Kingsman: The Secret Service" else 0,
            }
        )

    write_csv(
        "taron_egerton_chart_01_timeline.csv",
        ["Year", "Title", "IMDb Rating", "Votes", "Top-billed Biography", "Breakout"],
        sorted(output, key=lambda item: (item["Year"], item["Title"])),
    )


def build_lead_lanes(rows):
    biography = [
        row for row in rows
        if row["principal_order"] == 1 and "Biography" in row["genres"]
    ]
    action = [
        row for row in rows
        if row["principal_order"] == 1 and "Action" in row["genres"]
    ]
    assert {row["title"] for row in biography} == {"Eddie the Eagle", "Rocketman", "Tetris"}
    assert {row["title"] for row in action} == {
        "Kingsman: The Golden Circle", "Robin Hood", "Carry-On"
    }

    biography_mean = statistics.mean(row["rating"] for row in biography)
    action_mean = statistics.mean(row["rating"] for row in action)
    assert round(biography_mean - action_mean, 2) == 1.13

    output = []
    ordered = sorted(biography, key=lambda row: (-row["rating"], row["year"])) + sorted(
        action, key=lambda row: (-row["rating"], row["year"])
    )
    for order, row in enumerate(ordered, start=1):
        lane = "Top-billed Biography" if row in biography else "Top-billed Action"
        output.append(
            {
                "Order": order,
                "Title": row["title"],
                "Lane": lane,
                "IMDb Rating": row["rating"],
                "Lane Mean": round(biography_mean if row in biography else action_mean, 2),
                "Biography Lead": 1 if row in biography else 0,
                "Detail Label": f"{row['rating']:.1f}",
            }
        )

    write_csv(
        "taron_egerton_chart_02_lead_lanes.csv",
        ["Order", "Title", "Lane", "IMDb Rating", "Lane Mean", "Biography Lead", "Detail Label"],
        output,
    )


def build_franchises(rows):
    lookups = {row["title"]: row for row in rows}
    sequence = [
        ("Kingsman", 1, "Kingsman: The Secret Service"),
        ("Kingsman", 2, "Kingsman: The Golden Circle"),
        ("Sing", 1, "Sing"),
        ("Sing", 2, "Sing 2"),
    ]
    output = []
    for franchise, film_number, title in sequence:
        row = lookups[title]
        output.append(
            {
                "Film Number": film_number,
                "Franchise": franchise,
                "Title": title,
                "Year": row["year"],
                "IMDb Rating": row["rating"],
            }
        )

    kingsman = [row["IMDb Rating"] for row in output if row["Franchise"] == "Kingsman"]
    sing = [row["IMDb Rating"] for row in output if row["Franchise"] == "Sing"]
    assert round(kingsman[1] - kingsman[0], 1) == -1.0
    assert round(sing[1] - sing[0], 1) == 0.2

    write_csv(
        "taron_egerton_chart_03_franchises.csv",
        ["Film Number", "Franchise", "Title", "Year", "IMDb Rating"],
        output,
    )


def main():
    rows = read_source()
    build_timeline(rows)
    build_lead_lanes(rows)
    build_franchises(rows)


if __name__ == "__main__":
    main()
