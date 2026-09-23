#!/usr/bin/env python3
"""Build the source dataset for the David Bowie reinvention project.

Outputs:
- data/artist_album_spans.csv
- data/david_bowie_album_genres.csv
- data/source_metadata.json

This script intentionally stops before creating a reinvention/reset metric.
The focus chronology must be inspected and cross-checked against the official
David Bowie discography before derived story datasets are frozen.
"""

from __future__ import annotations

import csv
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"
SEED_FILE = DATA_DIR / "artist_cohort_seed.csv"

API_ROOT = "https://musicbrainz.org/ws/2"
USER_AGENT = "coffeetableviz-chart-templates/1.0 (https://github.com/adamgreen1708/chart-templates)"
MIN_SECONDS_BETWEEN_CALLS = 1.1
MAX_RETRIES = 4

FOCUS_ARTIST = "David Bowie"

# Secondary types that are not ordinary studio-album scope for this project.
NON_STUDIO_SECONDARY_TYPES = {
    "Compilation",
    "Live",
    "Soundtrack",
    "Remix",
    "DJ-mix",
    "Mixtape/Street",
    "Demo",
    "Interview",
    "Audiobook",
    "Audio drama",
    "Field recording",
    "Spokenword",
}

_last_call_at = 0.0


def _throttle() -> None:
    global _last_call_at
    now = time.monotonic()
    wait = MIN_SECONDS_BETWEEN_CALLS - (now - _last_call_at)
    if wait > 0:
        time.sleep(wait)


def get_json(url: str) -> dict[str, Any]:
    global _last_call_at
    last_error: Exception | None = None

    for attempt in range(MAX_RETRIES):
        _throttle()
        req = Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "application/json",
            },
        )
        try:
            with urlopen(req, timeout=60) as response:
                payload = json.load(response)
            _last_call_at = time.monotonic()
            return payload
        except (HTTPError, URLError, TimeoutError) as exc:
            _last_call_at = time.monotonic()
            last_error = exc
            if attempt == MAX_RETRIES - 1:
                break
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
                "sort-name": a.get("sort-name"),
                "type": a.get("type"),
                "country": a.get("country"),
                "disambiguation": a.get("disambiguation"),
                "score": a.get("score"),
            }
            for a in exact or data.get("artists", [])[:10]
        ]
        raise RuntimeError(
            f"Artist resolution for {name!r} returned {len(exact)} exact matches. "
            f"Review candidates instead of guessing: {candidates}"
        )

    return exact[0]


