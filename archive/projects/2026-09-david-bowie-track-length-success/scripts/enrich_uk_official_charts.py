#!/usr/bin/env python3
"""Join Official Singles Chart history to canonical Bowie album tracks.

The Official Charts artist page contains multiple chart families. This script
extracts only the first main "Official Singles Chart" section and stops before
the next chart family. It then aggregates repeated chart entries by normalized
song title.

Input preference:
    data/david_bowie_tracks_streams.csv
Fallback:
    data/david_bowie_tracks_core.csv

Output:
    data/david_bowie_tracks_success.csv
"""

from __future__ import annotations

import csv
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

import requests
from bs4 import BeautifulSoup, NavigableString

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"
STREAMS_INPUT = DATA_DIR / "david_bowie_tracks_streams.csv"
CORE_INPUT = DATA_DIR / "david_bowie_tracks_core.csv"
OUTPUT = DATA_DIR / "david_bowie_tracks_success.csv"

OFFICIAL_CHARTS_URL = "https://www.officialcharts.com/artist/19138/david-bowie/"
TEXT_READER_URL = "https://r.jina.ai/https://www.officialcharts.com/artist/19138/david-bowie/"
USER_AGENT = "Mozilla/5.0 (compatible; coffeetableviz-data-research/1.0)"

TITLE_ALIASES = {
    "heroes": "heroes",
    "scary monsters and super creeps": "scary monsters and super creeps",
    "scary monsters": "scary monsters and super creeps",
    "sue or in a season of crime": "sue or in a season of crime",
    "tis a pity she was a whore": "tis a pity she was a whore",
}


