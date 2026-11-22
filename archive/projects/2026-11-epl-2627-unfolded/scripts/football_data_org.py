#!/usr/bin/env python3
"""Strict football-data.org v4 Premier League finished-match adapter.

Only full-time FINISHED results for the explicit 2026 season are eligible.
No token, scheduled fixture, inferred score or unofficial table is published.
"""
from __future__ import annotations
import csv
import io
import json
import os
import re
import time
from datetime import date, datetime
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

API_URL = "https://api.football-data.org/v4/competitions/PL/matches?season=2026"
SOURCE_URL = "https://www.football-data.org/"
FIELDS = ["Div", "Date", "Time", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"]
ALIASES = {
    "Arsenal": ("Arsenal", "Arsenal FC"),
    "Aston Villa": ("Aston Villa", "Aston Villa FC"),
    "Bournemouth": ("Bournemouth", "AFC Bournemouth", "Bournemouth AFC"),
    "Brentford": ("Brentford", "Brentford FC"),
    "Brighton": ("Brighton", "Brighton & Hove Albion", "Brighton and Hove Albion", "Brighton & Hove Albion FC"),
    "Chelsea": ("Chelsea", "Chelsea FC"),
    "Coventry": ("Coventry", "Coventry City", "Coventry City FC"),
    "Crystal Palace": ("Crystal Palace", "Crystal Palace FC"),
    "Everton": ("Everton", "Everton FC"),
    "Fulham": ("Fulham", "Fulham FC"),
    "Hull": ("Hull", "Hull City", "Hull City AFC", "Hull City FC"),
    "Ipswich": ("Ipswich", "Ipswich Town", "Ipswich Town FC"),
    "Leeds": ("Leeds", "Leeds United", "Leeds United FC"),
    "Liverpool": ("Liverpool", "Liverpool FC"),
    "Man City": ("Man City", "Manchester City", "Manchester City FC"),
    "Man United": ("Man United", "Manchester United", "Manchester United FC"),
    "Newcastle": ("Newcastle", "Newcastle United", "Newcastle United FC"),
    "Nott'm Forest": ("Nott'm Forest", "Nottingham Forest", "Nottingham Forest FC"),
    "Sunderland": ("Sunderland", "Sunderland AFC", "Sunderland FC"),
    "Tottenham": ("Tottenham", "Tottenham Hotspur", "Tottenham Hotspur FC"),
}

def _norm(value):
    return re.sub(r"[^a-z0-9]", "", str(value).casefold().replace("&", "and"))

LOOKUP = {}
for canonical, variants in ALIASES.items():
    for alias in variants:
        key = _norm(alias)
        if key in LOOKUP and LOOKUP[key] != canonical:
            raise RuntimeError("Ambiguous alias configuration")
        LOOKUP[key] = canonical

def club_name(team):
    if not isinstance(team, dict):
        raise ValueError("Invalid team object in football-data.org response")
    matches = {LOOKUP[_norm(team[key])] for key in ("name", "shortName")
               if isinstance(team.get(key), str) and _norm(team[key]) in LOOKUP}
    if len(matches) != 1:
        raise ValueError("Unknown or inconsistent Premier League team: " + repr({
            "name": team.get("name"), "shortName": team.get("shortName")}))
    return matches.pop()

def convert_payload(payload):
    if not isinstance(payload, dict):
        raise ValueError("Invalid football-data.org JSON envelope")
    if not isinstance(payload.get("competition"), dict) or payload["competition"].get("code") != "PL":
        raise ValueError("Provider response is not Premier League")
    match_list = payload.get("matches")
    if not isinstance(match_list, list) or not match_list:
        raise ValueError("Football-data.org returned no season match list")
    result = []
    seen_ids = set()
    for match in match_list:
        if not isinstance(match, dict):
            raise ValueError("Malformed match object")
        if match.get("status") != "FINISHED":
            continue
        season = match.get("season")
        if not isinstance(season, dict) or not str(season.get("startDate", "")).startswith("2026-"):
            raise ValueError("Finished match has incorrect season")
        competition = match.get("competition")
        if isinstance(competition, dict) and competition.get("code") != "PL":
            raise ValueError("Non-PL match in PL feed")
        match_id = match.get("id")
        if type(match_id) is not int or match_id in seen_ids:
            raise ValueError("Missing or duplicated finished match ID")
        seen_ids.add(match_id)
        home = club_name(match.get("homeTeam"))
        away = club_name(match.get("awayTeam"))
        if home == away:
            raise ValueError("Same home and away team")
        score = match.get("score")
        full = score.get("fullTime") if isinstance(score, dict) else None
        if not isinstance(full, dict):
            raise ValueError("No full-time score for FINISHED match")
        hg, ag = full.get("home"), full.get("away")
        if type(hg) is not int or type(ag) is not int or hg < 0 or ag < 0:
            raise ValueError("Invalid FINISHED full-time score")
        winner = "HOME_TEAM" if hg > ag else "AWAY_TEAM" if ag > hg else "DRAW"
        if score.get("winner") not in (None, winner):
            raise ValueError("Inconsistent provider score/winner")
        when_str = match.get("utcDate")
        if not isinstance(when_str, str):
            raise ValueError("Finished match missing UTC kickoff")
        try:
            utc = datetime.fromisoformat(when_str.replace("Z", "+00:00"))
            if utc.tzinfo is None:
                raise ValueError("Kickoff timezone missing")
            uk = utc.astimezone(ZoneInfo("Europe/London"))
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid finished match date") from exc
        result.append({
            "Div": "E0", "Date": uk.strftime("%d/%m/%Y"),
            "Time": uk.strftime("%H:%M"), "HomeTeam": home,
            "AwayTeam": away, "FTHG": str(hg), "FTAG": str(ag),
            "FTR": "H" if hg > ag else "A" if hg < ag else "D",
        })
    if not result:
        raise ValueError("No FINISHED matches with scores")
    csv_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(csv_buffer, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(result)
    return csv_buffer.getvalue()

# Confirmed via authenticated PR workflow run on 22 Nov 2026: the API returned
# 107 real FINISHED fixtures through 21 Nov; a second API request immediately
# returned a stale 100-game snapshot. Keep this dated, evidence-based floor:
# accepting fewer matches would knowingly throw away legitimate results.
VERIFIED_FLOOR = 107
VERIFIED_THROUGH = date(2026, 11, 21)

def fetch_source():
    token = os.environ.get("FOOTBALL_DATA_ORG_TOKEN", "").strip()
    if not token:
        raise RuntimeError("GitHub secret FOOTBALL_DATA_ORG_TOKEN is missing")
    request = Request(API_URL, headers={
        "X-Auth-Token": token,
        "Accept": "application/json",
        "Cache-Control": "no-cache",
        "User-Agent": "coffeetableviz-2627-verified-results/1.0",
    })
    last_count = 0
    last_date = None
    for attempt in range(3):
        try:
            with urlopen(request, timeout=45) as response:
                raw = response.read(4000001)
                if len(raw) > 4000000:
                    raise ValueError("Provider payload exceeds reasonable EPL season size")
        except HTTPError as exc:
            raise RuntimeError(f"football-data.org returned HTTP {exc.code} (token, plan or API access issue)") from None
        except (URLError, OSError, TimeoutError) as exc:
            raise RuntimeError("Could not contact football-data.org securely") from exc
        try:
            payload = json.loads(raw.decode("utf-8-sig"))
        except (ValueError, UnicodeError) as exc:
            raise ValueError("Provider returned invalid JSON") from exc
        converted = convert_payload(payload)
        finished = list(csv.DictReader(io.StringIO(converted)))
        last_count = len(finished)
        last_date = max(datetime.strptime(m["Date"], "%d/%m/%Y").date() for m in finished)
        if last_count >= VERIFIED_FLOOR and last_date >= VERIFIED_THROUGH:
            return converted
        print(f"Stale provider cache response ({last_count} finished, latest {last_date}); "
              f"verified minimum is {VERIFIED_FLOOR} through {VERIFIED_THROUGH}. "
              "Will not publish this response.", flush=True)
        if attempt < 2:
            time.sleep(4 * (attempt + 1))
    raise RuntimeError(
        f"football-data.org remained stale after three requests: {last_count} fixtures "
        f"through {last_date}; at least {VERIFIED_FLOOR} through {VERIFIED_THROUGH} required")
