CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_2025_wide.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "month",
    "y_col": "sunshine_hours",
    "series_col": None,
    "value_col": None,

    "title": "June sits clearly on top of East Anglia’s sunshine rankings",
    "subtitle": "Monthly sunshine hours in 2025 ranked from highest to lowest show a clear leader, with June well ahead of the rest.",
    "source_text": "Source: East Anglia sunshine dataset (user-provided)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranking",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "y_axis_min": 0,
    "y_axis_max": None,
    "y_tick_interval": 25,
    "y_tick_format": ".0f",

    "line_width": 2.6,
    "marker_size": 0,
    "show_markers": False,
    "auto_end_labels": True,
    "sort_descending": True,
    
    "fig_width": 8,
    "fig_height": 10,

    "title_fontsize": 24,
    "subtitle_fontsize": 15,
    "tick_label_fontsize": 12,
    "footer_fontsize": 10,

    "reference_lines": [
        {
            "value": 165.8,
            "label": "2025 monthly average"
        }
    ],

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
            "text": "June is the clear peak"
        }
    ],

    "end_labels": [],

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
}