from pathlib import Path
import textwrap

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon, Rectangle


BG = "#F3F4F6"
PRIMARY = "#1F8FA8"
ACCENT = "#C44E52"
CONTEXT = "#D9D9D9"
SECONDARY = "#7A7A7A"
TEXT = "#111111"
SUBTEXT = "#555555"
WHITE = "#FFFFFF"


EDITORIAL_TYPES = {"route_zigzag", "route_longitude", "mode_clusters"}


def _wrap(text, width, max_lines=2):
    lines = textwrap.wrap(str(text), width=width)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(" .,;:") + "…"
    return "\n".join(lines)


def _add_header(fig, title, subtitle, explainer=None):
    title_text = _wrap(title, 36, 2)
    title_lines = title_text.count("\n") + 1
    fig.text(
        0.06, 0.95, title_text,
        ha="left", va="top",
        fontsize=25, fontweight="bold", color=TEXT, linespacing=1.02,
    )
    subtitle_y = 0.865 if title_lines == 1 else 0.805
    fig.text(
        0.06, subtitle_y, _wrap(subtitle, 72, 2),
        ha="left", va="top",
        fontsize=14, color=SUBTEXT, linespacing=1.20,
    )
    if explainer:
        fig.text(
            0.06, subtitle_y - 0.088, _wrap(explainer, 72, 2),
            ha="left", va="top",
            fontsize=12.5, color=SUBTEXT, linespacing=1.18,
        )
        return subtitle_y - 0.16
    return subtitle_y - 0.10


def _add_footer(fig, left, right):
    fig.text(0.06, 0.045, left, ha="left", va="bottom", fontsize=9.5, color=SUBTEXT)
    fig.text(0.94, 0.045, right, ha="right", va="bottom", fontsize=9.5, color=SUBTEXT)


def _save(fig, repo_root, config):
    output_file = config.get("output_file", "output/chart.png")
    if "/" not in output_file:
        output_file = f"output/{output_file}"
    output_path = Path(repo_root) / output_file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_path,
        dpi=config.get("dpi", 200),
        facecolor=fig.get_facecolor(),
    )
    plt.close(fig)
    print(f"Saved chart to {output_path}")
    return output_path


def render_route_zigzag(repo_root, config, rows):
    rows = sorted(rows, key=lambda r: int(r["sequence"]))
    if len(rows) != 10:
        raise ValueError("route_zigzag expects exactly 10 country rows.")

    fig = plt.figure(figsize=(8, 8), facecolor=BG)
    plot_top = _add_header(
        fig,
        config["title"],
        config["subtitle"],
        config.get("explainer"),
    )

    ax = fig.add_axes([0.04, 0.18, 0.92, max(0.46, plot_top - 0.18)])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    xs = np.linspace(0.06, 0.94, 10)
    ys = np.array([0.66 if i % 2 == 0 else 0.38 for i in range(10)])

    ax.hlines(
        0.52, 0.00, 1.00,
        color="#989898", linewidth=1.3, linestyles=(0, (4, 4)), zorder=1,
    )
    ax.plot(xs, ys, color=PRIMARY, linewidth=3.0, zorder=2)

    for i, (row, x, y) in enumerate(zip(rows, xs, ys), start=1):
        endpoint = i in (1, 10)
        node_color = ACCENT if endpoint else PRIMARY
        ax.scatter(
            [x], [y], s=1700,
            color=node_color, edgecolor=BG, linewidth=2.0, zorder=4,
        )
        ax.text(
            x, y, str(i),
            ha="center", va="center",
            fontsize=16.5, fontweight="bold", color=WHITE, zorder=5,
        )
        above = y > 0.52
        ax.text(
            x, y + (0.145 if above else -0.145),
            row["country"],
            ha="center", va="center",
            fontsize=13.5, color=TEXT,
            fontweight="bold" if endpoint else "normal",
        )

    bracket_y = 0.10
    continent_groups = [
        ("Africa", xs[0] - 0.035, xs[4] + 0.035),
        ("Australia", xs[5] - 0.035, xs[5] + 0.035),
        ("South America", xs[6] - 0.035, xs[9] + 0.035),
    ]
    for label, left, right in continent_groups:
        ax.plot([left, right], [bracket_y, bracket_y], color="#9A9A9A", linewidth=1.8)
        ax.plot([left, left], [bracket_y - 0.018, bracket_y + 0.018], color="#9A9A9A", linewidth=1.3)
        ax.plot([right, right], [bracket_y - 0.018, bracket_y + 0.018], color="#9A9A9A", linewidth=1.3)
        ax.text(
            (left + right) / 2, bracket_y - 0.06, label,
            ha="center", va="top", fontsize=13, color=SUBTEXT,
        )

    _add_footer(
        fig,
        config.get("footer_left", "Adam Green | coffeetableviz"),
        config.get("source_text", "Schematic: stops evenly spaced"),
    )
    return _save(fig, repo_root, config)


