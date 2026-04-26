import csv
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from chart_538 import apply_538_template
from chart_config import CHART_CONFIG


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


def _format_axis(fmt):
    if fmt == "percent":
        return FuncFormatter(lambda x, pos: f"{x:.0f}%")
    if fmt == "currency":
        return FuncFormatter(lambda x, pos: f"${x:.2f}")
    return None


def _apply_filters(rows):
    filters = CHART_CONFIG.get("filters", [])
    if not filters:
        return rows

    filtered = rows

    for f in filters:
        col = f["column"]
        op = f["operator"]
        val = f["value"]

        def n(v):
            return float(v)

        if op == "<=":
            filtered = [r for r in filtered if n(r[col]) <= n(val)]
        elif op == "<":
            filtered = [r for r in filtered if n(r[col]) < n(val)]
        elif op == ">=":
            filtered = [r for r in filtered if n(r[col]) >= n(val)]
        elif op == ">":
            filtered = [r for r in filtered if n(r[col]) > n(val)]
        elif op == "==":
            filtered = [r for r in filtered if n(r[col]) == n(val)]
        elif op == "!=":
            filtered = [r for r in filtered if n(r[col]) != n(val)]
        else:
            raise ValueError(f"Unsupported filter operator: {op}")

    return filtered


def _apply_sort(rows):
    sort = CHART_CONFIG.get("sort")
    if not sort:
        return rows

    by = sort["by"]
    ascending = sort.get("ascending", True)

    return sorted(rows, key=lambda r: float(r[by]), reverse=not ascending)


def _apply_axis_config(ax):
    x_axis = CHART_CONFIG.get("x_axis", {})
    y_axis = CHART_CONFIG.get("y_axis", {})

    if x_axis:
        if x_axis.get("min") is not None or x_axis.get("max") is not None:
            ax.set_xlim(x_axis.get("min"), x_axis.get("max"))

        if x_axis.get("tick_interval") is not None:
            ax.xaxis.set_major_locator(MultipleLocator(x_axis["tick_interval"]))

        formatter = _format_axis(x_axis.get("format"))
        if formatter:
            ax.xaxis.set_major_formatter(formatter)

    if y_axis:
        if y_axis.get("min") is not None or y_axis.get("max") is not None:
            ax.set_ylim(y_axis.get("min"), y_axis.get("max"))

        if y_axis.get("tick_interval") is not None:
            ax.yaxis.set_major_locator(MultipleLocator(y_axis["tick_interval"]))

        formatter = _format_axis(y_axis.get("format"))
        if formatter:
            ax.yaxis.set_major_formatter(formatter)


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
                    1.01,
                    label,
                    transform=ax.get_xaxis_transform(),
                    ha="center",
                    va="bottom",
                    fontsize=8,
                    color=color,
                    rotation=90,
                )

        elif axis == "y":
            ax.axhline(value, color=color, linestyle=linestyle, linewidth=linewidth, zorder=1)
            if label:
                ax.text(
                    1.01,
                    value,
                    label,
                    transform=ax.get_yaxis_transform(),
                    ha="left",
                    va="center",
                    fontsize=8,
                    color=color,
                )


