CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_2025.csv",
    "data_format": "wide",
    "chart_type": "bar",

    "x_col": "month",
    "y_col": "sunshine_hours",

    "title": "Spring did the heavy lifting",
    "subtitle": "East Anglia’s sunshine in 2025 surged from subdued winter levels to a June peak, with most of the year’s standout brightness concentrated in spring and early summer. Months should remain in calendar order, not be ranked.",
    "source_text": "Source: East Anglia sunshine dataset (user-provided)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "natural_order_seasonal_surge",

    "focus_series": None,
    "secondary_series": None,

    "context_style": {
        "color": "#CFCFCF",
        "linewidth": 1.0,
        "alpha": 0.45,
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 2.5,
        "alpha": 1.0,
    },

    "secondary_style": {
        "color": "#7A7A7A",
        "linewidth": 1.8,
        "alpha": 0.9,
    },

    "reference_lines": [],
    "highlight_points": [],
    "annotate_points": [],

    "y_axis_min": 0,
    "y_axis_max": None,
    "y_tick_interval": 25,
    "y_tick_format": ".0f",

    "auto_end_labels": True,
    "sort_descending": False,
}