def _panel_x(longitude, panel):
    if panel == "Africa":
        lo, hi, x0, x1 = 15.0, 50.0, 0.055, 0.395
    elif panel == "Australia":
        lo, hi, x0, x1 = 116.0, 153.5, 0.445, 0.695
    elif panel == "South America":
        lo, hi, x0, x1 = -70.5, -44.0, 0.745, 0.955
    else:
        raise ValueError(f"Unsupported longitude panel: {panel}")
    frac = (float(longitude) - lo) / (hi - lo)
    return x0 + frac * (x1 - x0)


def render_route_longitude(repo_root, config, rows):
    rows = sorted(rows, key=lambda r: int(r["stop_order"]))
    fig = plt.figure(figsize=(8, 8), facecolor=BG)
    _add_header(
        fig,
        config["title"],
        config["subtitle"],
        config.get("explainer"),
    )

    ax = fig.add_axes([0.00, 0.10, 1.00, 0.68])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    tropic = float(config.get("tropic_latitude", -23.4366))
    exaggeration = float(config.get("vertical_exaggeration", 3.0))
    y_base = 0.49
    y_scale = 0.0105 * exaggeration

    panels = {
        "Africa": (0.055, 0.395),
        "Australia": (0.445, 0.695),
        "South America": (0.745, 0.955),
    }

    for panel, (x0, x1) in panels.items():
        ax.hlines(
            y_base, x0, x1,
            color="#999999", linewidth=1.2, linestyles=(0, (4, 4)), zorder=1,
        )
        ax.hlines(0.15, x0, x1, color="#999999", linewidth=1.2)
        ax.plot([x0, x0], [0.14, 0.16], color="#999999", linewidth=1.1)
        ax.plot([x1, x1], [0.14, 0.16], color="#999999", linewidth=1.1)
        ax.text(
            (x0 + x1) / 2, 0.075, panel,
            ha="center", va="center",
            fontsize=13, color=SUBTEXT, fontweight="bold",
        )

    ax.text(0.420, 0.15, "//", ha="center", va="center", fontsize=18, color="#9A9A9A")
    ax.text(0.720, 0.15, "//", ha="center", va="center", fontsize=18, color="#9A9A9A")

    tick_defs = {
        "Africa": [(20, "20°E"), (40, "40°E")],
        "Australia": [(120, "120°E"), (140, "140°E")],
        "South America": [(-70, "70°W"), (-50, "50°W")],
    }
    for panel, ticks in tick_defs.items():
        for value, label in ticks:
            x = _panel_x(value, panel)
            ax.plot([x, x], [0.15, 0.13], color="#999999", linewidth=1.0)
            ax.text(x, 0.105, label, ha="center", va="top", fontsize=11, color=SUBTEXT)

    grouped = {"Africa": [], "Australia": [], "South America": []}
    for row in rows:
        grouped[row["continent"]].append(row)

    point_xy = {}
    label_exclusions = set(config.get("label_exclusions", []))
    for panel, values in grouped.items():
        xs = [_panel_x(r["longitude"], panel) for r in values]
        ys = [y_base + (float(r["latitude"]) - tropic) * y_scale for r in values]
        ax.plot(xs, ys, color=PRIMARY, linewidth=2.4, zorder=3)
        ax.scatter(xs, ys, s=82, color=PRIMARY, edgecolor=BG, linewidth=0.9, zorder=4)

        for r, x, y in zip(values, xs, ys):
            point_xy[int(r["stop_order"])] = (x, y)

        label_values = [r for r in values if r["place"] not in label_exclusions]
        x0, x1 = panels[panel]
        if len(label_values) == 1:
            label_slots = [(x0 + x1) / 2]
        else:
            label_slots = np.linspace(x0 + 0.012, x1 - 0.012, len(label_values))

        value_lookup = {int(r["stop_order"]): (x, y) for r, x, y in zip(values, xs, ys)}
        for r, label_x in zip(label_values, label_slots):
            x, y = value_lookup[int(r["stop_order"])]
            label_y = 0.315
            ax.plot([x, label_x], [y - 0.01, label_y + 0.012], color="#A0A0A0", linewidth=0.7, zorder=2)
            ax.text(
                label_x, label_y, r["place"],
                ha="left", va="top", rotation=-90,
                fontsize=7.6, color=SUBTEXT,
            )

    country_rows = {}
    for row in rows:
        seq = int(row["country_sequence"])
        country_rows.setdefault(seq, row)

    panel_sequences = {
        "Africa": [1, 2, 3, 4, 5],
        "Australia": [6],
        "South America": [7, 8, 9, 10],
    }
    country_marker_x = {}
    for panel, sequences in panel_sequences.items():
        x0, x1 = panels[panel]
        if len(sequences) == 1:
            positions = [(x0 + x1) / 2]
        else:
            positions = np.linspace(x0 + 0.020, x1 - 0.020, len(sequences))
        for seq, marker_x in zip(sequences, positions):
            country_marker_x[seq] = marker_x

    for seq in range(1, 11):
        row = country_rows[seq]
        point_x = _panel_x(row["longitude"], row["continent"])
        point_y = y_base + (float(row["latitude"]) - tropic) * y_scale
        marker_x = country_marker_x[seq]
        marker_y = 0.82
        color = ACCENT if seq in (1, 10) else PRIMARY
        ax.plot(
            [marker_x, point_x], [marker_y - 0.045, point_y + 0.018],
            color="#A8A8A8", linewidth=0.75, zorder=1,
        )
        ax.scatter([marker_x], [marker_y], s=950, color=color, edgecolor=BG, linewidth=1.7, zorder=5)
        ax.text(
            marker_x, marker_y, str(seq),
            ha="center", va="center",
            fontsize=13.5, fontweight="bold", color=WHITE, zorder=6,
        )
        country_label_y = marker_y + (0.067 if seq % 2 else 0.102)
        ax.text(
            marker_x, country_label_y, _wrap(row["country"], 10, 2),
            ha="center", va="bottom",
            fontsize=8.1, color=TEXT, linespacing=0.95,
            fontweight="bold" if seq in (1, 10) else "normal",
        )

    _add_footer(
        fig,
        config.get("footer_left", "Adam Green | coffeetableviz"),
        config.get("source_text", "Positions approximate"),
    )
    return _save(fig, repo_root, config)


