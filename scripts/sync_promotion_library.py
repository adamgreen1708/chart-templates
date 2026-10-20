#!/usr/bin/env python3
"""Discover new published coffeetableviz content without overwriting editorial choices.

Usage:
    python scripts/sync_promotion_library.py --check
    python scripts/sync_promotion_library.py --write

New rows are *unreviewed* promotion candidates. The script never sends social posts,
edits source articles, or invents date/actor connections.
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = Path("data/promotion/content_index.csv")
EVENTS = Path("data/promotion/blockbuster_events.csv")

INDEX_FIELDS = [
    "id", "type", "title", "category", "source_path", "priority",
    "evergreen_class", "hook_seed", "freshness_gate",
]
EVENT_FIELDS = [
    "event_id", "original_date", "month_day", "film", "performer",
    "recorded_connection", "source_path", "matched_content_ids",
    "match_type", "editorial_note",
]
REVIEW_NOTE = (
    "Automatically discovered; verify source claims, age of data, public "
    "destination, image reuse rights and hook before promotion"
)


def frontmatter(path: Path) -> dict[str, str]:
    """Read top-level scalar YAML fields, without interpreting arbitrary YAML."""
    with path.open(encoding="utf-8") as f:
        contents = f.read(50000)
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|\s*\Z)", contents, re.S)
    if not match:
        return {}
    out = {}
    for line in match.group(1).splitlines():
        found = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if not found:
            continue
        key, value = found.groups()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
            if line.split(":", 1)[1].lstrip().startswith("'"):
                value = value.replace("''", "'")
        out[key] = value
    return out


def title_from_path(path: Path) -> str:
    return path.stem.replace("-", " ").strip().title()


def read_csv(path: Path, fields: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing promotion seed: {path}")
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != fields:
            raise ValueError(f"Promotion CSV schema differs at {path}: {reader.fieldnames}")
        rows = list(reader)
    for unique_col in ("source_path", fields[0]):
        values = [r[unique_col] for r in rows]
        if len(values) != len(set(values)):
            raise ValueError(f"Duplicate {unique_col} in {path}")
    return rows


def new_index_rows(root: Path, current: list[dict[str, str]]) -> list[dict[str, str]]:
    seen_paths = {r["source_path"] for r in current}
    known_ids = {r["id"] for r in current}
    candidates: list[tuple[Path, str, str]] = []
    candidates += [(p, "article", "article_" + p.stem) for p in sorted((root / "site/_posts").glob("*.md"))]
    candidates += [(p, "data_lens", "data_lens_" + p.stem) for p in sorted((root / "site/_data_lens").glob("*.md"))]
    candidates += [
        (p, "resource", "resource_" + p.parent.name.replace("-", "_"))
        for p in sorted((root / "site/resources").glob("*/index.html"))
    ]
    additions = []
    for file, kind, ident in candidates:
        relative = file.relative_to(root).as_posix()
        if relative in seen_paths:
            continue
        if ident in known_ids:
            raise ValueError(f"Generated ID already exists for a different source: {ident}")
        metadata = frontmatter(file)
        additions.append({
            "id": ident,
            "type": kind,
            "title": metadata.get("title") or (file.parent.name.replace("-", " ").title() if kind == "resource" else title_from_path(file)),
            "category": metadata.get("category") or ("Resource" if kind == "resource" else ("Data Lens" if kind == "data_lens" else "")),
            "source_path": relative,
            "priority": "REVIEW",
            "evergreen_class": "unclassified",
            "hook_seed": "",
            "freshness_gate": REVIEW_NOTE,
        })
        seen_paths.add(relative)
        known_ids.add(ident)
    return additions


def new_event_rows(root: Path, current: list[dict[str, str]]) -> list[dict[str, str]]:
    seen_paths = {r["source_path"] for r in current}
    known_ids = {r["event_id"] for r in current}
    additions = []
    for file in sorted((root / "site/_blockbuster_quotes").glob("*.md")):
        relative = file.relative_to(root).as_posix()
        if relative in seen_paths:
            continue
        meta = frontmatter(file)
        date = meta.get("date", "")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            raise ValueError(f"New Blockbuster needs ISO date in front matter: {relative}")
        ident = "blockbuster_" + file.stem
        if ident in known_ids:
            raise ValueError(f"Generated event ID already exists for another source: {ident}")
        additions.append({
            "event_id": ident,
            "original_date": date,
            "month_day": date[5:],
            "film": meta.get("film", ""),
            "performer": meta.get("performer", ""),
            "recorded_connection": meta.get("connection_type", ""),
            "source_path": relative,
            "matched_content_ids": "",
            "match_type": "",
            "editorial_note": (
                "New archived edition; reverify date link and sources for future reuse. "
                "No article match proposed automatically"
            ),
        })
        seen_paths.add(relative)
        known_ids.add(ident)
    return additions


def append_csv(path: Path, fields: list[str], additions: list[dict[str, str]]) -> None:
    if not additions:
        return
    # Append only: preserve existing editorial decisions and avoid noisy rewrites.
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writerows(additions)


def sync(root: Path, write: bool = False) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    index_path, event_path = root / INDEX, root / EVENTS
    index_additions = new_index_rows(root, read_csv(index_path, INDEX_FIELDS))
    event_additions = new_event_rows(root, read_csv(event_path, EVENT_FIELDS))
    if write:
        append_csv(index_path, INDEX_FIELDS, index_additions)
        append_csv(event_path, EVENT_FIELDS, event_additions)
    return index_additions, event_additions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="Append unreviewed content and event rows")
    mode.add_argument("--check", action="store_true", help="Read-only report; nonzero exit if new content is missing")
    args = parser.parse_args()
    new_content, new_events = sync(ROOT, write=args.write)
    for item in new_content:
        print("New content:", item["source_path"])
    for item in new_events:
        print("New Blockbuster:", item["source_path"])
    print(f"Promotion library: {len(new_content)} new content items, {len(new_events)} new Blockbuster events")
    if args.check and (new_content or new_events):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
