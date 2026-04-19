import csv
from pathlib import Path


def _coerce_value(value):
    try:
        num = float(value)
        if num.is_integer():
            return int(num)
        return num
    except ValueError:
        return value


def load_rows(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def detect_numeric_columns(rows):
    if not rows:
        return []

    cols = rows[0].keys()
    numeric_cols = []

    for col in cols:
        ok = True
        for row in rows:
            val = row[col]
            try:
                float(val)
            except ValueError:
                ok = False
                break
        if ok:
            numeric_cols.append(col)

    return numeric_cols


def choose_columns(rows):
    cols = list(rows[0].keys())
    numeric_cols = detect_numeric_columns(rows)

    for candidate in ["year", "date", "month", "x"]:
        if candidate in cols:
            x_col = candidate
            break
    else:
        x_col = cols[0]

    for candidate in ["value", "y", "inflation", "temperature", "rate"]:
        if candidate in numeric_cols:
            y_col = candidate
            break
    else:
        remaining = [c for c in numeric_cols if c != x_col]
        y_col = remaining[0] if remaining else None

    series_col = "series" if "series" in cols else None
    return x_col, y_col, series_col


def analyse_wide(rows, x_col, y_col):
    x_vals = [_coerce_value(r[x_col]) for r in rows]
    y_vals = [float(r[y_col]) for r in rows]

    min_y = min(y_vals)
    max_y = max(y_vals)
    latest_x = x_vals[-1]
    latest_y = y_vals[-1]
    peak_idx = y_vals.index(max_y)
    trough_idx = y_vals.index(min_y)

    start_y = y_vals[0]
    end_y = y_vals[-1]
    delta = end_y - start_y

    if abs(delta) < 0.01:
        story = "flat"
    elif delta > 0:
        story = "rising"
    else:
        story = "falling"

    return {
        "x_vals": x_vals,
        "y_vals": y_vals,
        "latest_x": latest_x,
        "latest_y": latest_y,
        "peak_x": x_vals[peak_idx],
        "peak_y": y_vals[peak_idx],
        "trough_x": x_vals[trough_idx],
        "trough_y": y_vals[trough_idx],
        "mean_y": sum(y_vals) / len(y_vals),
        "story": story,
    }


def build_title_subtitle(y_col, stats):
    metric = y_col.replace("_", " ").title()

    if stats["story"] == "rising":
        title = f"{metric} has risen over time"
        subtitle = (
            f"The latest value is above the starting point, with a peak at "
            f"{stats['peak_y']:.1f}."
        )
    elif stats["story"] == "falling":
        title = f"{metric} has fallen over time"
        subtitle = (
            f"The latest value is below the starting point, with the low point at "
            f"{stats['trough_y']:.1f}."
        )
    else:
        title = f"{metric} has stayed broadly flat"
        subtitle = (
            f"Values moved within a relatively narrow range, ending at "
            f"{stats['latest_y']:.1f}."
        )

    return title, subtitle


def suggest_chart_type(rows, x_col, y_col, series_col):
    if series_col:
        return "line"

    x_sample = _coerce_value(rows[0][x_col])

    if isinstance(x_sample, (int, float)):
        return "line"

    return "bar"


def generate_chart_config(data_file, source_text="Source: data"):
    csv_path = Path(data_file)
    rows = load_rows(csv_path)

    if not rows:
        raise ValueError("CSV file is empty.")

    x_col, y_col, series_col = choose_columns(rows)

    if y_col is None:
        raise ValueError("Could not identify a numeric y column.")

    chart_type = suggest_chart_type(rows, x_col, y_col, series_col)

    base_config = {
        "data_file": str(data_file),
        "chart_type": chart_type,
        "title": "Generated chart",
        "subtitle": "Auto-generated first-pass config.",
        "source_text": source_text,
        "footer_left": "Adam Green | coffeetableviz",
        "vertical_gridlines": False,
        "x_col": x_col,
        "y_col": y_col,
        "series_col": "series",
        "value_col": "value",
        "xlim_right_pad": 0.8,
        "sort_descending": True,
        "series_style": {
            "default_color": "#1F8FA8",
            "default_linewidth": 3,
            "default_bar_width": 0.7,
            "default_marker_size": 55,
            "palette": ["#1F8FA8", "#C44E52", "#7A7A7A", "#999999"],
        },
        "series_overrides": {},
        "reference_lines": [],
        "highlight_points": [],
        "auto_end_labels": True,
        "end_labels": [],
    }

    if series_col:
        base_config["data_format"] = "long"
        base_config["series_col"] = series_col
        base_config["value_col"] = y_col
        base_config["title"] = "Multi-series comparison over time"
        base_config["subtitle"] = "Detected long-format data with a series column."
        return base_config

    stats = analyse_wide(rows, x_col, y_col)
    title, subtitle = build_title_subtitle(y_col, stats)

    base_config["data_format"] = "wide"
    base_config["title"] = title
    base_config["subtitle"] = subtitle

    if chart_type == "line":
        base_config["reference_lines"] = [
            {
                "y": round(stats["mean_y"], 1),
                "label": f"Average: {stats['mean_y']:.1f}",
                "color": "#999999",
                "linestyle": "--",
                "linewidth": 1.5,
                "label_x": "left",
                "label_offset": 0.15,
            }
        ]
        base_config["highlight_points"] = [
            {
                "x": stats["peak_x"],
                "y": stats["peak_y"],
                "label": f"Peak: {stats['peak_y']:.1f}",
                "color": "#C44E52",
                "dx": 0.15,
                "dy": 0.15,
                "ha": "left",
                "size": 45,
            }
        ]

    return base_config