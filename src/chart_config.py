CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/world_cup_chart_03_home_winners.csv",
    "data_format": "wide",
    "chart_type": "dot",  # line | bar | dot | scatter

    "x_col": "year",
    "y_col": "home_win_label",
    "series_col": None,
    "value_col": None,

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "Home advantage is rare, but it sticks",
    "subtitle": "Only six World Cup finals in this dataset ended with the host nation lifting the trophy.",
    "source_text": "Source: Wikipedia - List of FIFA World Cup Finals",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "timeline_highlight",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    # ---------------------------
    # AXES
    # ---------------------------
    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "x_label": "World Cup year",
    "y_label": "Host nation winners",

    "x_axis": {
        "min": 1928,
        "max": 2002,
        "tick_interval": 12,
        "format": ".0f"  # percent | currency | millions | ".1f"
    },

    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    # ---------------------------
    # SORTING
    # ---------------------------
    "sort": {
        "by": "year",
        "ascending": True
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
    "reference_lines": [],

    "highlight_points": [
        {
            "column": "highlight",
            "value": "TRUE"
        }
    ],

    "annotate_points": [
        {
            "column": "winner",
            "value": "England",
            "text": "England 1966",
            "xytext": [10, -14],
            "fontsize": 8
        },
        {
            "column": "winner",
            "value": "France",
            "text": "France 1998",
            "xytext": [-64, 14],
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
    "tick_label_fontsize": 9,
    "axis_label_fontsize": 10,
    "footer_fontsize": 8,

    "title_wrap_width": 38,
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
    "subtitle_y": 0.855,

    "footer_left_x": 0.10,
    "footer_right_x": 0.90,
    "footer_y": 0.075,

    "plot_top": 0.74,
    "plot_bottom": 0.18,
    "plot_left": 0.26,
    "plot_right": 0.86,

    "vertical_gridlines": False,

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "output_file": "output/world_cup_chart_03_home_winners.png"
}
