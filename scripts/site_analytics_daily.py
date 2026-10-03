#!/usr/bin/env python3
"""Build the Coffeetableviz Daily Pulse from GoatCounter.

Uses real GoatCounter data only. The default report date is the previous
complete Europe/London calendar day. The tracker went live on 3 October 2026,
so 4 October 2026 is the first full reporting day.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from datetime import date, datetime, time, timedelta
from pathlib import Path
from statistics import mean
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from render_538 import BG, SUBTEXT, TEXT, apply_538_template  # noqa: E402

API_BASE = "https://coffeetableviz.goatcounter.com/api/v0"
TZ = ZoneInfo("Europe/London")
TRACKING_START_DATE = date(2026, 10, 4)

DATA_FILE = REPO_ROOT / "data" / "site_analytics_daily.csv"
OUTPUT_IMAGE = REPO_ROOT / "output" / "daily_site_pulse.png"
OUTPUT_SUMMARY = REPO_ROOT / "output" / "daily_site_pulse_summary.md"
OUTPUT_JSON = REPO_ROOT / "output" / "daily_site_pulse_latest.json"

BLUE = "#1F8FA8"
RED = "#C44E52"
GREY = "#7A7A7A"
GRID = "#D9D9D9"

CSV_FIELDS = [
    "report_date",
    "visits",
    "prior_7d_avg",
    "pct_vs_prior_7d",
    "top_page_path",
    "top_page_title",
    "top_page_visits",
    "top_referrer",
    "top_referrer_visits",
    "observation",
    "generated_at_utc",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--report-date",
        help="Europe/London report date in YYYY-MM-DD. Defaults to yesterday.",
    )
    return parser.parse_args()


def report_date_from_args(value: str | None) -> date:
    if value:
        return date.fromisoformat(value)
    return datetime.now(TZ).date() - timedelta(days=1)


def iso_midnight(day: date) -> str:
    dt = datetime.combine(day, time.min, TZ)
    return dt.isoformat(timespec="seconds")


def api_get(path: str, token: str, params: dict | None = None) -> dict:
    url = f"{API_BASE}{path}"
    if params:
        url = f"{url}?{urlencode(params, doseq=True)}"

    req = Request(
        url,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "coffeetableviz-daily-pulse/1.0",
        },
    )

    try:
        with urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GoatCounter API returned HTTP {exc.code}: {body}") from exc
    except URLError as exc:
        raise RuntimeError(f"Could not reach GoatCounter API: {exc}") from exc


def date_params(start: date, end_exclusive: date) -> dict[str, str]:
    return {
        "start": iso_midnight(start),
        "end": iso_midnight(end_exclusive),
    }


def fetch_daily_totals(token: str, start: date, end_exclusive: date) -> dict[date, int]:
    payload = api_get("/stats/total", token, date_params(start, end_exclusive))
    out: dict[date, int] = {}
    for stat in payload.get("stats", []):
        day_value = stat.get("day")
        if not day_value:
            continue
        out[date.fromisoformat(day_value)] = int(stat.get("daily") or 0)
    return out


def fetch_top_page(token: str, report_date: date) -> dict:
    params = date_params(report_date, report_date + timedelta(days=1))
    params.update({"group": "day", "limit": 100})
    payload = api_get("/stats/hits", token, params)

    hits = [h for h in payload.get("hits", []) if not h.get("event")]
    if not hits:
        return {"path": "(none)", "title": "No page visits", "count": 0, "path_id": None}

    hit = hits[0]
    return {
        "path": hit.get("path") or "(unknown)",
        "title": hit.get("title") or hit.get("path") or "(untitled)",
        "count": int(hit.get("count") or 0),
        "path_id": hit.get("path_id"),
    }


def fetch_top_referrer(token: str, report_date: date) -> dict:
    params = date_params(report_date, report_date + timedelta(days=1))
    params.update({"limit": 20})
    payload = api_get("/stats/toprefs", token, params)
    stats = payload.get("stats", [])

    if not stats:
        return {"name": "Direct / unknown", "count": 0}

    first = stats[0]
    name = (first.get("name") or "").strip() or "Direct / unknown"
    return {"name": name, "count": int(first.get("count") or 0)}


def truncate(text: str, max_chars: int) -> str:
    text = " ".join(str(text).split())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip() + "…"


def make_observation(
    report_date: date,
    visits: int,
    prior_avg: float | None,
    pct_vs_avg: float | None,
    top_page_visits: int,
) -> str:
    if report_date == TRACKING_START_DATE:
        return "The baseline has, technically, begun."

    if visits > 0 and top_page_visits / visits >= 0.5:
        return "One page did most of the work."

    if prior_avg is None or pct_vs_avg is None:
        return "Still building enough history for a proper baseline."

    if pct_vs_avg >= 50:
        return "A noticeably busier day than the seven-day baseline."
    if pct_vs_avg <= -50:
        return "A noticeably quieter day than the seven-day baseline."
    return "Traffic stayed fairly close to its recent rhythm."


def load_history() -> list[dict[str, str]]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def save_history(new_row: dict[str, object]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    rows = [r for r in load_history() if r.get("report_date") != new_row["report_date"]]
    rows.append({k: "" if new_row.get(k) is None else str(new_row.get(k)) for k in CSV_FIELDS})
    rows.sort(key=lambda r: r["report_date"])

    with DATA_FILE.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def render_pulse(
    report_date: date,
    daily_counts: dict[date, int],
    visits: int,
    prior_avg: float | None,
    pct_vs_avg: float | None,
    top_page: dict,
    top_referrer: dict,
    observation: str,
) -> None:
    trend_start = max(TRACKING_START_DATE, report_date - timedelta(days=13))
    dates = []
    values = []
    cursor = trend_start
    while cursor <= report_date:
        dates.append(cursor)
        values.append(int(daily_counts.get(cursor, 0)))
        cursor += timedelta(days=1)

    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    ax.plot(dates, values, color=BLUE, linewidth=3.0, marker="o", markersize=4.5, zorder=3)
    ax.scatter([report_date], [visits], s=110, color=RED, zorder=5)

    if prior_avg is not None:
        ax.axhline(prior_avg, color=GREY, linewidth=1.3, linestyle="--", alpha=0.85, zorder=2)
        ax.text(
            dates[0],
            prior_avg,
            f"  Prior 7-day avg {prior_avg:.1f}",
            ha="left",
            va="bottom",
            fontsize=9,
            color=GREY,
        )

    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%-d %b"))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=3, maxticks=6))
    ax.margins(x=0.04)

    if prior_avg is None:
        context = "First complete day of tracking."
    else:
        direction = "above" if pct_vs_avg >= 0 else "below"
        context = f"{abs(pct_vs_avg):.0f}% {direction} the previous seven-day daily average."

    apply_538_template(
        ax,
        fig,
        title=f"Yesterday brought {visits:,} visit{'s' if visits != 1 else ''}",
        subtitle=f"Coffeetableviz Daily Pulse · {report_date.strftime('%-d %B %Y')} · {context}",
        source_text="Source: GoatCounter",
        footer_left="Coffeetableviz",
        vertical_gridlines=False,
        title_fontsize=22,
        subtitle_fontsize=11.5,
        tick_label_fontsize=9.5,
        footer_fontsize=9,
        title_x=0.10,
        title_y=0.93,
        subtitle_x=0.10,
        subtitle_y=0.855,
        footer_left_x=0.10,
        footer_right_x=0.90,
        footer_y=0.055,
        plot_top=0.70,
        plot_bottom=0.34,
        plot_left=0.12,
        plot_right=0.90,
    )

    fig.text(0.10, 0.735, "14-DAY VISITS TREND", ha="left", va="bottom", fontsize=9, fontweight="bold", color=SUBTEXT)

    fig.text(0.10, 0.255, "MOST READ", ha="left", va="bottom", fontsize=9, fontweight="bold", color=SUBTEXT)
    fig.text(
        0.10,
        0.220,
        truncate(top_page["title"], 42),
        ha="left",
        va="bottom",
        fontsize=11,
        fontweight="bold",
        color=TEXT,
    )
    fig.text(
        0.10,
        0.190,
        f'{top_page["count"]:,} visit{"s" if top_page["count"] != 1 else ""} · {truncate(top_page["path"], 42)}',
        ha="left",
        va="bottom",
        fontsize=9,
        color=SUBTEXT,
    )

    fig.text(0.57, 0.255, "TOP REFERRER", ha="left", va="bottom", fontsize=9, fontweight="bold", color=SUBTEXT)
    fig.text(
        0.57,
        0.220,
        truncate(top_referrer["name"], 28),
        ha="left",
        va="bottom",
        fontsize=11,
        fontweight="bold",
        color=TEXT,
    )
    fig.text(
        0.57,
        0.190,
        f'{top_referrer["count"]:,} visit{"s" if top_referrer["count"] != 1 else ""}',
        ha="left",
        va="bottom",
        fontsize=9,
        color=SUBTEXT,
    )

    fig.text(0.10, 0.135, "OBSERVATION", ha="left", va="bottom", fontsize=9, fontweight="bold", color=SUBTEXT)
    fig.text(0.10, 0.103, observation, ha="left", va="bottom", fontsize=10.5, color=TEXT)

    OUTPUT_IMAGE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_IMAGE, dpi=200, facecolor=BG)
    plt.close(fig)


def write_summary(
    report_date: date,
    visits: int,
    prior_avg: float | None,
    pct_vs_avg: float | None,
    top_page: dict,
    top_referrer: dict,
    observation: str,
) -> None:
    comparison = "Not enough history yet"
    if prior_avg is not None and pct_vs_avg is not None:
        direction = "above" if pct_vs_avg >= 0 else "below"
        comparison = f"{abs(pct_vs_avg):.0f}% {direction} prior 7-day daily average ({prior_avg:.1f})"

    text = f"""# Coffeetableviz Daily Pulse — {report_date.strftime('%-d %B %Y')}

