import csv
import os
import sys
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
            return fmt.format(val)
        except Exception:
            pass

    if isinstance(val, float):
        return f"{val:.1f}".rstrip("0").rstrip(".")
    return str(val)


def _get_reference_line_value(ref):
    if "y" in ref:
        return ref.get("y")
    return ref.get("value")


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
        zorder=6,
    )


def _add_safe_highlight_label(ax, x, y, label, color="#C44E52"):
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    x_span = x_max - x_min
    y_span = y_max - y_min

    # Prefer up-right, but flip if too close to edge
    if isinstance(x, (int, float)):
        near_right = x > x_min + x_span * 0.84
        x_offset = -x_span * 0.02 if near_right else x_span * 0.02
        ha = "right" if near_right else "left"
        text_x = x + x_offset
    else:
        text_x = x
        ha = "left"

    text_y = y + y_span * 0.02
    text_y = _safe_text_y(ax, text_y, 0.04)

    ax.text(
        text_x,
        text_y,
        label,
        fontsize=9,
        color=color,
        ha=ha,
        va="bottom",
        clip_on=True,
        zorder=7,
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


def render_line(ax, data, cfg):
    color = _get_color(cfg)
    lw = cfg.get("line_width", 2.6)
    show_markers = cfg.get("show_markers", False)
    marker_size = cfg.get("marker_size", 18)

    for _, vals in data.items():
        ax.plot(
            vals["x"],
            vals["y"],
            color=color,
            linewidth=lw,
            marker="o" if show_markers else None,
            markersize=marker_size if show_markers else None,
            zorder=3,
        )

        if cfg.get("auto_end_labels", True):
            y = vals["y"][-1]
            _add_safe_end_label(
                ax,
                y=y,
                label=_format_value(y, cfg.get("y_tick_format")),
                color=color,
            )


def apply_reference_lines(ax, cfg):
    for ref in cfg.get("reference_lines", []):
        try:
            y = _get_reference_line_value(ref)
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
                zorder=6,
            )

            if pt.get("label"):
                _add_safe_highlight_label(
                    ax,
                    x=x,
                    y=y,
                    label=pt["label"],
                    color=pt_color,
                )
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
            )
        except Exception:
            continue


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


def main():
    print("RUNNING 538 RENDER V2.5")

    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    cfg = CHART_CONFIG

    if "data_file" not in cfg:
        raise ValueError("Missing 'data_file' in CHART_CONFIG")

    data_path = REPO_ROOT / cfg["data_file"]
    print(f"Reading CSV from: {data_path}")

    if "x_col" not in cfg or "y_col" not in cfg:
        raise ValueError("CHART_CONFIG must include 'x_col' and 'y_col'")

    data = load_wide_data(data_path, cfg["x_col"], cfg["y_col"])

    fig, ax = plt.subplots(figsize=(12, 8.5))

    render_line(ax, data, cfg)
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