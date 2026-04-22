CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_2025_wide.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "month",
    "y_col": "sunshine_hours",
    "series_col": None,
    "value_col": None,

    "title": "June towers over East Anglia’s 2025 sunshine table",
    "subtitle": "Monthly sunshine hours ranked from highest to lowest show one standout peak and a steep drop into the darker months.",
    "source_text": "Source: Met Office East Anglia sunshine dataset",
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

    "reference_lines": [
        {
            "value": 165.8,
            "label": "2025 monthly average",
            "linestyle": "--",
            "linewidth": 1.0,
            "alpha": 0.9,
        }
    ],

    "highlight_points": [
        {
            "x": "Jun",
            "y": 276.8,
            "label": "#1",
            "color": "#C44E52",
        }
    ],

    "annotate_points": [
        {
            "x": "Jun",
            "y": 276.8,
            "text": "June is the clear peak",
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

    "fig_width": 8.0,
    "fig_height": 8.0,

    "title_fontsize": 22,
    "subtitle_fontsize": 13,
    "tick_label_fontsize": 12,
    "footer_fontsize": 10,

    "title_wrap_width": 30,
    "subtitle_wrap_width": 58,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,

    "title_x": 0.11,
    "title_y": 0.94,
    "subtitle_x": 0.11,
    "subtitle_y": 0.865,

    "footer_left_x": 0.11,
    "footer_right_x": 0.89,
    "footer_y": 0.075,

    "plot_top": 0.70,
    "plot_bottom": 0.16,
    "plot_left": 0.11,
    "plot_right": 0.89,
}