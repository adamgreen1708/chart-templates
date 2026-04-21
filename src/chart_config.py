CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_clean.csv",
    "data_format": "long",
    "chart_type": "line",

    "x_col": "year",
    "y_col": "sunshine_hours",
    "series_col": "month",
    "value_col": "sunshine_hours",

    "title": "Spring is arriving brighter in East Anglia",
    "subtitle": "March sunshine has trended upward over the long run, suggesting the darker months are giving way earlier. Some of the brightest early springs in the series have come in recent decades.",
    "source_text": "Source: Met Office regional climate statistics (East Anglia sunshine)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "single_series_trend",

    "focus_series": "Mar",
    "secondary_series": None,

    "context_style": {
        "color": "#E0E0E0",
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

    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "y_axis_min": 0,
    "y_axis_max": 230,
    "y_tick_interval": 25,
    "y_tick_format": ".0f",

    "line_width": 2.6,
    "marker_size": 0,
    "show_markers": False,

    "auto_end_labels": True,

    "reference_lines": [],
    "highlight_points": [],
    "annotate_points": [],
    "end_labels": [],
}