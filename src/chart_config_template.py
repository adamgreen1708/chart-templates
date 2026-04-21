CHART_CONFIG = {
    "data_file": "data/your_file.csv",
    "data_format": "wide",  # "wide" or "long"
    "chart_type": "line",   # "line", "bar", "dot", "scatter"

    "x_col": "Year",
    "y_col": "Value",
    "series_col": None,
    "value_col": None,

    "title": "Your headline title",
    "subtitle": "Your explanatory subtitle",
    "source_text": "Source: ...",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "single_series_trend",  # "single_series_trend", "focus_vs_context", "comparison"
    "focus_series": None,                  # None, "Series A", or ["Series A", "Series B"]
    "secondary_series": None,              # None, "Series B", or ["Series B", "Series C"]
    "label_strategy": "focus_only",        # "none", "all", "focus_only", "focus_and_secondary"

    "context_style": {
        "color": "#D9D9D9",
        "linewidth": 0.8,
        "alpha": 0.25,
    },
    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 3.2,
        "alpha": 1.0,
    },
    "secondary_style": {
        "color": "#7A7A7A",
        "linewidth": 2.0,
        "alpha": 0.9,
    },

    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": ".0f",

    "line_width": 2.6,
    "marker_size": 0,
    "show_markers": False,
    "auto_end_labels": True,

    "reference_lines": [],
    "highlight_points": [],
    "annotate_points": [],
    "end_labels": [],
    "sort_descending": False,
}
