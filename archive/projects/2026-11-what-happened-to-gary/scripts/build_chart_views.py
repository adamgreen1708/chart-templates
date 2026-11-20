#!/usr/bin/env python3
"""Build auditable Gary story datasets from published ONS-derived England & Wales data.

Run from repository root. Source: TidyTuesday 2026-06-16 E&W CSV,
derived from ONS Baby Names 1996-2024. The exact Git blob hash is pinned.
Historical ranking rows are separately sourced: see gary_historical_ranks.csv.
No chart is generated until these source and coverage gates pass.
"""
import csv
import hashlib
import io
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SOURCE = ("https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
          "main/data/2026/2026-06-16/england_wales_names.csv")
EXPECTED_GIT_BLOB = "2d2c3837eb1d3c82601bdf5539e95ffab15d0579"
NAMES = ("Gary", "Nigel", "Wayne", "Barry", "Arthur", "George", "Kevin")

def write_csv(filename, columns, rows):
    DATA.mkdir(parents=True, exist_ok=True)
    with (DATA / filename).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

def main():
    request = Request(SOURCE, headers={"User-Agent": "coffeetableviz-reproducible-analysis/1.0"})
    with urlopen(request, timeout=100) as response:
        raw = response.read()
    git_blob = hashlib.sha1(("blob %d\0" % len(raw)).encode("ascii") + raw).hexdigest()
    assert git_blob == EXPECTED_GIT_BLOB, ("Source changed; re-review it", git_blob)
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")))
    assert {"Year", "Sex", "Name", "Number", "Rank"} <= set(reader.fieldnames or []), reader.fieldnames
    selected = {}
    all_boy_records = 0
    for row in reader:
        if row["Sex"].strip().lower() not in ("boy", "male"):
            continue
        year = int(row["Year"])
        if not (1996 <= year <= 2024):
            continue
        all_boy_records += 1
        name = row["Name"].strip()
        if name not in NAMES:
            continue
        key = (year, name)
        assert key not in selected, "Duplicate source row: " + str(key)
        selected[key] = {"year": year, "name": name, "births": int(float(row["Number"])),
                         "rank": int(float(row["Rank"]))}
    assert all_boy_records > 50000, "Unexpected truncated ONS-derived file"
    gary = [selected[(year, "Gary")] for year in range(1996, 2025)]
    assert len(gary) == 29 and gary[0]["births"] == 235 and gary[0]["rank"] == 147
    assert gary[-1]["births"] >= 3, "Current Gary row unexpectedly suppressed"
    assert all(r["births"] >= 3 and r["rank"] > 0 for r in gary)
    historical = list(csv.DictReader((DATA / "gary_historical_ranks.csv").open(encoding="utf-8")))
    hist_map = {int(r["year"]): int(r["rank"]) for r in historical}
    assert hist_map == {1944: 95, 1954: 34, 1964: 16, 1974: 30, 1984: 26}
    assert len(historical) == 5
    write_csv("chart_01_historical_rank.csv", ["year", "rank", "rank_score"],
              [{"year": r["year"], "rank": r["rank"],
                "rank_score": 101 - int(r["rank"])} for r in historical])
    write_csv("chart_02_gary_births.csv", ["year", "births", "rank"], gary)
    # Direct comparison: same geography, sex, year, statistic and source.
    paired = [selected[(year, name)] for year in range(1996, 2025)
              for name in ("Gary", "Arthur") if (year, name) in selected]
    assert len(paired) == 58, "Gary/Arthur annual comparison not complete"
    write_csv("chart_03_gary_arthur.csv", ["year", "name", "births", "rank"], paired)
    peer_rows = [selected[(year, name)] for name in NAMES for year in (1996, 2024)
                 if (year, name) in selected]
    write_csv("peer_name_endpoints.csv", ["year", "name", "births", "rank"], peer_rows)
    tail = gary[-1]
    arthur_1996 = selected[(1996, "Arthur")]["births"]
    arthur_2024 = selected[(2024, "Arthur")]["births"]
    change = 100 * (tail["births"] - gary[0]["births"]) / gary[0]["births"]
    evidence = f"""# Gary: reproducible story discovery (England and Wales)

- Source (annual): {SOURCE}
- Source Git blob: {EXPECTED_GIT_BLOB}
- Period: 1996-2024, annual registrations for boys, exact first-name spelling.
- Raw source rows inspected (boy records): {all_boy_records:,}.
- Historical source: ONS top-100 decade rankings, verified against the published Behind the Name transcription (see data/gary_historical_ranks.csv).
- **Gary 1964**: historical rank **16** (not a count).
- **Gary 1996**: **235** boys, rank **147**.
- **Gary 2024**: **{tail["births"]}** boys, rank **{tail["rank"]}**.
- Gary 1996-to-2024 registrations: **{change:+.1f}%** (raw counts, not adjusted for births).
- Arthur 1996: **{arthur_1996}**; Arthur 2024: **{arthur_2024}** (boys, same source).
- 2025: **not included in charted time series**; ONS published newer workbook, pending primary-workbook import.

## Editorial checks
1. Gary's rapid postwar entry: sample rankings at ten-year intervals only; no annual mid-century counts.
2. Gary's post-1996 decline: annual counts are measured, but changes in total births are not controlled.
3. Gary vs Arthur: a defensible generational contrast, not evidence of a fixed 100-year cycle.
4. Gary Cooper: historically linked to popularising the name in America; no proof of UK causation.
5. Famous later Garys: chronological context only; cannot infer effect from a chart coincidence.
6. ONS suppresses names used for one or two births. Missing does not mean zero.

## Unselected comparisons to challenge before publication
Peer endpoints are in data/peer_name_endpoints.csv for Nigel, Wayne, Barry, Kevin and George.
Choose third-chart comparison only after review of those data, not because Arthur makes a neat story.
"""
    (DATA / "story_evidence.md").write_text(evidence, encoding="utf-8")
    print(evidence)
    print("QA PASSED: source blob, unique rows, coverage, rank/count semantics")

if __name__ == "__main__":
    main()
