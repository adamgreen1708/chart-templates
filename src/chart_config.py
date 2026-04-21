CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_2025.csv",
    "data_format": "wide",
    "chart_type": "bar",

    "x_col": "month",
    "y_col": "sunshine_hours",

    "title": "East Anglia’s sunshine exploded in spring",
    "subtitle": "Monthly sunshine hours in 2025 jumped from muted winter levels to a June peak, before falling sharply back into autumn and winter. Months should remain in calendar order.",
    "source_text": "Source: East Anglia sunshine dataset (user-provided)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "category_comparison",

    "sort_descending": False,

    "focus_style": {
        "color": "#1F8FA8",
        "alpha": 1.0
    },

    "secondary_style": {
        "color": "#C44E52",
        "alpha": 1.0
    },

    "context_style": {
        "color": "#D0D0D0",
        "alpha": 0.5
    },

    "highlight_points": [],
    "annotate_points": [],
    "reference_lines": [],

    "label_strategy": "none",

    "y_axis_min": 0,
    "y_axis_max": None,
    "y_tick_interval": 25,
    "y_tick_format": ".0f",
    "auto_end_labels": True
}