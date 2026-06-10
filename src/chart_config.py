CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/world_cup_chart_01_titles_by_winner.csv",
    "data_format": "wide",
    "chart_type": "bar",  # line | bar | dot | scatter

    "x_col": "titles",
    "y_col": "winner",
    "series_col": None,
    "value_col": None,

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "The World Cup has a tiny winners club",
    "subtitle": "Across nearly a century of finals, the trophy has still only been lifted by a small group of countries.",
    "source_text": "Source: Wikipedia - List of FIFA World Cup finals",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_comparison",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "all",

    # ---------------------------
    # AXES
    # ---------------------------
    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "x_label": "World Cup final wins",
    "y_label": "Winner",

    "x_axis": {
        "min": 0,
        "max": 5.5,
        "tick_interval": 1,
        "format": None  # percent | currency | millions | ".1f"
    },

    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    # ---------------------------
    # SORTING
    # ---------------------------
    "sort": {
        "by": "titles",
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

    "bar_style": {
        "color": "#1F8FA8",
        "alpha": 0.9
    },

    # ---------------------------
    # ANNOTATIONS
    # ---------------------------
    "reference_lines": [],

    "highlight_points": [
        {
            "column": "winner",
            "value": "Brazil"
        }
    ],

    "annotate_points": [
        {
            "column": "winner",
            "value": "Brazil",
            "text": "Brazil set the benchmark",
            "xytext": [-98, -14],
            "fontsize": 8
        }
    ],

    "end_labels": [],

    "label_style": {
        "enabled": True,
        "label_col": "titles",
        "label_format": "{:.0f}",
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
    "plot_bottom": 0.16,
    "plot_left": 0.24,
    "plot_right": 0.86,

    "vertical_gridlines": False,
    "orientation": "horizontal",

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "output_file": "output/world_cup_chart_01_titles_by_winner.png"
}
