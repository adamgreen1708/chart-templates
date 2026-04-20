import csv
import os
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from chart_538 import apply_538_template


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
    return {k.strip(): v for k, v in row.items()}


def _fail_with_columns(reader, missing):
    raise ValueError(
        f"Column '{missing}' not found.\nAvailable columns: {', '.join(reader.fieldnames)}"
    )


def _get_color(d, default="#1F8FA8"):
    return d.get("color") or d.get("colour") or default


def _format_value(val, fmt=None):
    if fmt:
        try:
            return fmt.format(val)
        except Exception:
            pass
    if isinstance(val, float):
        return f"{val:.1f}".rstrip("0").rstrip(".")
    return str(val)


def _safe_text_x_right(ax, frac=0.985):
    x_min, x_max = ax.get_xlim()
    return x_min + (x_max - x_min) * frac


def _safe_text_x_left(ax, frac=0.015):
    x_min, x_max = ax.get_xlim()
    return x_min + (x_max - x_min) * frac


def _safe_text_y(ax, y, frac=0.02):
    y_min, y_max = ax.get_ylim()
    span = y_max - y_min
    low = y_min + span * frac
    high = y_max - span * frac
    return min(max(y, low), high)


def _add_safe_end_label(ax, y, label, color="#1F8FA8"):
    x_pos = _safe_text_x_right(ax, 0.985)
    y_pos = _safe_text_y(ax, y, 0.025)

    ax.text(
        x_pos,
        y_pos,
        label,
        fontsize=10,
        color=color,
        ha="right",
        va="center",
        clip_on=True,
        zorder=8,
    )


def _add_safe_highlight_label(ax, x, y, label, color="#C44E52"):
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    x_span = x_max - x_min
    y_span = y_max - y_min

    if isinstance(x, (int, float)):
        near_right = x > x_min + x_span * 0.84
        text_x = x - x_span * 0.02 if near_right else x + x_span * 0.02
        ha = "right" if near_right else "left"
    else:
        text_x = x
        ha = "left"

    text_y = _safe_text_y(ax, y + y_span * 0.02, 0.04)

    ax.text(
        text_x,
        text_y,
        label,
        fontsize=9,
        color=color,
        ha=ha,
        va="bottom",
        clip_on=True,
        zorder=9,
    )


def load_wide_data(csv_path, x_col, y_col):
    x_vals, y_vals = [], []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = _safe_headers(csv.DictReader(f))

        if x_col not in reader.fieldnames:
            _fail_with_columns(reader, x_col)
        if y_col not in reader.fieldnames:
            _fail_with_columns(reader, y_col)

        for row in reader:
            row = _clean_row(row)
            x_vals.append(_coerce_value(row[x_col]))
            y_vals.append(_coerce_value(row[y_col]))

    return {"Main": {"x": x_vals, "y": y_vals}}


def load_long_data(csv_path, x_col, series_col, value_col):
    grouped = defaultdict(lambda: {"x": [], "y": []})

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = _safe_headers(csv.DictReader(f))

        for col in [x_col, series_col, value_col]:
            if col not in reader.fieldnames:
                _fail_with_columns(reader, col)

        for row in reader:
            row = _clean_row(row)
            series_name = row[series_col]
            grouped[series_name]["x"].append(_coerce_value(row[x_col]))
            grouped[series_name]["y"].append(_coerce_value(row[value_col]))

    return dict(grouped)


def sort_single_series_for_rank_chart(series_data, descending=True):
    if len(series_data) != 1:
        return series_data

    series_name = next(iter(series_data))
    values = series_data[series_name]
    pairs = list(zip(values["x"], values["y"]))
    pairs.sort(key=lambda t: t[1], reverse=descending)

    return {
        series_name: {
            "x": [p[0] for p in pairs],
            "y": [p[1] for p in pairs],
        }
    }


