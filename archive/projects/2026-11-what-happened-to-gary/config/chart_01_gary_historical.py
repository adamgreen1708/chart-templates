# Historical ONS data have ONLY decennial ranks. Plot the actual positions;
# connecting lines guide the eye between snapshots; they are not annual values.
CHART_CONFIG = {
    "data_file": "archive/projects/2026-11-what-happened-to-gary/data/chart_01_historical_rank.csv",
    "data_format": "wide", "chart_type": "line", "orientation": None,
    "x_col": "year", "y_col": "rank",
    "series_col": None, "value_col": None,
    "story_angle": "single_series_trend", "render_profile": "social_square",
    "title": "Gary really had a moment",
    "subtitle": "Up 79 places in 20 years. Out of the top 100 by 1994. Decade snapshots only.",
    "source_text": "Source: ONS historical top-100 ranks (10-year snapshots)",
    "footer_left": "Adam Green | coffeetableviz",
    "x_label": "Historical snapshot year",
    "y_label": "Rank (No. 1 = most popular)",
    "x_axis": {"min": 1939, "max": 1992, "tick_interval": None, "format": ".0f"},
    "x_tick_labels": [
        {"value": 1944, "label": "1944"},
        {"value": 1954, "label": "1954"},
        {"value": 1964, "label": "1964"},
        {"value": 1974, "label": "1974"},
        {"value": 1984, "label": "1984"},
    ],
    # Reversed ranking axis: 1 at the top, 100 at the bottom.
    # A zero rank does not exist, so omit zero ticks entirely.
    "y_axis_min": 104, "y_axis_max": 1, "y_tick_interval": None,
    "y_tick_labels": [
        {"value": 1, "label": "1"},
        {"value": 20, "label": "20"},
        {"value": 40, "label": "40"},
        {"value": 60, "label": "60"},
        {"value": 80, "label": "80"},
        {"value": 100, "label": "100"},
    ],
    "show_markers": True, "line_width": 3.0,
    "focus_style": {"color": "#1F8FA8", "linewidth": 3.0, "alpha": 1.0},
    "highlight_style": {"color": "#C44E52", "size": 185, "alpha": 1.0},
    "highlight_points": [{"year": 1964}],
    # Exact rank labels are generated FROM the CSV's rank column.
    "label_strategy": "all",
    "label_style": {
        "enabled": True, "label_col": "rank", "position": "right",
        "label_format": "No. {:.0f}", "fontsize": 12, "color": "#222222",
    },
    "sort": {"by": "year", "ascending": True}, "sort_descending": False,
    "annotate_points": [], "end_labels": [], "reference_lines": [],
    "x_margin": 0.02, "vertical_gridlines": False,
    "output_file": "output/01_gary_historical_ranks.png",
}
