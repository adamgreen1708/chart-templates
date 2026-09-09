CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/james_bond_villain_age_rank.csv",
    "data_format": "wide",
    "chart_type": "dot",
    "orientation": None,
    "x_col": "villain_age_at_release",
    "y_col": "villain_label",
    "series_col": None,
    "value_col": None,
    "filters": [],

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "A Bond villain is usually in their forties",
    "subtitle": "Thirteen of 24 comparable first-listed villain actors were in their 40s at UK release; average age 46.6.",
    "source_text": "Sources: Wikipedia; 007 Under the Mango Tree. DAD excluded.",
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
    "x_label": "Villain actor age at UK release",
    "y_label": "",
    "x_margin": 0.04,
    "x_axis": {"min": 30, "max": 68, "tick_interval": 5, "format": ".0f"},
    "y_axis": {"min": None, "max": None, "tick_interval": None, "format": None},
    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    # ---------------------------
    # SORTING
    # ---------------------------
    "sort": {"by": "villain_age_at_release", "ascending": False},
    "sort_descending": False,

    # ---------------------------
    # MARKS / STYLE
    # ---------------------------
    "line_width": 2.6,
    "marker_size": 60,
    "show_markers": True,
    "auto_end_labels": False,
    "dot_style": {"color": "#1F8FA8", "size": 48, "alpha": 0.75},
    "point_style": {"color": "#7A7A7A", "size": 52, "alpha": 0.70},
    "bar_style": {"color": "#1F8FA8", "alpha": 0.90},
    "highlight_style": {"color": "#C44E52", "size": 90, "alpha": 1.0},
    "context_style": {"color": "#D9D9D9", "linewidth": 0.8, "alpha": 0.25},
    "focus_style": {"color": "#1F8FA8", "linewidth": 3.2, "alpha": 1.0},
    "secondary_style": {"color": "#7A7A7A", "linewidth": 2.0, "alpha": 0.9},

    # ---------------------------
    # REFERENCE / ANNOTATION
    # ---------------------------
    "reference_lines": [],
    "trend_line": {"enabled": False, "color": "#7A7A7A", "linewidth": 1.4, "linestyle": "-", "alpha": 0.8},
    "highlight_points": [
        {"villain_label": "Rosa Klebb"},
        {"villain_label": "Elektra King"},
    ],
    "annotate_points": [],
    "end_labels": [],
    "label_style": {
        "enabled": True,
        "label_col": "villain_age_at_release",
        "label_format": "{:.0f}",
        "position": "right",
        "fontsize": 7,
    },

    # ---------------------------
    # TYPOGRAPHY / LAYOUT
    # ---------------------------
    "title_fontsize": 22,
    "subtitle_fontsize": 12,
    "tick_label_fontsize": 8,
    "axis_label_fontsize": 10,
    "footer_fontsize": 10,
    "title_wrap_width": 40,
    "subtitle_wrap_width": 74,
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
    "plot_left": 0.29,
    "plot_right": 0.90,
    "vertical_gridlines": True,

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "output_file": "output/bond_villains_01_age_rank.png",
}
