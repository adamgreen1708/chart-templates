#!/usr/bin/env python3
"""Read-only upstream health probe. Never publishes, merges or fabricates results.
The Analyst/Opta is for human review only; do not scrape its proprietary tables.
"""
import csv
import io
import json
from datetime import date, datetime
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen

SOURCES = {
  "football_data_co_uk": "https://www.football-data.co.uk/mmz4281/2627/E0.csv",
  "open_matchday": "https://raw.githubusercontent.com/oladeeayo/open-matchday/master/data/ENG_1_premier-league/results_2627.csv",
}

def probe(name, url):
    try:
        req = Request(url, headers={"User-Agent":"Mozilla/5.0 (compatible; coffeetableviz-source-probe/1.0)", "Accept":"text/csv,*/*"})
        with urlopen(req,timeout=25) as res:
            status=res.status
            content=res.read(4000000).decode("utf-8-sig")
        rows=list(csv.DictReader(io.StringIO(content)))
        if name=="football_data_co_uk":
            required={"Date","HomeTeam","AwayTeam","FTHG","FTAG","FTR"}
            if not rows or not required.issubset(rows[0]):
                raise ValueError("Not a valid Football-Data E0 CSV")
            completed=[r for r in rows if r.get("FTR") in ("H","A","D") and r.get("FTHG") and r.get("FTAG")]
            dates=[datetime.strptime(r["Date"],"%d/%m/%Y").date() for r in completed]
        else:
            required={"date","home","away","ft_home","ft_away","ft_result"}
            if not rows or not required.issubset(rows[0]):
                raise ValueError("Not a valid open-matchday CSV")
            completed=[r for r in rows if r.get("ft_result") in ("H","A","D") and r.get("ft_home") and r.get("ft_away")]
            dates=[date.fromisoformat(r["date"]) for r in completed]
        return {"source":name,"http_status":status,"completed":len(completed),"last_result":str(max(dates)) if dates else None,"reachable":True}
    except (URLError, HTTPError, ValueError, UnicodeError, TimeoutError, OSError) as e:
        return {"source":name, "reachable":False, "error":str(e)[:240]}

if __name__=="__main__":
    report=[probe(name,url) for name,url in SOURCES.items()]
    print("EPL 2026–27 source health check (READ ONLY; no automatic source switch):")
    for item in report:
        print(json.dumps(item,sort_keys=True))
    print("No provider automatically promoted. Compare to Opta Analyst manually for a recent-result spot-check.")
