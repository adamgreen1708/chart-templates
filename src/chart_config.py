CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/athlete_earnings_top50_cleaned.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "off_field_earnings_usd_m",
    "y_col": "name",
    "series_col": None,
    "value_col": None,

    "filters": [
        {"column": "off_field_earnings_usd_m", "operator": ">=", "value": 30}
    ],

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "Ohtani has turned his sporting fame into the $ main event",
    "subtitle": "His $125m off field is $40m clear of the top 50.",
    "source_text": "Source: Forbes, 2026",
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

    "x_axis": {
        "min": 0,
        "max": 160,
        "tick_interval": 20,
        "format": "currency"
    },

    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    # ---------------------------
    # SORTING
    # ---------------------------
    "sort": {
        "by": "off_field_earnings_usd_m",
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
    "plot_left": 0.27,
    "plot_right": 0.90,

    "vertical_gridlines": False,

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "reference_lines": [],

    "highlight_points": [
        {"column": "name", "target": "Shohei Ohtani"}
    ],

    "annotate_points": [
        {
            "column": "name",
            "target": "Shohei Ohtani",
            "label": "$125m",
            "xytext": (8, 0),
            "ha": "left",
            "va": "center",
            "fontsize": 9,
            "color": "#C44E52",
            "fontweight": "bold",
            "arrowprops": None
        },
        {
            "column": "name",
            "target": "LeBron James",
            "label": "$85m",
            "xytext": (8, 0),
            "ha": "left",
            "va": "center",
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

    "output_file": "output/athlete_earnings_03_off_field.png"
}
