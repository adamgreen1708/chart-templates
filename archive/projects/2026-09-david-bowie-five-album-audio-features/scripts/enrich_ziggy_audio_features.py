#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import time
import unicodedata
from pathlib import Path

import requests
from bs4 import BeautifulSoup

PROJECT = Path(__file__).resolve().parents[1]
INPUT = PROJECT / "data" / "five_album_track_spine.csv"
OUTPUT = PROJECT / "data" / "ziggy_audio_features.csv"
API = "https://api.reccobeats.com/v1"
TARGET_ALBUM = "The Rise and Fall of Ziggy Stardust and the Spiders from Mars"
ARTIST = "David Bowie"
FEATURES = [
    "acousticness","danceability","energy","instrumentalness","liveness",
    "loudness","speechiness","tempo","valence",
]
KWORB_URL = "https://kworb.net/spotify/artist/0oSGxfWSnnOXhD2fKuz2Gy_songs.html"

SESSION = requests.Session()
SESSION.headers.update({"Accept":"application/json","User-Agent":"coffeetableviz-research/1.0"})


def get_json(url: str, params: dict | None = None, retries: int = 5):
    for attempt in range(retries):
        r = SESSION.get(url, params=params, timeout=60)
        if r.status_code == 429:
            wait = float(r.headers.get("Retry-After", "2"))
            time.sleep(max(wait, 1))
            continue
        r.raise_for_status()
        return r.json()
    raise RuntimeError(f"Rate limit persisted: {url}")


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = value.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    value = value.lower().strip()
    value = re.sub(r"\s+-\s+.*(?:remaster|remastered|mix|remix|live|edit|version).*?$", "", value, flags=re.I)
    value = re.sub(r"\s*\((?:\d{4}\s+)?(?:remaster|remastered|mix|remix|edit|version)[^)]*\)\s*$", "", value, flags=re.I)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def norm_full(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = value.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    value = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return " ".join(value.split())


def version_penalty(title: str) -> int:
    t = (title or "").lower()
    bad = ["live", "remix", "instrumental", "radio edit", "single version", "acoustic"]
    return 1 if any(x in t for x in bad) else 0


def kworb_spotify_ids() -> dict[str, str]:
    r = SESSION.get(KWORB_URL, timeout=60)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    out = {}
    for a in soup.find_all("a", href=True):
        href = a.get("href") or ""
        title = a.get_text(" ", strip=True)
        m = re.search(r"open\.spotify\.com/track/([A-Za-z0-9]+)", href)
        if m and title:
            out[norm_full(title)] = m.group(1)
    if not out:
        raise RuntimeError("Could not parse Spotify track links from Kworb")
    return out


def lookup_reccobeats_by_spotify_id(spotify_id: str) -> dict | None:
    data = get_json(f"{API}/track", {"ids": spotify_id})
    content = data.get("content", [])
    if len(content) != 1:
        return None
    return content[0]


def resolve_artist() -> dict:
    data = get_json(f"{API}/artist/search", {"searchText": ARTIST, "page": 0, "size": 20})
    exact = [x for x in data.get("content", []) if (x.get("name") or "").strip().lower() == ARTIST.lower()]
    if len(exact) != 1:
        raise RuntimeError(f"Expected one exact David Bowie artist result, got {len(exact)}: {exact}")
    return exact[0]


def fetch_artist_tracks(artist_id: str) -> list[dict]:
    all_rows = []
    for page in range(30):
        data = get_json(f"{API}/artist/{artist_id}/track", {"page": page, "size": 40})
        content = data.get("content", [])
        if not content:
            break
        all_rows.extend(content)
        if len(content) < 40:
            break
        time.sleep(0.4)
    if not all_rows:
        raise RuntimeError("ReccoBeats returned no tracks for David Bowie")
    return all_rows


def choose_match(row: dict, catalogue: list[dict]) -> tuple[dict | None, str]:
    key = norm(row["track_title"])
    candidates = [x for x in catalogue if norm(x.get("trackTitle") or "") == key]
    if not candidates:
        return None, "no_title_match"

    canonical = float(row["duration_seconds"])
    target_spotify_title = norm_full(row.get("spotify_title") or "")

    ranked = []
    for x in candidates:
        returned_title = x.get("trackTitle") or ""
        ms = x.get("durationMs")
        diff = 999999 if ms is None else abs(float(ms) / 1000 - canonical)

        exact_spotify = (
            0 if target_spotify_title and norm_full(returned_title) == target_spotify_title else 1
        )
        penalty = version_penalty(returned_title)

        # Ranking priority:
        # 1. exact match to the already-validated Spotify/Kworb version title;
        # 2. avoid live/remix/instrumental/edit alternatives;
        # 3. closest duration to the canonical album track.
        ranked.append(((exact_spotify, penalty, diff), x))

    ranked.sort(key=lambda z: z[0])
    (_, _, diff), best = ranked[0]

    if diff > 12:
        return None, f"closest_duration_diff_{diff:.1f}s"

    best = dict(best)
    best["_duration_diff"] = diff
    best["_candidate_count"] = len(candidates)
    best["_exact_spotify_title"] = (
        bool(target_spotify_title)
        and norm_full(best.get("trackTitle") or "") == target_spotify_title
    )
    return best, "matched"


def main():
    with INPUT.open(newline="", encoding="utf-8") as fh:
        rows = [r for r in csv.DictReader(fh) if r["album_title"] == TARGET_ALBUM]
    if len(rows) != 11:
        raise RuntimeError(f"Expected 11 Ziggy rows, got {len(rows)}")

    spotify_ids = kworb_spotify_ids()
    artist = None
    catalogue = None

    out = []
    for row in rows:
        spotify_id = spotify_ids.get(norm_full(row.get("spotify_title") or ""))
        match = None
        status = "no_spotify_id"
        match_method = ""

        if spotify_id:
            exact = lookup_reccobeats_by_spotify_id(spotify_id)
            if exact:
                match = dict(exact)
                ms = match.get("durationMs")
                diff = 999999 if ms is None else abs(float(ms) / 1000 - float(row["duration_seconds"]))
                match["_duration_diff"] = diff
                match["_candidate_count"] = 1
                match["_exact_spotify_title"] = True
                if diff <= 12:
                    status = "matched"
                    match_method = "exact_spotify_id"
                else:
                    match = None
                    status = f"spotify_id_duration_diff_{diff:.1f}s"

        if match is None:
            if catalogue is None:
                artist = resolve_artist()
                catalogue = fetch_artist_tracks(artist["id"])
                print(f"Fallback ReccoBeats artist: {artist['name']} ({artist['id']}); catalogue rows={len(catalogue)}")
            match, status = choose_match(row, catalogue)
            if match:
                match_method = "title_duration_fallback"

        result = dict(row)
        result.update({
            "reccobeats_match_status": status,
            "reccobeats_match_method": match_method,
            "spotify_track_id": spotify_id or "",
            "reccobeats_track_id": "",
            "reccobeats_track_title": "",
            "reccobeats_duration_seconds": "",
            "reccobeats_duration_diff_seconds": "",
            "reccobeats_candidate_count": "",
            "reccobeats_exact_spotify_title_match": "",
            "audio_feature_source": "ReccoBeats",
        })
        for name in FEATURES:
            result[name] = ""

        if match:
            result["reccobeats_track_id"] = match.get("id", "")
            result["reccobeats_track_title"] = match.get("trackTitle", "")
            result["reccobeats_duration_seconds"] = round(float(match.get("durationMs", 0)) / 1000, 3) if match.get("durationMs") is not None else ""
            result["reccobeats_duration_diff_seconds"] = round(match["_duration_diff"], 3)
            result["reccobeats_candidate_count"] = match["_candidate_count"]
            result["reccobeats_exact_spotify_title_match"] = "Yes" if match["_exact_spotify_title"] else "No"
            feat = get_json(f"{API}/track/{match['id']}/audio-features")
            for name in FEATURES:
                result[name] = feat.get(name, "")
            time.sleep(0.25)

        out.append(result)
        print(row["track_title"], status, result["reccobeats_track_title"], result["reccobeats_duration_diff_seconds"])

    fields = list(out[0].keys())
    with OUTPUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(out)

    matched = [r for r in out if r["reccobeats_match_status"] == "matched"]
    print(f"Wrote {len(out)} rows; matched={len(matched)}; unmatched={len(out)-len(matched)}")

    if len(matched) < 10:
        raise SystemExit(f"Coverage QA failed: only {len(matched)}/11 Ziggy tracks matched")

    for r in matched:
        for name in ["acousticness","danceability","energy","instrumentalness","liveness","speechiness","valence"]:
            v = float(r[name])
            if not (0 <= v <= 1):
                raise SystemExit(f"{name} outside 0-1 for {r['track_title']}: {v}")
        if float(r["tempo"]) <= 0:
            raise SystemExit(f"Non-positive tempo for {r['track_title']}")


if __name__ == "__main__":
    main()