def normalize_title(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = value.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    value = re.sub(r"\([^)]*remaster[^)]*\)", "", value, flags=re.IGNORECASE)
    value = re.sub(r"[^a-z0-9]+", " ", value.lower())
    key = " ".join(value.split())
    return TITLE_ALIASES.get(key, key)


def clean_token(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def is_chart_heading(token: str) -> bool:
    token = clean_token(token)
    if token == "Official Singles Chart":
        return False
    return (
        token.startswith("Official ")
        and " Chart" in token
        and len(token) < 100
    ) or token in {
        "End of Year Singles Chart",
        "End of Year Albums Chart",
    }


def extract_main_singles_section(soup: BeautifulSoup) -> list[str]:
    start = None
    for string in soup.find_all(string=True):
        token = clean_token(str(string))
        if token == "Official Singles Chart":
            start = string
            break
    if start is None:
        raise RuntimeError("Could not find the main Official Singles Chart heading.")

    tokens: list[str] = []
    for node in start.find_all_next(string=True):
        if not isinstance(node, NavigableString):
            continue
        token = clean_token(str(node))
        if not token:
            continue
        if token != "Official Singles Chart" and is_chart_heading(token):
            break
        tokens.append(token)

    if sum(1 for token in tokens if "Peak" in token) < 5:
        preview = " | ".join(tokens[:200])
        raise RuntimeError(
            "Official Singles Chart section did not contain enough Peak markers. "
            f"Preview: {preview[:4000]}"
        )
    return tokens


def parse_peak(token: str) -> int | None:
    match = re.search(r"Peak(?:\s+position)?\s*:?\s*(\d+)", token, flags=re.IGNORECASE)
    return int(match.group(1)) if match else None


def parse_weeks(token: str) -> int | None:
    match = re.search(r"Weeks(?:\s+on\s+chart)?\s*:?\s*(\d+)", token, flags=re.IGNORECASE)
    return int(match.group(1)) if match else None


def extract_chart_rows(tokens: list[str]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for i, token in enumerate(tokens):
        peak = parse_peak(token)
        if peak is None:
            continue

        # Locate the nearest DAVID BOWIE artist token before this Peak marker.
        artist_idx = None
        for j in range(i - 1, max(-1, i - 20), -1):
            if tokens[j].upper() == "DAVID BOWIE":
                artist_idx = j
                break
        if artist_idx is None:
            continue

        # Walk backwards from the artist token to find a plausible song title.
        title = ""
        noise = {
            "view as list", "view as cards", "view as list view as cards",
            "official singles chart", "david bowie",
        }
        for j in range(artist_idx - 1, max(-1, artist_idx - 12), -1):
            candidate = tokens[j]
            low = candidate.lower()
            if low in noise:
                continue
            if re.fullmatch(r"\d{1,2}", candidate):
                continue
            if re.fullmatch(r"\d{4}", candidate):
                continue
            if len(candidate) == 3 and candidate.title() in {
                "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
            }:
                continue
            if candidate.lower().endswith("cover art"):
                continue
            if "Image:" in candidate:
                continue
            if "Peak" in candidate or "Weeks" in candidate:
                continue
            title = candidate
            break
        if not title:
            continue

        # Text renderers can place Peak and Weeks in the same list token,
        # e.g. "Peak: 10, Weeks: 11". Check the current token first, then
        # nearby following tokens.
        weeks = parse_weeks(token)
        if weeks is None:
            for j in range(i + 1, min(len(tokens), i + 12)):
                weeks = parse_weeks(tokens[j])
                if weeks is not None:
                    break

        rows.append(
            {
                "chart_title": title,
                "match_key": normalize_title(title),
                "peak": peak,
                "weeks": weeks or 0,
            }
        )

    # De-duplicate exact parse duplicates that can arise from repeated accessible text.
    unique: list[dict[str, object]] = []
    seen: set[tuple[str, int, int]] = set()
    for row in rows:
        sig = (str(row["chart_title"]), int(row["peak"]), int(row["weeks"]))
        if sig not in seen:
            unique.append(row)
            seen.add(sig)
    return unique


def markdown_tokens(text: str) -> list[str]:
    tokens: list[str] = []
    for raw in text.splitlines():
        token = clean_token(raw)
        token = re.sub(r"^#{1,6}\\s*", "", token)
        token = token.replace("**", "").replace("__", "").strip()
        if token.startswith("![") or token.startswith("[Image"):
            continue
        if token:
            tokens.append(token)
    return tokens


def extract_main_singles_from_markdown(text: str) -> list[str]:
    all_tokens = markdown_tokens(text)
    start = None
    for i, token in enumerate(all_tokens):
        if token == "Official Singles Chart" or token.endswith("Official Singles Chart"):
            start = i
            break
    if start is None:
        raise RuntimeError("Text-rendered Official Charts page has no Official Singles Chart heading.")

    section: list[str] = []
    for token in all_tokens[start:]:
        canonical = token
        if canonical != "Official Singles Chart" and (
            canonical.startswith("Official ") and " Chart" in canonical and len(canonical) < 110
        ):
            break
        section.append(token)
    return section


def fetch_chart_rows() -> list[dict[str, object]]:
    response = requests.get(OFFICIAL_CHARTS_URL, headers={"User-Agent": USER_AGENT}, timeout=90)
    response.raise_for_status()

    tokens: list[str]
    transport = "officialcharts_html"
    try:
        soup = BeautifulSoup(response.text, "html.parser")
        tokens = extract_main_singles_section(soup)
    except RuntimeError:
        # Official Charts currently client-renders much of the artist-history page,
        # so a normal HTTP client can receive a shell with no visible chart rows.
        # Jina Reader is used only as a text transport for the same public Official
        # Charts URL; provenance remains Official Charts and the original URL is
        # stored in every joined row.
        rendered = requests.get(TEXT_READER_URL, headers={"User-Agent": USER_AGENT}, timeout=120)
        rendered.raise_for_status()
        tokens = extract_main_singles_from_markdown(rendered.text)
        transport = "officialcharts_via_text_reader"

    rows = extract_chart_rows(tokens)
    if len(rows) < 20:
        sample = " | ".join(tokens[:250])
        raise RuntimeError(
            f"Parsed only {len(rows)} Official Singles Chart rows via {transport}; "
            f"expected materially more. Section sample: {sample[:5000]}"
        )
    print(f"Official Charts transport={transport}; parsed main-chart rows={len(rows)}")
    return rows


def main() -> None:
    input_path = STREAMS_INPUT if STREAMS_INPUT.exists() else CORE_INPUT
    with input_path.open(newline="", encoding="utf-8") as fh:
        tracks = list(csv.DictReader(fh))
    if not tracks:
        raise RuntimeError(f"Input track table is empty: {input_path}")

    chart_rows = fetch_chart_rows()
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in chart_rows:
        grouped[str(row["match_key"])].append(row)

    out: list[dict[str, object]] = []
    matched = 0
    for track in tracks:
        key = normalize_title(track["track_title"])
        entries = grouped.get(key, [])
        peaks = [int(x["peak"]) for x in entries if x.get("peak") is not None]
        weeks = [int(x["weeks"]) for x in entries]
        titles = sorted({str(x["chart_title"]) for x in entries})

        row = dict(track)
        row.update(
            {
                "uk_chart_match_status": "matched" if entries else "unmatched",
                "uk_chart_best_peak": min(peaks) if peaks else "",
                "uk_chart_total_weeks": sum(weeks) if entries else "",
                "uk_chart_entry_count": len(entries),
                "uk_chart_source_titles": "|".join(titles),
                "uk_chart_source_url": OFFICIAL_CHARTS_URL,
                "uk_chart_scope": "Official Singles Chart only",
            }
        )
        if entries:
            matched += 1
        out.append(row)

    fields = list(out[0].keys())
    with OUTPUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out)

    print(
        f"Official Charts source rows={len(chart_rows)}; canonical tracks={len(out)}; "
        f"matched album-track rows={matched}; unmatched={len(out)-matched}"
    )


if __name__ == "__main__":
    main()
