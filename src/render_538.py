import csv
import sys
import textwrap
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from chart_config import CHART_CONFIG


BG = "#F3F4F6"
GRID = "#D9D9D9"
TEXT = "#111111"
SUBTEXT = "#555555"


def _wrap_text(text: str, width: int, max_lines: int | None = None) -> str:
    if not text:
        return ""

    wrapped = textwrap.wrap(str(text), width=width)

    if max_lines is not None and len(wrapped) > max_lines:
        wrapped = wrapped[:max_lines]
        wrapped[-1] = wrapped[-1].rstrip(" .,;:") + "…"

    return "\n".join(wrapped)


def apply_538_template(
    ax,
    fig,
    title="",
    subtitle="",
    source_text="",
    footer_left="",
    vertical_gridlines=True,
    fig_bg=BG,
    plot_bg=BG,
    text_color=TEXT,
    subtext_color=SUBTEXT,
    grid_color=GRID,
    title_fontsize=22,
    subtitle_fontsize=13,
    tick_label_fontsize=12,
    footer_fontsize=10,
    title_wrap_width=28,
    subtitle_wrap_width=56,
    title_max_lines=2,
    subtitle_max_lines=2,
    title_x=0.10,
    title_y=0.93,
    subtitle_x=0.10,
    subtitle_y=0.855,
    footer_left_x=0.10,
    footer_right_x=0.90,
    footer_y=0.075,
    plot_top=0.72,
    plot_bottom=0.15,
    plot_left=0.10,
    plot_right=0.90,
):
    fig.patch.set_facecolor(fig_bg)
    ax.set_facecolor(plot_bg)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#B0B0B0")

    ax.tick_params(axis="x", colors=subtext_color, labelsize=tick_label_fontsize, length=0)
    ax.tick_params(axis="y", colors=subtext_color, labelsize=tick_label_fontsize, length=0)

    ax.grid(axis="y", color=grid_color, linewidth=0.8)

    if vertical_gridlines:
        ax.grid(axis="x", color=grid_color, linewidth=0.35, alpha=0.6)

    fig.subplots_adjust(
        top=plot_top,
        bottom=plot_bottom,
        left=plot_left,
        right=plot_right,
    )

    wrapped_title = _wrap_text(title, title_wrap_width, title_max_lines)
    wrapped_subtitle = _wrap_text(subtitle, subtitle_wrap_width, subtitle_max_lines)

    fig.text(
        title_x,
        title_y,
        wrapped_title,
        ha="left",
        va="top",
        fontsize=title_fontsize,
        fontweight="bold",
        color=text_color,
        linespacing=1.08,
        clip_on=True,
    )

    fig.text(
        subtitle_x,
        subtitle_y,
        wrapped_subtitle,
        ha="left",
        va="top",
        fontsize=subtitle_fontsize,
        color=subtext_color,
        linespacing=1.15,
        clip_on=True,
    )

    fig.text(
        footer_left_x,
        footer_y,
        footer_left,
        ha="left",
        va="bottom",
        fontsize=footer_fontsize,
        color=subtext_color,
        clip_on=True,
    )

    fig.text(
        footer_right_x,
        footer_y,
        source_text,
        ha="right",
        va="bottom",
        fontsize=footer_fontsize,
        color=subtext_color,
        clip_on=True,
    )


def _coerce_value(value):
    try:
        num = float(value)
        return int(num) if num.is_integer() else num
    except Exception:
        return value


def _safe_headers(reader):
    reader.fieldnames = [h.strip().replace("\ufeff", "") for h in reader.fieldnames]
    return reader


def _clean_row(row):
    return {k.strip(): _coerce_value(v) for k, v in row.items()}


def _require_columns(columns, required):
    missing = [c for c in required if c and c not in columns]
    if missing:
        raise ValueError(
            f"Missing column(s): {', '.join(missing)}\n"
            f"Available columns: {', '.join(columns)}"
        )


