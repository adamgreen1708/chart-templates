import csv
import os
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

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


def _add_safe_end_label(ax, y, label, color="#1F8FA8"):
    """
    Place the end label just inside the right plot boundary so it never
    overruns the chart margin.
    """
    x_min, x_max = ax.get_xlim()
    x_pos = x_max - (x_max - x_min) * 0.01  # 1% inset from right edge

    ax.text(
        x_pos,
        y,
        label,
        fontsize=10,
        color=color,
        ha="right",
        va="center",
        clip_on=True,
        zorder=6,
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

    for _, vals in data.items():
        ax.plot(vals["x"], vals["y"], color=color, linewidth=lw)

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
            y = ref.get("y") if "y" in ref else ref.get("value")
            if y is None:
                continue

            line_color = _get_color(ref, "#999999")

            ax.axhline(
                y=y,
                color=line_color,
                linestyle=ref.get("linestyle", "--"),
                linewidth=ref.get("linewidth", 1.2),
            )

            if ref.get("label"):
                x_min, x_max = ax.get_xlim()
                x_pos = x_min + (x_max - x_min) * 0.002

                ax.text(
                    x_pos,
                    y,
                    ref["label"],
                    fontsize=9,
                    color=line_color,
                    va="bottom",
                    ha="left",
                    clip_on=True,
                )
        except Exception:
            continue


def apply_highlights(ax, cfg):
    for pt in cfg.get("highlight_points", []):
        try:
            pt_color = _get_color(pt, "#C44E52")

            ax.scatter(
                pt["x"],
                pt["y"],
                color=pt_color,
                s=40,
                zorder=5,
            )

            if pt.get("label"):
                ax.text(
                    pt["x"],
                    pt["y"],
                    pt["label"],
                    fontsize=9,
                    color=pt_color,
                    ha="left",
                    va="bottom",
                    clip_on=True,
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


def main():
    print("RUNNING 538 RENDER V2")

    os.makedirs(REPO_ROOT / "output", exist_ok=True)

    cfg = CHART_CONFIG

    if "data_file" not in cfg:
        raise ValueError("Missing 'data_file' in CHART_CONFIG")

    data_path = REPO_ROOT / cfg["data_file"]
    print(f"Reading CSV from: {data_path}")

    data = load_wide_data(data_path, cfg["x_col"], cfg["y_col"])

    fig, ax = plt.subplots(figsize=(12, 8.5))

    render_line(ax, data, cfg)

    if cfg.get("y_axis_min") is not None or cfg.get("y_axis_max") is not None:
        current_min, current_max = ax.get_ylim()
        ax.set_ylim(
            bottom=cfg.get("y_axis_min", current_min),
            top=cfg.get("y_axis_max", current_max),
        )

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
        vertical_gridlines=cfg.get("show_grid_x", False),
    )

    base = Path(cfg["data_file"]).stem
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    fig.savefig(REPO_ROOT / f"output/{base}.png", dpi=300)
    fig.savefig(REPO_ROOT / f"output/{base}_{ts}.png", dpi=300)

    plt.close(fig)


if __name__ == "__main__":
    main()