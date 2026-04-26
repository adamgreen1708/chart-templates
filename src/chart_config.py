CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/rapeseed-production-europe-1974-2024.csv",
    "data_format": "wide",
    "chart_type": "bar",

    "x_col": "Year",
    "y_col": "pct_change_yoy",
    "series_col": None,
    "value_col": None,

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "The fall wasn’t smooth",
    "subtitle": "UK rapeseed production has swung sharply year to year, with recent drops showing how uneven the decline has been.",
    "source_text": "Source: Our World in Data (rapeseed production)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "single_series_volatility",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    # ---------------------------
    # FILTERS
    # ---------------------------
    "filters": [
        {
            "column": "Entity",
            "operator": "==",
            "value": "United Kingdom"
        },
        {
            "column": "Year",
            "operator": ">",
            "value": 1974
        }
    ],

    # ---------------------------
    # AXES
    # ---------------------------
    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_axis": {
        "min": 1975,
        "max": 2027,
        "tick_interval": 10,
        "format": None
    },

    "y_axis_min": -60,
    "y_axis_max": 80,
    "y_tick_interval": 20,
    "y_tick_format": "percent",

    # ---------------------------
    # SORTING
    # ---------------------------
    "sort": None,
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
    "bar_style": {
        "color": "#1F8FA8",
        "alpha": 0.85
    },

    "highlight_style": {
        "color": "#C44E52",
        "size": 85,
        "alpha": 1.0
    },

    "context_style": {
        "color": "#BFC3C7",
        "linewidth": 1.0,
        "alpha": 0.35
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

    # ---------------------------
    # ANNOTATIONS
    # ---------------------------
    "reference_lines": [
        {
            "axis": "y",
            "value": 0,
            "label": "No change",
            "color": "#7A7A7A",
            "linestyle": "-",
            "linewidth": 1.0
        }
    ],

    "highlight_points": [],

    "annotate_points": [
        {
            "x": 2020,
            "y": -43,
            "label": "Sharp recent fall",
            "xytext": [-70, -22],
            "ha": "right"
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
    "title_fontsize": 24,
    "subtitle_fontsize": 13,
    "tick_label_fontsize": 11,
    "axis_label_fontsize": 11,
    "footer_fontsize": 10,

    "title_wrap_width": 34,
    "subtitle_wrap_width": 72,

    # ---------------------------
    # LAYOUT
    # ---------------------------
    "fig_width": 8.0,
    "fig_height": 8.0,

    "title_x": 0.10,
    "title_y": 0.91,
    "subtitle_x": 0.10,
    "subtitle_y": 0.835,

    "footer_left_x": 0.10,
    "footer_right_x": 0.90,
    "footer_y": 0.08,

    "plot_top": 0.70,
    "plot_bottom": 0.16,
    "plot_left": 0.18,
    "plot_right": 0.90,

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "output_file": "output/uk_rapeseed_yoy_swings.png"
}