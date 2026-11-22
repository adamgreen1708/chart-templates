#!/usr/bin/env python3
"""Validated, monotonic 2026–27 EPL result snapshot; source: Football-Data.co.uk E0.csv."""
from __future__ import annotations
import argparse
import csv
import io
import json
import time
from collections import defaultdict
from datetime import datetime, date
from pathlib import Path
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[4]
PROJECT = Path(__file__).resolve().parents[1]
INPUT = PROJECT / "data/matches_2627.csv"
OUTPUT = ROOT / "site/assets/data/epl-2627-unfolded.json"
SOURCE = "https://www.football-data.co.uk/mmz4281/2627/E0.csv"
MIRROR = "https://github.com/learningEngineer24/premier-league-predictor/blob/main/data/raw/E0_2627.csv"
FIELDS = ["Div","Date","Time","HomeTeam","AwayTeam","FTHG","FTAG","FTR"]
CLUBS = ["Arsenal","Aston Villa","Bournemouth","Brentford","Brighton","Chelsea",
         "Coventry","Crystal Palace","Everton","Fulham","Hull","Ipswich","Leeds",
         "Liverpool","Man City","Man United","Newcastle","Nott'm Forest","Sunderland","Tottenham"]

def validate(text, today=None):
    today = today or datetime.now(ZoneInfo("Europe/London")).date()
    parsed = csv.DictReader(io.StringIO(text.lstrip("\ufeff")))
    if not parsed.fieldnames or any(f not in parsed.fieldnames for f in FIELDS):
        raise ValueError("Source is not the expected E0 CSV schema (possibly HTML redirect)")
    complete = []
    seen = set()
    for raw in parsed:
        if not raw or not any(raw.values()):
            continue
        if raw.get("Div","").strip() != "E0":
            raise ValueError("Unexpected league or malformed E0 row")
        home,away=raw["HomeTeam"].strip(),raw["AwayTeam"].strip()
        if home not in CLUBS or away not in CLUBS or home==away:
            raise ValueError(f"Unknown 2026–27 Premier League club: {home} / {away}")
        score=[(raw.get(f) or "").strip() for f in ("FTHG","FTAG","FTR")]
        if not any(score):  # unplayed fixture: never publish a guessed result
            continue
        if not all(score):
            raise ValueError(f"Partially populated full-time result: {home} / {away}")
        when=datetime.strptime(raw["Date"].strip(), "%d/%m/%Y").date()
        if when < date(2026,8,1) or when > date(2027,5,31) or when > today:
            raise ValueError(f"Result outside completed season/date range: {when}")
        hg,ag=int(score[0]),int(score[1])
        if hg<0 or ag<0 or score[2] != ("H" if hg>ag else "A" if hg<ag else "D"):
            raise ValueError(f"Invalid full-time score/result: {home} v {away}")
        key=(home,away)
        if key in seen:
            raise ValueError(f"Duplicate home/away fixture: {home} v {away}")
        seen.add(key)
        clean={f:(raw.get(f) or "").strip() for f in FIELDS}
        complete.append(clean)
    if not 1<=len(complete)<=380:
        raise ValueError(f"Unexpected completed fixture total: {len(complete)}")
    if set(x for m in complete for x in (m["HomeTeam"],m["AwayTeam"])) != set(CLUBS):
        raise ValueError("Expected 20 participating clubs in completed results")
    complete.sort(key=lambda m:(datetime.strptime(m["Date"],"%d/%m/%Y").date().isoformat(),m["Time"],m["HomeTeam"],m["AwayTeam"]))
    plays=defaultdict(lambda: {"H":0,"A":0})
    for m in complete:
        plays[m["HomeTeam"]]["H"]+=1
        plays[m["AwayTeam"]]["A"]+=1
    if any(v["H"]>19 or v["A"]>19 for v in plays.values()):
        raise ValueError("More than 19 completed fixtures at one venue")
    if len(complete)==380 and any(v["H"]!=19 or v["A"]!=19 for v in plays.values()):
        raise ValueError("Full season venue balance failed")
    return complete

def csv_text(matches):
    buf=io.StringIO(newline="")
    writer=csv.DictWriter(buf,fieldnames=FIELDS,lineterminator="\n")
    writer.writeheader()
    writer.writerows(matches)
    return buf.getvalue()

