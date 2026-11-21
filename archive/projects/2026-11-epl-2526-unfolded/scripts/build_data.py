#!/usr/bin/env python3
"""Rebuild the standalone EPL interactive dataset from a frozen 380-fixture CSV."""
from collections import defaultdict
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[4]
PROJECT = Path(__file__).resolve().parents[1]
INPUT = PROJECT / "data" / "matches_2526.csv"
OUTPUT = ROOT / "site" / "assets" / "data" / "epl-2526-unfolded.json"

META = json.loads("{\"season\":\"2025–26\",\"scope\":\"English Premier League\",\"matchCount\":380,\"teamCount\":20,\"firstDate\":\"2025-08-15\",\"lastDate\":\"2026-05-24\",\"x_definition\":\"Each club's nth completed league match; not simultaneous calendar matchweeks\",\"source\":\"Football-Data.co.uk E0.csv via qhtexas/football-dataset\",\"source_mirror\":\"https://github.com/qhtexas/football-dataset/blob/9ec38fd9149216e3110d8b6edb1c0e8457d3016b/datasets/premier-league/season-2526.csv\",\"source_upstream\":\"https://www.football-data.co.uk/mmz4281/2526/E0.csv\",\"source_blob_sha\":\"92c659f51c53f7a0212892ed2796db8e324da74d\",\"retrieved\":\"2026-11-21\",\"provenance_note\":\"Full-time results only; no fabricated matchweek assignments; all points recomputed.\"}")  # frozen source metadata
def main():
    with INPUT.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 380, f"Expected 380 matches, got {len(rows)}"
    seen = set()
    by_team = defaultdict(list)
    for m in rows:
        home, away = m["HomeTeam"], m["AwayTeam"]
        hg, ag = int(m["FTHG"]), int(m["FTAG"])
        assert (home, away) not in seen, f"Duplicate home-away fixture: {home} v {away}"
        seen.add((home, away))
        assert hg >= 0 and ag >= 0 and m["FTR"] == ("H" if hg > ag else "A" if hg < ag else "D")
        for name, is_home in ((home, True), (away, False)):
            gf, ga = (hg, ag) if is_home else (ag, hg)
            by_team[name].append(dict(
                date=m["Date"], opponent=away if is_home else home,
                venue="H" if is_home else "A", gf=gf, ga=ga,
                result="W" if gf > ga else "L" if gf < ga else "D",
            ))
    assert len(by_team) == 20, "Expected exactly 20 clubs"
    teams = []
    for name, fixtures in by_team.items():
        assert len(fixtures) == 38, f"{name}: expected 38 fixtures"
        fixtures.sort(key=lambda m: m["date"])
        points = 0
        gf_total = ga_total = wins = draws = losses = 0
        games = []
        for i, game in enumerate(fixtures, 1):
            result = game["result"]
            points += 3 if result == "W" else 1 if result == "D" else 0
            gf_total += game["gf"]
            ga_total += game["ga"]
            wins += result == "W"
            draws += result == "D"
            losses += result == "L"
            games.append(dict(number=i, **game, points=points))
        teams.append(dict(
            name=name, played=38, points=points, gd=gf_total-ga_total,
            gf=gf_total, ga=ga_total, w=wins, d=draws, l=losses, games=games
        ))
    teams.sort(key=lambda t: (-t["points"], -t["gd"], -t["gf"], t["name"]))
    for i, team in enumerate(teams, 1):
        team["rank"] = i
    assert teams[0]["name"] == "Arsenal" and teams[0]["points"] == 85
    assert teams[1]["name"] == "Man City" and teams[1]["points"] == 78
    assert sum(t["w"] for t in teams) == sum(t["l"] for t in teams)
    assert sum(t["d"] for t in teams) % 2 == 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(dict(meta=META, teams=teams), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Validated and rendered {len(rows)} fixtures, {len(teams)} clubs -> {OUTPUT}")

if __name__ == "__main__":
    main()
