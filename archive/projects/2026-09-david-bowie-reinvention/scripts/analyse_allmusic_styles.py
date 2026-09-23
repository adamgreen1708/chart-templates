#!/usr/bin/env python3
"""Derive adjacent-album AllMusic style turnover for the Bowie project.

The metric is deliberately simple and auditable:
Jaccard similarity = shared styles / union of styles
style reset score = 1 - Jaccard similarity

No score is calculated when either album lacks AllMusic Styles metadata.
MusicBrainz supplemental genres are preserved in the source CSV but are not
mixed into this metric because the two services use different taxonomies.
"""

from __future__ import annotations

import csv
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
SOURCE = PROJECT_DIR / "data" / "david_bowie_studio_albums.csv"
OUTPUT = PROJECT_DIR / "data" / "david_bowie_style_transitions.csv"


def split_styles(value: str) -> set[str]:
    return {item.strip() for item in value.split("|") if item.strip()}


def main() -> None:
    with SOURCE.open(newline="", encoding="utf-8") as fh:
        albums = list(csv.DictReader(fh))

    if len(albums) != 26:
        raise RuntimeError(f"Expected 26 scoped lifetime studio albums, found {len(albums)}.")

    rows = []
    for previous, current in zip(albums, albums[1:]):
        a = split_styles(previous["allmusic_styles"])
        b = split_styles(current["allmusic_styles"])

        if a and b:
            shared = a & b
            union = a | b
            similarity = len(shared) / len(union)
            reset = 1 - similarity
            status = "calculated"
            shared_n = len(shared)
            union_n = len(union)
            similarity_out = f"{similarity:.4f}"
            reset_out = f"{reset:.4f}"
            introduced = "|".join(sorted(b - a))
            dropped = "|".join(sorted(a - b))
        else:
            status = "not_calculated_missing_allmusic_styles"
            shared_n = union_n = similarity_out = reset_out = ""
            introduced = dropped = ""

        rows.append({
            "from_sequence": previous["sequence"],
            "to_sequence": current["sequence"],
            "from_year": previous["year"],
            "to_year": current["year"],
            "from_album": previous["title"],
            "to_album": current["title"],
            "shared_style_count": shared_n,
            "union_style_count": union_n,
            "jaccard_similarity": similarity_out,
            "style_reset_score": reset_out,
            "styles_introduced": introduced,
            "styles_dropped": dropped,
            "analysis_status": status,
        })

    fields = list(rows[0])
    with OUTPUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    valid = [r for r in rows if r["analysis_status"] == "calculated"]
    print(f"Wrote {len(rows)} transitions; {len(valid)} have a reset score.")


if __name__ == "__main__":
    main()
