"""Strict, reproducible data QA and chart-view generation for marathon winners.

Source: pinned 2026-11-13 chart-templates marathon-majors masters.
The source contains not-independently-checked winner entries. A successful
structural build is NOT a certificate of an exhaustive official-results audit.
"""
from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PROJECT = Path(__file__).resolve().parents[1]
OUT = PROJECT / "data"
SOURCE = ROOT / "data" / "marathon-majors"
LEDGER = PROJECT / "review" / "flagged_source_evidence.csv"
ORIGINAL_KEYS = ("Race", "Year", "Sex", "Winner", "Nationality", "Time",
                 "Notes", "Birth_Country", "Birth_Country_Source")
MASTERS = {
    "Men": ("marathon_major_winners_men_2000_2026.csv",
            "4707c23f1e3557b2d89897d02225658da50765e9"),
    "Women": ("marathon_major_winners_women_2000_2026.csv",
              "11c4bd6039fc4280bf7adee719fee5faaf74addb"),
}
UPSTREAM = ("source/SIS-marathon_major_winners_2000_2026.csv",
            "de9682df90e34943a97d3b963fb3df07bc743c2e")
POSITIONS = {"Tokyo": 6, "Boston": 5, "London": 4,
             "Berlin": 3, "Chicago": 2, "New York City": 1}
EAST = {"Kenya", "Ethiopia"}
# ISO 3166-1 alpha-2. GB, not UK, is the standard code for United Kingdom.
COUNTRY_ISO2 = {
    "Kenya": "KE", "Ethiopia": "ET", "Japan": "JP", "Russia": "RU",
    "United Kingdom": "GB", "Romania": "RO", "United States": "US",
    "Latvia": "LV", "China": "CN", "Germany": "DE",
}
require_codes = set(COUNTRY_ISO2.values())
assert len(require_codes) == len(COUNTRY_ISO2) and all(len(x)==2 and x.isalpha() for x in require_codes)
EXPECTED_EXCEPTIONS = {
    ("Tokyo", 2010, "Alevtina Biktimirova", "Russia"),
    ("Tokyo", 2011, "Noriko Higuchi", "Japan"),
    ("New York City", 2017, "Shalane Flanagan", "United States"),
    ("Boston", 2018, "Desiree Linden", "United States"),
}
FLAG_TYPES = {"Disqualification mentioned", "Source flagged for review"}

def require(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError("MARATHON DATA QA FAILED: " + description)

def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def checked_rows(path: Path, expected_sha: str):
    require(path.is_file(), f"Missing source {path}")
    actual_sha = git_blob_sha(path)
    require(actual_sha == expected_sha,
            f"Pinned source checksum changed for {path.name}: {actual_sha}")
    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        require(reader.fieldnames is not None, f"Missing header {path.name}")
        require(len(reader.fieldnames) == len(set(reader.fieldnames)),
                f"Duplicate headers in {path.name}")
        rows = list(reader)
        require(all(None not in r for r in rows),
                f"Malformed CSV columns in {path.name}")
    return rows

def write_csv(filename: str, fields: tuple[str, ...] | list[str], rows) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / filename).open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(fields)
        writer.writerows(rows)

