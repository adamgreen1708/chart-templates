CHART_CONFIG = {
    "data_file": "east_anglia_sunshine_clean.csv",
    "data_format": "long",
    "chart_type": "line",

    "x_col": "year",
    "y_col": "sunshine_hours",
    "series_col": "month",
    "value_col": "sunshine_hours",

    "title": "June 2025 was almost off the charts",
    "subtitle": "East Anglia recorded 276.8 sunshine hours in June 2025, making it one of the brightest Junes in the series and far above the typical June level.",
    "source_text": "Source: East Anglia sunshine dataset (user-provided)",
    "footer_left": "Adam Green | coffeetableviz",
    "footer_right": "",

    "story_angle": "focus_vs_context",

    "focus_series": "Jun",
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

    "sort_descending": False,
    "auto_end_labels": True,

    "reference_lines": [
        {
            "y": 202.6,
            "label": "Average June"
        }
    ],

    "highlight_points": [
        {
            "series": "Jun",
            "x": 2025,
            "y": 276.8,
            "label": "June 2025"
        }
    ],

    "annotate_points": [
        {
            "series": "Jun",
            "x": 2025,
            "y": 276.8,
            "label": "276.8 hours"
        }
    ],

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
    "plot_right": 0.89
}