def apply_axis_controls(ax, cfg):
    y_min = cfg.get("y_axis_min")
    y_max = cfg.get("y_axis_max")

    if y_min is not None or y_max is not None:
        current_min, current_max = ax.get_ylim()
        ax.set_ylim(
            bottom=y_min if y_min is not None else current_min,
            top=y_max if y_max is not None else current_max,
        )

    y_tick_interval = cfg.get("y_tick_interval")
    if y_tick_interval is not None:
        ax.yaxis.set_major_locator(MultipleLocator(y_tick_interval))

    y_tick_format = cfg.get("y_tick_format")
    if y_tick_format:
        ax.yaxis.set_major_formatter(
            FuncFormatter(lambda val, pos: _format_value(val, y_tick_format))
        )

    x_tick_rotation = cfg.get("x_tick_rotation", 0)
    if x_tick_rotation:
        plt.setp(ax.get_xticklabels(), rotation=x_tick_rotation, ha="right")


def apply_reference_lines(ax, cfg):
    for ref in cfg.get("reference_lines", []):
        try:
            y = ref.get("y") if "y" in ref else ref.get("value")
            if y is None:
                continue

            line_color = _get_color(ref, "#999999")

            ax.axhline(
                y=y,
                color=line_color,
                linestyle=ref.get("linestyle", "--"),
                linewidth=ref.get("linewidth", 1.0),
                zorder=1,
            )

            label = ref.get("label")
            if label:
                label_x = ref.get("label_x", "left")
                label_offset = ref.get("label_offset", 0.0)

                x_pos = _safe_text_x_right(ax, 0.985) if label_x == "right" else _safe_text_x_left(ax, 0.015)
                y_pos = _safe_text_y(ax, y + label_offset, 0.03)

                ax.text(
                    x_pos,
                    y_pos,
                    label,
                    fontsize=9,
                    color=line_color,
                    ha="right" if label_x == "right" else "left",
                    va="bottom",
                    clip_on=True,
                    zorder=5,
                )
        except Exception:
            continue


def apply_highlights(ax, cfg):
    for pt in cfg.get("highlight_points", []):
        try:
            pt_color = _get_color(pt, "#C44E52")
            x = pt["x"]
            y = pt["y"]

            ax.scatter(
                x,
                y,
                color=pt_color,
                s=55,
                zorder=7,
            )

            if pt.get("label"):
                _add_safe_highlight_label(ax, x, y, pt["label"], pt_color)
        except Exception:
            continue


def apply_annotations(ax, cfg):
    for ann in cfg.get("annotate_points", []):
        try:
            ax.annotate(
                ann["text"],
                (ann["x"], ann["y"]),
                xytext=ann.get("xytext", (0, 0)),
                textcoords="offset points",
                ha=ann.get("ha", "left"),
                fontsize=9,
                zorder=9,
            )
        except Exception:
            continue


def _get_story_styles(cfg):
    return {
        "context": cfg.get(
            "context_style",
            {"color": "#CFCFCF", "linewidth": 1.0, "alpha": 0.40},
        ),
        "focus": cfg.get(
            "focus_style",
            {"color": "#1F8FA8", "linewidth": 3.0, "alpha": 1.0},
        ),
        "secondary": cfg.get(
            "secondary_style",
            {"color": "#7A7A7A", "linewidth": 2.0, "alpha": 0.90},
        ),
    }


def _plot_series(ax, x_vals, y_vals, style, cfg, zorder=3):
    ax.plot(
        x_vals,
        y_vals,
        color=_get_color(style, "#1F8FA8"),
        linewidth=style.get("linewidth", cfg.get("line_width", 2.6)),
        alpha=style.get("alpha", 1.0),
        marker="o" if cfg.get("show_markers", False) else None,
        markersize=cfg.get("marker_size", 0) if cfg.get("show_markers", False) else None,
        zorder=zorder,
    )


def render_line_single_series(ax, data, cfg):
    styles = _get_story_styles(cfg)
    series_name = next(iter(data))
    vals = data[series_name]

    _plot_series(ax, vals["x"], vals["y"], styles["focus"], cfg, zorder=4)

    if cfg.get("auto_end_labels", True):
        y = vals["y"][-1]
        _add_safe_end_label(ax, y, _format_value(y, cfg.get("y_tick_format")), _get_color(styles["focus"]))


