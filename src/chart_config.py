CHART_CONFIG = {
    "data_file": "data/east_anglia_sunshine_clean.csv",
    "data_format": "long",
    "chart_type": "line",

    "x_col": "month",
    "y_col": "sunshine_hours",
    "series_col": "year",
    "value_col": "sunshine_hours",

    "title": "East Anglia’s 2025 sunshine haul was built in spring",
    "subtitle": "Two record-breaking months in March and April helped 2025 pull clear of the pack, even before the year-end total made it the standout year in the series.",
    "source_text": "Source: East Anglia sunshine dataset (user-provided)",
    "footer_left": "Adam Green | coffeetableviz",
    "footer_right": "",

    "story_angle": "focus_vs_context",

    "focus_series": 2025,
    "secondary_series": 2022,

    "context_style": {
        "color": "#CFCFCF",
        "linewidth": 1.0,
        "alpha": 0.35,
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 3.0,
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

    "label_strategy": "end",
    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "y_axis_min": 0,
    "y_axis_max": 360,
    "y_tick_interval": 60,
    "y_tick_format": "{:,.0f}",

    "line_width": 2.5,
    "marker_size": 0,
    "show_markers": False,

    "auto_end_labels": True,
    "end_labels": [],

    "sort_descending": False,

    "reference_lines": [],

    "highlight_points": [
        {"series": 2025, "x": "Mar", "y": 222.0},
        {"series": 2025, "x": "Apr", "y": 269.2}
    ],

    "annotate_points": [
        {
            "series": 2025,
            "x": "Mar",
            "y": 222.0,
            "label": "Record March",
            "dx": 0,
            "dy": 12
        },
        {
            "series": 2025,
            "x": "Apr",
            "y": 269.2,
            "label": "Record April",
            "dx": 0,
            "dy": 12
        }
    ]
}