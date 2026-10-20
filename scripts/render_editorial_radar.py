#!/usr/bin/env python3
"""Render forward-looking editorial ideas from a human-researched event ledger.

Never asserts that the full event universe has been searched. Never publishes,
schedules or modifies source articles, Blockbuster editions or the promotion
content index. Month-only dates are deliberately NOT rendered as day one.
"""
from __future__ import annotations

import argparse
import csv
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
EVENTS_PATH = ROOT / "data/promotion/editorial_radar_events.csv"
OUTPUT_DIR = ROOT / "docs/editorial_radar"
FIELDS = [
    "id", "target_date", "date_precision", "original_date",
    "event_type", "subject", "milestone_years", "territory",
    "source_urls", "source_note", "story_mode", "priority",
    "proposed_headline", "research_question", "data_plan",
    "existing_content_path", "status", "blockbuster_alignment",
]
PRIORITY = {"A", "B", "C"}
TYPE_DESCRIPTIONS = {
    "actor_birthday": "Actor birthday",
    "artist_birthday": "Artist birthday",
    "actor_death_anniversary": "Actor death anniversary",
    "artist_death_anniversary": "Artist death anniversary",
    "film_anniversary": "Film anniversary",
    "album_anniversary": "Album anniversary",
    "album_release": "Album anniversary",
}
MODE_LABELS = {"resurface": "Resurface", "new": "New analysis", "hybrid": "New + resurface"}


def month_after(d: date) -> date:
    return date(d.year + (d.month == 12), (d.month % 12) + 1, 1)


def months_from(d: date, count: int) -> list[str]:
    value = date(d.year, d.month, 1)
    out = []
    for _ in range(count):
        out.append(value.strftime("%Y-%m"))
        value = month_after(value)
    return out


def read_events(path: Path = EVENTS_PATH) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != FIELDS:
            raise ValueError(f"Unexpected editorial radar headers: {reader.fieldnames}")
        rows = list(reader)
    seen = set()
    for r in rows:
        event_id = r["id"]
        if not event_id or event_id in seen:
            raise ValueError(f"Missing or duplicate radar event ID: {event_id}")
        seen.add(event_id)
        target = date.fromisoformat(r["target_date"])
        precision = r["date_precision"]
        original = r["original_date"]
        if precision not in {"day", "month"}:
            raise ValueError(f"{event_id}: invalid precision")
        if precision == "day":
            earlier = date.fromisoformat(original)
            if (earlier.month, earlier.day) != (target.month, target.day):
                raise ValueError(f"{event_id}: original and target day/month differ")
        else:
            if len(original) != 7 or original != target.strftime("%Y-%m").replace(str(target.year), original[:4], 1):
                raise ValueError(f"{event_id}: month-only record should use YYYY-MM matching the target month")
            if target.day != 1:
                raise ValueError(f"{event_id}: month-only anchor must be the first of its month")
        expected_years = target.year - int(original[:4])
        if int(r["milestone_years"]) != expected_years or expected_years < 0:
            raise ValueError(f"{event_id}: milestone years inconsistent")
        if r["priority"] not in PRIORITY or r["story_mode"] not in MODE_LABELS:
            raise ValueError(f"{event_id}: invalid priority or story mode")
        if r["event_type"] not in TYPE_DESCRIPTIONS:
            raise ValueError(f"{event_id}: unsupported event type")
        if not r["source_urls"] or not all(
            s.startswith("https://") for s in r["source_urls"].split("|")
        ):
            raise ValueError(f"{event_id}: missing valid research source")
        if r["status"] not in {"candidate", "researching", "data_verified", "chart_ready",
                               "copy_ready", "approved", "published", "parked"}:
            raise ValueError(f"{event_id}: unrecognised workflow status")
    return rows


