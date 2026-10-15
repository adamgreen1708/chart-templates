#!/usr/bin/env python3
"""Rebuild the three house-renderer input datasets from ONS principal projections.

Execute from the repository root. No third-party dependencies.
"""
import csv
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
DATA = PROJECT / "data"

def read_csv(name):
    with (DATA / name).open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))

def write_csv(name, headers, rows):
    with (DATA / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

def main():
    ages = read_csv("uk_population_by_age_2026.csv")
    projections = read_csv("uk_population_projection_2026_2050.csv")
    years = {int(r["year"]): r for r in projections}

    assert len(ages) == 107, "Expected ages 0–104, 105–109, 110+"
    assert len(projections) == 25 and set(years) == set(range(2026, 2051))
    assert sum(int(r["total_people"]) for r in ages) == int(years[2026]["uk_total"])
    assert int(next(r["total_people"] for r in ages if r["age"] == "35")) == 982419

    age_profile = []
    very_old = 0
    for row in ages:
        try:
            age = int(row["age"])
        except ValueError:
            assert row["age"] in ("105 - 109", "110 and over")
            very_old += int(row["total_people"])
            continue
        age_profile.append({"age": age, "people_thousands": f'{int(row["total_people"])/1000:.3f}'})

    assert len(age_profile) == 105
    # The two oldest ONS grouped categories cannot be plotted as individual ages.
    # Add a single visibly disclosed '105+' bucket at x=105.
    age_profile.append({"age": 105, "people_thousands": f"{very_old/1000:.3f}"})
    assert sum(round(float(r["people_thousands"])*1000) for r in age_profile) == int(years[2026]["uk_total"])
    write_csv("chart_01_age_profile.csv", ["age", "people_thousands"], age_profile)

    shares = []
    for year in sorted(years):
        row = years[year]
        total = int(row["uk_total"])
        for label, column, given in [
            ("Aged 65+", "aged_65_plus", "pct_65_plus"),
            ("Under 15", "aged_0_14", "pct_0_14"),
        ]:
            value = 100 * int(row[column]) / total
            assert abs(value - float(row[given])) < 0.00001, (year, label)
            shares.append({"year": year, "age_group": label, "share_pct": f"{value:.6f}"})
    write_csv("chart_02_age_shares.csv", ["year", "age_group", "share_pct"], shares)

    start, end = years[2026], years[2050]
    growth = []
    for name, column in [
        ("Whole UK", "uk_total"),
        ("Aged 65+", "aged_65_plus"),
        ("Aged 85+", "aged_85_plus"),
    ]:
        a, b = int(start[column]), int(end[column])
        growth.append({"group": name, "growth_percent": f"{100 * (b/a - 1):.6f}",
                       "people_2026": a, "people_2050": b})
    write_csv("chart_03_growth.csv", ["group", "growth_percent", "people_2026", "people_2050"], growth)
    print("ONS inputs validated; three chart-ready data views rebuilt.")

if __name__ == "__main__":
    main()
