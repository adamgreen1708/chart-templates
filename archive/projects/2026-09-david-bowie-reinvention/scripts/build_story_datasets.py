#!/usr/bin/env python3
"""Build the three chart-specific Bowie datasets from the validated source files."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"

ALBUMS = DATA_DIR / "david_bowie_studio_albums.csv"
TRANSITIONS = DATA_DIR / "david_bowie_style_transitions.csv"

BROAD_CONTEXT_STYLES = {
    "Contemporary Pop/Rock",
    "Art Rock",
    "Experimental Rock",
}

SHORT_TITLE = {
    "The Rise and Fall of Ziggy Stardust and the Spiders from Mars": "Ziggy Stardust",
    "The Buddha of Suburbia": "Buddha of Suburbia",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    albums = read_csv(ALBUMS)
    transitions = read_csv(TRANSITIONS)

    timeline = []
    for album in albums:
        year = int(album["year"])
        timeline.append({
            "sequence": int(album["sequence"]),
            "year": year,
            "title": album["title"],
            "display_title": SHORT_TITLE.get(album["title"], album["title"]),
            "decade": f"{(year // 10) * 10}s",
        })
    write_csv(
        DATA_DIR / "bowie_chart_01_timeline.csv",
        timeline,
        ["sequence", "year", "title", "display_title", "decade"],
    )

    style_sets = {
        int(album["sequence"]): {
            s for s in album["allmusic_styles"].split("|") if s
        }
        for album in albums
    }
    frequency = Counter(style for styles in style_sets.values() for style in styles)
    first_seen = {
        style: min(seq for seq, styles in style_sets.items() if style in styles)
        for style in frequency
    }
    styles = sorted(
        (s for s in frequency if s not in BROAD_CONTEXT_STYLES),
        key=lambda s: (first_seen[s], -frequency[s], s),
    )
    style_order = {style: idx + 1 for idx, style in enumerate(styles)}

    matrix = []
    for album in albums:
        for style in sorted(style_sets[int(album["sequence"])], key=lambda s: style_order.get(s, 999)):
            if style in BROAD_CONTEXT_STYLES:
                continue
            matrix.append({
                "sequence": int(album["sequence"]),
                "year": int(album["year"]),
                "title": album["title"],
                "style": style,
                "style_order": style_order[style],
                "style_frequency": frequency[style],
            })
    write_csv(
        DATA_DIR / "bowie_chart_02_style_matrix.csv",
        matrix,
        ["sequence", "year", "title", "style", "style_order", "style_frequency"],
    )

    reset_rows = []
    for row in transitions:
        missing = row["analysis_status"] != "calculated"
        reset = None if missing else float(row["style_reset_score"])
        reset_rows.append({
            "from_sequence": int(row["from_sequence"]),
            "to_sequence": int(row["to_sequence"]),
            "from_year": int(row["from_year"]),
            "to_year": int(row["to_year"]),
            "from_album": row["from_album"],
            "to_album": row["to_album"],
            "display_album": SHORT_TITLE.get(row["to_album"], row["to_album"]),
            "style_reset_score": "" if missing else f"{reset:.4f}",
            "reset_percent": "" if missing else f"{reset * 100:.1f}",
            # Missing rows are deliberately placed in a small non-data gutter
            # left of 0%. The chart uses explicit 0–100% ticks, so this cannot
            # be read as a negative reset score.
            "plot_position": "-0.035" if missing else f"{reset:.4f}",
            "analysis_status": row["analysis_status"],
            "missing_note": "No comparable Styles data" if missing else "",
        })
    write_csv(
        DATA_DIR / "bowie_chart_03_style_reset.csv",
        reset_rows,
        [
            "from_sequence", "to_sequence", "from_year", "to_year",
            "from_album", "to_album", "display_album",
            "style_reset_score", "reset_percent", "plot_position",
            "analysis_status", "missing_note",
        ],
    )

    measurable = sum(r["analysis_status"] == "calculated" for r in reset_rows)
    print(
        f"Wrote {len(timeline)} timeline rows, {len(matrix)} matrix rows, "
        f"and {len(reset_rows)} reset rows ({measurable} measurable)."
    )


if __name__ == "__main__":
    main()
