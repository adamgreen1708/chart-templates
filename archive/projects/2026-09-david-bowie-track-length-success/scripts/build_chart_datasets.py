#!/usr/bin/env python3
"""Rebuild the three chart-specific Bowie datasets from the validated success table."""

from __future__ import annotations

import csv
import math
import re
import statistics
import unicodedata
from collections import defaultdict
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"
INPUT = DATA_DIR / "david_bowie_tracks_success.csv"


def mmss(seconds: float) -> str:
    seconds = round(seconds)
    return f"{seconds // 60}:{seconds % 60:02d}"


def normalise_title(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "").lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", value).split())


def percentile(values: list[float], q: float) -> float:
    values = sorted(values)
    pos = (len(values) - 1) * q
    lo, hi = math.floor(pos), math.ceil(pos)
    if lo == hi:
        return values[lo]
    return values[lo] + (values[hi] - values[lo]) * (pos - lo)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


with INPUT.open(newline="", encoding="utf-8") as fh:
    rows = list(csv.DictReader(fh))

# Chart 1
by_album: dict[str, list[dict]] = defaultdict(list)
for row in rows:
    by_album[row["album_title"]].append(row)

chart1 = []
for album, album_rows in by_album.items():
    durations = [float(r["duration_seconds"]) for r in album_rows]
    med = statistics.median(durations)
    chart1.append({
        "album_sequence": int(album_rows[0]["album_sequence"]),
        "album_year": int(album_rows[0]["album_year"]),
        "album_title": album,
        "track_count": len(album_rows),
        "median_seconds": round(med),
        "median_minutes": round(med / 60, 3),
        "median_label": mmss(med),
        "q1_seconds": round(percentile(durations, 0.25)),
        "q3_seconds": round(percentile(durations, 0.75)),
        "min_seconds": round(min(durations)),
        "max_seconds": round(max(durations)),
    })
chart1.sort(key=lambda r: r["album_sequence"])
write_csv(DATA_DIR / "bowie_track_length_chart_01_album_medians.csv", ["album_sequence","album_year","album_title","track_count","median_seconds","median_minutes","median_label","q1_seconds","q3_seconds","min_seconds","max_seconds"], chart1)

# Chart 2
selected_styles = ["Blue-Eyed Soul","Dance-Rock","Art Rock","Album Rock","Proto-Punk","Glam Rock","Singer/Songwriter"]
chart2 = []
for style in selected_styles:
    style_rows = [r for r in rows if style in r["allmusic_album_styles"].split("|")]
    durations = [float(r["duration_seconds"]) for r in style_rows]
    med = statistics.median(durations)
    album_count = len({r["album_title"] for r in style_rows})
    chart2.append({
        "style": style,
        "track_rows": len(style_rows),
        "album_count": album_count,
        "median_seconds": round(med),
        "median_minutes": round(med / 60, 3),
        "median_label": mmss(med),
        "detail_label": f"{mmss(med)} · {len(style_rows)} tracks · {album_count} albums",
    })
chart2.sort(key=lambda r: r["median_minutes"], reverse=True)
write_csv(DATA_DIR / "bowie_track_length_chart_02_styles.csv", ["style","track_rows","album_count","median_seconds","median_minutes","median_label","detail_label"], chart2)

# Chart 3
best_by_composition: dict[str, dict] = {}
for row in rows:
    if row["spotify_match_status"] != "matched" or not row["spotify_streams"]:
        continue
    key = normalise_title(row["track_title"])
    current = best_by_composition.get(key)
    if current is None or int(row["spotify_streams"]) > int(current["spotify_streams"]):
        best_by_composition[key] = row

chart3 = []
for row in best_by_composition.values():
    streams = int(row["spotify_streams"])
    duration_seconds = int(row["duration_seconds"])
    chart3.append({
        "track_title": row["track_title"],
        "album_title": row["album_title"],
        "album_year": int(row["album_year"]),
        "duration_seconds": duration_seconds,
        "duration_minutes": round(duration_seconds / 60, 3),
        "duration_label": row["duration_display"],
        "spotify_streams": streams,
        "log10_streams": round(math.log10(streams), 5),
        "spotify_daily": row["spotify_daily"],
        "spotify_snapshot_date": row["spotify_snapshot_date"],
        "uk_charted": "Yes" if row["uk_chart_match_status"] == "matched" else "No",
        "uk_chart_best_peak": row["uk_chart_best_peak"],
        "uk_chart_total_weeks": row["uk_chart_total_weeks"],
    })
chart3.sort(key=lambda r: r["spotify_streams"], reverse=True)
write_csv(DATA_DIR / "bowie_track_length_chart_03_streams.csv", ["track_title","album_title","album_year","duration_seconds","duration_minutes","duration_label","spotify_streams","log10_streams","spotify_daily","spotify_snapshot_date","uk_charted","uk_chart_best_peak","uk_chart_total_weeks"], chart3)

print(f"Chart 1: {len(chart1)} albums")
print(f"Chart 2: {len(chart2)} selected recurring AllMusic Styles")
print(f"Chart 3: {len(chart3)} unique matched compositions")
