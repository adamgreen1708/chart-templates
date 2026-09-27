#!/usr/bin/env python3
"""Build David Bowie's canonical lifetime studio-album track/duration table.

Input:
    data/source_album_spine.csv

Output:
    data/david_bowie_tracks_core.csv

The script deliberately builds the reproducible track spine first. Streaming
and UK-chart success are separate enrichments because they use different
sources and measure different concepts.

MusicBrainz is used for release-group identity, original-release selection and
track lengths. AllMusic album Styles are inherited from the validated album
spine with style_granularity='album'. Song-level AllMusic Styles are not
scraped here.
"""

from __future__ import annotations

import csv
import json
import time
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"
SPINE = DATA_DIR / "source_album_spine.csv"
OUTPUT = DATA_DIR / "david_bowie_tracks_core.csv"

API_ROOT = "https://musicbrainz.org/ws/2"
USER_AGENT = "coffeetableviz-chart-templates/1.0 (https://github.com/adamgreen1708/chart-templates)"
MIN_SECONDS_BETWEEN_CALLS = 1.1
MAX_RETRIES = 4
ARTIST_NAME = "David Bowie"

_last_call_at = 0.0


def throttle() -> None:
    global _last_call_at
    wait = MIN_SECONDS_BETWEEN_CALLS - (time.monotonic() - _last_call_at)
    if wait > 0:
        time.sleep(wait)


def get_json(url: str) -> dict[str, Any]:
    global _last_call_at
    last_error: Exception | None = None
    for attempt in range(MAX_RETRIES):
        throttle()
        req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        try:
            with urlopen(req, timeout=60) as response:
                payload = json.load(response)
            _last_call_at = time.monotonic()
            return payload
        except (HTTPError, URLError, TimeoutError) as exc:
            _last_call_at = time.monotonic()
            last_error = exc
            if attempt < MAX_RETRIES - 1:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"MusicBrainz request failed after retries: {url}") from last_error


def resolve_artist(name: str) -> dict[str, Any]:
    query = f'artist:"{name}"'
    url = f"{API_ROOT}/artist/?{urlencode({'query': query, 'fmt': 'json', 'limit': 25})}"
    data = get_json(url)
    exact = [a for a in data.get("artists", []) if a.get("name") == name]
    if len(exact) != 1:
        candidates = [
            {
                "id": a.get("id"),
                "name": a.get("name"),
                "disambiguation": a.get("disambiguation"),
                "country": a.get("country"),
                "score": a.get("score"),
            }
            for a in exact or data.get("artists", [])[:10]
        ]
        raise RuntimeError(f"Ambiguous artist resolution for {name!r}: {candidates}")
    return exact[0]


def browse_release_groups(artist_mbid: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    offset = 0
    while True:
        params = {
            "artist": artist_mbid,
            "type": "album",
            "release-group-status": "website-default",
            "limit": 100,
            "offset": offset,
            "fmt": "json",
        }
        data = get_json(f"{API_ROOT}/release-group?{urlencode(params)}")
        page = data.get("release-groups", [])
        rows.extend(page)
        offset += len(page)
        if not page or offset >= int(data.get("release-group-count", 0)):
            break
    return rows


def exact_artist_credit(rg: dict[str, Any], artist_mbid: str) -> bool:
    credits = rg.get("artist-credit") or []
    ids = [c.get("artist", {}).get("id") for c in credits if isinstance(c, dict)]
    return ids == [artist_mbid]


def choose_release(release_group_id: str) -> dict[str, Any]:
    params = {"inc": "releases", "fmt": "json"}
    rg = get_json(f"{API_ROOT}/release-group/{quote(release_group_id)}?{urlencode(params)}")
    releases = [r for r in rg.get("releases", []) if r.get("status") in (None, "Official")]
    if not releases:
        raise RuntimeError(f"No releases found for release group {release_group_id}")

    def key(r: dict[str, Any]) -> tuple[Any, ...]:
        date = r.get("date") or "9999-99-99"
        country = r.get("country") or ""
        country_rank = 0 if country == "GB" else 1 if country == "US" else 2
        return (date, country_rank, r.get("title") or "", r.get("id") or "")

    return sorted(releases, key=key)[0]


def fetch_release_tracks(release_id: str) -> dict[str, Any]:
    params = {"inc": "recordings", "fmt": "json"}
    return get_json(f"{API_ROOT}/release/{quote(release_id)}?{urlencode(params)}")


def mmss(seconds: int | None) -> str:
    if seconds is None:
        return ""
    return f"{seconds // 60}:{seconds % 60:02d}"


def main() -> None:
    with SPINE.open(newline="", encoding="utf-8") as fh:
        albums = list(csv.DictReader(fh))
    if len(albums) != 26:
        raise RuntimeError(f"Expected 26 validated studio albums, found {len(albums)}")

    artist = resolve_artist(ARTIST_NAME)
    artist_mbid = artist["id"]
    release_groups = [rg for rg in browse_release_groups(artist_mbid) if exact_artist_credit(rg, artist_mbid)]

    by_title: dict[str, list[dict[str, Any]]] = {}
    for rg in release_groups:
        by_title.setdefault((rg.get("title") or "").strip(), []).append(rg)

    out: list[dict[str, Any]] = []

    for album in albums:
        title = album["title"].strip()
        matches = by_title.get(title, [])
        if len(matches) != 1:
            raise RuntimeError(
                f"Release-group match for {title!r} returned {len(matches)} exact matches; "
                "review rather than guessing."
            )

        rg = matches[0]
        release = choose_release(rg["id"])
        release_payload = fetch_release_tracks(release["id"])

        track_rows: list[dict[str, Any]] = []
        for disc_number, medium in enumerate(release_payload.get("media", []), start=1):
            for track in medium.get("tracks", []):
                recording = track.get("recording") or {}
                length_ms = track.get("length")
                if length_ms is None:
                    length_ms = recording.get("length")
                seconds = round(length_ms / 1000) if isinstance(length_ms, int) else None
                track_rows.append(
                    {
                        "album_sequence": int(album["sequence"]),
                        "album_year": int(album["year"]),
                        "album_title": title,
                        "disc_number": disc_number,
                        "track_number": track.get("number") or track.get("position"),
                        "track_position": track.get("position"),
                        "track_title": track.get("title") or recording.get("title"),
                        "duration_ms": length_ms if isinstance(length_ms, int) else "",
                        "duration_seconds": seconds if seconds is not None else "",
                        "duration_display": mmss(seconds),
                        "decade": f"{(int(album['year']) // 10) * 10}s",
                        "allmusic_album_styles": album.get("allmusic_styles", ""),
                        "allmusic_album_style_count": album.get("allmusic_style_count", ""),
                        "style_granularity": "album",
                        "allmusic_album_url": album.get("allmusic_source_url", ""),
                        "musicbrainz_release_group_id": rg["id"],
                        "musicbrainz_release_id": release["id"],
                        "musicbrainz_recording_id": recording.get("id", ""),
                        "source_release_date": release.get("date", ""),
                        "source_release_country": release.get("country", ""),
                        "duration_status": "available" if seconds is not None else "missing",
                    }
                )

        if not track_rows:
            raise RuntimeError(f"No tracks found for {title!r} using release {release['id']}")
        out.extend(track_rows)

    fields = list(out[0].keys())
    with OUTPUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out)

    missing = sum(row["duration_status"] == "missing" for row in out)
    print(f"Wrote {len(out)} canonical track rows across {len(albums)} albums; missing durations={missing}")


if __name__ == "__main__":
    main()
