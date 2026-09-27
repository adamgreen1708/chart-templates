#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import time
import unicodedata
from collections import Counter
from pathlib import Path

import requests
from bs4 import BeautifulSoup

PROJECT = Path(__file__).resolve().parents[1]
INPUT = PROJECT / "data" / "five_album_track_spine.csv"
OUTPUT = PROJECT / "data" / "five_album_audio_features.csv"
API = "https://api.reccobeats.com/v1"
ARTIST = "David Bowie"
FEATURES = [
    "acousticness","danceability","energy","instrumentalness","liveness",
    "loudness","speechiness","tempo","valence",
]
KWORB_URL = "https://kworb.net/spotify/artist/0oSGxfWSnnOXhD2fKuz2Gy_songs.html"

SESSION = requests.Session()
SESSION.headers.update({"Accept":"application/json","User-Agent":"coffeetableviz-research/1.0"})


def get_json(url: str, params: dict | None = None, retries: int = 5):
    for _ in range(retries):
        r = SESSION.get(url, params=params, timeout=60)
        if r.status_code == 429:
            time.sleep(max(float(r.headers.get("Retry-After", "2")), 1))
            continue
        r.raise_for_status()
        return r.json()
    raise RuntimeError(f"Rate limit persisted: {url}")


def get_json_optional(url: str, params: dict | None = None):
    r = SESSION.get(url, params=params, timeout=60)
    if r.status_code in (400, 404):
        return None
    if r.status_code == 429:
        time.sleep(max(float(r.headers.get("Retry-After", "2")), 1))
        r = SESSION.get(url, params=params, timeout=60)
    r.raise_for_status()
    return r.json()


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = value.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    value = value.lower().strip()

    # Strip only a trailing version/remaster qualifier. Do not discard meaningful
    # subtitles before it: "Sweet Thing - Reprise; 2016 Remaster" must retain
    # "Reprise" so it can match the canonical album track.
    value = re.sub(
        r"\s*[-;]\s*(?:\d{4}\s+)?(?:remaster(?:ed)?|mix|remix|edit|version)[^;()]*$",
        "",
        value,
        flags=re.I,
    )
    value = re.sub(
        r"\s*\((?:\d{4}\s+)?(?:remaster(?:ed)?|mix|remix|edit|version)[^)]*\)\s*$",
        "",
        value,
        flags=re.I,
    )
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
    return content[0] if len(content) == 1 else None


def resolve_artist() -> dict:
    data = get_json(f"{API}/artist/search", {"searchText": ARTIST, "page": 0, "size": 20})
    exact = [x for x in data.get("content", []) if (x.get("name") or "").strip().lower() == ARTIST.lower()]
    if len(exact) != 1:
        raise RuntimeError(f"Expected one exact David Bowie result, got {len(exact)}")
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
        time.sleep(0.35)
    if not all_rows:
        raise RuntimeError("ReccoBeats returned no David Bowie tracks")
    return all_rows


ALBUM_SEARCH_TERMS = {
    "The Rise and Fall of Ziggy Stardust and the Spiders from Mars": "Ziggy Stardust",
    "Heroes": "Heroes",
    "Space Oddity": "Space Oddity",
    "Diamond Dogs": "Diamond Dogs",
    "Hunky Dory": "Hunky Dory",
}


def fetch_album_tracks(album_id: str) -> list[dict]:
    out = []
    for page in range(8):
        data = get_json(f"{API}/album/{album_id}/track", {"page": page, "size": 40})
        content = data.get("content", [])
        if not content:
            break
        out.extend(content)
        if len(content) < 40:
            break
        time.sleep(0.20)
    return out


def resolve_album_catalogues(rows: list[dict]) -> dict[str, list[dict]]:
    by_album: dict[str, list[dict]] = {}
    for row in rows:
        by_album.setdefault(row["album_title"], []).append(row)

    resolved: dict[str, list[dict]] = {}
    for album, canonical_rows in by_album.items():
        search_text = ALBUM_SEARCH_TERMS[album]
        data = get_json(f"{API}/album/search", {"searchText": search_text, "page": 0, "size": 40})
        candidates = []
        for candidate in data.get("content", []):
            artists = [str(a.get("name") or "").strip().lower() for a in candidate.get("artists", [])]
            if ARTIST.lower() not in artists:
                continue
            tracks = fetch_album_tracks(candidate["id"])
            if not tracks:
                continue

            title_keys = {norm(t.get("trackTitle") or "") for t in tracks}
            hits = sum(1 for r in canonical_rows if norm(r["track_title"]) in title_keys)

            diffs = []
            for r in canonical_rows:
                key = norm(r["track_title"])
                matches = [t for t in tracks if norm(t.get("trackTitle") or "") == key and t.get("durationMs") is not None]
                if matches:
                    canonical = float(r["duration_seconds"])
                    diffs.append(min(abs(float(t["durationMs"]) / 1000 - canonical) for t in matches))

            mean_diff = sum(diffs) / len(diffs) if diffs else 999999
            release = str(candidate.get("releaseDate") or "")
            target_year = str(canonical_rows[0]["album_year"])
            year_penalty = 0 if release.startswith(target_year) else 1
            candidates.append(((hits, -year_penalty, -mean_diff), candidate, tracks))

        if not candidates:
            print(f"Album catalogue unresolved | {album}")
            resolved[album] = []
            continue

        candidates.sort(key=lambda x: x[0], reverse=True)
        score, candidate, tracks = candidates[0]
        resolved[album] = tracks
        print(
            f"Album catalogue | {album} -> {candidate.get('albumTitle')} "
            f"({candidate.get('releaseDate')}) | track rows={len(tracks)} | title hits={score[0]}"
        )
    return resolved


