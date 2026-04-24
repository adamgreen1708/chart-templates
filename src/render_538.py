import csv
import os
import sys
import textwrap
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from chart_config import CHART_CONFIG


def _coerce_value(value):
    try:
        num = float(value)
        return int(num) if num.is_integer() else num
    except Exception:
        return value


def _series_matches(series_value, target_value):
    if target_value is None:
        return False

    if series_value == target_value:
        return True

    return str(series_value) == str(target_value)


def _clean_headers(headers):
    return [h.strip().replace("\ufeff", "") for h in headers]


def _read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        reader.fieldnames = _clean_headers(reader.fieldnames)

        rows = []
        for row in reader:
            clean = {k.strip().replace("\ufeff", ""): _coerce_value(v) for k, v in row.items()}
            rows.append(clean)

    return rows, reader.fieldnames


def _require_columns(columns, required):
    missing = [c for c in required if c and c not in columns]
    if missing:
        raise ValueError(
            f"Missing column(s): {', '.join(missing)}\n"
            f"Available columns: {', '.join(columns)}"
        )


def _get_style(style, fallback):
    merged = fallback.copy()
    merged.update(style or {})
    return merged


def _apply_house_style(fig, ax):
    bg = CHART_CONFIG.get("background_color", "#F3F4F6")
    grid = CHART_CONFIG.get("grid_color", "#D9D9D9")

    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    ax.grid(axis="y", color=grid, linewidth=0.8, alpha=0.8)
    ax.grid(axis="x", color=grid, linewidth=0.5, alpha=0.35)

    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)

    ax.spines["bottom"].set_color("#A8A8A8")

    ax.tick_params(
        axis="both",
        labelsize=CHART_CONFIG.get("tick_label_fontsize", 12),
        colors="#4A4A4A",
        length=0,
    )


def _wrap_text(text, width, max_lines=None):
    if not text:
        return ""

    lines = textwrap.wrap(str(text), width=width)

    if max_lines is not None:
        lines = lines[:max_lines]

    return "\n".join(lines)


def _add_titles_and_footer(fig):
    title = _wrap_text(
        CHART_CONFIG.get("title", ""),
        CHART_CONFIG.get("title_wrap_width", 30),
        CHART_CONFIG.get("title_max_lines", 2),
    )

    subtitle = _wrap_text(
        CHART_CONFIG.get("subtitle", ""),
        CHART_CONFIG.get("subtitle_wrap_width", 58),
        CHART_CONFIG.get("subtitle_max_lines", 2),
    )

    footer_left = CHART_CONFIG.get("footer_left", "")
    footer_right = CHART_CONFIG.get("source_text", CHART_CONFIG.get("footer_right", ""))

    fig.text(
        CHART_CONFIG.get("title_x", 0.11),
        CHART_CONFIG.get("title_y", 0.94),
        title,
        fontsize=CHART_CONFIG.get("title_fontsize", 22),
        fontweight="bold",
        ha="left",
        va="top",
        color="#111111",
    )

    fig.text(
        CHART_CONFIG.get("subtitle_x", 0.11),
        CHART_CONFIG.get("subtitle_y", 0.865),
        subtitle,
        fontsize=CHART_CONFIG.get("subtitle_fontsize", 13),
        ha="left",
        va="top",
        color="#4A4A4A",
        linespacing=1.15,
    )

    fig.text(
        CHART_CONFIG.get("footer_left_x", 0.11),
        CHART_CONFIG.get("footer_y", 0.075),
        footer_left,
        fontsize=CHART_CONFIG.get("footer_fontsize", 10),
        ha="left",
        va="bottom",
        color="#555555",
    )

    fig.text(
        CHART_CONFIG.get("footer_right_x", 0.89),
        CHART_CONFIG.get("footer_y", 0.075),
        footer_right,
        fontsize=CHART_CONFIG.get("footer_fontsize", 10),
        ha="right",
        va="bottom",
        color="#555555",
    )

def _plot_reference_lines(ax):
    for ref in CHART_CONFIG.get("reference_lines", []):
        axis = ref.get("axis", "y")
        value = ref.get("value")
        label = ref.get("label", "")

        if value is None:
            continue

        if axis == "y":
            ax.axhline(
                value,
                color=ref.get("color", "#888888"),
                linewidth=ref.get("linewidth", 1.0),
                linestyle=ref.get("linestyle", "--"),
                alpha=ref.get("alpha", 0.8),
                zorder=0,
            )
            if label:
                ax.text(
                    ax.get_xlim()[1],
                    value,
                    label,
                    ha="right",
                    va="bottom",
                    fontsize=10,
                    color=ref.get("color", "#888888"),
                )

        if axis == "x":
            ax.axvline(
                value,
                color=ref.get("color", "#888888"),
                linewidth=ref.get("linewidth", 1.0),
                linestyle=ref.get("linestyle", "--"),
                alpha=ref.get("alpha", 0.8),
                zorder=0,
            )


def _plot_highlights_and_annotations(ax):
    focus_style = CHART_CONFIG.get("focus_style", {})
    highlight_color = CHART_CONFIG.get("highlight_color", "#C44E52")

    for p in CHART_CONFIG.get("highlight_points", []):
        ax.scatter(
            p["x"],
            p["y"],
            s=p.get("size", 46),
            color=p.get("color", highlight_color),
            zorder=p.get("zorder", 8),
        )

    for p in CHART_CONFIG.get("annotate_points", []):
        ax.annotate(
            p.get("text", ""),
            xy=(p["x"], p["y"]),
            xytext=(p.get("dx", 10), p.get("dy", 10)),
            textcoords="offset points",
            fontsize=p.get("fontsize", 9),
            color=p.get("color", "#111111"),
            ha=p.get("ha", "left"),
            va=p.get("va", "bottom"),
            arrowprops=p.get(
                "arrowprops",
                {
                    "arrowstyle": "-",
                    "color": p.get("color", "#555555"),
                    "linewidth": 0.8,
                },
            ),
            zorder=p.get("zorder", 9),
        )


