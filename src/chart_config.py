# =========================
# CHART 3
# International rise
# =========================

CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/snooker_crucible_uk_vs_world.csv",
    "data_format": "long",
    "chart_type": "line",

    "x_col": "year",
    "y_col": "cumulative_titles",
    "series_col": "group",
    "value_col": "cumulative_titles",

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "The world finally broke into Sheffield",
    "subtitle": "The Crucible began as a UK stronghold, but international champions have accelerated in the modern era.",
    "source_text": "Source: World Snooker Championship winners 1977–2026",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "shift",
    "focus_series": "International",
    "secondary_series": "UK",
    "label_strategy": "focus_and_secondary",

    # ---------------------------
    # AXES
    # ---------------------------
    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_axis": {
        "min": 1977,
        "max": 2026,
        "tick_interval": 5,
        "format": ".0f"
    },

    "y_axis_min": 0,
    "y_axis_max": 40,
    "y_tick_interval": 5,
    "y_tick_format": ".0f",

    # ---------------------------
    # SORTING
    # ---------------------------
    "sort": None,
    "sort_descending": False,

    # ---------------------------
    # MARKS
    # ---------------------------
    "line_width": 2.6,
    "marker_size": 40,
    "show_markers": False,
    "auto_end_labels": True,

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
        "linewidth": 1.4,
        "alpha": 0.35
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 3.4,
        "alpha": 1.0
    },

    "secondary_style": {
        "color": "#7A7A7A",
        "linewidth": 2.2,
        "alpha": 0.9
    },

    # ---------------------------
    # ANNOTATIONS
    # ---------------------------
    "reference_lines": [],

    "highlight_points": [
        {"year": 2023},
        {"year": 2025},
        {"year": 2026}
    ],

    "annotate_points": [
        {
            "x": 2025,
            "y": 12,
            "label": "China arrives",
            "xytext": (-12, -10),
            "ha": "right",
            "va": "top",
            "fontsize": 8,
            "color": "#333333",
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
    "output_file": "output/snooker_world_vs_uk.png"
}