def escape_cell(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ").strip()


def render_month(month: str, events: list[dict[str, str]]) -> str:
    start = date.fromisoformat(month + "-01")
    subset = [r for r in events if r["target_date"].startswith(month)]
    subset.sort(key=lambda r: (r["target_date"], r["priority"], r["id"]))
    lines = [
        f"# Editorial Radar — {start.strftime('%B %Y')}",
        "",
        "> **Research candidates, not an approved publishing schedule.** Dates refer to "
        "birthday, death or release events, not confirmed articles. Source links are "
        "starting evidence; full Blockbuster two-source QA still applies.",
        "",
        f"**Candidate opportunities:** {len(subset)}. "
        "This list is curated, **not exhaustive**; independently research additional "
        "anniversaries each month.",
        "",
        "| Occasion | Editorial opportunity | Approach | Start research by | Priority | Status |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for r in subset:
        target = date.fromisoformat(r["target_date"])
        when = (target.strftime("%-d %b") if r["date_precision"] == "day"
                else target.strftime("%B") + " (date unconfirmed)")
        milestone = f"{r['milestone_years']} years" if r["event_type"] in {
            "album_release", "album_anniversary", "film_anniversary",
            "artist_death_anniversary", "actor_death_anniversary",
        } else f"{r['milestone_years']}th birthday"
        occasion = f"**{when}** — {r['subject']} ({milestone})"
        prep = target - timedelta(days=28)
        if r["date_precision"] == "month":
            prep_note = prep.strftime("%-d %b %Y") + " (month-window)"
        else:
            prep_note = prep.strftime("%-d %b %Y")
        line = [
            occasion, r["proposed_headline"], MODE_LABELS[r["story_mode"]],
            prep_note, r["priority"], r["status"],
        ]
        lines.append("| " + " | ".join(escape_cell(v) for v in line) + " |")
    lines += ["", "## Research notes and source checks", ""]
    for r in subset:
        links = ", ".join(
            f"[source {i}]({url})" for i, url in enumerate(r["source_urls"].split("|"), 1)
        )
        lines += [
            f"### {r['subject']} — {r['id']}",
            f"- **Question:** {r['research_question']}",
            f"- **Suggested data:** {r['data_plan']}",
            f"- **Connection:** {r['blockbuster_alignment']}",
            f"- **Date / territorial gate:** {r['territory']}. {r['source_note']}",
            f"- **Sources to recheck:** {links}",
        ]
        if r["existing_content_path"]:
            lines.append(f"- **Existing story:** \`{r['existing_content_path']}\`")
        lines.append("")
    lines += [
        "## Preparation and review",
        "",
        "Choose no more than one or two substantial new data projects each month. "
        "For each, check date evidence, IMDb/music dataset feasibility, scope, "
        "three possible charts and article-level source notes before any rendering.",
        "",
        "A Blockbuster edition may connect to a finished article, but must pass "
        "its own exact-date, verified-quote and final-pixel approval gates. "
        "**Never invent findings just because the anniversary is approaching.**",
        "",
        "The content/promotion library indexes only actually published articles "
        "after merge. This Radar may include an unpublished idea indefinitely.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-month", help="YYYY-MM; defaults to next UK month")
    parser.add_argument("--months", type=int, default=3)
    parser.add_argument("--write", action="store_true", help="Write month snapshots in docs/editorial_radar")
    parser.add_argument("--check", action="store_true", help="Check snapshots exist and exactly match ledger")
    args = parser.parse_args()
    if args.months < 1 or args.months > 12:
        parser.error("--months must be in 1..12")
    if args.write and args.check:
        parser.error("--write and --check are mutually exclusive")
    today = datetime.now(ZoneInfo("Europe/London")).date()
    first = (date.fromisoformat(args.start_month + "-01") if args.start_month
             else month_after(today))
    events = read_events()
    failed = False
    for month in months_from(first, args.months):
        body = render_month(month, events)
        output = OUTPUT_DIR / f"{month}.md"
        if args.write:
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            output.write_text(body, encoding="utf-8")
            print(f"Updated {output.relative_to(ROOT)}")
        elif args.check:
            if not output.exists() or output.read_text(encoding="utf-8") != body:
                print(f"Missing/stale monthly radar: {output}")
                failed = True
        else:
            print(body)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