def _axis_formatter(fmt):
    if fmt is None:
        return None

    if fmt == "percent":
        return FuncFormatter(lambda x, pos: f"{x:.0f}%")

    if fmt == "currency":
        return FuncFormatter(lambda x, pos: f"${x:,.0f}")

    if fmt == "millions":
        return FuncFormatter(lambda x, pos: f"{x / 1_000_000:.0f}M")

    return FuncFormatter(lambda x, pos: format(x, fmt))


def _read_data():
    data_file = REPO_ROOT / CHART_CONFIG["data_file"]

    with open(data_file, newline="", encoding="utf-8-sig") as f:
        reader = _safe_headers(csv.DictReader(f))
        rows = [_clean_row(row) for row in reader]
        columns = reader.fieldnames

    return rows, columns


def _apply_filters(rows):
    filters = CHART_CONFIG.get("filters", [])
    if not filters:
        return rows

    filtered = rows

    for f in filters:
        col = f["column"]
        op = f["operator"]
        val = f["value"]

        new_filtered = []

        for r in filtered:
            try:
                a = float(r[col])
                b = float(val)
            except Exception:
                a = str(r[col])
                b = str(val)

            if op == "<=":
                keep = a <= b
            elif op == "<":
                keep = a < b
            elif op == ">=":
                keep = a >= b
            elif op == ">":
                keep = a > b
            elif op == "==":
                keep = a == b
            elif op == "!=":
                keep = a != b
            else:
                raise ValueError(f"Unsupported filter operator: {op}")

            if keep:
                new_filtered.append(r)

        filtered = new_filtered

    return filtered


def _normalise_sort_config():
    sort = CHART_CONFIG.get("sort")
    sort_descending = CHART_CONFIG.get("sort_descending", False)

    if isinstance(sort, dict):
        return sort.get("by"), sort.get("ascending", not sort_descending)

    if isinstance(sort, str):
        return sort, not sort_descending

    if sort_descending:
        return CHART_CONFIG.get("y_col"), False

    return None, True


def _sort_value(value):
    if value is None or value == "":
        return float("-inf")

    try:
        return float(value)
    except Exception:
        return str(value).lower()


def _apply_sort(rows):
    sort_by, ascending = _normalise_sort_config()

    if not sort_by or not rows:
        return rows

    if sort_by not in rows[0]:
        available = ", ".join(rows[0].keys())
        raise ValueError(
            f"Sort column '{sort_by}' not found.\n"
            f"Available columns: {available}"
        )

    return sorted(
        rows,
        key=lambda r: _sort_value(r.get(sort_by)),
        reverse=not ascending,
    )


def _apply_axis_config(ax):
    x_axis = CHART_CONFIG.get("x_axis", {})
    y_axis = CHART_CONFIG.get("y_axis", {})

    x_min = x_axis.get("min")
    x_max = x_axis.get("max")

    if x_min is not None or x_max is not None:
        ax.set_xlim(x_min, x_max)

    if x_axis.get("tick_interval") is not None:
        ax.xaxis.set_major_locator(MultipleLocator(x_axis["tick_interval"]))

    x_formatter = _axis_formatter(x_axis.get("format"))
    if x_formatter:
        ax.xaxis.set_major_formatter(x_formatter)

    y_min = CHART_CONFIG.get("y_axis_min", y_axis.get("min"))
    y_max = CHART_CONFIG.get("y_axis_max", y_axis.get("max"))

    if y_min is not None or y_max is not None:
        ax.set_ylim(y_min, y_max)

    y_tick_interval = CHART_CONFIG.get("y_tick_interval", y_axis.get("tick_interval"))

    if y_tick_interval is not None:
        ax.yaxis.set_major_locator(MultipleLocator(y_tick_interval))

    y_format = CHART_CONFIG.get("y_tick_format", y_axis.get("format"))
    y_formatter = _axis_formatter(y_format)

    if y_formatter:
        ax.yaxis.set_major_formatter(y_formatter)


