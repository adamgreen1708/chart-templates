CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_2025.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "month",
    "y_col": "sunshine_hours",

    "title": "June dominated East Anglia’s sunshine in 2025",
    "subtitle": "Ranking months by sunshine hours shows a sharp concentration in late spring and early summer, with winter months far behind.",
    "source_text": "Source: East Anglia sunshine dataset (user-provided)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranking",

    "focus_series": None,
    "secondary_series": None,

    "context_style": {
        "color": "#CFCFCF",
        "linewidth": 1.0,
        "alpha": 0.45
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 3.0,
        "alpha": 1.0
    },

    "secondary_style": {
        "color": "#7A7A7A",
        "linewidth": 2.0,
        "alpha": 0.9
    },

    "reference_lines": [],
    "highlight_points": [],
    "annotate_points": [],

    "show_legend": False,
    "legend_loc": "best",

    "x_axis_label": "",
    "y_axis_label": "Sunshine hours",
    "y_axis_min": 0,
    "y_axis_max": None,
    "y_tick_interval": 25,
    "y_tick_format": ".0f",

    "auto_end_labels": True,
    "sort_descending": True
}