# =========================
# CHART 2
# Final margins
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
    "title": "The Crucible still loves a cliffhanger",
    "subtitle": "Four finals have been decided by a single frame, including Wu Yize’s dramatic 18–17 win in 2026.",
    "source_text": "Source: World Snooker Championship winners 1977–2026",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "outlier",
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
        "format": ".0f"
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
        "alpha": 0.25
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
            "axis": "x",
            "value": 1,
            "label": "Single-frame final",
            "rotation": 0,
            "color": "#7A7A7A",
            "linewidth": 1.0,
            "linestyle": "--",
            "alpha": 0.7
        }
    ],

   "highlight_points": [
    {"year": 1985},
    {"year": 1994},
    {"year": 2002},
    {"year": 2026},
    ],

    "annotate_points": [
    {
        "x": 1,
        "y": 1985,
        "label": "1985: Taylor 18–17 Davis",
        "xytext": (10, 0),
        "ha": "left",
        "va": "center",
        "fontsize": 8,
        "color": "#333333",
        "arrowprops": None,
    },
    {
        "x": 1,
        "y": 1994,
        "label": "1994: Hendry 18–17 White",
        "xytext": (10, 0),
        "ha": "left",
        "va": "center",
        "fontsize": 8,
        "color": "#333333",
        "arrowprops": None,
    },
    {
        "x": 1,
        "y": 2002,
        "label": "2002: Ebdon 18–17 Hendry",
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
        "label": "2026: Wu 18–17 Murphy",
        "xytext": (10, 0),
        "ha": "left",
        "va": "center",
        "fontsize": 8,
        "color": "#333333",
        "arrowprops": None,
    },
    ],
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
    "output_file": "output/snooker_crucible_final_margins.png"
}