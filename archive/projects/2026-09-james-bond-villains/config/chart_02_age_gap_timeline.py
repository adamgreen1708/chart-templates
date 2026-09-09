CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/james_bond_villain_age_gap_by_film.csv",
    "data_format": "wide",
    "chart_type": "scatter",
    "orientation": None,
    "x_col": "year",
    "y_col": "age_gap_years",
    "series_col": None,
    "value_col": None,
    "filters": [],

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "Bond used to fight his elders",
    "subtitle": "From 1962–71, first-listed villains were 14.3 years older than Bond on average; after that, 1.8 years younger.",
    "source_text": "Sources: Wikipedia; 007 Under the Mango Tree. DAD excluded.",
    "footer_left": "Adam Green | coffeetableviz",
    "story_angle": "shift",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    # ---------------------------
    # AXES
    # ---------------------------
    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "x_label": "Film release year",
    "y_label": "Villain age minus Bond age (years)",
    "x_margin": 0.03,
    "x_axis": {"min": 1960, "max": 2024, "tick_interval": 10, "format": ".0f"},
    "y_axis": {"min": -20, "max": 35, "tick_interval": 10, "format": ".0f"},
    "y_axis_min": -20,
    "y_axis_max": 35,
    "y_tick_interval": 10,
    "y_tick_format": ".0f",

    # ---------------------------
    # SORTING
    # ---------------------------
    "sort": {"by": "year", "ascending": True},
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
    "reference_lines": [
        {
            "axis": "y",
            "value": 0,
            "label": "Same age",
            "rotation": 0,
            "color": "#7A7A7A",
            "linewidth": 1.0,
            "linestyle": "--",
            "alpha": 0.8,
        }
    ],
    "trend_line": {
        "enabled": True,
        "color": "#7A7A7A",
        "linewidth": 1.4,
        "linestyle": "--",
        "alpha": 0.8,
    },
    "highlight_points": [
        {"title": "From Russia with Love"},
        {"title": "A View to a Kill"},
        {"title": "No Time to Die"},
    ],
    "annotate_points": [
        {
            "title": "From Russia with Love",
            "text": "Klebb +32",
            "xytext": (8, -12),
            "ha": "left",
            "va": "top",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None,
        },
        {
            "title": "A View to a Kill",
            "text": "Zorin -15",
            "xytext": (8, 10),
            "ha": "left",
            "va": "bottom",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None,
        },
        {
            "title": "No Time to Die",
            "text": "Safin -13",
            "xytext": (-8, 10),
            "ha": "right",
            "va": "bottom",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None,
        },
    ],
    "end_labels": [],
    "label_style": {
        "enabled": False,
        "label_col": None,
        "label_format": "{}",
        "position": "right",
        "fontsize": 8,
    },

    # ---------------------------
    # TYPOGRAPHY / LAYOUT
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
    "plot_left": 0.15,
    "plot_right": 0.90,
    "vertical_gridlines": False,

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "output_file": "output/bond_villains_02_age_gap_timeline.png",
}