def render_line_focus_vs_context(ax, data, cfg):
    styles = _get_story_styles(cfg)
    focus_series = cfg.get("focus_series")
    secondary_series = cfg.get("secondary_series")
    label_strategy = cfg.get("label_strategy", "focus_only")

    # Context first
    for series_name, vals in data.items():
        if series_name in {focus_series, secondary_series}:
            continue
        _plot_series(ax, vals["x"], vals["y"], styles["context"], cfg, zorder=2)

    # Secondary next
    if secondary_series and secondary_series in data:
        vals = data[secondary_series]
        _plot_series(ax, vals["x"], vals["y"], styles["secondary"], cfg, zorder=4)

        if cfg.get("auto_end_labels", True) and label_strategy in {"focus_and_secondary", "all"}:
            y = vals["y"][-1]
            _add_safe_end_label(ax, y, secondary_series, _get_color(styles["secondary"]))

    # Focus last
    if focus_series and focus_series in data:
        vals = data[focus_series]
        _plot_series(ax, vals["x"], vals["y"], styles["focus"], cfg, zorder=6)

        if cfg.get("auto_end_labels", True) and label_strategy in {"focus_only", "focus_and_secondary", "all"}:
            y = vals["y"][-1]
            _add_safe_end_label(ax, y, focus_series, _get_color(styles["focus"]))
    else:
        # fallback if focus series missing
        for series_name, vals in data.items():
            _plot_series(ax, vals["x"], vals["y"], styles["focus"], cfg, zorder=4)


def render_line_comparison(ax, data, cfg):
    styles = _get_story_styles(cfg)
    focus_series = cfg.get("focus_series")
    secondary_series = cfg.get("secondary_series")
    label_strategy = cfg.get("label_strategy", "all")

    for series_name, vals in data.items():
        if focus_series and series_name == focus_series:
            style = styles["focus"]
            z = 6
        elif secondary_series and series_name == secondary_series:
            style = styles["secondary"]
            z = 5
        else:
            style = styles["context"] if len(data) > 4 else styles["secondary"]
            z = 4

        _plot_series(ax, vals["x"], vals["y"], style, cfg, zorder=z)

        if not cfg.get("auto_end_labels", True):
            continue

        if label_strategy == "none":
            continue
        if label_strategy == "focus_only" and series_name != focus_series:
            continue
        if label_strategy == "focus_and_secondary" and series_name not in {focus_series, secondary_series}:
            continue

        _add_safe_end_label(ax, vals["y"][-1], series_name, _get_color(style))


def render_line(ax, data, cfg):
    story_angle = cfg.get("story_angle", "single_series_trend")

    if len(data) == 1 or story_angle == "single_series_trend":
        render_line_single_series(ax, data, cfg)
    elif story_angle == "focus_vs_context":
        render_line_focus_vs_context(ax, data, cfg)
    else:
        render_line_comparison(ax, data, cfg)


def render_bar(ax, data, cfg):
    series_name = next(iter(data))
    vals = data[series_name]
    color = _get_color(cfg, "#1F8FA8")
    positions = list(range(len(vals["x"])))

    ax.bar(positions, vals["y"], color=color, width=0.7, zorder=3)
    ax.set_xticks(positions)
    ax.set_xticklabels(vals["x"])

    if cfg.get("auto_end_labels", True):
        for pos, y in zip(positions, vals["y"]):
            ax.text(pos, y, _format_value(y, cfg.get("y_tick_format")), ha="center", va="bottom", fontsize=9)


def render_dot(ax, data, cfg):
    series_name = next(iter(data))
    vals = data[series_name]
    color = _get_color(cfg, "#1F8FA8")
    positions = list(range(len(vals["x"])))

    ax.scatter(vals["y"], positions, color=color, s=55, zorder=4)
    ax.set_yticks(positions)
    ax.set_yticklabels(vals["x"])
    ax.invert_yaxis()

    max_y = max(vals["y"]) if vals["y"] else 0
    ax.set_xlim(0, max_y * 1.08 if max_y else 1)

    if cfg.get("auto_end_labels", True):
        for pos, y in zip(positions, vals["y"]):
            ax.text(y, pos, _format_value(y, cfg.get("y_tick_format")), ha="left", va="center", fontsize=9)


