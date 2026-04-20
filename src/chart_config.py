CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_clean.csv",
    "data_format": "long",
    "chart_type": "line",

    "x_col": "year",
    "y_col": "sunshine_hours",
    "series_col": "month",
    "value_col": "sunshine_hours",

    "title": "April is pulling away",
    "subtitle": "East Anglia sunshine shows April strengthening faster than any other month, peaking with a record in 2025 while others sit in the background.",
    "source_text": "Source: Met Office regional climate statistics (East Anglia sunshine)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "focus_vs_context",

    "focus_series": "Apr",
    "secondary_series": None,

    "context_style": {
        "color": "#CFCFCF",
        "linewidth": 1.0,
        "alpha": 0.35,
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
    "y_axis_max": 325,
    "y_tick_interval": 50,
    "y_tick_format": ".0f",

    "line_width": 2.6,
    "marker_size": 0,
    "show_markers": False,

    "auto_end_labels": True,

    "reference_lines": [
        {
            "axis": "y",
            "value": 200,
            "label": "200 hours",
            "color": "#9A9A9A",
            "linestyle": "--",
            "linewidth": 1.2,
            "alpha": 0.8,
        }
    ],

    "highlight_points": [
        {
            "series": "Apr",
            "x": 2025,
            "y": 269.2,
            "label": "Record April",
        }
    ],

    "annotate_points": [
        {
            "series": "Apr",
            "x": 2025,
            "y": 269.2,
            "text": "Sunniest April on record",
        }
    ],

    "end_labels": [],
}