def _plot_line(ax, rows):
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]
    series_col = CHART_CONFIG.get("series_col")

    focus_series = CHART_CONFIG.get("focus_series")
    secondary_series = CHART_CONFIG.get("secondary_series")

    context_style = _get_style(
        CHART_CONFIG.get("context_style"),
        {"color": "#D9D9D9", "linewidth": 0.8, "alpha": 0.25, "zorder": 1},
    )

    focus_style = _get_style(
        CHART_CONFIG.get("focus_style"),
        {"color": "#1F8FA8", "linewidth": 3.5, "alpha": 1.0, "zorder": 5},
    )

    secondary_style = _get_style(
        CHART_CONFIG.get("secondary_style"),
        {"color": "#7A7A7A", "linewidth": 2.0, "alpha": 0.9, "zorder": 4},
    )

    if series_col:
        grouped = defaultdict(list)

        for row in rows:
            grouped[row[series_col]].append(row)

        for series_name, points in grouped.items():
            points = sorted(points, key=lambda d: d[x_col])

            x_values = [p[x_col] for p in points]
            y_values = [p[y_col] for p in points]

            if _series_matches(series_name, focus_series):
                style = focus_style
            elif _series_matches(series_name, secondary_series):
                style = secondary_style
            elif focus_series is not None:
                style = context_style
            else:
                style = focus_style

            ax.plot(
                x_values,
                y_values,
                color=style.get("color", "#1F8FA8"),
                linewidth=style.get("linewidth", 2.0),
                alpha=style.get("alpha", 1.0),
                zorder=style.get("zorder", 3),
            )

    else:
        rows = sorted(rows, key=lambda d: d[x_col])

        ax.plot(
            [r[x_col] for r in rows],
            [r[y_col] for r in rows],
            color=focus_style.get("color", "#1F8FA8"),
            linewidth=focus_style.get("linewidth", 3.0),
            alpha=focus_style.get("alpha", 1.0),
            zorder=focus_style.get("zorder", 3),
        )


def _plot_bar(ax, rows):
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    rows = sorted(rows, key=lambda d: d[y_col], reverse=CHART_CONFIG.get("sort_desc", False))

    ax.bar(
        [r[x_col] for r in rows],
        [r[y_col] for r in rows],
        color=CHART_CONFIG.get("focus_style", {}).get("color", "#1F8FA8"),
        alpha=CHART_CONFIG.get("focus_style", {}).get("alpha", 1.0),
    )


def _plot_dot(ax, rows):
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    rows = sorted(rows, key=lambda d: d[y_col])

    ax.scatter(
        [r[y_col] for r in rows],
        [r[x_col] for r in rows],
        color=CHART_CONFIG.get("focus_style", {}).get("color", "#1F8FA8"),
        s=CHART_CONFIG.get("dot_size", 52),
        zorder=4,
    )

    ax.set_xlabel(y_col)
    ax.set_ylabel("")


def _plot_scatter(ax, rows):
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    ax.scatter(
        [r[x_col] for r in rows],
        [r[y_col] for r in rows],
        color=CHART_CONFIG.get("focus_style", {}).get("color", "#1F8FA8"),
        alpha=0.85,
        s=CHART_CONFIG.get("dot_size", 52),
        zorder=4,
    )


def main():
    data_file = REPO_ROOT / CHART_CONFIG["data_file"]
    rows, columns = _read_csv(data_file)

    required = [
        CHART_CONFIG.get("x_col"),
        CHART_CONFIG.get("y_col"),
        CHART_CONFIG.get("series_col"),
    ]

    _require_columns(columns, required)

    fig = plt.figure(
        figsize=(
            CHART_CONFIG.get("fig_width", 8.0),
            CHART_CONFIG.get("fig_height", 8.0),
        )
    )

    ax = fig.add_axes(
        [
            CHART_CONFIG.get("plot_left", 0.11),
            CHART_CONFIG.get("plot_bottom", 0.16),
            CHART_CONFIG.get("plot_right", 0.89) - CHART_CONFIG.get("plot_left", 0.11),
            CHART_CONFIG.get("plot_top", 0.70) - CHART_CONFIG.get("plot_bottom", 0.16),
        ]
    )

    _apply_house_style(fig, ax)

    chart_type = CHART_CONFIG.get("chart_type")

    if chart_type == "line":
        _plot_line(ax, rows)
    elif chart_type == "bar":
        _plot_bar(ax, rows)
    elif chart_type == "dot":
        _plot_dot(ax, rows)
    elif chart_type == "scatter":
        _plot_scatter(ax, rows)
    else:
        raise ValueError(f"Unsupported chart_type: {chart_type}")

    _plot_reference_lines(ax)
    _plot_highlights_and_annotations(ax)
    _add_titles_and_footer(fig)

output_dir = REPO_ROOT / "output"
output_dir.mkdir(exist_ok=True)

from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_slug = CHART_CONFIG.get("output_slug", Path(CHART_CONFIG["data_file"]).stem)

output_path = output_dir / f"{output_slug}_{timestamp}.png"

fig.savefig(output_path, dpi=200, facecolor=fig.get_facecolor())
print(f"Saved chart to {output_path}")

if __name__ == "__main__":
    main()