def browse_album_release_groups(artist_mbid: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    offset = 0
    limit = 100

    while True:
        params = {
            "artist": artist_mbid,
            "type": "album",
            "release-group-status": "website-default",
            "limit": limit,
            "offset": offset,
            "fmt": "json",
        }
        url = f"{API_ROOT}/release-group?{urlencode(params)}"
        data = get_json(url)
        page = data.get("release-groups", [])
        rows.extend(page)

        offset += len(page)
        if not page or offset >= int(data.get("release-group-count", 0)):
            break

    return rows


def is_exact_artist_credit(rg: dict[str, Any], artist_mbid: str) -> bool:
    credits = rg.get("artist-credit") or []
    credited_artists = [c.get("artist", {}).get("id") for c in credits if isinstance(c, dict)]
    return credited_artists == [artist_mbid]


def is_qualifying_album(rg: dict[str, Any], artist_mbid: str) -> bool:
    if rg.get("primary-type") != "Album":
        return False
    if not is_exact_artist_credit(rg, artist_mbid):
        return False

    secondary = set(rg.get("secondary-types") or [])
    if secondary & NON_STUDIO_SECONDARY_TYPES:
        return False

    first_date = rg.get("first-release-date") or ""
    if len(first_date) < 4 or not first_date[:4].isdigit():
        return False

    return True


def get_release_group_genres(rgid: str) -> list[dict[str, Any]]:
    url = f"{API_ROOT}/release-group/{quote(rgid)}?{urlencode({'inc': 'genres', 'fmt': 'json'})}"
    data = get_json(url)
    genres = data.get("genres") or []
    return sorted(
        (
            {"name": g.get("name"), "count": int(g.get("count") or 0)}
            for g in genres
            if g.get("name")
        ),
        key=lambda x: (-x["count"], x["name"]),
    )


def decade_label(year: int) -> str:
    return f"{(year // 10) * 10}s"


def load_seed() -> list[dict[str, str]]:
    with SEED_FILE.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        raise RuntimeError("Seed cohort is empty.")
    if sum(r.get("role") == "focus" for r in rows) != 1:
        raise RuntimeError("Seed cohort must contain exactly one focus artist.")
    return rows


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    seed = load_seed()

    resolved: list[dict[str, Any]] = []
    spans: list[dict[str, Any]] = []
    focus_album_rows: list[dict[str, Any]] = []

    for seed_row in seed:
        name = seed_row["artist"].strip()
        role = seed_row["role"].strip()
        artist = resolve_artist(name)
        mbid = artist["id"]

        release_groups = browse_album_release_groups(mbid)
        qualifying = [rg for rg in release_groups if is_qualifying_album(rg, mbid)]
        qualifying.sort(key=lambda rg: (rg.get("first-release-date") or "9999", rg.get("title") or ""))

        if not qualifying:
            raise RuntimeError(f"No qualifying album release groups found for {name} ({mbid}).")

        years = [int(rg["first-release-date"][:4]) for rg in qualifying]
        decades = sorted({decade_label(y) for y in years})

        resolved.append(
            {
                "artist": name,
                "role": role,
                "mbid": mbid,
                "type": artist.get("type"),
                "country": artist.get("country"),
                "disambiguation": artist.get("disambiguation"),
            }
        )
        spans.append(
            {
                "artist": name,
                "role": role,
                "mbid": mbid,
                "first_album_year": min(years),
                "last_album_year": max(years),
                "elapsed_year_difference": max(years) - min(years),
                "calendar_decades_with_albums": len(decades),
                "release_decades": "|".join(decades),
                "qualifying_album_count": len(qualifying),
            }
        )

        if name == FOCUS_ARTIST:
            for rg in qualifying:
                genres = get_release_group_genres(rg["id"])
                year = int(rg["first-release-date"][:4])
                focus_album_rows.append(
                    {
                        "artist": name,
                        "artist_mbid": mbid,
                        "release_group_mbid": rg["id"],
                        "title": rg.get("title"),
                        "first_release_date": rg.get("first-release-date"),
                        "year": year,
                        "decade": decade_label(year),
                        "secondary_types": "|".join(rg.get("secondary-types") or []),
                        "genre_count": len(genres),
                        "genres": "|".join(g["name"] for g in genres),
                        "genres_with_counts": "|".join(f"{g['name']}:{g['count']}" for g in genres),
                        "scope_status": "needs_official_bowie_crosscheck",
                    }
                )

    span_fields = [
        "artist",
        "role",
        "mbid",
        "first_album_year",
        "last_album_year",
        "elapsed_year_difference",
        "calendar_decades_with_albums",
        "release_decades",
        "qualifying_album_count",
    ]
    with (DATA_DIR / "artist_album_spans.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=span_fields)
        writer.writeheader()
        writer.writerows(spans)

    focus_fields = [
        "artist",
        "artist_mbid",
        "release_group_mbid",
        "title",
        "first_release_date",
        "year",
        "decade",
        "secondary_types",
        "genre_count",
        "genres",
        "genres_with_counts",
        "scope_status",
    ]
    with (DATA_DIR / "david_bowie_album_genres.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=focus_fields)
        writer.writeheader()
        writer.writerows(focus_album_rows)

    metadata = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "musicbrainz_api_root": API_ROOT,
        "user_agent": USER_AGENT,
        "minimum_seconds_between_calls": MIN_SECONDS_BETWEEN_CALLS,
        "cohort_definition": "qualifying studio albums in six or more named calendar decades is the project target; seed cohort remains illustrative until inspected",
        "focus_artist": FOCUS_ARTIST,
        "resolved_artists": resolved,
        "focus_scope_gate": "Cross-check Bowie chronology against davidbowie.com before derived reinvention metrics.",
        "outputs": [
            "data/artist_album_spans.csv",
            "data/david_bowie_album_genres.csv",
        ],
    }
    with (DATA_DIR / "source_metadata.json").open("w", encoding="utf-8") as fh:
        json.dump(metadata, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(
        f"Wrote {len(spans)} artist span rows and "
        f"{len(focus_album_rows)} raw Bowie album rows."
    )


if __name__ == "__main__":
    main()
