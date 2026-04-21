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
            if "{" in fmt:
                return fmt.format(val)
            return format(val, fmt)
        except Exception:
            pass

    if isinstance(val, float):
        return f"{val:.1f}".rstrip("0").rstrip(".")
    return str(val)


def _axis_formatter_from_fmt(fmt):
    if not fmt:
        return None

    def _formatter(val, pos):
        try:
            if "{" in fmt:
                return fmt.format(val)
            return format(val, fmt)
        except Exception:
            return _format_value(val)

    return FuncFormatter(_formatter)


def _safe_text_x_right(ax, frac=0.955):
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


def _as_list(value):
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return list(value)
    return [value]


def _normalise_cfg(cfg):
    out = dict(cfg)
    out["_focus_list"] = _as_list(cfg.get("focus_series"))
    out["_secondary_list"] = _as_list(cfg.get("secondary_series"))
    out["_highlighted_series"] = set(out["_focus_list"] + out["_secondary_list"])
    return out


def _series_is_focus(series_name, cfg):
    return series_name in cfg.get("_focus_list", [])


def _series_is_secondary(series_name, cfg):
    return series_name in cfg.get("_secondary_list", [])


def _should_label_series(series_name, cfg):
    label_strategy = cfg.get("label_strategy", "all")
    if label_strategy == "none":
        return False
    if label_strategy == "all":
        return True
    if label_strategy == "focus_only":
        return _series_is_focus(series_name, cfg)
    if label_strategy == "focus_and_secondary":
        return series_name in cfg.get("_highlighted_series", set())
    return True


def _build_end_label(series_name, y_value, cfg, include_series_name=True):
    value_text = _format_value(y_value, cfg.get("y_tick_format"))
    if include_series_name and series_name:
        return f"{series_name} {value_text}"
    return value_text


def _add_safe_end_label(ax, y, label, color="#1F8FA8"):
    x_pos = _safe_text_x_right(ax, 0.955)
    y_min, y_max = ax.get_ylim()
    y_span = y_max - y_min
    y_pos = _safe_text_y(ax, y + y_span * 0.01, 0.03)
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
        near_right = x > x_min + x_span * 0.82
        text_x = x - x_span * 0.025 if near_right else x + x_span * 0.02
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


def _approx_equal(a, b, tolerance=0.5):
    try:
        return abs(float(a) - float(b)) <= tolerance
    except Exception:
        return a == b


def _sort_series_by_x(data):
    sorted_data = {}
    for series_name, vals in data.items():
        pairs = list(zip(vals["x"], vals["y"]))
        pairs.sort(key=lambda t: t[0])
        sorted_data[series_name] = {"x": [p[0] for p in pairs], "y": [p[1] for p in pairs]}
    return sorted_data


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
    return _sort_series_by_x(dict(grouped))


def sort_single_series_for_rank_chart(series_data, descending=True):
    if len(series_data) != 1:
        return series_data
    series_name = next(iter(series_data))
    values = series_data[series_name]
    pairs = list(zip(values["x"], values["y"]))
    pairs.sort(key=lambda t: t[1], reverse=descending)
    return {series_name: {"x": [p[0] for p in pairs], "y": [p[1] for p in pairs]}}


def validate_config_points(data, cfg, tolerance=0.75):
    warnings = []
    for block_name in ("highlight_points", "annotate_points"):
        for item in cfg.get(block_name, []) or []:
            series = item.get("series")
            x = item.get("x")
            y = item.get("y")
            candidate_series = (
                [series]
                if series is not None and series in data
                else list(data.keys()) if series is None
                else []
            )
            if series is not None and series not in data:
                warnings.append(f"{block_name}: series {series!r} not found in loaded data.")
                continue
            matched_x = False
            matched_xy = False
            for series_name in candidate_series:
                vals = data[series_name]
                for xv, yv in zip(vals["x"], vals["y"]):
                    if xv == x:
                        matched_x = True
                        if y is None or _approx_equal(yv, y, tolerance=tolerance):
                            matched_xy = True
                            break
                if matched_xy:
                    break
            if not matched_x:
                warnings.append(
                    f"{block_name}: no matching x={x!r} found"
                    + (f" for series={series!r}" if series is not None else "")
                    + "."
                )
            elif y is not None and not matched_xy:
                warnings.append(
                    f"{block_name}: x={x!r} found"
                    + (f" for series={series!r}" if series is not None else "")
                    + f", but y={y!r} does not match the data."
                )
    return warnings