def _icon_circle(ax, x, y, radius=0.055):
    ax.add_patch(Circle((x, y), radius, facecolor=PRIMARY, edgecolor="none", zorder=5))


def _wheel(ax, x, y, r=0.009):
    ax.add_patch(Circle((x, y), r, facecolor=WHITE, edgecolor="none", zorder=7))


def _draw_icon(ax, mode, x, y):
    white = WHITE
    if mode == "van":
        ax.add_patch(Rectangle((x-0.038, y-0.016), 0.076, 0.036, facecolor=white, edgecolor="none", zorder=7))
        ax.add_patch(Rectangle((x-0.029, y+0.002), 0.018, 0.013, facecolor=PRIMARY, edgecolor="none", zorder=8))
        ax.add_patch(Rectangle((x-0.006, y+0.002), 0.018, 0.013, facecolor=PRIMARY, edgecolor="none", zorder=8))
        _wheel(ax, x-0.024, y-0.020)
        _wheel(ax, x+0.024, y-0.020)
    elif mode == "car":
        ax.add_patch(Rectangle((x-0.038, y-0.014), 0.076, 0.025, facecolor=white, edgecolor="none", zorder=7))
        ax.add_patch(Polygon([(x-0.022,y+0.011),(x-0.010,y+0.030),(x+0.018,y+0.030),(x+0.031,y+0.011)], closed=True, facecolor=white, edgecolor="none", zorder=7))
        _wheel(ax, x-0.025, y-0.018)
        _wheel(ax, x+0.025, y-0.018)
    elif mode == "train":
        ax.add_patch(Rectangle((x-0.030, y-0.030), 0.060, 0.066, facecolor=white, edgecolor="none", zorder=7))
        ax.add_patch(Rectangle((x-0.020, y+0.010), 0.040, 0.015, facecolor=PRIMARY, edgecolor="none", zorder=8))
        ax.plot([x-0.018,x+0.018],[y-0.038,y-0.038],color=white,linewidth=2.0,zorder=8)
    elif mode == "road train":
        ax.add_patch(Rectangle((x-0.044, y-0.014), 0.022, 0.026, facecolor=white, edgecolor="none", zorder=7))
        ax.add_patch(Rectangle((x-0.018, y-0.012), 0.026, 0.024, facecolor=white, edgecolor="none", zorder=7))
        ax.add_patch(Rectangle((x+0.012, y-0.012), 0.026, 0.024, facecolor=white, edgecolor="none", zorder=7))
        for wx in (x-0.034,x-0.005,x+0.025):
            _wheel(ax, wx, y-0.019, 0.0065)
    elif mode == "helicopter":
        ax.add_patch(Ellipse((x, y), 0.060, 0.030, facecolor=white, edgecolor="none", zorder=7))
        ax.plot([x-0.010,x-0.010],[y+0.015,y+0.038],color=white,linewidth=2.0,zorder=8)
        ax.plot([x-0.045,x+0.045],[y+0.038,y+0.038],color=white,linewidth=2.0,zorder=8)
        ax.plot([x+0.025,x+0.050],[y+0.002,y+0.018],color=white,linewidth=3.0,zorder=8)
        ax.plot([x-0.025,x+0.020],[y-0.022,y-0.022],color=white,linewidth=2.0,zorder=8)
    elif mode == "plane":
        ax.add_patch(Polygon([
            (x-0.048,y-0.006),(x-0.010,y-0.006),(x+0.035,y-0.040),
            (x+0.043,y-0.035),(x+0.015,y-0.004),(x+0.050,y+0.006),
            (x+0.050,y+0.012),(x+0.012,y+0.009),(x-0.012,y+0.040),
            (x-0.020,y+0.036),(x-0.010,y+0.008),(x-0.048,y+0.008)
        ], closed=True, facecolor=white, edgecolor="none", zorder=7))
    elif mode == "boat":
        ax.add_patch(Polygon([(x-0.040,y-0.005),(x+0.040,y-0.005),(x+0.026,y-0.030),(x-0.028,y-0.030)], closed=True, facecolor=white, edgecolor="none", zorder=7))
        ax.add_patch(Rectangle((x-0.012,y-0.002),0.025,0.024,facecolor=white,edgecolor="none",zorder=7))
        for yy in (y-0.038, y-0.047):
            ax.plot([x-0.043,x-0.020,x+0.003,x+0.026,x+0.045],[yy,yy+0.004,yy,yy+0.004,yy],color=white,linewidth=1.5,zorder=8)
    elif mode == "horseback":
        ax.add_patch(Ellipse((x-0.005,y),0.052,0.030,facecolor=white,edgecolor="none",zorder=7))
        ax.add_patch(Circle((x+0.028,y+0.018),0.014,facecolor=white,edgecolor="none",zorder=7))
        ax.plot([x+0.015,x+0.028],[y+0.005,y+0.019],color=white,linewidth=4.0,zorder=8)
        for lx in (x-0.020,x-0.002,x+0.012):
            ax.plot([lx,lx-0.004],[y-0.012,y-0.040],color=white,linewidth=2.2,zorder=8)
        ax.plot([x-0.032,x-0.048],[y+0.005,y+0.022],color=white,linewidth=2.0,zorder=8)


