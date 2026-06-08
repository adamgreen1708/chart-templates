CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/arsenal_monthly_form.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "PPG",
    "y_col": "Month",
    "series_col": None,
    "value_col": None,

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "One bad month wasn’t enough",
    "subtitle": "April was Arsenal’s only poor month, but the champions were consistent enough either side of it.",
    "source_text": "Source: Football-Data.co.uk, Premier League 2025/26 results",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_comparison",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    # ---------------------------
    # AXES
    # ---------------------------
    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_axis": {
        "min": 0,
        "max": 3,
        "tick_interval": 0.5,
        "format": ".1f"
    },

    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    # ---------------------------
    # SORTING
    # ---------------------------
    "sort": {
        "by": "Month",
        "ascending": False
    },
    "sort_descending": False,

    # ---------------------------
    # MARKS
    # ---------------------------
    "line_width": 2.6,
    "marker_size": 60,
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
            "value": 2,
            "label": "Title pace",
            "color": "#7A7A7A",
            "linestyle": "--",
            "linewidth": 1.0,
            "alpha": 0.7
        }
    ],

    "highlight_points": [
        {
            "column": "Month",
            "value": "2026-04"
        }
    ],

    "annotate_points": [],

    "end_labels": [],

    "label_style": {
        "enabled": True,
        "label_col": "PPG",
        "label_format": "{:.2f}",
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
    "plot_left": 0.18,
    "plot_right": 0.88,

    "vertical_gridlines": False,

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "output_file": "output/chart.png"
}