def _plot_reference_lines(ax):
    for ref in CHART_CONFIG.get("reference_lines", []):
        axis = ref.get("axis")
        value = ref.get("value")
        label = ref.get("label", "")
        color = ref.get("color", "#7A7A7A")
        linestyle = ref.get("linestyle", "--")
        linewidth = ref.get("linewidth", 1.2)

        if axis == "x":
            ax.axvline(value, color=color, linestyle=linestyle, linewidth=linewidth, zorder=1)

            if label:
                ax.text(
                    value,
                    1.02,
                    label,
                    transform=ax.get_xaxis_transform(),
                    ha="center",
                    va="bottom",
                    fontsize=8,
                    color=color,
                    rotation=0,
                    clip_on=False,
                )

        elif axis == "y":
            ax.axhline(value, color=color, linestyle=linestyle, linewidth=linewidth, zorder=1)

            if label:
                ax.text(
                    -0.02,
                    value,
                    label,
                    transform=ax.get_yaxis_transform(),
                    ha="right",
                    va="center",
                    fontsize=8,
                    color=color,
                    clip_on=False,
                )


def _point_matches_row(point, row):
    for key, value in point.items():
        if key in ["x", "y", "label", "color", "size", "alpha"]:
            continue

        if key not in row:
            return False

        if str(row[key]) != str(value):
            return False

    return True


def _resolve_point_xy(point, rows):
    if "x" in point and "y" in point:
        return point["x"], point["y"]

    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    for row in rows:
        if _point_matches_row(point, row):
            return row[x_col], row[y_col]

    return None, None


def _plot_highlights(ax, rows):
    highlight_style = CHART_CONFIG.get("highlight_style", {})
    default_color = highlight_style.get("color", "#C44E52")
    default_size = highlight_style.get("size", 90)
    default_alpha = highlight_style.get("alpha", 1.0)

    for p in CHART_CONFIG.get("highlight_points", []):
        x, y = _resolve_point_xy(p, rows)

        if x is None or y is None:
            continue

        color = p.get("color", default_color)
        size = p.get("size", default_size)
        alpha = p.get("alpha", default_alpha)

        ax.scatter(x, y, s=size, color=color, alpha=alpha, zorder=5)

        if p.get("label"):
            ax.annotate(
                p["label"],
                xy=(x, y),
                xytext=(8, 0),
                textcoords="offset points",
                ha="left",
                va="center",
                fontsize=8,
                color=color,
                fontweight="bold",
                clip_on=False,
            )


def _plot_annotations(ax):
    for p in CHART_CONFIG.get("annotate_points", []):
        if "x" not in p or "y" not in p:
            continue

        ax.annotate(
            p.get("label", p.get("text", "")),
            xy=(p["x"], p["y"]),
            xytext=p.get("xytext", (10, 10)),
            textcoords="offset points",
            ha=p.get("ha", "left"),
            va=p.get("va", "center"),
            fontsize=p.get("fontsize", 9),
            color=p.get("color", "#333333"),
            arrowprops=p.get(
                "arrowprops",
                {
                    "arrowstyle": "-",
                    "color": p.get("color", "#333333"),
                    "lw": 0.8,
                },
            ),
            clip_on=True,
        )


def _plot_labels(ax, rows):
    label_style = CHART_CONFIG.get("label_style", {})

    if not label_style.get("enabled", False):
        return

    label_col = label_style.get("label_col")

    if not label_col:
        return

    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    label_format = label_style.get("label_format", "{}")
    fontsize = label_style.get("fontsize", 8)
    position = label_style.get("position", "right")

    for r in rows:
        x = r[x_col]
        y = r[y_col]
        val = r[label_col]

        try:
            text = label_format.format(float(val))
        except Exception:
            text = str(val)

        if position == "left":
            offset = (-6, 0)
            ha = "right"
        else:
            offset = (6, 0)
            ha = "left"

        ax.annotate(
            text,
            xy=(x, y),
            xytext=offset,
            textcoords="offset points",
            ha=ha,
            va="center",
            fontsize=fontsize,
            color="#4A4A4A",
            clip_on=True,
        )


