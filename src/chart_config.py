CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_2025.csv",
    "data_format": "wide",
    "chart_type": "bar",

    "x_col": "month",
    "y_col": "sunshine_hours",

    "title": "June dominates East Anglia’s sunshine rankings",
    "subtitle": "Sunshine hours in 2025 were heavily skewed — June stands clear at the top, with a sharp drop to the rest of the year.",
    "source_text": "Source: East Anglia sunshine dataset (user-provided)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_outlier",

    "focus_series": None,
    "secondary_series": None,

    "context_style": {
        "color": "#CFCFCF",
        "linewidth": 1.0,
        "alpha": 0.45,
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 2.0,
        "alpha": 1.0,
    },

    "secondary_style": {
        "color": "#7A7A7A",
        "linewidth": 2.0,
        "alpha": 0.9,
    },

    "sort_descending": True,

    "y_axis_min": 0,
    "y_axis_max": None,
    "y_tick_interval": 25,
    "y_tick_format": ".0f",

    "auto_end_labels": True,

    "reference_lines": [
        {
            "axis": "y",
            "value": 165.8,
            "label": "2025 monthly average",
            "color": "#7A7A7A",
            "linestyle": ":",
            "linewidth": 1.5,
            "alpha": 0.9,
        }
    ],

    "highlight_points": [
        {
            "x": "Jun",
            "y": 276.8,
            "label": "Highest"
        }
    ],

    "annotate_points": [
        {
            "x": "Jun",
            "y": 276.8,
            "text": "June leads by a wide margin\n(276.8 hours)",
            "xytext": (12, 0),
            "ha": "left"
        }
    ]
}