CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/arsenal_2025_26_matches.csv",
    "data_format": "wide",
    "chart_type": "line",

    "x_col": "Matchweek",
    "y_col": "CumulativePoints",
    "series_col": None,
    "value_col": None,

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "The title was built before April",
    "subtitle": "Arsenal hit 70 points by matchweek 31, then survived back-to-back defeats before finishing seven points clear.",
    "source_text": "Source: Football-Data.co.uk, Premier League 2025/26 results",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "time_trend",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    # ---------------------------
    # AXES
    # ---------------------------
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

    # ---------------------------
    # SORTING
    # ---------------------------
    "sort": {
        "by": "Matchweek",
        "ascending": True
    },
    "sort_descending": False,

    # ---------------------------
    # MARKS
    # ---------------------------
    "line_width": 3.0,
    "marker_size": 44,
    "show_markers": True,
    "auto_end_labels": False,

    # ---------------------------
    # STYLING
    # ---------------------------
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

    # ---------------------------
    # ANNOTATIONS
    # ---------------------------
    "reference_lines": [
        {
            "axis": "x",
            "value": 31,
            "label": "70 pts before April",
            "color": "#7A7A7A",
            "linestyle": "--",
            "linewidth": 1.0,
            "alpha": 0.75
        }
    ],

    "highlight_points": [
        {
            "column": "Matchweek",
            "value": 31
        },
        {
            "column": "Matchweek",
            "value": 32
        },
        {
            "column": "Matchweek",
            "value": 33
        },
        {
            "column": "Matchweek",
            "value": 38
        }
    ],

    "annotate_points": [
        {
            "column": "Matchweek",
            "value": 31,
            "text": "70 points",
            "xytext": [8, 12],
            "fontsize": 8
        },
        {
            "column": "Matchweek",
            "value": 38,
            "text": "Champions: 85",
            "xytext": [-68, 8],
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

    # ---------------------------
    # TYPOGRAPHY
    # ---------------------------
    "title_fontsize": 22,
    "subtitle_fontsize": 12,
    "tick_label_fontsize": 10,
    "axis_label_fontsize": 10,
    "footer_fontsize": 10,

    "title_wrap_width": 40,
    "subtitle_wrap_width": 72,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,

    # ---------------------------
    # LAYOUT
    # ---------------------------
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

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "output_file": "output/chart.png"
}