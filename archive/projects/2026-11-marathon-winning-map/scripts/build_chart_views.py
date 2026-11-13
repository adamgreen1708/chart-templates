"""Derive three chart views from the pinned Shorts in Sports-based masters."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
PROJECT = Path(__file__).resolve().parents[1]
OUT = PROJECT / "data"
SOURCE_DIR = REPO / "data" / "marathon-majors"
SOURCE_SHA = "999b9b57c2cf61a1222bb4f08a4bdd885898e09a"
PERIODS = [(2000, 2009, "2000–09"), (2010, 2019, "2010–19"), (2020, 2025, "2020–25")]

def load(sex: str) -> dict[tuple[str, int], dict[str, str]]:
    path = SOURCE_DIR / f"marathon_major_winners_{sex}_2000_2026.csv"
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 154:
        raise AssertionError(f"{path} row count drift: {len(rows)}")
    keyed = {(r["Race"], int(r["Year"])): r for r in rows}
    if len(keyed) != len(rows):
        raise AssertionError("Duplicate race-year source rows")
    return keyed

def eligible(row: dict[str, str]) -> bool:
    return (row["Event_Status"] == "Completed"
            and row["Result_Status"] == "Not independently checked"
            and int(row["Year"]) <= 2025
            and bool(row["Nationality"]))

def write(path: Path, header: list[str], rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)

def main() -> None:
    men, women = load("men"), load("women")
    common = sorted(set(men) & set(women), key=lambda k: (k[1], k[0]))
    paired = [(key, men[key], women[key])
              for key in common if eligible(men[key]) and eligible(women[key])]
    if len(paired) != 133:
        raise AssertionError(f"Expected 133 qualifying matched race-years; got {len(paired)}")
    summary = []
    for i, (start, end, name) in enumerate(PERIODS, 1):
        subset = [(m, w) for (race, year), m, w in paired if start <= year <= end]
        n = len(subset)
        if n != {1: 51, 2: 53, 3: 29}[i]:
            raise AssertionError(f"Period {name}: unexpected denominator {n}")
        for sex, index in (("Men", 0), ("Women", 1)):
            ct = Counter(pair[index]["Nationality"] for pair in subset)
            tally = ct["Kenya"] + ct["Ethiopia"]
            share = tally / n
            summary.append([i, name, sex, f"{share:.6f}", f"{share*100:.1f}",
                            tally, n, sex if i == 3 else ""])
            if sex == "Women" and i in (1, 2):
                sorted_rows = sorted(ct.items(), key=lambda x: (-x[1], x[0]))
                write(OUT / f"0{i}_women_nationalities.csv",
                      ["Nationality", "Wins"], [[country, wins] for country, wins in sorted_rows])
    assert summary[0][5] == 39 and summary[1][5] == 22
    assert summary[2][5] == 48 and summary[3][5] == 50
    write(OUT / "03_two_country_share.csv",
          ["PeriodIndex", "Period", "Sex", "Share", "SharePct",
           "TwoCountryWins", "EligibleWins", "EndLabel"], summary)
    print("Source-checked: 133 paired race-years (51 / 53 / 29).")
    print("Kenya + Ethiopia: women 22/51 → 50/53 → 26/29.")

if __name__ == "__main__":
    main()