def validate_chart_config(cfg, data):
    chart_type = cfg.get("chart_type")
    data_format = cfg.get("data_format")
    errors = []

    if chart_type not in {"line", "bar", "dot", "scatter"}:
        errors.append(f"Invalid chart_type: {chart_type}")
    if data_format not in {"long", "wide"}:
        errors.append(f"Invalid data_format: {data_format}")

    for required_key in (
        "y_axis_min",
        "y_axis_max",
        "y_tick_interval",
        "y_tick_format",
        "auto_end_labels",
        "sort_descending",
    ):
        if required_key not in cfg:
            errors.append(f"Missing required config key: '{required_key}'")

    if chart_type == "line":
        if data_format != "long":
            errors.append("Line charts require data_format='long'")
        if not cfg.get("series_col"):
            errors.append("Line charts require 'series_col'")
        if not cfg.get("value_col"):
            errors.append("Line charts require 'value_col'")

    if chart_type == "bar":
        if data_format != "wide":
            errors.append("Bar charts require data_format='wide'")
        if cfg.get("series_col") is not None:
            errors.append("Bar charts must not use 'series_col'")
        if cfg.get("value_col") is not None:
            errors.append("Bar charts must not use 'value_col'")

    if chart_type == "dot":
        if data_format != "wide":
            errors.append("Dot charts require data_format='wide'")
        if cfg.get("sort_descending") is not True:
            errors.append(
                f"Dot charts require sort_descending=True (got {cfg.get('sort_descending')})"
            )
        if cfg.get("series_col") is not None:
            errors.append("Dot charts must not use 'series_col'")
        if cfg.get("value_col") is not None:
            errors.append("Dot charts must not use 'value_col'")
        if cfg.get("story_angle") == "category_comparison":
            errors.append(
                "Dot charts are for ranked comparisons; use bar for natural-order category comparison"
            )

    if chart_type == "scatter":
        for vals in data.values():
            if not all(isinstance(x, (int, float)) for x in vals["x"]):
                errors.append("Scatter charts require numeric x values")
                break
        for vals in data.values():
            if not all(isinstance(y, (int, float)) for y in vals["y"]):
                errors.append("Scatter charts require numeric y values")
                break
        if cfg.get("auto_end_labels") is not False:
            errors.append("Scatter charts should set auto_end_labels=False")

    # For dot charts the numeric value axis is x, not y
    if chart_type == "dot":
        value_axis_max = cfg.get("y_axis_max")
        if value_axis_max is not None:
            all_vals = []
            for vals in data.values():
                all_vals.extend(vals["y"])
            if all_vals and max(all_vals) > value_axis_max:
                errors.append(f"y_axis_max={value_axis_max} is below data max {max(all_vals)}")
    else:
        y_axis_max = cfg.get("y_axis_max")
        if y_axis_max is not None:
            all_y = []
            for vals in data.values():
                all_y.extend(vals["y"])
            if all_y and max(all_y) > y_axis_max:
                errors.append(f"y_axis_max={y_axis_max} is below data max {max(all_y)}")

    if errors:
        raise ValueError("CHART CONFIG VALIDATION FAILED:\n- " + "\n- ".join(errors))


def apply_axis_controls(ax, cfg):
    chart_type = cfg.get("chart_type")

    if chart_type in {"line", "bar", "scatter"}:
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
        formatter = _axis_formatter_from_fmt(y_tick_format)
        if formatter:
            ax.yaxis.set_major_formatter(formatter)

    elif chart_type == "dot":
        # Dot charts use numeric x-axis and categorical y-axis.
        # We keep the standard config field names, but apply them to the x-axis.
        x_min = cfg.get("y_axis_min")
        x_max = cfg.get("y_axis_max")
        if x_min is not None or x_max is not None:
            current_min, current_max = ax.get_xlim()
            ax.set_xlim(
                left=x_min if x_min is not None else current_min,
                right=x_max if x_max is not None else current_max,
            )

        x_tick_interval = cfg.get("y_tick_interval")
        if x_tick_interval is not None:
            ax.xaxis.set_major_locator(MultipleLocator(x_tick_interval))

        x_tick_format = cfg.get("y_tick_format")
        formatter = _axis_formatter_from_fmt(x_tick_format)
        if formatter:
            ax.xaxis.set_major_formatter(formatter)

    x_tick_rotation = cfg.get("x_tick_rotation", 0)
    if x_tick_rotation:
        plt.setp(ax.get_xticklabels(), rotation=x_tick_rotation, ha="right")

    if cfg.get("x_axis_label"):
        ax.set_xlabel(cfg["x_axis_label"])
    if cfg.get("y_axis_label"):
        ax.set_ylabel(cfg["y_axis_label"])


