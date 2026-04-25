import csv
import sys
import textwrap
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

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


def _clean_headers(headers):
    return [h.strip().replace("\ufeff", "") for h in headers]


def _read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        reader.fieldnames = _clean_headers(reader.fieldnames)

        rows = []
        for row in reader:
            clean = {
                k.strip().replace("\ufeff", ""): _coerce_value(v)
                for k, v in row.items()
            }
            rows.append(clean)

    return rows, reader.fieldnames


def _require_columns(columns, required):
    missing = [c for c in required if c and c not in columns]
    if missing:
        raise ValueError(
            f"Missing column(s): {', '.join(missing)}\n"
            f"Available columns: {', '.join(columns)}"
        )


def _series_matches(series_value, target_value):
    if target_value is None:
        return False

    return series_value == target_value or str(series_value) == str(target_value)


def _get_style(style, fallback):
    merged = fallback.copy()
    merged.update(style or {})
    return merged


def _apply_filters(rows):
    condition = CHART_CONFIG.get("filter_condition")

    if not condition:
        return rows

    if condition == "near_zero":
        col = CHART_CONFIG.get("filter_column", CHART_CONFIG.get("x_col"))
        threshold = CHART_CONFIG.get("filter_threshold", 2)

        return [
            r for r in rows
            if isinstance(r.get(col), (int, float)) and abs(r.get(col)) <= threshold
        ]

    return rows


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
    footer_right = CHART_CONFIG.get("footer_right", CHART_CONFIG.get("source_text", ""))

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


def _apply_axis_formatting(ax):
    x_format = CHART_CONFIG.get("x_tick_format")
    y_format = CHART_CONFIG.get("y_tick_format")

    if x_format:
        ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: x_format.format(x=x)))

    if y_format:
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: y_format.format(x=x)))

    if CHART_CONFIG.get("x_axis_label"):
        ax.set_xlabel(CHART_CONFIG.get("x_axis_label"), fontsize=11, color="#4A4A4A")

    if CHART_CONFIG.get("y_axis_label"):
        ax.set_ylabel(CHART_CONFIG.get("y_axis_label"), fontsize=11, color="#4A4A4A")


def _apply_limits_ticks_and_aspect(ax):
    if CHART_CONFIG.get("x_limits"):
        ax.set_xlim(CHART_CONFIG["x_limits"])

    if CHART_CONFIG.get("y_limits"):
        ax.set_ylim(CHART_CONFIG["y_limits"])

    tick_step = CHART_CONFIG.get("tick_step")
    if tick_step:
        ax.xaxis.set_major_locator(MultipleLocator(tick_step))
        ax.yaxis.set_major_locator(MultipleLocator(tick_step))

    if CHART_CONFIG.get("axis_equal"):
        ax.set_aspect("equal", adjustable="box")


def _get_stat_value(rows, axis, stat):
    x_col = CHART_CONFIG.get("x_col")
    y_col = CHART_CONFIG.get("y_col")

    if axis == "x":
        col = x_col
    elif axis == "y":
        col = y_col
    else:
        return None

    values = [r[col] for r in rows if isinstance(r.get(col), (int, float))]

    if not values:
        return None

    values = sorted(values)

    if stat == "median":
        n = len(values)
        mid = n // 2

        if n % 2 == 1:
            return values[mid]

        return (values[mid - 1] + values[mid]) / 2

    if stat == "mean":
        return sum(values) / len(values)

    return None


