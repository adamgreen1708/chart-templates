# =========================
# CHART 1
# Crucible dynasties timeline
# =========================

CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/snooker_world_championship_winners.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "year",
    "y_col": "winner",
    "series_col": None,
    "value_col": None,

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "The Crucible belonged to a few giants",
    "subtitle": "Steve Davis, Stephen Hendry and Ronnie O’Sullivan dominated entire eras of snooker history.",
    "source_text": "Source: World Snooker Championship winners 1977–2026",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "concentration",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    # ---------------------------
    # AXES
    # ---------------------------
    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_axis": {
        "min": 1976,
        "max": 2027,
        "tick_interval": 5,
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
    "marker_size": 70,
    "show_markers": True,
    "auto_end_labels": False,

    # ---------------------------
    # STYLING
    # ---------------------------
    "dot_style": {
        "color": "#D9D9D9",
        "size": 44,
        "alpha": 0.45,
    },

    "highlight_style": {
        "color": "#C44E52",
        "size": 100,
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
        {"winner": "Steve Davis"},
        {"winner": "Stephen Hendry"},
        {"winner": "Ronnie O'Sullivan"},
    ],

    "annotate_points": [
        {
            "x": 1989,
            "y": "Steve Davis",
            "label": "1980s dominance",
            "xytext": (0, -12),
            "ha": "center",
            "va": "top",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None,
        },
        {
            "x": 1996,
            "y": "Stephen Hendry",
            "label": "1990s dynasty",
            "xytext": (0, -12),
            "ha": "center",
            "va": "top",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None,
        },
        {
            "x": 2022,
            "y": "Ronnie O'Sullivan",
            "label": "Longevity era",
            "xytext": (-10, -12),
            "ha": "right",
            "va": "top",
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
    "plot_left": 0.22,
    "plot_right": 0.92,

    "vertical_gridlines": True,

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "output_file": "output/snooker_crucible_dynasty_timeline.png",
}
