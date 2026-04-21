CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_2025_wide.csv",
    "data_format": "wide",
    "chart_type": "bar",

    "x_col": "month",
    "y_col": "sunshine_hours",

    "title": "June sits clearly on top of East Anglia’s sunshine rankings",
    "subtitle": "Monthly sunshine hours in 2025 ranked from highest to lowest show a clear leader, with June ahead of the rest of the year.",
    "source_text": "Source: East Anglia sunshine dataset (user-provided)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_outlier",

    "focus_series": None,
    "secondary_series": None,

    "context_style": {
        "color": "#CFCFCF",
        "linewidth": 1.0,
        "alpha": 0.45
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 2.0,
        "alpha": 1.0
    },

    "secondary_style": {
        "color": "#7A7A7A",
        "linewidth": 2.0,
        "alpha": 0.9
    },

    "sort_descending": True,

    "y_axis_min": 0,
    "y_axis_max": None,
    "y_tick_interval": 25,
    "y_tick_format": ".0f",

    "auto_end_labels": True,

    "reference_lines": [],

    "highlight_points": [
        {
            "x": "Jun",
            "y": 276.8,
            "label": "#1"
        }
    ],

    "annotate_points": [
        {
            "x": "Jun",
            "y": 276.8,
            "text": "June ranks first\n(276.8 hours)",
            "xytext": (12, 0),
            "ha": "left"
        }
    ]
}