def render_mode_clusters(repo_root, config, rows):
    counts = {}
    modes = {}
    for row in rows:
        family = str(row["transport_family"])
        counts[family] = int(row["family_count"])
        modes.setdefault(family, []).append(str(row["mode"]))

    order = ["Ground", "Air", "Water", "Animal"]
    expected = {"Ground": 4, "Air": 2, "Water": 1, "Animal": 1}
    if any(counts.get(k) != v for k, v in expected.items()):
        raise ValueError("mode_clusters expects Ground=4, Air=2, Water=1, Animal=1.")

    fig = plt.figure(figsize=(8, 8), facecolor=BG)
    plot_top = _add_header(fig, config["title"], config["subtitle"])

    ax = fig.add_axes([0.03, 0.18, 0.94, max(0.46, plot_top - 0.16)])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    centres = {"Ground": 0.16, "Air": 0.43, "Water": 0.68, "Animal": 0.88}
    group_r = {"Ground": 0.165, "Air": 0.140, "Water": 0.118, "Animal": 0.118}
    group_y = 0.44

    connector_y = 0.44
    ax.plot(
        [0.26, 0.33, 0.53, 0.58, 0.78, 0.80],
        [connector_y, connector_y+0.04, connector_y, connector_y+0.04, connector_y, connector_y+0.04],
        color=PRIMARY, linewidth=2.0, linestyle=(0, (3, 3)), zorder=1,
    )
    for nx in (0.33, 0.58, 0.80):
        ax.scatter([nx], [connector_y+0.04], s=230, color=PRIMARY, zorder=2)

    for family in order:
        cx = centres[family]
        r = group_r[family]
        ax.text(cx, 0.88, family, ha="center", va="center", fontsize=16, fontweight="bold", color=TEXT)
        ax.scatter([cx], [0.77], s=1500, color=ACCENT, edgecolor=BG, linewidth=1.6, zorder=6)
        ax.text(cx, 0.77, str(counts[family]), ha="center", va="center", fontsize=19, fontweight="bold", color=WHITE, zorder=7)
        ax.add_patch(Circle((cx, group_y), r, facecolor="#DDEFF2", edgecolor="none", alpha=0.72, zorder=0))

        family_modes = modes[family]
        if family == "Ground":
            positions = [(cx-0.060,0.52),(cx+0.060,0.52),(cx-0.060,0.36),(cx+0.060,0.36)]
        elif family == "Air":
            positions = [(cx,0.52),(cx,0.34)]
        else:
            positions = [(cx,0.44)]

        for mode, (mx,my) in zip(family_modes, positions):
            _icon_circle(ax, mx, my, 0.056)
            _draw_icon(ax, mode, mx, my)
            ax.text(mx, my-0.078, mode, ha="center", va="top", fontsize=10.5, color=TEXT)

    _add_footer(
        fig,
        config.get("footer_left", "Adam Green | coffeetableviz"),
        config.get("source_text", "Source: Simon Reeve official site"),
    )
    return _save(fig, repo_root, config)


def render_editorial_schematic(repo_root, config, rows, columns=None):
    chart_type = config.get("chart_type")
    if chart_type == "route_zigzag":
        return render_route_zigzag(repo_root, config, rows)
    if chart_type == "route_longitude":
        return render_route_longitude(repo_root, config, rows)
    if chart_type == "mode_clusters":
        return render_mode_clusters(repo_root, config, rows)
    raise ValueError(f"Unsupported editorial schematic chart_type: {chart_type}")
