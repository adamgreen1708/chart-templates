see import csv
import os
import sys
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


def _read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        reader.fieldnames = [h.strip().replace("\ufeff", "") for h in reader.fieldnames]
        rows = []
        for row in reader:
            rows.append({k.strip(): _coerce_value(v) for k, v in row.items()})
    return rows, reader.fieldnames


def _require_columns(columns, required):
    missing = [c for c in required if c and c not in columns]
    if missing:
        raise ValueError(
            f"Missing column(s): {', '.join(missing)}\n"
            f"Available columns: {', '.join(columns)}"
        )


def _apply_filters(rows):
    filters = CHART_CONFIG.get("filters", [])
    if not filters:
        return rows

    out = rows
    for f in filters:
        col = f["column"]
        op = f["operator"]
        val = f["value"]

        if op == "<=":
            out = [r for r in out if float(r[col]) <= float(val)]
        elif op == "<":
            out = [r for r in out if float(r[col]) < float(val)]
        elif op == ">=":
            out = [r for r in out if float(r[col]) >= float(val)]
        elif op == ">":
            out = [r for r in out if float(r[col]) > float(val)]
        elif op == "==":
            out = [r for r in out if float(r[col]) == float(val)]
        elif op == "!=":
            out = [r for r in out if float(r[col]) != float(val)]
        else:
            raise ValueError(f"Unsupported filter operator: {op}")

    return out


def _apply_sort(rows):
    sort = CHART_CONFIG.get("sort")
    if not sort:
        return rows

    by = sort["by"]
    ascending = sort.get("ascending", True)
    return sorted(rows, key=lambda r: float(r[by]), reverse=not ascending)


def _fmt_percent(x, pos=None):
    return f"{x:.0f}%"


def _fmt_currency(x, pos=None):
    return f"${x:.2f}"


def _axis_formatter(fmt):
    if fmt == "percent":
        return FuncFormatter(_fmt_percent)
    if fmt == "currency":
        return FuncFormatter(_fmt_currency)
    return None


def _apply_axis_config(ax):
    x_axis = CHART_CONFIG.get("x_axis", {})
    y_axis = CHART_CONFIG.get("y_axis", {})

    if x_axis:
        if x_axis.get("min") is not None or x_axis.get("max") is not None:
            ax.set_xlim(x_axis.get("min"), x_axis.get("max"))
        if x_axis.get("tick_interval") is not None:
            ax.xaxis.set_major_locator(MultipleLocator(x_axis["tick_interval"]))
        formatter = _axis_formatter(x_axis.get("format"))
        if formatter:
            ax.xaxis.set_major_formatter(formatter)

    if y_axis:
        if y_axis.get("min") is not None or y_axis.get("max") is not None:
            ax.set_ylim(y_axis.get("min"), y_axis.get("max"))
        if y_axis.get("tick_interval") is not None:
            ax.yaxis.set_major_locator(MultipleLocator(y_axis["tick_interval"]))
        formatter = _axis_formatter(y_axis.get("format"))
        if formatter:
            ax.yaxis.set_major_formatter(formatter)


def _apply_house_style(fig, ax):
    bg = "#F3F4F6"
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#B5B5B5")

    ax.grid(axis="x", color="#D9D9D9", linewidth=0.8, alpha=0.65)
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.8, alpha=0.65)

    ax.tick_params(axis="both", labelsize=9, colors="#4A4A4A", length=0)

    ax.xaxis.label.set_size(9)
    ax.yaxis.label.set_size(9)


def _add_titles(fig):
    fig.text(
        0.14,
        0.91,
        CHART_CONFIG.get("title", ""),
        fontsize=22,
        fontweight="bold",
        ha="left",
        va="top",
        color="#111111",
        wrap=True,
    )
    fig.text(
        0.14,
        0.855,
        CHART_CONFIG.get("subtitle", ""),
        fontsize=11,
        ha="left",
        va="top",
        color="#555555",
        wrap=True,
    )


def _add_footer(fig):
    fig.text(
        0.14,
        0.06,
        CHART_CONFIG.get("footer_left", ""),
        fontsize=9,
        ha="left",
        color="#555555",
    )
    fig.text(
        0.98,
        0.06,
        CHART_CONFIG.get("source_text", ""),
        fontsize=9,
        ha="right",
        color="#555555",
    )


