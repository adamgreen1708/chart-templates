CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "archive/projects/2026-09-tom-hanks-colour-bank-revisited/data/tom_hanks_chart_03_toy_story.csv",
    "data_format": "wide",
    "chart_type": "line",
    "orientation": None,

    "x_col": "Year",
    "y_col": "IMDb Rating",
    "series_col": None,
    "value_col": None,

    "filters": [],

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "Woody outlasted the golden run",
    "subtitle": "All five Toy Story films sit above Hanks' 6.9 career median; their median is 7.9 across 31 years.",
    "source_text": "Source: IMDb datasets · ratings 19 Sep 2026",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "franchise_sequence",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    # ---------------------------
    # AXES
    # ---------------------------
    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "x_label": "Film year",
    "y_label": "IMDb rating",
    "x_margin": 0.08,

    "x_axis": {
        "min": 1992,
        "max": 2029,
        "tick_interval": 5,
        "format": ".0f"
    },

    "y_axis": {
        "min": 6.6,
        "max": 8.65,
        "tick_interval": 0.5,
        "format": ".1f"
    },
    "y_axis_min": 6.6,
    "y_axis_max": 8.65,
    "y_tick_interval": 0.5,
    "y_tick_format": ".1f",

    # ---------------------------
    # SORTING
    # ---------------------------
    "sort": {
        "by": "Year",
        "ascending": True
    },
    "sort_descending": False,

    # ---------------------------
    # MARKS
    # ---------------------------
    "line_width": 3.0,
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
        "color": "#1F8FA8",
        "size": 82,
        "alpha": 1.0
    },

    "context_style": {
        "color": "#D9D9D9",
        "linewidth": 0.8,
        "alpha": 0.25,
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 3.0,
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
    "reference_lines": [
        {
            "axis": "y",
            "value": 6.9,
            "label": "Career median 6.9",
            "rotation": 0,
            "color": "#7A7A7A",
            "linewidth": 1.0,
            "linestyle": "--",
            "alpha": 0.7
        }
    ],

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
    "highlight_points": [
        {"column": "Latest Film", "value": 0},
        {"Title": "Toy Story 5", "color": "#C44E52", "size": 100},
    ],
    "annotate_points": [
        {
            "Title": "Toy Story",
            "text": "Toy Story · 8.3",
            "xytext": (8, 9),
            "ha": "left",
            "va": "bottom",
            "fontsize": 8,
            "color": "#111111",
            "arrowprops": None,
        },
        {
            "Title": "Toy Story 2",
            "text": "2 · 7.9",
            "xytext": (-8, -10),
            "ha": "right",
            "va": "top",
            "fontsize": 8,
            "color": "#111111",
            "arrowprops": None,
        },
        {
            "Title": "Toy Story 3",
            "text": "3 · 8.3",
            "xytext": (0, 9),
            "ha": "center",
            "va": "bottom",
            "fontsize": 8,
            "color": "#111111",
            "arrowprops": None,
        },
        {
            "Title": "Toy Story 4",
            "text": "4 · 7.6",
            "xytext": (-8, -10),
            "ha": "right",
            "va": "top",
            "fontsize": 8,
            "color": "#111111",
            "arrowprops": None,
        },
        {
            "Title": "Toy Story 5",
            "text": "5 · 7.4",
            "xytext": (-8, 8),
            "ha": "right",
            "va": "bottom",
            "fontsize": 8,
            "color": "#C44E52",
            "fontweight": "bold",
            "arrowprops": None,
        },
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

    "vertical_gridlines": True,

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "output_file": "output/tom_hanks_03_toy_story.png"
}