def _plot_dot(ax, rows):
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    style = CHART_CONFIG.get("dot_style", {})
    color = style.get("color", CHART_CONFIG.get("focus_style", {}).get("color", "#1F8FA8"))
    size = style.get("size", CHART_CONFIG.get("marker_size", 65))
    alpha = style.get("alpha", 0.8)

    ax.scatter(
        [r[x_col] for r in rows],
        [r[y_col] for r in rows],
        s=size,
        color=color,
        alpha=alpha,
        zorder=3,
    )


def _plot_bar(ax, rows):
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    style = CHART_CONFIG.get("bar_style", {})
    color = style.get("color", CHART_CONFIG.get("focus_style", {}).get("color", "#1F8FA8"))
    alpha = style.get("alpha", 0.9)

    ax.bar(
        [r[x_col] for r in rows],
        [r[y_col] for r in rows],
        color=color,
        alpha=alpha,
        zorder=3,
    )


def _plot_scatter(ax, rows):
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    style = CHART_CONFIG.get("point_style", {})
    color = style.get("color", CHART_CONFIG.get("focus_style", {}).get("color", "#1F8FA8"))
    size = style.get("size", CHART_CONFIG.get("marker_size", 55))
    alpha = style.get("alpha", 0.75)

    ax.scatter(
        [r[x_col] for r in rows],
        [r[y_col] for r in rows],
        s=size,
        color=color,
        alpha=alpha,
        zorder=3,
    )


def _plot_line(ax, rows):
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]
    series_col = CHART_CONFIG.get("series_col")

    if not series_col:
        ax.plot(
            [r[x_col] for r in rows],
            [r[y_col] for r in rows],
            color=CHART_CONFIG.get("focus_style", {}).get("color", "#1F8FA8"),
            linewidth=CHART_CONFIG.get("line_width", 2.6),
            zorder=3,
        )
        return

    grouped = defaultdict(list)

    for r in rows:
        grouped[r[series_col]].append(r)

    focus_series = CHART_CONFIG.get("focus_series")
    secondary_series = CHART_CONFIG.get("secondary_series")

    for series, values in grouped.items():
        values = sorted(values, key=lambda r: _sort_value(r[x_col]))

        if focus_series and series == focus_series:
            style = CHART_CONFIG.get("focus_style", {})
        elif secondary_series and series == secondary_series:
            style = CHART_CONFIG.get("secondary_style", {})
        else:
            style = CHART_CONFIG.get("context_style", {})

        ax.plot(
            [r[x_col] for r in values],
            [r[y_col] for r in values],
            color=style.get("color", "#D9D9D9"),
            linewidth=style.get("linewidth", CHART_CONFIG.get("line_width", 2.6)),
            alpha=style.get("alpha", 1.0),
            zorder=3,
        )


def _plot_end_labels(ax):
    for label in CHART_CONFIG.get("end_labels", []):
        if "x" not in label or "y" not in label:
            continue

        ax.annotate(
            label.get("label", ""),
            xy=(label["x"], label["y"]),
            xytext=(6, 0),
            textcoords="offset points",
            ha="left",
            va="center",
            fontsize=label.get("fontsize", 9),
            color=label.get("color", "#333333"),
            fontweight=label.get("fontweight", "normal"),
            clip_on=True,
        )