def apply_reference_lines(ax, cfg):
    for ref in cfg.get("reference_lines", []):
        try:
            axis = ref.get("axis", "y")
            value = ref.get("value")
            if value is None:
                value = ref.get(axis)
            if value is None:
                value = ref.get("y") if axis == "y" else ref.get("x")
            if value is None:
                continue

            line_color = _get_color(ref, "#999999")

            if axis == "x":
                ax.axvline(
                    x=value,
                    color=line_color,
                    linestyle=ref.get("linestyle", "--"),
                    linewidth=ref.get("linewidth", 1.0),
                    alpha=ref.get("alpha", 1.0),
                    zorder=1,
                )
            else:
                ax.axhline(
                    y=value,
                    color=line_color,
                    linestyle=ref.get("linestyle", "--"),
                    linewidth=ref.get("linewidth", 1.0),
                    alpha=ref.get("alpha", 1.0),
                    zorder=1,
                )

            label = ref.get("label")
            if label:
                if axis == "x":
                    y_min, y_max = ax.get_ylim()
                    y_pos = y_max - (y_max - y_min) * 0.04
                    ax.text(
                        value,
                        y_pos,
                        label,
                        fontsize=9,
                        color=line_color,
                        ha="center",
                        va="top",
                        clip_on=True,
                        zorder=5,
                    )
                else:
                    label_x = ref.get("label_x", "left")
                    label_offset = ref.get("label_offset", 0.0)
                    x_pos = (
                        _safe_text_x_right(ax, 0.955)
                        if label_x == "right"
                        else _safe_text_x_left(ax, 0.015)
                    )
                    y_pos = _safe_text_y(ax, value + label_offset, 0.03)
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
            ax.scatter(x, y, color=pt_color, s=55, zorder=7)
            if pt.get("label"):
                _add_safe_highlight_label(ax, x, y, pt["label"], pt_color)
        except Exception:
            continue


def apply_annotations(ax, cfg):
    for ann in cfg.get("annotate_points", []):
        try:
            x = ann["x"]
            y = ann["y"]
            text = ann["text"]
            x_min, x_max = ax.get_xlim()
            x_span = x_max - x_min
            if isinstance(x, (int, float)) and x > x_min + x_span * 0.82:
                base_xytext = ann.get("xytext", (-55, -10))
                if not isinstance(base_xytext, tuple):
                    base_xytext = (-55, -10)
                xytext = (-55, base_xytext[1])
                ha = "right"
            else:
                xytext = ann.get("xytext", (0, 0))
                if not isinstance(xytext, tuple):
                    xytext = (0, 0)
                ha = ann.get("ha", "left")
            ax.annotate(
                text,
                (x, y),
                xytext=xytext,
                textcoords="offset points",
                ha=ha,
                fontsize=9,
                zorder=9,
                clip_on=True,
            )
        except Exception:
            continue