def main() -> None:
    # Gate 1: independently enforce the Git blob checksums of the exact
    # source snapshot, not merely the overall row counts.
    upstream = checked_rows(SOURCE / UPSTREAM[0], UPSTREAM[1])
    require(len(upstream) == 308, "The pinned upstream source is not 308 rows")
    masters: dict[str, dict[tuple[str, int], dict[str, str]]] = {}
    entire = []
    for sex, (filename, sha) in MASTERS.items():
        rows = checked_rows(SOURCE / filename, sha)
        require(len(rows) == 154, f"{sex} master expected 154 rows")
        keyed = {}
        for r in rows:
            require(r["Sex"] == sex, f"Incorrect sex label in {filename}")
            require(r["Race"] in POSITIONS, f"Unknown race {r['Race']}")
            require(re.fullmatch(r"\d{4}", r["Year"]) is not None, "Invalid year")
            key = (r["Race"], int(r["Year"]))
            require(key not in keyed, f"Duplicate race-year {sex} {key}")
            require(r["Winner"] and r["Event_Status"], f"Blank winner/status at {sex} {key}")
            if r["Event_Status"] == "Completed":
                require(bool(r["Nationality"]) and bool(r["Time"]), f"Missing winner details {sex} {key}")
                require(re.fullmatch(r"\d+:[0-5]\d:[0-5]\d", r["Time"]) is not None,
                        f"Bad time text {sex} {key}")
                h, m, s = map(int, r["Time"].split(":"))
                require(int(r["Time_Seconds"]) == 3600*h + 60*m + s,
                        f"Time mismatch {sex} {key}")
            keyed[key] = r
        masters[sex] = keyed
        entire.extend(rows)

    # Gate 2: verify that the nine original upstream columns remain unchanged
    # in the enriched master, including notes and blank source values.
    orig_by_key = {}
    for r in upstream:
        key = (r["Race"], int(r["Year"]), r["Sex"])
        require(key not in orig_by_key, f"Duplicate upstream race-year-sex: {key}")
        orig_by_key[key] = r
    require(len(orig_by_key) == 308, "Unexpected original source key count")
    for r in entire:
        key = (r["Race"], int(r["Year"]), r["Sex"])
        require(key in orig_by_key, f"Extra enriched row {key}")
        require(all(r[k] == orig_by_key[key][k] for k in ORIGINAL_KEYS),
                f"Source original columns changed {key}")

    # Gate 3: force the repository's own upstream dataset generator to agree
    # with all 10 committed datasets. This never changes the files.
    check = subprocess.run(["node", "scripts/build_marathon_bauhaus.js", "--check"],
                           cwd=ROOT, capture_output=True, text=True)
    require(check.returncode == 0,
            "Canonical Bauhaus source regeneration --check failed: "
            + (check.stderr or check.stdout)[-1200:])

    men, women = masters["Men"], masters["Women"]
    require(set(men) == set(women), "Men and women have different race-year sets")
    expected = set()
    for year in range(2000, 2020):
        for race in POSITIONS:
            if race == "Tokyo" and year < 2007:
                continue
            expected.add((race, year))
    require(set(men).issuperset(expected),
            "Historical 2000-19 race/year records absent")
    for key in expected:
        male, female = men[key], women[key]
        expected_status = "Cancelled" if key == ("New York City", 2012) else "Completed"
        require(male["Event_Status"] == female["Event_Status"] == expected_status,
                f"Unexpected race status {key}")
        if expected_status == "Cancelled":
            require(male["Winner"] == female["Winner"] == "NO RACE",
                    "NYC 2012 cancelled rows must have NO RACE")
    require(len(expected) == 113, "Unexpected historical race schedule length")
    completed = [key for key in sorted(expected, key=lambda x:(x[1], x[0]))
                 if men[key]["Event_Status"] == women[key]["Event_Status"] == "Completed"]
    require(len(completed) == 112, "Expected 112 matched completed race-years")
    early = [key for key in completed if key[1] <= 2009]
    later = [key for key in completed if key[1] >= 2010]
    require((len(early), len(later)) == (53, 59),
            "Wrong 2000s/2010s denominators")

    # Gate 4: every explicitly flagged source row has an exact-match,
    # individually sourced editorial adjudication. Never discard all
    # disqualification-labelled results: some are later reassigned champions.
    require(LEDGER.is_file(), "Missing evidence ledger")
    with LEDGER.open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        require(reader.fieldnames == ["Race", "Year", "Sex", "Winner",
                "Nationality", "Result_Status", "EvidenceURL"],
                "Evidence ledger schema changed")
        evidence = {}
        for item in reader:
            key = (item["Race"], int(item["Year"]), item["Sex"])
            require(key not in evidence, f"Duplicate evidence entry: {key}")
            require(item["EvidenceURL"].startswith("https://"),
                    f"Missing authoritative URL {key}")
            evidence[key] = item
    source_flags = {}
    for key in completed:
        for sex, row in (("Men", men[key]), ("Women", women[key])):
            if row["Result_Status"] in FLAG_TYPES:
                source_flags[(key[0], key[1], sex)] = row
    require(len(source_flags) == 8, "Expected eight review/disqualification flags")
    require(set(source_flags) == set(evidence),
            "Flagged source events and evidence ledger disagree")
    for key, row in source_flags.items():
        ledger = evidence[key]
        require(all(row[field] == ledger[field]
                    for field in ("Winner", "Nationality", "Result_Status")),
                f"Evidence metadata doesn't match original source for {key}")

    # Gate 5: validate the *actual chart evidence*, not manually typed
    # denominators or data points.
    streak = [women[("Berlin", year)] for year in range(2000, 2006)]
    require(all(r["Nationality"] == "Japan" for r in streak),
            "Berlin 2000-05 streak no longer all Japanese")
    first_nations = Counter(women[k]["Nationality"] for k in early)
    require(len(first_nations) == 10, "Women's 2000s nationality count changed")
    every_country = {women[k]["Nationality"] for k in completed}
    require(every_country == set(COUNTRY_ISO2),
            f"Country ISO2 lookup no longer matches observed nationalities: {every_country ^ set(COUNTRY_ISO2)}")
    exceptions = {(women[k]["Race"], int(women[k]["Year"]),
                   women[k]["Winner"], women[k]["Nationality"])
                  for k in later if women[k]["Nationality"] not in EAST}
    require(exceptions == EXPECTED_EXCEPTIONS,
            f"The four red-dot winners changed: {exceptions}")
    observed = {}
    slope = []
    for sex in ("Women", "Men"):
        for i, (label, keys) in enumerate((("2000–09", early), ("2010–19", later)), 1):
            n = len(keys)
            others = sum(1 for k in keys if masters[sex][k]["Nationality"] not in EAST)
            observed[(sex, label)] = (others, n)
            slope.append((i, label, sex, f"{others/n:.6f}", others, n))
    require(observed == {
        ("Women", "2000–09"): (31, 53), ("Women", "2010–19"): (4, 59),
        ("Men", "2000–09"): (12, 53), ("Men", "2010–19"): (6, 59),
    }, "The final chart's numerator/denominator contract changed")
    require(sum(1 for k in early if women[k]["Nationality"] not in EAST) == 31,
            "First matrix red-dot count mismatch")

    # Gate 6: derive the three published chart views strictly from masters.
    first_ranked = sorted(first_nations.items(), key=lambda item:(-item[1], item[0]))
    write_csv("01_women_nationalities.csv", ["Nationality", "Wins"], first_ranked)
    for keys, filename in ((early, "01_winner_race_year.csv"),
                           (later, "02_exception_race_year.csv")):
        dots = []
        for key in sorted(keys, key=lambda k:(k[1], -POSITIONS[k[0]])):
            row = women[key]
            group = "Kenya/Ethiopia" if row["Nationality"] in EAST else "Outside"
            dots.append((key[1], key[0], POSITIONS[key[0]],
                         row["Winner"], row["Nationality"], COUNTRY_ISO2[row["Nationality"]], group))
        write_csv(filename, ["Year", "Race", "RaceRow", "Winner",
                             "Nationality", "CountryISO2", "Group"], dots)
    # Bauhaus-ready counts: real win counts rather than dummy values.
    # Filter by Decade; label with Nationality or CountryISO2; value = Wins.
    bauhaus = []
    for label, keys in (("2000–09", early), ("2010–19", later)):
        counts = Counter(women[k]["Nationality"] for k in keys)
        for country, wins in sorted(counts.items(), key=lambda pair: (-pair[1], pair[0])):
            bauhaus.append((label, country, COUNTRY_ISO2[country], wins,
                            f"{100 * wins / len(keys):.1f}",
                            "Kenya/Ethiopia" if country in EAST else "Outside"))
    require(sum(int(row[3]) for row in bauhaus if row[0] == "2000–09") == 53
            and sum(int(row[3]) for row in bauhaus if row[0] == "2010–19") == 59,
            "Bauhaus counts differ from verified winner-level tables")
    require(len(bauhaus) == 15, "Unexpected Bauhaus nationality-decade count")
    write_csv("bauhaus_women_wins_by_nationality_decade.csv",
              ["Decade", "Nationality", "CountryISO2", "Wins", "SharePct", "Group"], bauhaus)
    write_csv("03_outside_winners_share.csv",
              ["PeriodIndex", "Period", "Sex", "OutsideShare",
               "OtherWins", "TotalWins"], slope)

    # Gate 7: check the actual committed chart configs against the current
    # repository social-square contract before GitHub renders anything.
    configs = {}
    for filename in ("01_women_2000s.py", "02_women_2010s.py", "03_share_by_sex.py"):
        path = PROJECT / "config" / filename
        module = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        assignments = [stmt for stmt in module.body if isinstance(stmt, ast.Assign)
                       and any(isinstance(t, ast.Name) and t.id == "CHART_CONFIG"
                               for t in stmt.targets)]
        require(len(assignments) == 1, f"Missing CHART_CONFIG: {filename}")
        config = ast.literal_eval(assignments[0].value)
        require(config["render_profile"] == "social_square",
                f"{filename} does not use the production house profile")
        require(config["fig_width"] == 8.0 and config["fig_height"] == 8.0
                and config["dpi"] == 200, f"{filename} must be square 1600px PNG")
        require(config["source_text"].startswith("Source: Shorts in Sports"),
                f"{filename} omits the actual credited source")
        require(config["footer_left"] == "Adam Green | coffeetableviz",
                f"{filename} has inconsistent brand credit")
        require(bool(config["title"]) and bool(config["subtitle"]),
                f"{filename} missing editorial hierarchy")
        require(config["vertical_gridlines"] is False,
                f"{filename} has unexpected vertical gridlines")
        require(config["output_file"].startswith("output/") and
                config["output_file"].endswith(".png"),
                f"{filename} output must be a descriptive PNG")
        require(config["sort"] is None or isinstance(config["sort"], dict),
                f"{filename} sort must be a dict or None")
        require(config["data_file"].startswith(
                "archive/projects/2026-11-marathon-winning-map/data/"),
                f"{filename} data must be source-generated within this project")
        configs[filename] = config
    first_cfg, second_cfg = configs["01_women_2000s.py"], configs["02_women_2010s.py"]
    for c in (first_cfg, second_cfg):
        require(c["chart_type"] == "scatter", "The two puzzles must be dot matrices")
        labels = c["label_style"]
        require(labels.get("enabled") is True
                and labels.get("label_col") == "CountryISO2"
                and labels.get("position") == "center"
                and labels.get("highlight_color") == "#FFFFFF"
                and labels.get("color") == "#20303A"
                and float(labels.get("fontsize")) >= 11.5,
                "Every dot must carry a contrast-safe ISO2 code derived from CSV")
        require(c["point_style"]["size"] >= 850, "Dots too small for a two-letter code")
        require(c["y_axis_min"] == 0 and c["y_axis_max"] == 7,
                "Unclipped identical race axis required")
        require(c["highlight_points"] == [{"Group": "Outside"}],
                "Red must always represent outside Kenya/Ethiopia")
        require(c["point_style"]["size"] == c["highlight_style"]["size"],
                "Colour, not mark area, must encode winner group")
    require(first_cfg["y_tick_labels"] == second_cfg["y_tick_labels"],
            "The two decade matrices must have identical race order")
    require(first_cfg["point_style"] == second_cfg["point_style"] and
            first_cfg["highlight_style"] == second_cfg["highlight_style"],
            "The two decade matrices must have identical marker style")
    require(first_cfg["profile_overrides"] == second_cfg["profile_overrides"],
            "The two decade matrices must use the same labelled plot margins")
    require(first_cfg["output_file"].endswith("01_berlin_six_and_the_world.png")
            and second_cfg["output_file"].endswith("02_find_the_four.png"),
            "Descriptive source output names drifted from the corrected story")
    last_cfg = configs["03_share_by_sex.py"]
    require(last_cfg["chart_type"] == "line" and
            last_cfg["series_col"] == "Sex" and last_cfg["focus_series"] == "Women",
            "The comparison must have two separately sourced sex series")
    require(last_cfg["y_axis_min"] == 0 and last_cfg["y_axis_max"] == 1
            and last_cfg["y_tick_format"] == "percent",
            "Comparison percentages must use a zero-to-100-percent axis")
    require(last_cfg["focus_style"]["color"] == "#C44E52",
            "Women must be highlighted red consistently")
    require(len(last_cfg["annotate_points"]) == 5,
            "Expected four endpoints and one source-derived comparison callout")
    annotation_texts = {a["text"] for a in last_cfg["annotate_points"]}
    expected_texts = {
        f"{sex} {count / n * 100:.1f}%"
        for (sex, _), (count, n) in observed.items()
    }
    women_drop = 100 * (observed[("Women", "2000–09")][0] / 53
                        - observed[("Women", "2010–19")][0] / 59)
    men_drop = 100 * (observed[("Men", "2000–09")][0] / 53
                      - observed[("Men", "2010–19")][0] / 59)
    callout = f"Women: down {women_drop:.1f} points\nMen: down {men_drop:.1f} points"
    expected_texts.add(callout)
    require(annotation_texts == expected_texts,
            "Annotations no longer match source-derived percentages and declines")

    # A pass confirms integrity, calculations and named high-risk cases.
    # It does not claim the other source winners were independently audited.
    unreviewed = sum(r["Result_Status"] == "Not independently checked"
                     for r in entire if 2000 <= int(r["Year"]) <= 2019
                     and r["Event_Status"] == "Completed")
    require(unreviewed == 216, "Unreviewed source-claim count changed")
    report = {
        "structural_data_qa": "PASS",
        "social_square_config_qa": "PASS",
        "full_official_results_audit": "NOT COMPLETE",
        "source_snapshot": "999b9b57c2cf61a1222bb4f08a4bdd885898e09a",
        "source_github_blob_sha": {v[0]: v[1] for v in MASTERS.values()},
        "upstream_source_blob_sha": UPSTREAM[1],
        "source_rows": len(upstream),
        "matched_completed_race_years": len(completed),
        "period_race_years": {"2000-09": len(early), "2010-19": len(later)},
        "status_flagged_events_with_evidence": len(source_flags),
        "source_completed_rows_not_independently_checked": unreviewed,
        "exceptions_verified_by_editorial_evidence": 4,
        "women_outside_kenya_ethiopia": {"2000-09": {"wins":31,"n":53},
                                          "2010-19": {"wins":4,"n":59}},
        "men_outside_kenya_ethiopia": {"2000-09": {"wins":12,"n":53},
                                        "2010-19": {"wins":6,"n":59}},
        "limitation": "All charts describe this pinned source; most individual rows are not independently verified against official race results."
    }
    (OUT / "qa_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("MARATHON DATA QA PASS: 308 original rows preserved; pinned source checksums match.")
    print("THREE SOCIAL-SQUARE CONFIGS PASS SEMANTIC COLOUR, AXIS AND FOOTER CONTRACT.")
    print("CANONICAL DATA BUILD --check PASS; 112 completed race-year pairs.")
    print("EIGHT SOURCE FLAGS MATCH OFFICIAL-EVIDENCE LEDGER; NO SILENT EXCLUSIONS.")
    print("Story arithmetic: women 31/53 -> 4/59; men 12/53 -> 6/59.")
    print("CAVEAT: remaining 216 completed entries are not independently verified by source-status; no blanket official validation claimed.")

if __name__ == "__main__":
    main()