def season_json(matches):
    by_team={club:[] for club in CLUBS}
    for m in matches:
        when=datetime.strptime(m["Date"], "%d/%m/%Y").date().isoformat()
        home,away=m["HomeTeam"],m["AwayTeam"]
        hg,ag=int(m["FTHG"]),int(m["FTAG"])
        for name,venue in ((home,"H"),(away,"A")):
            gf,ga=(hg,ag) if venue=="H" else (ag,hg)
            by_team[name].append(dict(date=when,opponent=away if venue=="H" else home,
                                      venue=venue,gf=gf,ga=ga,
                                      result="W" if gf>ga else "L" if gf<ga else "D",
                                      _time=m["Time"]))
    teams=[]
    for name, games in by_team.items():
        games.sort(key=lambda g:(g["date"],g["_time"],g["opponent"]))
        pts=gf=ga=w=d=l=0
        output_games=[]
        for i,g in enumerate(games,1):
            pts+=3 if g["result"]=="W" else 1 if g["result"]=="D" else 0
            gf+=g["gf"];ga+=g["ga"]
            w+=g["result"]=="W";d+=g["result"]=="D";l+=g["result"]=="L"
            output_games.append(dict(number=i,date=g["date"],opponent=g["opponent"],
                                     venue=g["venue"],gf=g["gf"],ga=g["ga"],
                                     result=g["result"],points=pts))
        teams.append(dict(name=name,played=len(games),points=pts,gd=gf-ga,
                          gf=gf,ga=ga,w=w,d=d,l=l,games=output_games))
    teams.sort(key=lambda t:(-t["points"],-t["gd"],-t["gf"],t["name"]))
    for i,team in enumerate(teams,1):
        team["rank"]=i
    dates=[datetime.strptime(m["Date"], "%d/%m/%Y").date().isoformat() for m in matches]
    meta=dict(season="2026–27",scope="English Premier League",matchCount=len(matches),
              teamCount=20,firstDate=min(dates),lastDate=max(dates),complete=len(matches)==380,
              x_definition="Each club's nth completed league match, not a shared fixture week",
              source=SOURCE,source_mirror_initial=MIRROR,
              source_note="Only validated completed matches. Provisional standings until 380 verified results.")
    if sum(t["played"] for t in teams)!=2*len(matches):
        raise ValueError("Team match totals do not balance")
    return json.dumps(dict(meta=meta,teams=teams),indent=2,ensure_ascii=False)+"\n"

def fetch_source():
    request=Request(SOURCE,headers={"User-Agent":"Mozilla/5.0 (compatible; coffeetableviz-data-refresh/1.0)","Accept":"text/csv,*/*"})
    for attempt in range(1,4):
        try:
            with urlopen(request,timeout=40) as response:
                payload=response.read(3000000)
            text=payload.decode("utf-8-sig")
            if "HomeTeam" not in text[:2000]:
                raise ValueError("Football-Data returned no CSV header; refusing an HTML fallback")
            return text
        except (OSError,ValueError,UnicodeError) as exc:
            if attempt==3:
                raise RuntimeError("Direct Football-Data.co.uk fetch failed after three attempts") from exc
            print(f"Source attempt {attempt} failed: {exc}",flush=True)
            time.sleep(6*attempt)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--refresh",action="store_true",help="Download original 2627/E0.csv, validate and reject changes to past scores")
    parser.add_argument("--check",action="store_true",help="Fail if committed CSV/JSON differs from deterministic rebuild")
    args=parser.parse_args()
    old=validate(INPUT.read_text(encoding="utf-8-sig"))
    matches=validate(fetch_source()) if args.refresh else old
    old_scores={(r["HomeTeam"],r["AwayTeam"]):(r["FTHG"],r["FTAG"],r["FTR"],r["Date"]) for r in old}
    new_scores={(r["HomeTeam"],r["AwayTeam"]):(r["FTHG"],r["FTAG"],r["FTR"],r["Date"]) for r in matches}
    missing=set(old_scores)-set(new_scores)
    revised=[k for k,v in old_scores.items() if k in new_scores and new_scores[k]!=v]
    if missing or revised or len(matches)<len(old):
        raise ValueError(f"Historical results disappeared/changed; editorial review required. Missing={sorted(missing)} revised={sorted(revised)}")
    csv_out=csv_text(matches)
    json_out=season_json(matches)
    if args.check:
        if INPUT.read_text(encoding="utf-8-sig")!=csv_out or OUTPUT.read_text(encoding="utf-8")!=json_out:
            raise ValueError("Committed snapshot does not match deterministic source build")
    else:
        INPUT.write_text(csv_out,encoding="utf-8")
        OUTPUT.parent.mkdir(parents=True,exist_ok=True)
        OUTPUT.write_text(json_out,encoding="utf-8")
    print(f"PASS: {len(matches)} verified completed matches, 20 clubs, last result {max(m['Date'] for m in matches)}")
if __name__=="__main__":
    main()
