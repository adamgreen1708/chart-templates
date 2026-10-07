from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read_csv(name: str):
    with (DATA / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


annual = read_csv("messi_argentina_yearly.csv")
finals = read_csv("messi_argentina_major_finals.csv")

assert sum(int(r["appearances"]) for r in annual) == 208
assert sum(int(r["goals"]) for r in annual) == 126
assert annual[-1]["year"] == "2026"
assert int(annual[-1]["appearances"]) == 12
assert int(annual[-1]["goals"]) == 11

early = [r for r in annual if int(r["year"]) <= 2020]
late = [r for r in annual if int(r["year"]) >= 2021]

def totals(rows):
    apps = sum(int(r["appearances"]) for r in rows)
    goals = sum(int(r["goals"]) for r in rows)
    return apps, goals, goals / apps

early_apps, early_goals, early_rate = totals(early)
late_apps, late_goals, late_rate = totals(late)

assert (early_apps, early_goals) == (142, 71)
assert (late_apps, late_goals) == (66, 55)
assert round(early_rate, 3) == 0.500
assert round(late_rate, 3) == 0.833

with (DATA / "messi_argentina_era_split.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["period", "appearances", "goals", "goals_per_appearance", "appearance_share", "goal_share"])
    writer.writerow(["2005–20", early_apps, early_goals, f"{early_rate:.3f}", f"{early_apps / 208:.3f}", f"{early_goals / 126:.3f}"])
    writer.writerow(["2021–26", late_apps, late_goals, f"{late_rate:.3f}", f"{late_apps / 208:.3f}", f"{late_goals / 126:.3f}"])

assert len(finals) == 9
assert [int(r["won_title"]) for r in finals[:4]] == [0, 0, 0, 0]
assert [int(r["won_title"]) for r in finals[4:8]] == [1, 1, 1, 1]
assert int(finals[8]["won_title"]) == 0

print("PASS: 208 caps / 126 goals")
print("PASS: 2005–20 = 71/142 = 0.500")
print("PASS: 2021–26 = 55/66 = 0.833")
print("PASS: finals sequence = four losses, four wins, 2026 runner-up")