def _get_story_styles(cfg):
    return {
        "context": cfg.get("context_style", {"color": "#D9D9D9", "linewidth": 0.7, "alpha": 0.25}),
        "focus": cfg.get("focus_style", {"color": "#1F8FA8", "linewidth": 3.4, "alpha": 1.0}),
        "secondary": cfg.get("secondary_style", {"color": "#7A7A7A", "linewidth": 2.0, "alpha": 0.90}),
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


def _get_single_series_name(data, cfg):
    if len(data) == 1:
        return next(iter(data))
    focus_list = cfg.get("_focus_list", [])
    if focus_list and focus_list[0] in data:
        return focus_list[0]
    return next(iter(data))


def render_line_single_series(ax, data, cfg):
    styles = _get_story_styles(cfg)
    series_name = _get_single_series_name(data, cfg)
    vals = data[series_name]
    _plot_series(ax, vals["x"], vals["y"], styles["focus"], cfg, zorder=4)
    if cfg.get("auto_end_labels", True):
        label = _build_end_label(series_name, vals["y"][-1], cfg, include_series_name=False)
        _add_safe_end_label(ax, vals["y"][-1], label, _get_color(styles["focus"]))


def render_line_focus_vs_context(ax, data, cfg):
    styles = _get_story_styles(cfg)
    label_strategy = cfg.get("label_strategy", "focus_only")

    for series_name, vals in data.items():
        if _series_is_focus(series_name, cfg) or _series_is_secondary(series_name, cfg):
            continue
        _plot_series(ax, vals["x"], vals["y"], styles["context"], cfg, zorder=2)

    for series_name in cfg.get("_secondary_list", []):
        if series_name not in data:
            continue
        vals = data[series_name]
        _plot_series(ax, vals["x"], vals["y"], styles["secondary"], cfg, zorder=4)
        if cfg.get("auto_end_labels", True) and label_strategy in {"focus_and_secondary", "all"}:
            label = _build_end_label(series_name, vals["y"][-1], cfg, include_series_name=True)
            _add_safe_end_label(ax, vals["y"][-1], label, _get_color(styles["secondary"]))

    focus_plotted = False
    for series_name in cfg.get("_focus_list", []):
        if series_name not in data:
            continue
        vals = data[series_name]
        _plot_series(ax, vals["x"], vals["y"], styles["focus"], cfg, zorder=6)
        focus_plotted = True
        if cfg.get("auto_end_labels", True) and label_strategy in {"focus_only", "focus_and_secondary", "all"}:
            label = _build_end_label(series_name, vals["y"][-1], cfg, include_series_name=True)
            _add_safe_end_label(ax, vals["y"][-1], label, _get_color(styles["focus"]))

    if not focus_plotted:
        for _, vals in data.items():
            _plot_series(ax, vals["x"], vals["y"], styles["focus"], cfg, zorder=4)


def render_line_comparison(ax, data, cfg):
    styles = _get_story_styles(cfg)
    for series_name, vals in data.items():
        if _series_is_focus(series_name, cfg):
            style = styles["focus"]
            z = 6
        elif _series_is_secondary(series_name, cfg):
            style = styles["secondary"]
            z = 5
        else:
            style = styles["context"] if len(data) > 4 else styles["secondary"]
            z = 4

        _plot_series(ax, vals["x"], vals["y"], style, cfg, zorder=z)

        if cfg.get("auto_end_labels", True) and _should_label_series(series_name, cfg):
            label = _build_end_label(series_name, vals["y"][-1], cfg, include_series_name=True)
            _add_safe_end_label(ax, vals["y"][-1], label, _get_color(style))


def render_line(ax, data, cfg):
    story_angle = cfg.get("story_angle", "single_series_trend")
    if len(data) == 1 or story_angle == "single_series_trend":
        render_line_single_series(ax, data, cfg)
    elif story_angle == "focus_vs_context":
        render_line_focus_vs_context(ax, data, cfg)
    else:
        render_line_comparison(ax, data, cfg)


def render_bar(ax, data, cfg):
    series_name = _get_single_series_name(data, cfg)
    vals = data[series_name]
    color = _get_color(cfg, "#1F8FA8")
    positions = list(range(len(vals["x"])))

    ax.bar(positions, vals["y"], color=color, width=0.7, zorder=3)
    ax.set_xticks(positions)
    ax.set_xticklabels(vals["x"])

    if cfg.get("auto_end_labels", True):
        for pos, y in zip(positions, vals["y"]):
            ax.text(
                pos,
                y,
                _format_value(y, cfg.get("y_tick_format")),
                ha="center",
                va="bottom",
                fontsize=9,
            )


def render_dot(ax, data, cfg):
    series_name = _get_single_series_name(data, cfg)
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
        label_offset = max(max_y * 0.012, 2)
        for pos, y in zip(positions, vals["y"]):
            ax.text(
                y + label_offset,
                pos,
                _format_value(y, cfg.get("y_tick_format")),
                ha="left",
                va="center",
                fontsize=9,
            )


def render_scatter(ax, data, cfg):
    styles = _get_story_styles(cfg)
    story_angle = cfg.get("story_angle", "comparison")

    for series_name, vals in data.items():
        if story_angle == "focus_vs_context":
            if _series_is_focus(series_name, cfg):
                style = styles["focus"]
                z = 6
            elif _series_is_secondary(series_name, cfg):
                style = styles["secondary"]
                z = 5
            else:
                style = styles["context"]
                z = 3
        else:
            if _series_is_focus(series_name, cfg):
                style = styles["focus"]
                z = 6
            elif _series_is_secondary(series_name, cfg):
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


def main():
    print("RUNNING 538 RENDER V7")
    os.makedirs(REPO_ROOT / "output", exist_ok=True)
    cfg = _normalise_cfg(CHART_CONFIG)

    if "data_file" not in cfg:
        raise ValueError("Missing 'data_file' in CHART_CONFIG")

    data_path = REPO_ROOT / cfg["data_file"]
    print(f"Reading CSV from: {data_path}")

    chart_type = cfg.get("chart_type", "line")
    data_format = cfg.get("data_format", "wide")

    if data_format == "long":
        if not cfg.get("x_col") or not cfg.get("series_col") or not cfg.get("value_col"):
            raise ValueError("Long format requires valid 'x_col', 'series_col', and 'value_col'")
        data = load_long_data(data_path, cfg["x_col"], cfg["series_col"], cfg["value_col"])
    else:
        if not cfg.get("x_col") or not cfg.get("y_col"):
            raise ValueError("Wide format requires valid 'x_col' and 'y_col'")
        data = load_wide_data(data_path, cfg["x_col"], cfg["y_col"])

    validate_chart_config(cfg, data)

    point_warnings = validate_config_points(data, cfg, tolerance=0.75)
    if point_warnings:
        raise ValueError("Config point validation failed:\n- " + "\n- ".join(point_warnings))

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