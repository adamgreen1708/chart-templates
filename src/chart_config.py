CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_clean.csv",
    "data_format": "long",
    "chart_type": "line",

    "x_col": "month_num",
    "y_col": "sunshine_hours",
    "series_col": "year",
    "value_col": "sunshine_hours",

    "title": "East Anglia’s 2025 sunshine surge was built in spring",
    "subtitle": "Monthly sunshine hours. Against more than a century of background years, 2025 stands out most in March and April, both record months in this dataset.",
    "source_text": "Source: East Anglia sunshine dataset (user-provided)",
    "footer_left": "Adam Green | coffeetableviz",
    "footer_right": "",

    "story_angle": "focus_vs_context",

    "focus_series": 2025,
    "secondary_series": None,

    "context_style": {
        "color": "#CFCFCF",
        "linewidth": 1.0,
        "alpha": 0.35
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

    "reference_lines": [],

    "highlight_points": [
        {"x": 3, "y": 222.0, "series": 2025},
        {"x": 4, "y": 269.2, "series": 2025}
    ],

    "annotate_points": [
        {"x": 3, "y": 222.0, "series": 2025, "text": "Record March"},
        {"x": 4, "y": 269.2, "series": 2025, "text": "Record April"}
    ],

    "auto_end_labels": True,

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