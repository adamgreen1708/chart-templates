#!/usr/bin/env python3
"""Build three deterministic Coffeetableviz chart views from the source CSV.

Original source is not modified. All measured values are computed from the
checked-in marathon major winners CSV. External record evidence is referenced
in project_manifest.md; no external records are invented by this script.
"""
import csv
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PROJECT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/marathon-majors/marathon_major_winners_men_2000_2026.csv"
DEST = PROJECT / "data"
ALIASES = {"Robert Cheruiyot": "Robert Kipkoech Cheruiyot"}
ISO3 = {"Kenya": "KEN", "Ethiopia": "ETH"}  # ISO 3166-1 alpha-3
BIRTH_DATE = date(1984, 11, 5)  # World Athletics athlete profile
CITY_CODE = {"Chicago": "CHI", "London": "LON", "Berlin": "BER", "Tokyo": "TOK"}
# Verified actual racing dates (not calendar-edition labels for Tokyo).
RACE_DATES = {
    "Chicago (2014)": "2014-10-12",
    "London (2015)": "2015-04-26",
    "Berlin (2015)": "2015-09-27",
    "London (2016)": "2016-04-24",
    "Berlin (2017)": "2017-09-24",
    "London (2018)": "2018-04-22",
    "Berlin (2018)": "2018-09-16",
    "London (2019)": "2019-04-28",
    "Tokyo (2021)": "2022-03-06",
    "Berlin (2022)": "2022-09-25",
    "Berlin (2023)": "2023-09-24",
}
DISPLAY_NAMES = {
    "Robert Kipkoech Cheruiyot": "R. K. Cheruiyot",
    "Haile Gebrselassie": "H. Gebrselassie",
}
RECORD_EVENTS = [
    ("London", 2002), ("Berlin", 2003), ("Berlin", 2007),
    ("Berlin", 2008), ("Berlin", 2011), ("Berlin", 2013),
    ("Berlin", 2014), ("Berlin", 2018), ("Berlin", 2022),
    ("Chicago", 2023), ("London", 2026),
]
RECORD_LABELS = {
    "Khalid Khannouchi": "Khannouchi",
    "Paul Tergat": "Tergat",
    "Haile Gebrselassie": "Gebrselassie",
    "Patrick Makau Musyoki": "Makau",
    "Wilson Kipsang": "Kipsang",
    "Dennis Kimetto": "Kimetto",
    "Eliud Kipchoge": "Kipchoge",
    "Kelvin Kiptum": "Kiptum",
    "Sabastian Sawe": "Sawe",
}

def secs(t):
    p = [int(v) for v in t.split(":")]
    assert len(p) == 3 and p[1] < 60 and p[2] < 60, t
    return p[0] * 3600 + p[1] * 60 + p[2]

def write(name, fields, rows):
    DEST.mkdir(parents=True, exist_ok=True)
    with (DEST / name).open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"{name}: {len(rows)} rows")

def main():
    with SOURCE.open(newline="", encoding="utf-8-sig") as fh:
        raw = list(csv.DictReader(fh))
    assert len(raw) == 154, f"Source row count changed: {len(raw)}"
    events = [r for r in raw if r["Event_Status"] == "Completed"]
    assert len(events) == 149, len(events)
    assert len({(r["Race"], r["Year"]) for r in raw}) == len(raw)
    for r in events:
        assert secs(r["Time"]) == int(r["Time_Seconds"]), r["Race_Year"]

    # Chart 1: count victories by named winner, reconciling one known alias.
    counts = Counter(ALIASES.get(r["Winner"], r["Winner"]) for r in events)
    assert counts["Eliud Kipchoge"] == 11
    leaders = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:7]
    assert leaders[0][1] == 11 and leaders[1][1] == 5
    nationals = {}
    for r in events:
        name = ALIASES.get(r["Winner"], r["Winner"])
        nationals.setdefault(name, set()).add(r["Nationality"])
    chart1 = []
    for name, total in leaders:
        countries = nationals[name]
        assert len(countries) == 1, f"Ambiguous nationality: {name}: {countries}"
        country = next(iter(countries))
        assert country in ISO3, f"Unknown ISO3 country: {country}"
        code = ISO3[country]
        chart1.append({
            "Runner": f"{DISPLAY_NAMES.get(name, name)} · {code}",
            "Winner": name,
            "Country": country,
            "ISO3": code,
            "Wins": total,
        })
    assert sum(r["ISO3"] == "KEN" for r in chart1) == 6
    write("01_major_win_rank.csv", ["Runner", "Winner", "Country", "ISO3", "Wins"], chart1)

    # Chart 2: 11 winning performances, in actual race-year chronology.
    k = [r for r in events if r["Winner"] == "Eliud Kipchoge"]
    assert len(k) == 11, len(k)
    perf = []
    for r in k:
        year = int(r["Year"])
        if r["Race"] == "Tokyo" and year == 2021:
            year = 2022  # 2021 edition took place on 6 March 2022
        assert r["Race_Year"] in RACE_DATES, f"Missing actual race date: {r['Race_Year']}"
        race_date = date.fromisoformat(RACE_DATES[r["Race_Year"]])
        assert race_date.year == year, r["Race_Year"]
        age = race_date.year - BIRTH_DATE.year - (
            (race_date.month, race_date.day) < (BIRTH_DATE.month, BIRTH_DATE.day)
        )
        code = CITY_CODE[r["Race"]]
        perf.append({
            "Year": year,
            "Race_Date": race_date.isoformat(),
            "Race_Year": r["Race_Year"],
            "Race": r["Race"],
            "City_Code": code,
            "Age": age,
            "City_Age_Label": f"{code} · {age}",
            "Time": r["Time"],
            "Seconds_Over_2h": secs(r["Time"]) - 7200,
        })
    perf.sort(key=lambda x: (x["Year"], x["Race_Year"]))
    assert min(r["Age"] for r in perf) == 29 and max(r["Age"] for r in perf) == 38
    assert {(r["Race_Year"], r["Age"]) for r in perf if r["Race_Year"] in ("Berlin (2018)", "Berlin (2022)")} == {("Berlin (2018)", 33), ("Berlin (2022)", 37)}
    write("02_kipchoge_winning_times.csv",
          ["Year", "Race_Date", "Race_Year", "Race", "City_Code", "Age", "City_Age_Label", "Time", "Seconds_Over_2h"], perf)

    # Chart 3: successive world-record improvements from a 2002 baseline.
    by_event = {(r["Race"], int(r["Year"])): r for r in events}
    record_rows = []
    prev = None
    for race, year in RECORD_EVENTS:
        source = by_event[(race, year)]
        winner = source["Winner"]
        seconds = secs(source["Time"])
        if prev is not None:
            improvement = prev - seconds
            assert improvement > 0, (race, year, improvement)
            record_rows.append({
                "Record": f"{RECORD_LABELS[winner]} · {race} · {year}",
                "City": race,
                "Winner": winner,
                "Year": year,
                "Time": source["Time"],
                "Seconds_Saved": improvement,
            })
        prev = seconds
    assert len(record_rows) == 10
    assert {(v["Year"], v["Seconds_Saved"]) for v in record_rows if v["Year"] in (2018, 2026)} == {(2018, 78), (2026, 65)}
    record_rows.sort(key=lambda x: (-x["Seconds_Saved"], x["Year"]))
    assert sum(r["City"] == "Berlin" for r in record_rows) == 8
    write("03_record_improvements.csv",
          ["Record", "City", "Winner", "Year", "Time", "Seconds_Saved"], record_rows)

if __name__ == "__main__":
    main()
