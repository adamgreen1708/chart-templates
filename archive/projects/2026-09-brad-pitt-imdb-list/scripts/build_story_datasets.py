from pathlib import Path
import csv
from collections import defaultdict

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE = PROJECT_ROOT / "data" / "brad_pitt_imdb_films.csv"
CHART_02 = PROJECT_ROOT / "data" / "brad_pitt_chart_02_repeat_directors.csv"
CHART_03 = PROJECT_ROOT / "data" / "brad_pitt_chart_03_timeline.csv"


def read_rows():
    with SOURCE.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def build_repeat_directors(rows):
    credits = defaultdict(list)

    for row in rows:
        title = row["Title"]
        rating = float(row["IMDb Rating"])
        for director in [d.strip() for d in row["Directors"].split(",") if d.strip()]:
            credits[director].append((title, rating))

    output = []
    for director, films in credits.items():
        if len(films) < 2:
            continue
        output.append({
            "Director": director,
            "Film Count": len(films),
            "Average IMDb Rating": round(sum(r for _, r in films) / len(films), 2),
            "Films": " | ".join(title for title, _ in films),
        })

    output.sort(key=lambda r: (-float(r["Average IMDb Rating"]), r["Director"]))

    with CHART_02.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["Director", "Film Count", "Average IMDb Rating", "Films"],
        )
        writer.writeheader()
        writer.writerows(output)


def best_five_year_window(rows):
    years = [int(r["Year"]) for r in rows]
    best = None

    for start in range(min(years), max(years) - 3):
        selected = [r for r in rows if start <= int(r["Year"]) <= start + 4]
        if len(selected) < 3:
            continue
        avg = sum(float(r["IMDb Rating"]) for r in selected) / len(selected)
        candidate = (avg, len(selected), start, selected)
        if best is None or candidate[:2] > best[:2]:
            best = candidate

    return best


def build_timeline(rows):
    avg, count, start, selected = best_five_year_window(rows)
    end = start + 4
    selected_titles = {r["Title"] for r in selected}

    output = []
    for row in sorted(rows, key=lambda r: (int(r["Year"]), r["Title"])):
        output.append({
            "Year": int(row["Year"]),
            "Title": row["Title"],
            "IMDb Rating": float(row["IMDb Rating"]),
            "Peak 1995-99": 1 if row["Title"] in selected_titles else 0,
        })

    with CHART_03.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["Year", "Title", "IMDb Rating", "Peak 1995-99"],
        )
        writer.writeheader()
        writer.writerows(output)

    print(
        f"Best 5-year window with at least 3 films: {start}-{end}; "
        f"{count} films; average IMDb rating {avg:.2f}"
    )


def main():
    rows = read_rows()
    if len(rows) != 54:
        raise ValueError(f"Expected 54 source rows, found {len(rows)}")
    build_repeat_directors(rows)
    build_timeline(rows)
    print(f"Wrote {CHART_02}")
    print(f"Wrote {CHART_03}")


if __name__ == "__main__":
    main()