- **Visits:** {visits:,}
- **7-day context:** {comparison}
- **Most read:** {top_page['title']} — {top_page['count']:,} visits
- **Top referrer:** {top_referrer['name']} — {top_referrer['count']:,} visits
- **Observation:** {observation}

Latest image: `output/daily_site_pulse.png`
"""
    OUTPUT_SUMMARY.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_SUMMARY.write_text(text, encoding="utf-8")


def main() -> int:
    args = parse_args()
    token = os.environ.get("GOATCOUNTER_API_TOKEN", "").strip()
    if not token:
        print("GOATCOUNTER_API_TOKEN is not set; no report generated.")
        return 0

    report_date = report_date_from_args(args.report_date)
    if report_date < TRACKING_START_DATE:
        print(
            f"Skipping {report_date}: tracking only has a full day from "
            f"{TRACKING_START_DATE} onwards."
        )
        return 0

    trend_start = max(TRACKING_START_DATE, report_date - timedelta(days=13))
    daily_counts = fetch_daily_totals(token, trend_start, report_date + timedelta(days=1))
    visits = int(daily_counts.get(report_date, 0))

    prior_start = report_date - timedelta(days=7)
    has_full_baseline = prior_start >= TRACKING_START_DATE
    prior_counts: list[int] = []
    if has_full_baseline:
        baseline_totals = fetch_daily_totals(token, prior_start, report_date)
        prior_counts = [
            int(baseline_totals.get(prior_start + timedelta(days=i), 0))
            for i in range(7)
        ]

    prior_avg = mean(prior_counts) if prior_counts else None
    pct_vs_avg = None
    if prior_avg is not None and prior_avg > 0:
        pct_vs_avg = ((visits - prior_avg) / prior_avg) * 100

    top_page = fetch_top_page(token, report_date)
    top_referrer = fetch_top_referrer(token, report_date)
    observation = make_observation(
        report_date,
        visits,
        prior_avg,
        pct_vs_avg,
        int(top_page["count"]),
    )

    row = {
        "report_date": report_date.isoformat(),
        "visits": visits,
        "prior_7d_avg": "" if prior_avg is None else f"{prior_avg:.2f}",
        "pct_vs_prior_7d": "" if pct_vs_avg is None else f"{pct_vs_avg:.1f}",
        "top_page_path": top_page["path"],
        "top_page_title": top_page["title"],
        "top_page_visits": top_page["count"],
        "top_referrer": top_referrer["name"],
        "top_referrer_visits": top_referrer["count"],
        "observation": observation,
        "generated_at_utc": datetime.now(ZoneInfo("UTC")).isoformat(timespec="seconds"),
    }

    save_history(row)
    render_pulse(
        report_date,
        daily_counts,
        visits,
        prior_avg,
        pct_vs_avg,
        top_page,
        top_referrer,
        observation,
    )
    write_summary(
        report_date,
        visits,
        prior_avg,
        pct_vs_avg,
        top_page,
        top_referrer,
        observation,
    )

    OUTPUT_JSON.write_text(json.dumps(row, indent=2) + "\n", encoding="utf-8")

    print(f"Generated Daily Pulse for {report_date}")
    print(f"Image: {OUTPUT_IMAGE.relative_to(REPO_ROOT)}")
    print(f"History: {DATA_FILE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
