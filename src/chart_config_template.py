CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/your_file.csv",
    "data_format": "wide",
    "chart_type": "dot",  # line | bar | dot | scatter
    "orientation": None,  # None | horizontal for bar charts

    "x_col": "x_column",
    "y_col": "y_column",
    "series_col": None,
    "value_col": None,

    "filters": [],

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "Your headline title",
    "subtitle": "Your explanatory subtitle",
    "source_text": "Source: ...",
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
    "x_label": "",
    "y_label": "",
    "x_margin": 0.08,

    "x_axis": {
        "min": None,
        "max": None,
        "tick_interval": None,
        "format": None  # percent | currency | millions | billions | ".1f" | "%Y"
    },

    "y_axis": {
        "min": None,
        "max": None,
        "tick_interval": None,
        "format": None
    },
    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    # ---------------------------
    # SORTING
    # ---------------------------
    "sort": {
        "by": "x_column",
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

    "point_style": {
        "color": "#D9D9D9",
        "size": 48,
        "alpha": 0.55
    },

    "bar_style": {
        "color": "#1F8FA8",
        "alpha": 0.9
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
    # REFERENCE LINES / TREND
    # ---------------------------
    "reference_lines": [],

    "trend_line": {
        "enabled": False,
        "color": "#7A7A7A",
        "linewidth": 1.4,
        "linestyle": "-",
        "alpha": 0.8
    },

    # ---------------------------
    # ANNOTATIONS
    # ---------------------------
    "highlight_points": [],
    "annotate_points": [],
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
    "subtitle_wrap_width": 74,
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
