#!/usr/bin/env python3
"""Join a dated current Spotify/Kworb snapshot to canonical Bowie album tracks.

This is a composition-level popularity join, not a claim that the Kworb row is
the exact original album master. For each canonical title we select the
highest-streaming non-feature Spotify row after stripping common version labels
(remaster, live, radio edit, single version, etc.). The matched Spotify title,
candidate count and snapshot date are retained for QA.

Input:
    data/david_bowie_tracks_core.csv

Output:
    data/david_bowie_tracks_streams.csv
"""

from __future__ import annotations

import csv
import re
import unicodedata
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"
INPUT = DATA_DIR / "david_bowie_tracks_core.csv"
OUTPUT = DATA_DIR / "david_bowie_tracks_streams.csv"

KWORB_URL = "https://kworb.net/spotify/artist/0oSGxfWSnnOXhD2fKuz2Gy_songs.html"
USER_AGENT = "Mozilla/5.0 (compatible; coffeetableviz-data-research/1.0)"

VERSION_PATTERNS = [
    r"\s+-\s+\d{4}\s+remaster(?:ed)?(?:\s+version)?\b.*$",
    r"\s+-\s+remaster(?:ed)?\b.*$",
    r"\s+-\s+\d{4}\s+mix\b.*$",
    r"\s+-\s+\d{4}\s+remix\b.*$",
    r"\s+-\s+live\b.*$",
    r"\s+-\s+radio edit\b.*$",
    r"\s+-\s+single version\b.*$",
    r"\s+-\s+us single version\b.*$",
    r"\s+-\s+album version\b.*$",
    r"\s+-\s+edit\b.*$",
    r"\s+-\s+mono\b.*$",
    r"\s+-\s+stereo\b.*$",
    r"\s*;\s*\d{4}\s+remaster.*$",
]

# Rare title cases where Spotify/Kworb punctuation or editorial naming differs.
TITLE_ALIASES = {
    "heroes": {"heroes"},
    "tis a pity she was a whore": {"tis a pity she was a whore"},
    "sue or in a season of crime": {"sue or in a season of crime"},
    "scary monsters and super creeps": {"scary monsters and super creeps"},
    "the pretty things are going to hell": {"the pretty things are going to hell"},
}


def normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = value.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    value = value.strip().strip('"').strip("'")
    value = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return " ".join(value.split())


def base_spotify_title(title: str) -> str:
    value = (title or "").strip()
    if value.startswith("*"):
        value = value[1:].strip()
    for pattern in VERSION_PATTERNS:
        value = re.sub(pattern, "", value, flags=re.IGNORECASE)
    return value.strip()


def parse_int(value: str) -> int | None:
    value = (value or "").replace(",", "").strip()
    if not value or value in {"-", "—"}:
        return None
    return int(value)


def fetch_kworb_rows() -> tuple[str, list[dict[str, object]]]:
    response = requests.get(KWORB_URL, headers={"User-Agent": USER_AGENT}, timeout=60)
    response.raise_for_status()
    text = response.text

    match = re.search(r"Last updated:\s*(\d{4}/\d{2}/\d{2})", text, flags=re.IGNORECASE)
    if not match:
        match = re.search(r"Last updated:\s*(\d{4}-\d{2}-\d{2})", text, flags=re.IGNORECASE)
    snapshot_date = ""
    if match:
        raw = match.group(1).replace("/", "-")
        snapshot_date = datetime.strptime(raw, "%Y-%m-%d").date().isoformat()

    soup = BeautifulSoup(text, "html.parser")
    chosen = None
    for table in soup.find_all("table"):
        headers = [cell.get_text(" ", strip=True) for cell in table.find_all("th")]
        joined = " | ".join(headers).lower()
        if "song title" in joined and "streams" in joined:
            chosen = table
            break
    if chosen is None:
        raise RuntimeError("Could not locate Kworb Song Title / Streams table.")

    rows: list[dict[str, object]] = []
    for tr in chosen.find_all("tr"):
        cells = [cell.get_text(" ", strip=True) for cell in tr.find_all(["td", "th"])]
        if len(cells) < 2:
            continue
        if cells[0].lower() == "song title":
            continue
        title = cells[0].strip()
        if not title:
            continue
        streams = parse_int(cells[1]) if len(cells) > 1 else None
        daily = parse_int(cells[2]) if len(cells) > 2 else None
        if streams is None:
            continue
        feature_flag = title.startswith("*")
        base_title = base_spotify_title(title)
        rows.append(
            {
                "spotify_title": title,
                "base_title": base_title,
                "match_key": normalize_text(base_title),
                "streams": streams,
                "daily": daily,
                "feature_flag": feature_flag,
            }
        )
    if not rows:
        raise RuntimeError("Kworb song table parsed zero rows.")
    return snapshot_date, rows


def main() -> None:
    with INPUT.open(newline="", encoding="utf-8") as fh:
        tracks = list(csv.DictReader(fh))
    if not tracks:
        raise RuntimeError("Core Bowie track table is empty.")

    snapshot_date, kworb = fetch_kworb_rows()
    by_key: dict[str, list[dict[str, object]]] = {}
    for row in kworb:
        if row["feature_flag"]:
            continue
        by_key.setdefault(str(row["match_key"]), []).append(row)

    out: list[dict[str, object]] = []
    matched = 0
    ambiguous = 0

    for track in tracks:
        key = normalize_text(track["track_title"])
        keys = {key}
        keys.update(TITLE_ALIASES.get(key, set()))
        candidates: list[dict[str, object]] = []
        seen: set[tuple[str, int]] = set()
        for candidate_key in keys:
            for row in by_key.get(candidate_key, []):
                sig = (str(row["spotify_title"]), int(row["streams"]))
                if sig not in seen:
                    candidates.append(row)
                    seen.add(sig)
        candidates.sort(key=lambda r: int(r["streams"]), reverse=True)
        best = candidates[0] if candidates else None

        row = dict(track)
        row.update(
            {
                "spotify_match_status": "matched" if best else "unmatched",
                "spotify_match_candidate_count": len(candidates),
                "spotify_title": best["spotify_title"] if best else "",
                "spotify_streams": best["streams"] if best else "",
                "spotify_daily": best["daily"] if best and best["daily"] is not None else "",
                "spotify_snapshot_date": snapshot_date,
                "spotify_source_url": KWORB_URL,
                "spotify_match_note": "highest-streaming non-feature version for normalized composition title" if best else "",
            }
        )
        if best:
            matched += 1
        if len(candidates) > 1:
            ambiguous += 1
        out.append(row)

    fields = list(out[0].keys())
    with OUTPUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out)

    print(
        f"Wrote {len(out)} rows; matched Spotify compositions={matched}; "
        f"unmatched={len(out)-matched}; multi-candidate matches={ambiguous}; "
        f"snapshot={snapshot_date or 'unknown'}"
    )


if __name__ == "__main__":
    main()