def _plot_highlights(ax):
    highlight_style = CHART_CONFIG.get("highlight_style", {})
    default_color = highlight_style.get("color", "#C44E52")
    size = highlight_style.get("size", 90)
    alpha = highlight_style.get("alpha", 1)

    for p in CHART_CONFIG.get("highlight_points", []):
        # Safe guard: old renderer crashed if x/y were missing
        if "x" not in p or "y" not in p:
            continue

        color = p.get("color", default_color)

        ax.scatter(
            p["x"],
            p["y"],
            s=size,
            color=color,
            alpha=alpha,
            zorder=5,
        )

        if p.get("label"):
            ax.annotate(
                p["label"],
                xy=(p["x"], p["y"]),
                xytext=(8, 0),
                textcoords="offset points",
                ha="left",
                va="center",
                fontsize=8,
                color=color,
                fontweight="bold",
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
            label = label_format.format(float(val))
        except Exception:
            label = str(val)

        if position == "left":
            xytext = (-6, 0)
            ha = "right"
        else:
            xytext = (6, 0)
            ha = "left"

        ax.annotate(
            label,
            xy=(x, y),
            xytext=xytext,
            textcoords="offset points",
            ha=ha,
            va="center",
            fontsize=fontsize,
            color="#4A4A4A",
            clip_on=False,
        )


def _plot_dot(ax, rows):
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    style = CHART_CONFIG.get("dot_style", {})
    color = style.get("color", "#1F8FA8")
    size = style.get("size", 65)
    alpha = style.get("alpha", 0.75)

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
    color = style.get("color", "#1F8FA8")
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
    color = style.get("color", "#1F8FA8")
    size = style.get("size", 55)
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
            color="#1F8FA8",
            linewidth=3,
        )
        return

    grouped = defaultdict(list)
    for r in rows:
        grouped[r[series_col]].append(r)

    focus_series = CHART_CONFIG.get("focus_series")

    for series, values in grouped.items():
        values = sorted(values, key=lambda r: r[x_col])

        if focus_series and series == focus_series:
            style = CHART_CONFIG.get("focus_style", {})
            color = style.get("color", "#1F8FA8")
            linewidth = style.get("linewidth", 3)
            alpha = style.get("alpha", 1)
            zorder = 4
        else:
            style = CHART_CONFIG.get("context_style", {})
            color = style.get("color", "#CFCFCF")
            linewidth = style.get("linewidth", 1)
            alpha = style.get("alpha", 0.45)
            zorder = 2

        ax.plot(
            [r[x_col] for r in values],
            [r[y_col] for r in values],
            color=color,
            linewidth=linewidth,
            alpha=alpha,
            zorder=zorder,
        )


def _read_data():
    data_file = REPO_ROOT / CHART_CONFIG["data_file"]

    with open(data_file, newline="", encoding="utf-8-sig") as f:
        reader = _safe_headers(csv.DictReader(f))
        rows = [_clean_row(row) for row in reader]
        columns = reader.fieldnames

    return rows, columns


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

    sort = CHART_CONFIG.get("sort")
    if sort:
        required.append(sort.get("by"))

    label_col = CHART_CONFIG.get("label_style", {}).get("label_col")
    if label_col:
        required.append(label_col)

    _require_columns(columns, required)

    rows = _apply_filters(rows)
    rows = _apply_sort(rows)

    if not rows:
        raise ValueError("No rows remain after filtering.")

    # Restored square output behaviour
    fig_size = CHART_CONFIG.get("figsize", (8, 8))
    fig, ax = plt.subplots(figsize=fig_size)

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

    # Temporary smaller axis label fix
    axis_label_style = CHART_CONFIG.get("axis_label_style", {})
    axis_label_size = axis_label_style.get("fontsize", 9)
    ax.xaxis.label.set_size(axis_label_size)
    ax.yaxis.label.set_size(axis_label_size)

    _apply_axis_config(ax)
    _plot_reference_lines(ax)
    _plot_highlights(ax)
    _plot_labels(ax, rows)

    apply_538_template(
        fig=fig,
        ax=ax,
        title=CHART_CONFIG.get("title", ""),
        subtitle=CHART_CONFIG.get("subtitle", ""),
        source_text=CHART_CONFIG.get("source_text", ""),
        footer_left=CHART_CONFIG.get("footer_left", ""),
    )

    # Restored / protected padding logic, with extra left room for country labels
    padding = CHART_CONFIG.get("padding", {})

    plt.subplots_adjust(
        left=padding.get("left", 0.34),
        right=padding.get("right", 0.92),
        top=padding.get("top", 0.78),
        bottom=padding.get("bottom", 0.14),
    )

    output_file = CHART_CONFIG.get("output_file", "output/chart.png")

    # Keep original repo convention: output/, not outputs/
    if "/" not in output_file:
        output_file = f"output/{output_file}"

    output_path = REPO_ROOT / output_file
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        output_path,
        dpi=CHART_CONFIG.get("dpi", 200),
        bbox_inches="tight",
        facecolor=fig.get_facecolor(),
    )

    print(f"Saved chart to {output_path}")


if __name__ == "__main__":
    main()