def _add_reference_lines(ax):
    for ref in CHART_CONFIG.get("reference_lines", []):
        axis = ref.get("axis")
        value = ref.get("value")
        label = ref.get("label", "")
        color = ref.get("color", "#7A7A7A")
        linestyle = ref.get("linestyle", "--")
        linewidth = ref.get("linewidth", 1.2)

        if axis == "x":
            ax.axvline(value, color=color, linestyle=linestyle, linewidth=linewidth, zorder=1)
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


def _add_highlights(ax):
    style = CHART_CONFIG.get("highlight_style", {})
    default_color = style.get("color", "#C44E52")
    size = style.get("size", 90)
    alpha = style.get("alpha", 1.0)

    for p in CHART_CONFIG.get("highlight_points", []):
        if "x" not in p or "y" not in p:
            continue

        x = p["x"]
        y = p["y"]
        label = p.get("label")
        color = p.get("color", default_color)

        ax.scatter(x, y, s=size, color=color, alpha=alpha, zorder=5)

        if label:
            ax.annotate(
                label,
                xy=(x, y),
                xytext=(8, 0),
                textcoords="offset points",
                ha="left",
                va="center",
                fontsize=8,
                color=color,
                fontweight="bold",
            )


def _add_value_labels(ax, rows):
    label_style = CHART_CONFIG.get("label_style", {})
    if not label_style.get("enabled", False):
        return

    label_col = label_style.get("label_col")
    label_format = label_style.get("label_format", "{}")
    fontsize = label_style.get("fontsize", 8)
    position = label_style.get("position", "right")

    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    for r in rows:
        x = r[x_col]
        y = r[y_col]
        val = r[label_col]

        try:
            text = label_format.format(float(val))
        except Exception:
            text = str(val)

        offset = 6 if position == "right" else -6
        ha = "left" if position == "right" else "right"

        ax.annotate(
            text,
            xy=(x, y),
            xytext=(offset, 0),
            textcoords="offset points",
            ha=ha,
            va="center",
            fontsize=fontsize,
            color="#4A4A4A",
        )


def _plot_dot(ax, rows):
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    style = CHART_CONFIG.get("dot_style", {})
    color = style.get("color", "#1F8FA8")
    size = style.get("size", 60)
    alpha = style.get("alpha", 0.8)

    x = [r[x_col] for r in rows]
    y = [r[y_col] for r in rows]

    ax.scatter(x, y, s=size, color=color, alpha=alpha, zorder=3)


def _plot_bar(ax, rows):
    x_col = CHART_CONFIG["x_col"]
    y_col = CHART_CONFIG["y_col"]

    style = CHART_CONFIG.get("bar_style", {})
    color = style.get("color", "#1F8FA8")
    alpha = style.get("alpha", 0.9)

    x = [r[x_col] for r in rows]
    y = [r[y_col] for r in rows]

    ax.bar(x, y, color=color, alpha=alpha, zorder=3)


def main():
    data_file = REPO_ROOT / CHART_CONFIG["data_file"]
    rows, columns = _read_csv(data_file)

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

    fig, ax = plt.subplots(figsize=(10, 7))

    chart_type = CHART_CONFIG.get("chart_type")

    if chart_type == "dot":
        _plot_dot(ax, rows)
    elif chart_type == "bar":
        _plot_bar(ax, rows)
    else:
        raise ValueError(f"Unsupported chart_type: {chart_type}")

    ax.set_xlabel(CHART_CONFIG.get("x_label", ""), fontsize=9)
    ax.set_ylabel(CHART_CONFIG.get("y_label", ""), fontsize=9)

    _apply_axis_config(ax)
    _apply_house_style(fig, ax)
    _add_reference_lines(ax)
    _add_highlights(ax)
    _add_value_labels(ax, rows)
    _add_titles(fig)
    _add_footer(fig)

    # IMPORTANT: fixes country labels bleeding off the left
    plt.subplots_adjust(
        left=0.28,
        right=0.94,
        top=0.72,
        bottom=0.13,
    )

    output_file = CHART_CONFIG.get("output_file", "output/chart.png")

    # Force output folder if filename only is supplied
    if "/" not in output_file:
        output_file = f"output/{output_file}"

    output_path = REPO_ROOT / output_file
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        output_path,
        dpi=200,
        bbox_inches="tight",
        facecolor=fig.get_facecolor()
    )

    print(f"Saved chart to {output_path}")

if __name__ == "__main__":
    main()