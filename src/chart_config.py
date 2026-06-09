CHART_CONFIG = {
    "data_file": "data/arsenal_2025_26_matches.csv",
    "data_format": "wide",
    "chart_type": "line",

    "x_col": "Matchweek",
    "y_col": "CumulativePoints",
    "series_col": None,
    "value_col": None,

    "title": "Even April couldn’t stop them",
    "subtitle": "Back-to-back defeats briefly stalled Arsenal on 70 points, before five wins from the final six sealed the title.",
    "source_text": "Source: Football-Data.co.uk, Premier League 2025/26 results",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "time_trend",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_axis": {
        "min": 1,
        "max": 38,
        "tick_interval": 5,
        "format": None
    },

    "y_axis_min": 0,
    "y_axis_max": 90,
    "y_tick_interval": 10,
    "y_tick_format": None,

    "sort": {
        "by": "Matchweek",
        "ascending": True
    },
    "sort_descending": False,

    "line_width": 3.2,
    "marker_size": 44,
    "show_markers": True,
    "auto_end_labels": False,

    "dot_style": {
        "color": "#D9D9D9",
        "size": 48,
        "alpha": 0.55
    },

    "highlight_style": {
        "color": "#C44E52",
        "size": 90,
        "alpha": 1.0
    },

    "context_style": {
        "color": "#D9D9D9",
        "linewidth": 0.8,
        "alpha": 0.25
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 3.2,
        "alpha": 1.0
    },

    "secondary_style": {
        "color": "#7A7A7A",
        "linewidth": 2.0,
        "alpha": 0.9
    },

    "reference_lines": [
        {
            "axis": "x",
            "value": 32,
            "label": "April wobble",
            "color": "#7A7A7A",
            "linestyle": "--",
            "linewidth": 1.0,
            "alpha": 0.7
        }
    ],

    "highlight_points": [],

    "annotate_points": [
        {
            "column": "Matchweek",
            "value": 31,
            "text": "70 pts before the wobble",
            "xytext": [8, -18],
            "fontsize": 8
        },
        {
            "column": "Matchweek",
            "value": 33,
            "text": "Two straight defeats",
            "xytext": [-80, 18],
            "fontsize": 8
        },
        {
            "column": "Matchweek",
            "value": 38,
            "text": "85 pts",
            "xytext": [-42, 10],
            "fontsize": 8
        }
    ],

    "end_labels": [],

    "label_style": {
        "enabled": False,
        "label_col": None,
        "label_format": "{}",
        "position": "right",
        "fontsize": 8
    },

    "title_fontsize": 22,
    "subtitle_fontsize": 12,
    "tick_label_fontsize": 10,
    "axis_label_fontsize": 10,
    "footer_fontsize": 10,

    "title_wrap_width": 40,
    "subtitle_wrap_width": 72,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,

    "fig_width": 8.0,
    "fig_height": 8.0,

    "title_x": 0.10,
    "title_y": 0.92,
    "subtitle_x": 0.10,
    "subtitle_y": 0.86,

    "footer_left_x": 0.10,
    "footer_right_x": 0.90,
    "footer_y": 0.08,

    "plot_top": 0.75,
    "plot_bottom": 0.14,
    "plot_left": 0.12,
    "plot_right": 0.90,

    "vertical_gridlines": False,

    "dpi": 200,
    "output_file": "output/chart.png"
}