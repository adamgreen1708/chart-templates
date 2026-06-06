CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/athlete_earnings_top50_cleaned.csv",
    "data_format": "wide",
    "chart_type": "scatter",

    "x_col": "on_field_earnings_usd_m",
    "y_col": "off_field_earnings_usd_m",
    "series_col": None,
    "value_col": None,

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "Most fortunes are still made in competition",
    "subtitle": "Only six of the top 50 earn more off the field than they do from salary, winnings or prize money.",
    "source_text": "Source: Forbes, 2026",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "relationship",
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
        "max": 250,
        "tick_interval": 50,
        "format": "currency"
    },

    "y_axis_min": 0,
    "y_axis_max": 140,
    "y_tick_interval": 20,
    "y_tick_format": "currency",

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
    # TYPOGRAPHY
    # ---------------------------
    "title_fontsize": 22,
    "subtitle_fontsize": 12,
    "tick_label_fontsize": 10,
    "axis_label_fontsize": 10,
    "footer_fontsize": 9,

    "title_wrap_width": 38,
    "subtitle_wrap_width": 68,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,

    # ---------------------------
    # LAYOUT
    # ---------------------------
    "fig_width": 8.0,
    "fig_height": 8.0,

    "title_x": 0.10,
    "title_y": 0.93,
    "subtitle_x": 0.10,
    "subtitle_y": 0.855,

    "footer_left_x": 0.10,
    "footer_right_x": 0.90,
    "footer_y": 0.055,

    "plot_top": 0.74,
    "plot_bottom": 0.13,
    "plot_left": 0.14,
    "plot_right": 0.90,

    "vertical_gridlines": False,

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "reference_lines": [
        {
            "axis": "diagonal",
            "label": "Equal on- and off-field earnings",
            "color": "#7A7A7A",
            "linestyle": "--",
            "linewidth": 1.0,
            "alpha": 0.7,
            "rotation": 29
        }
    ],

    "highlight_points": [
        {"column": "name", "target": "Shohei Ohtani"},
        {"column": "name", "target": "LeBron James"},
        {"column": "name", "target": "Rory McIlroy"},
        {"column": "name", "target": "Carlos Alcaraz"},
        {"column": "name", "target": "Jannik Sinner"},
        {"column": "name", "target": "Stephen Curry"}
    ],

    "annotate_points": [
        {
            "column": "name",
            "target": "Shohei Ohtani",
            "label": "Ohtani\n$2.6m on Â· $125m off",
            "xytext": (14, -4),
            "ha": "left",
            "va": "center",
            "fontsize": 9,
            "color": "#C44E52",
            "fontweight": "bold",
            "arrowprops": {
                "arrowstyle": "->",
                "color": "#C44E52",
                "lw": 1.0
            }
        },
        {
            "column": "name",
            "target": "LeBron James",
            "label": "LeBron",
            "xytext": (10, 10),
            "ha": "left",
            "va": "bottom",
            "fontsize": 8,
            "color": "#555555",
            "arrowprops": None
        },
        {
            "column": "name",
            "target": "Rory McIlroy",
            "label": "McIlroy",
            "xytext": (10, 7),
            "ha": "left",
            "va": "bottom",
            "fontsize": 8,
            "color": "#555555",
            "arrowprops": None
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

    "output_file": "output/athlete_earnings_02_on_vs_off.png"
}