def render_scatter(ax, data, cfg):
    styles = _get_story_styles(cfg)
    focus_series = cfg.get("focus_series")
    secondary_series = cfg.get("secondary_series")
    label_strategy = cfg.get("label_strategy", "focus_only")
    story_angle = cfg.get("story_angle", "comparison")

    for series_name, vals in data.items():
        if story_angle == "focus_vs_context":
            if series_name == focus_series:
                style = styles["focus"]
                z = 6
            elif secondary_series and series_name == secondary_series:
                style = styles["secondary"]
                z = 5
            else:
                style = styles["context"]
                z = 3
        else:
            if series_name == focus_series:
                style = styles["focus"]
                z = 6
            elif secondary_series and series_name == secondary_series:
                style = styles["secondary"]
                z = 5
            else:
                style = styles["secondary"] if len(data) <= 4 else styles["context"]
                z = 4

        ax.scatter(
            vals["x"],
            vals["y"],
            color=_get_color(style),
            s=55,
            alpha=style.get("alpha", 1.0),
            zorder=z,
        )

        if not cfg.get("auto_end_labels", True):
            continue
        if label_strategy == "none":
            continue
        if label_strategy == "focus_only" and series_name != focus_series:
            continue
        if label_strategy == "focus_and_secondary" and series_name not in {focus_series, secondary_series}:
            continue

        _add_safe_end_label(ax, vals["y"][-1], series_name, _get_color(style))


def main():
    print("RUNNING 538 RENDER V3")

    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    cfg = CHART_CONFIG

    if "data_file" not in cfg:
        raise ValueError("Missing 'data_file' in CHART_CONFIG")

    data_path = REPO_ROOT / cfg["data_file"]
    print(f"Reading CSV from: {data_path}")

    chart_type = cfg.get("chart_type", "line")
    data_format = cfg.get("data_format", "wide")

    if data_format == "long":
        if "x_col" not in cfg or "series_col" not in cfg or "value_col" not in cfg:
            raise ValueError("Long format requires 'x_col', 'series_col', and 'value_col'")
        data = load_long_data(data_path, cfg["x_col"], cfg["series_col"], cfg["value_col"])
    else:
        if "x_col" not in cfg or "y_col" not in cfg:
            raise ValueError("Wide format requires 'x_col' and 'y_col'")
        data = load_wide_data(data_path, cfg["x_col"], cfg["y_col"])

    if chart_type in {"bar", "dot"} and cfg.get("sort_descending", False):
        data = sort_single_series_for_rank_chart(data, descending=True)

    fig, ax = plt.subplots(figsize=(12, 8.5))

    if chart_type == "line":
        render_line(ax, data, cfg)
    elif chart_type == "bar":
        render_bar(ax, data, cfg)
    elif chart_type == "dot":
        render_dot(ax, data, cfg)
    elif chart_type == "scatter":
        render_scatter(ax, data, cfg)
    else:
        raise ValueError("chart_type must be one of: line, bar, dot, scatter")

    apply_axis_controls(ax, cfg)
    apply_reference_lines(ax, cfg)
    apply_highlights(ax, cfg)
    apply_annotations(ax, cfg)

    apply_538_template(
        ax,
        fig,
        title=cfg.get("title", ""),
        subtitle=cfg.get("subtitle", ""),
        source_text=cfg.get("source_text", ""),
        footer_left=cfg.get("footer_left", ""),
        vertical_gridlines=True,
    )

    base = Path(cfg["data_file"]).stem
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    fig.savefig(REPO_ROOT / f"output/{base}.png", dpi=300)
    fig.savefig(REPO_ROOT / f"output/{base}_{ts}.png", dpi=300)

    plt.close(fig)
    print(f"Saved output/{base}.png")
    print(f"Saved output/{base}_{ts}.png")


if __name__ == "__main__":
    main()