def choose_match(row: dict, catalogue: list[dict]) -> tuple[dict | None, str]:
    key = norm(row["track_title"])
    candidates = [x for x in catalogue if norm(x.get("trackTitle") or "") == key]
    if not candidates:
        return None, "no_title_match"

    canonical = float(row["duration_seconds"])
    target_spotify_title = norm_full(row.get("spotify_title") or "")
    ranked = []
    for x in candidates:
        title = x.get("trackTitle") or ""
        ms = x.get("durationMs")
        diff = 999999 if ms is None else abs(float(ms) / 1000 - canonical)
        exact_spotify = 0 if target_spotify_title and norm_full(title) == target_spotify_title else 1
        ranked.append(((exact_spotify, version_penalty(title), diff), x))

    ranked.sort(key=lambda z: z[0])
    (_, _, diff), best = ranked[0]
    exact_title = bool(target_spotify_title) and norm_full(best.get("trackTitle") or "") == target_spotify_title

    # Exact validated version titles allow small mastering-duration differences.
    # Title-only fallbacks are intentionally stricter to avoid mixing versions.
    allowed_diff = 12 if exact_title else 5
    if diff > allowed_diff:
        return None, f"unconfident_version_diff_{diff:.1f}s"

    best = dict(best)
    best["_duration_diff"] = diff
    best["_candidate_count"] = len(candidates)
    best["_exact_spotify_title"] = exact_title
    return best, "matched"


def main():
    with INPUT.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if len(rows) != 53:
        raise RuntimeError(f"Expected 53 five-album rows, got {len(rows)}")

    spotify_ids = kworb_spotify_ids()
    album_catalogues = resolve_album_catalogues(rows)
    artist = None
    catalogue = None
    out = []

    for row in rows:
        spotify_id = spotify_ids.get(norm_full(row.get("spotify_title") or ""))
        match = None
        status = "no_spotify_id"
        match_method = ""

        if spotify_id:
            direct_features = get_json_optional(f"{API}/track/{spotify_id}/audio-features")
            if direct_features:
                match = {
                    "id": direct_features.get("id", spotify_id),
                    "trackTitle": row.get("spotify_title") or row["track_title"],
                    "durationMs": None,
                    "_duration_diff": 0.0,
                    "_candidate_count": 1,
                    "_exact_spotify_title": True,
                    "_features": direct_features,
                }
                status = "matched"
                match_method = "exact_spotify_id_audio_features"
            else:
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
            album_catalogue = album_catalogues.get(row["album_title"], [])
            if album_catalogue:
                match, status = choose_match(row, album_catalogue)
                if match:
                    match_method = "album_title_duration_fallback"

        if match is None:
            if catalogue is None:
                artist = resolve_artist()
                catalogue = fetch_artist_tracks(artist["id"])
                print(f"Fallback artist catalogue: {artist['name']} ({artist['id']}); rows={len(catalogue)}")
            match, status = choose_match(row, catalogue)
            if match:
                match_method = "artist_title_duration_fallback"

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
            if match.get("durationMs") is not None:
                result["reccobeats_duration_seconds"] = round(float(match["durationMs"]) / 1000, 3)
            result["reccobeats_duration_diff_seconds"] = round(match["_duration_diff"], 3)
            result["reccobeats_candidate_count"] = match["_candidate_count"]
            result["reccobeats_exact_spotify_title_match"] = "Yes" if match["_exact_spotify_title"] else "No"
            feat = match.get("_features") or get_json(f"{API}/track/{match['id']}/audio-features")
            for name in FEATURES:
                result[name] = feat.get(name, "")
            time.sleep(0.20)

        out.append(result)
        print(row["album_title"], "|", row["track_title"], "|", status, "|", match_method)

    fields = list(out[0].keys())
    with OUTPUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(out)

    matched = [r for r in out if r["reccobeats_match_status"] == "matched"]
    counts = Counter(r["album_title"] for r in matched)
    totals = Counter(r["album_title"] for r in out)
    print(f"Wrote {len(out)} rows; matched={len(matched)}; unmatched={len(out)-len(matched)}")
    for album in sorted(totals):
        print(f"Coverage | {album}: {counts[album]}/{totals[album]}")
        if counts[album] / totals[album] < 0.80:
            raise SystemExit(f"Coverage QA failed for {album}: {counts[album]}/{totals[album]}")

    for r in matched:
        for name in ["acousticness","danceability","energy","instrumentalness","liveness","speechiness","valence"]:
            v = float(r[name])
            if not (0 <= v <= 1):
                raise SystemExit(f"{name} outside 0-1 for {r['track_title']}: {v}")
        if float(r["tempo"]) <= 0:
            raise SystemExit(f"Non-positive tempo for {r['track_title']}")


if __name__ == "__main__":
    main()
