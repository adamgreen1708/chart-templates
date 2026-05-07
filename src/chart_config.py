# =========================
# CHART 3
# International winners
# =========================

CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/snooker_world_championship_winners.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "frame_margin",
    "y_col": "year",
    "series_col": None,
    "value_col": None,

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "The Crucible’s world map is widening",
    "subtitle": "Champions from Canada, Ireland, Australia, Belgium and China have slowly reshaped snooker’s biggest stage.",
    "source_text": "Source: World Snooker Championship winners 1977–2026",
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

    "x_axis": {
        "min": 0,
        "max": 16,
        "tick_interval": 2,
        "format": ".0f",
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
        "ascending": True,
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
        "alpha": 0.55,
    },

    "highlight_style": {
        "color": "#C44E52",
        "size": 90,
        "alpha": 1.0,
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
        {"year": 1980},
        {"year": 1997},
        {"year": 2010},
        {"year": 2023},
        {"year": 2025},
        {"year": 2026},
    ],

    "annotate_points": [
        {
            "x": 2,
            "y": 1980,
            "label": "1980: Thorburn (Canada)",
            "xytext": (10, 0),
            "ha": "left",
            "va": "center",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None,
        },
        {
            "x": 6,
            "y": 1997,
            "label": "1997: Doherty (Ireland)",
            "xytext": (10, 0),
            "ha": "left",
            "va": "center",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None,
        },
        {
            "x": 5,
            "y": 2010,
            "label": "2010: Robertson (Australia)",
            "xytext": (10, 0),
            "ha": "left",
            "va": "center",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None,
        },
        {
            "x": 3,
            "y": 2023,
            "label": "2023: Brecel (Belgium)",
            "xytext": (10, 0),
            "ha": "left",
            "va": "center",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None,
        },
        {
            "x": 6,
            "y": 2025,
            "label": "2025: Zhao (China)",
            "xytext": (10, 0),
            "ha": "left",
            "va": "center",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None,
        },
        {
            "x": 1,
            "y": 2026,
            "label": "2026: Wu (China)",
            "xytext": (10, 0),
            "ha": "left",
            "va": "center",
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
    "output_file": "output/snooker_crucible_world_map.png",
}