def main():
    rows, columns = _read_data()

    required = [
        CHART_CONFIG.get("x_col"),
        CHART_CONFIG.get("y_col"),
        CHART_CONFIG.get("series_col"),
        CHART_CONFIG.get("value_col"),
    ]

    for f in CHART_CONFIG.get("filters", []):
        required.append(f.get("column"))

    sort_by, _ = _normalise_sort_config()

    if sort_by:
        required.append(sort_by)

    label_col = CHART_CONFIG.get("label_style", {}).get("label_col")

    if label_col:
        required.append(label_col)

    _require_columns(columns, required)

    rows = _apply_filters(rows)
    rows = _apply_sort(rows)

    if not rows:
        raise ValueError("No rows remain after filtering.")

    fig, ax = plt.subplots(
        figsize=(
            CHART_CONFIG.get("fig_width", 8.0),
            CHART_CONFIG.get("fig_height", 8.0),
        )
    )

    chart_type = CHART_CONFIG.get("chart_type")

    if chart_type == "dot":
        _plot_dot(ax, rows)
    elif chart_type == "bar":
        _plot_bar(ax, rows)
    elif chart_type == "scatter":
        _plot_scatter(ax, rows)
    elif chart_type == "line":
        _plot_line(ax, rows)
    else:
        raise ValueError(f"Unsupported chart_type: {chart_type}")

    ax.set_xlabel(CHART_CONFIG.get("x_label", ""))
    ax.set_ylabel(CHART_CONFIG.get("y_label", ""))

    ax.xaxis.label.set_size(CHART_CONFIG.get("axis_label_fontsize", 9))
    ax.yaxis.label.set_size(CHART_CONFIG.get("axis_label_fontsize", 9))

    if CHART_CONFIG.get("x_tick_rotation", 0):
        plt.setp(
            ax.get_xticklabels(),
            rotation=CHART_CONFIG.get("x_tick_rotation", 0),
            ha="right",
        )

    _apply_axis_config(ax)
    _plot_reference_lines(ax)
    _plot_highlights(ax, rows)
    _plot_annotations(ax)
    _plot_labels(ax, rows)
    _plot_end_labels(ax)

    apply_538_template(
        ax,
        fig,
        title=CHART_CONFIG.get("title", ""),
        subtitle=CHART_CONFIG.get("subtitle", ""),
        source_text=CHART_CONFIG.get("source_text", ""),
        footer_left=CHART_CONFIG.get("footer_left", ""),
        vertical_gridlines=CHART_CONFIG.get("vertical_gridlines", False),
        title_fontsize=CHART_CONFIG.get("title_fontsize", 22),
        subtitle_fontsize=CHART_CONFIG.get("subtitle_fontsize", 13),
        tick_label_fontsize=CHART_CONFIG.get("tick_label_fontsize", 10),
        footer_fontsize=CHART_CONFIG.get("footer_fontsize", 10),
        title_wrap_width=CHART_CONFIG.get("title_wrap_width", 28),
        subtitle_wrap_width=CHART_CONFIG.get("subtitle_wrap_width", 56),
        title_max_lines=CHART_CONFIG.get("title_max_lines", 2),
        subtitle_max_lines=CHART_CONFIG.get("subtitle_max_lines", 2),
        title_x=CHART_CONFIG.get("title_x", 0.10),
        title_y=CHART_CONFIG.get("title_y", 0.93),
        subtitle_x=CHART_CONFIG.get("subtitle_x", 0.10),
        subtitle_y=CHART_CONFIG.get("subtitle_y", 0.855),
        footer_left_x=CHART_CONFIG.get("footer_left_x", 0.10),
        footer_right_x=CHART_CONFIG.get("footer_right_x", 0.90),
        footer_y=CHART_CONFIG.get("footer_y", 0.075),
        plot_top=CHART_CONFIG.get("plot_top", 0.72),
        plot_bottom=CHART_CONFIG.get("plot_bottom", 0.15),
        plot_left=CHART_CONFIG.get("plot_left", 0.10),
        plot_right=CHART_CONFIG.get("plot_right", 0.90),
    )

    ax.margins(x=0.04)

    plt.subplots_adjust(
        left=CHART_CONFIG.get("plot_left", 0.10),
        right=CHART_CONFIG.get("plot_right", 0.90),
        top=CHART_CONFIG.get("plot_top", 0.72),
        bottom=CHART_CONFIG.get("plot_bottom", 0.15),
    )

    output_file = CHART_CONFIG.get("output_file", "output/chart.png")

    if "/" not in output_file:
        output_file = f"output/{output_file}"

    output_path = REPO_ROOT / output_file
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        output_path,
        dpi=CHART_CONFIG.get("dpi", 200),
        facecolor=fig.get_facecolor(),
    )

    print(f"Saved chart to {output_path}")


if __name__ == "__main__":
    main()