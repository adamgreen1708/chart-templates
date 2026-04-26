CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/rapeseed-production-europe-1974-2024.csv",
    "data_format": "long",
    "chart_type": "line",

    "x_col": "Year",
    "y_col": "Rape or colza seed - Production (tonnes)",
    "series_col": "Entity",
    "value_col": "Rape or colza seed - Production (tonnes)",

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "The UK’s rapeseed boom didn’t last",
    "subtitle": "UK production climbed for decades and peaked around 2011, but has fallen back while several European producers remained higher.",
    "source_text": "Source: Our World in Data (rapeseed production)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "focus_vs_context",
    "focus_series": "United Kingdom",
    "secondary_series": None,
    "label_strategy": "focus_only",

    # ---------------------------
    # AXES
    # ---------------------------
    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_axis": {
        "min": 1974,
        "max": 2029,
        "tick_interval": 10,
        "format": None
    },

    "y_axis_min": 0,
    "y_axis_max": None,
    "y_tick_interval": 1000000,
    "y_tick_format": "millions",

    # ---------------------------
    # SORTING
    # ---------------------------
    "sort": None,
    "sort_descending": False,

    # ---------------------------
    # MARKS
    # ---------------------------
    "line_width": 2.6,
    "marker_size": 0,
    "show_markers": False,
    "auto_end_labels": True,

    # ---------------------------
    # STYLING
    # ---------------------------
    "dot_style": {
        "color": "#1F8FA8",
        "size": 60,
        "alpha": 0.75
    },

    "highlight_style": {
        "color": "#C44E52",
        "size": 85,
        "alpha": 1.0
    },

    "context_style": {
        "color": "#D9D9D9",
        "linewidth": 1.0,
        "alpha": 0.18
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 3.4,
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
    "reference_lines": [],

    "highlight_points": [
        {
            "series": "United Kingdom",
            "x": 2011
        },
        {
            "series": "United Kingdom",
            "x": 2024
        }
    ],

    "annotate_points": [
        {
            "series": "United Kingdom",
            "x": 2011,
            "text": "UK peak",
            "xytext": [18, 22]
        },
        {
            "series": "United Kingdom",
            "x": 2024,
            "text": "2024: back below 1M tonnes",
            "xytext": [-105, -28]
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
    "plot_right": 0.86,

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "output_file": "output/uk_rapeseed_boom_didnt_last.png"
}