def _plot_reference_lines(ax, rows):
    for ref in CHART_CONFIG.get("reference_lines", []):
        axis = ref.get("axis", "y")
        value = ref.get("value")
        stat = ref.get("stat")
        label = ref.get("label", "")

        if stat:
            value = _get_stat_value(rows, axis, stat)

        if axis == "diagonal":
            x_min, x_max = ax.get_xlim()
            y_min, y_max = ax.get_ylim()
            low = max(x_min, y_min)
            high = min(x_max, y_max)

            ax.plot(
                [low, high],
                [low, high],
                color=ref.get("color", "#888888"),
                linewidth=ref.get("linewidth", 1.0),
                linestyle=ref.get("linestyle", "--"),
                alpha=ref.get("alpha", 0.8),
                zorder=ref.get("zorder", 0),
            )

            if label:
                ax.text(
                    high,
                    high,
                    label,
                    ha="right",
                    va="bottom",
                    fontsize=10,
                    color=ref.get("color", "#888888"),
                )

            continue

        if value is None:
            continue

        if axis == "y":
            ax.axhline(
                value,
                color=ref.get("color", "#888888"),
                linewidth=ref.get("linewidth", 1.0),
                linestyle=ref.get("linestyle", "--"),
                alpha=ref.get("alpha", 0.8),
                zorder=ref.get("zorder", 0),
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

        elif axis == "x":
            ax.axvline(
                value,
                color=ref.get("color", "#888888"),
                linewidth=ref.get("linewidth", 1.0),
                linestyle=ref.get("linestyle", "--"),
                alpha=ref.get("alpha", 0.8),
                zorder=ref.get("zorder", 0),
            )

            if label:
                ax.text(
                    value,
                    ax.get_ylim()[1],
                    label,
                    ha="left",
                    va="top",
                    rotation=90,
                    fontsize=10,
                    color=ref.get("color", "#888888"),
                )


def _plot_highlights_and_annotations(ax):
    highlight_style = CHART_CONFIG.get("highlight_style", {})
    highlight_color = CHART_CONFIG.get("highlight_color", "#C44E52")

    for p in CHART_CONFIG.get("highlight_points", []):
        ax.scatter(
            p["x"],
            p["y"],
            s=p.get("size", highlight_style.get("size", 90)),
            color=p.get("color", highlight_style.get("color", highlight_color)),
            alpha=p.get("alpha", highlight_style.get("alpha", 1.0)),
            zorder=p.get("zorder", highlight_style.get("zorder", 8)),
        )

    x_min, x_max = ax.get_xlim()
    x_range = x_max - x_min

    for p in CHART_CONFIG.get("annotate_points", []):
        x = p["x"]
        y = p["y"]

        xytext = p.get("xytext", [10, 10])
        dx = p.get("dx", xytext[0])
        dy = p.get("dy", xytext[1])
        ha = p.get("ha", "left")

        if isinstance(x, (int, float)) and x_range > 0:
            right_edge_threshold = x_min + (0.82 * x_range)
            if x >= right_edge_threshold and dx > 0:
                dx = -10
                ha = "right"

        ax.annotate(
            p.get("text", ""),
            xy=(x, y),
            xytext=(dx, dy),
            textcoords="offset points",
            fontsize=p.get("fontsize", 9),
            color=p.get("color", "#111111"),
            ha=ha,
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

            if _series_matches(series_name, focus_series):
                style = focus_style
            elif _series_matches(series_name, secondary_series):
                style = secondary_style
            elif focus_series is not None:
                style = context_style
            else:
                style = focus_style

            ax.plot(
                [p[x_col] for p in points],
                [p[y_col] for p in points],
                color=style.get("color", "#1F8FA8"),
                linewidth=style.get("linewidth", 2.0),
                alpha=style.get("alpha", 1.0),
                zorder=style.get("zorder", 3),
            )

    else:
        rows = sorted(rows, key=lambda d: d[x_col])
        focus_style = CHART_CONFIG.get("focus_style", {})

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

    rows = sorted(
        rows,
        key=lambda d: d[CHART_CONFIG.get("sort_by", y_col)],
        reverse=CHART_CONFIG.get("sort_order", "ascending") == "descending",
    )

    limit = CHART_CONFIG.get("limit")
    if limit:
        rows = rows[:limit]

    style = CHART_CONFIG.get("point_style", CHART_CONFIG.get("focus_style", {}))

    ax.bar(
        [r[x_col] for r in rows],
        [r[y_col] for r in rows],
        color=style.get("color", "#1F8FA8"),
        alpha=style.get("alpha", 0.75),
        zorder=4,
    )


def _plot_dot(ax, rows):
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    rows = sorted(
        rows,
        key=lambda d: d[CHART_CONFIG.get("sort_by", x_col)],
        reverse=CHART_CONFIG.get("sort_order", "ascending") == "descending",
    )

    limit = CHART_CONFIG.get("limit")
    if limit:
        rows = rows[:limit]

    point_style = CHART_CONFIG.get("point_style", {})

    ax.scatter(
        [r[x_col] for r in rows],
        [r[y_col] for r in rows],
        color=point_style.get("color", "#1F8FA8"),
        alpha=point_style.get("alpha", 0.75),
        s=point_style.get("size", 52),
        zorder=4,
    )

    if CHART_CONFIG.get("sort_order") == "descending":
        ax.invert_yaxis()


def _plot_scatter(ax, rows):
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    point_style = CHART_CONFIG.get("point_style", {})

    ax.scatter(
        [r[x_col] for r in rows],
        [r[y_col] for r in rows],
        color=point_style.get("color", "#1F8FA8"),
        alpha=point_style.get("alpha", 0.55),
        s=point_style.get("size", 42),
        zorder=4,
    )


def main():
    data_file = REPO_ROOT / CHART_CONFIG["data_file"]
    rows, columns = _read_csv(data_file)

    rows = _apply_filters(rows)

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

    _apply_limits_ticks_and_aspect(ax)
    _plot_reference_lines(ax, rows)
    _plot_highlights_and_annotations(ax)
    _apply_axis_formatting(ax)
    _add_titles_and_footer(fig)

    output_dir = REPO_ROOT / "output"
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_slug = CHART_CONFIG.get("output_slug", Path(CHART_CONFIG["data_file"]).stem)
    output_path = output_dir / f"{output_slug}_{timestamp}.png"

    fig.savefig(output_path, dpi=200, facecolor=fig.get_facecolor())
    print(f"Saved chart to {output_path}")


if __name__ == "__main__":
    main()