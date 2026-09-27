#!/usr/bin/env python3
"""Build the Bowie track-distribution mini-post dataset."""

from __future__ import annotations

import csv
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "2026-09-david-bowie-track-length-success" / "data" / "david_bowie_tracks_success.csv"
OUTPUT = ROOT / "data" / "bowie_track_distribution_rows.csv"


def percentile(values: list[float], q: float) -> float:
    values = sorted(values)
    pos = (len(values) - 1) * q
    lo = int(pos)
    hi = min(lo + 1, len(values) - 1)
    frac = pos - lo
    return values[lo] + (values[hi] - values[lo]) * frac


def mmss(seconds: float) -> str:
    s = round(seconds)
    return f"{s // 60}:{s % 60:02d}"


with SOURCE.open(newline="", encoding="utf-8") as fh:
    rows = list(csv.DictReader(fh))

by_album: dict[str, list[dict[str, str]]] = defaultdict(list)
for row in rows:
    by_album[row["album_title"]].append(row)

out = []

for album, album_rows in by_album.items():
    durations = [float(r["duration_seconds"]) for r in album_rows]
    avg = statistics.mean(durations)
    med = statistics.median(durations)
    q1 = percentile(durations, 0.25)
    q3 = percentile(durations, 0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    streamed = [r for r in album_rows if r["spotify_streams"]]
    streamed.sort(key=lambda r: int(r["spotify_streams"]), reverse=True)
    most = streamed[0] if streamed else None

    for row in album_rows:
        dur = float(row["duration_seconds"])
        is_outlier = dur < lower or dur > upper
        is_most = bool(
            most
            and row["track_title"] == most["track_title"]
            and row["spotify_streams"] == most["spotify_streams"]
        )
        distance = dur - med
        selected = is_outlier or (is_most and abs(distance) >= 60)

        out.append({
            "album_sequence": int(row["album_sequence"]),
            "album_year": int(row["album_year"]),
            "album_title": row["album_title"],
            "album_label": f'{row["album_year"]} · {row["album_title"]}',
            "track_number": row["track_number"],
            "track_title": row["track_title"],
            "duration_seconds": int(round(dur)),
            "duration_minutes": round(dur / 60, 3),
            "duration_display": row["duration_display"],
            "spotify_streams": row["spotify_streams"],
            "album_mean_seconds": round(avg),
            "album_mean_minutes": round(avg / 60, 3),
            "album_mean_display": mmss(avg),
            "album_median_seconds": round(med),
            "album_median_minutes": round(med / 60, 3),
            "album_median_display": mmss(med),
            "q1_seconds": round(q1),
            "q3_seconds": round(q3),
            "iqr_seconds": round(iqr),
            "is_tukey_outlier": "Yes" if is_outlier else "No",
            "is_most_streamed_on_album": "Yes" if is_most else "No",
            "duration_distance_from_median_seconds": round(distance),
            "selected_label": "Yes" if selected else "No",
            "label_role": (
                "outlier + most streamed" if is_outlier and is_most
                else "outlier" if is_outlier
                else "most streamed standout" if selected and is_most
                else ""
            ),
        })

out.sort(key=lambda r: (r["album_sequence"], str(r["track_number"])))

with OUTPUT.open("w", newline="", encoding="utf-8") as fh:
    writer = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
    writer.writeheader()
    writer.writerows(out)

print(f"Wrote {len(out)} rows across {len(by_album)} albums")
