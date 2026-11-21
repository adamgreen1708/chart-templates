#!/usr/bin/env python3
"""Reproducible ONS-derived boys' name chart views. Run from repository root."""
import csv, hashlib, io
from collections import defaultdict
from pathlib import Path
from urllib.request import urlopen, Request

DATA = Path(__file__).resolve().parents[1] / "data"
URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2026/2026-06-16/england_wales_names.csv"
PIN = "2d2c3837eb1d3c82601bdf5539e95ffab15d0579"
NAMES = ("Adam", "Adrian", "Alex")
YEARS = range(1996, 2025)

def write(filename, fields, rows):
    with (DATA / filename).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

def main():
    with urlopen(Request(URL, headers={"User-Agent":"Coffeetableviz-A-Team/1.0"}),timeout=90) as f:
        raw=f.read()
    digest=hashlib.sha1(("blob %d\0"%len(raw)).encode()+raw).hexdigest()
    assert digest==PIN, ("upstream source changed; stop and review",digest)
    reader=csv.DictReader(io.StringIO(raw.decode("utf-8-sig")))
    assert {"Year","Sex","Name","Number","Rank"}<=set(reader.fieldnames or [])
    chosen, totals, letters, seen = {}, defaultdict(int), defaultdict(int),set()
    n=0
    for r in reader:
        if r["Sex"].lower().strip() not in ("boy","male"):
            continue
        year=int(r["Year"])
        if year not in YEARS:
            continue
        name=r["Name"].strip()
        key=(year,name)
        assert key not in seen, "duplicate boy name/year"
        seen.add(key)
        count=int(float(r["Number"]))
        rank=int(float(r["Rank"]))
        assert count>=3 and rank>0
        totals[year]+=count
        if name and name[0].upper() in ("A","J"):
            letters[(year,name[0].upper())]+=count
        if name in NAMES:
            chosen[key]={"year":year,"name":name,"births":count,"rank":rank}
        n+=1
    assert n>100000 and len(totals)==29
    assert len(chosen)==87, "One or more brother-year observations missing"
    assert min(totals.values())>200000, "Unexpected total published registrations"
    annual=[chosen[(y,name)] for name in NAMES for y in YEARS]
    write("chart_02_annual.csv",["year","name","births","rank"],annual)

    historical=list(csv.DictReader((DATA/"historical_ranks.csv").open(encoding="utf-8")))
    expected={(1944,"Adrian",74),(1954,"Adrian",54),(1964,"Adrian",30),
       (1964,"Adam",68),(1974,"Adrian",38),(1974,"Adam",35),
       (1984,"Adrian",63),(1984,"Adam",12),(1984,"Alex",79),
       (1994,"Adam",11),(1994,"Alex",50)}
    assert len(historical)==11
    assert {(int(r["year"]),r["name"],int(r["rank"])) for r in historical}==expected
    write("chart_01_historical.csv",["year","name","rank"],historical)

    rows=[{"year":y,"initial":l,"share_pct":round(100*letters[(y,l)]/totals[y],5),
           "registrations":letters[(y,l)],"published_total":totals[y]}
          for l in ("A","J") for y in YEARS]
    write("chart_03_initial_shares.csv",
          ["year","initial","share_pct","registrations","published_total"],rows)
    v={(r["year"],r["initial"]):r["share_pct"] for r in rows}
    assert v[(2024,"A")]>v[(1996,"A")] and v[(2024,"J")]<v[(1996,"J")], "Unverified editorial A/J movement"
    lines=["# A-Team source evidence", "", "England and Wales, boys; 1996–2024; exact-name counts/ranks.",
      "Pinned Git blob: "+digest, "Boy-name records: "+str(n),
      "Historical top-100 rankings: ten-year observations only.",
      "Letter-share denominator: all published boy-name registrations, excluding suppressed 1–2 counts.",
      "2025 data are NOT included in this chart series.", "", "## Brothers"]
    for name in NAMES:
        a,b=chosen[(1996,name)],chosen[(2024,name)]
        lines.append(f"- {name}: 1996 {a['births']} births, rank {a['rank']}; 2024 {b['births']} births, rank {b['rank']}.")
    lines.extend(["", "## Published first-letter shares"])
    for y in (1996,2024):
        lines.append(f"- {y}: A {v[(y,'A')]:.2f}%, J {v[(y,'J')]:.2f}%")
    (DATA/"story_evidence.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print("\n".join(lines))
    print("PASS: source hash, rows, rank snapshots, complete annual series, initial denominators")

if __name__=="__main__":
    main()
