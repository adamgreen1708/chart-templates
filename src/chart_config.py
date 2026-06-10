CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/world_cup_chart_02_final_timeline.csv",
    "data_format": "wide",
    "chart_type": "scatter",  # line | bar | dot | scatter

    "x_col": "year",
    "y_col": "outcome_score",
    "series_col": None,
    "value_col": None,

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "Finals are getting harder to settle",
    "subtitle": "Extra time and penalties have become part of the World Cup final’s modern rhythm, after a timeline broken by war.",
    "source_text": "Source: Wikipedia - List of FIFA World Cup Finals",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "time_trend",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    # ---------------------------
    # AXES
    # ---------------------------
    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "x_label": "World Cup year",
    "y_label": "Outcome band",

    "x_axis": {
        "min": 1928,
        "max": 2028,
        "tick_interval": 12,
        "format": ".0f"  # percent | currency | millions | ".1f"
    },

    "y_axis_min": -0.4,
    "y_axis_max": 4.4,
    "y_tick_interval": 1,
    "y_tick_format": ".0f",

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

    "point_style": {
        "color": "#1F8FA8",
        "size": 62,
        "alpha": 0.7
    },

    # ---------------------------
    # ANNOTATIONS
    # ---------------------------
    "reference_lines": [
        {
            "axis": "y",
            "value": 0,
            "label": "Not played (WWII)",
            "color": "#7A7A7A",
            "linestyle": "--",
            "linewidth": 0.8,
            "alpha": 0.65
        },
        {
            "axis": "y",
            "value": 1,
            "label": "Settled in play",
            "color": "#7A7A7A",
            "linestyle": "--",
            "linewidth": 0.8,
            "alpha": 0.45
        },
        {
            "axis": "y",
            "value": 2,
            "label": "Extra time",
            "color": "#7A7A7A",
            "linestyle": "--",
            "linewidth": 0.8,
            "alpha": 0.45
        },
        {
            "axis": "y",
            "value": 3,
            "label": "Penalties",
            "color": "#7A7A7A",
            "linestyle": "--",
            "linewidth": 0.8,
            "alpha": 0.45
        },
        {
            "axis": "y",
            "value": 4,
            "label": "Scheduled",
            "color": "#7A7A7A",
            "linestyle": "--",
            "linewidth": 0.8,
            "alpha": 0.65
        }
    ],

    "highlight_points": [
        {"column": "year", "value": "1942"},
        {"column": "year", "value": "1946"},
        {"column": "year", "value": "1994"},
        {"column": "year", "value": "2006"},
        {"column": "year", "value": "2022"},
        {"column": "year", "value": "2026"}
    ],

    "annotate_points": [
        {
            "column": "year",
            "value": "1942",
            "text": "World War II gap",
            "xytext": [8, -18],
            "fontsize": 8
        },
        {
            "column": "year",
            "value": "1994",
            "text": "First penalty final",
            "xytext": [-70, 18],
            "fontsize": 8
        },
        {
            "column": "year",
            "value": "2026",
            "text": "2026 final scheduled",
            "xytext": [-92, 18],
            "fontsize": 8
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
    "title_fontsize": 21,
    "subtitle_fontsize": 12,
    "tick_label_fontsize": 9,
    "axis_label_fontsize": 10,
    "footer_fontsize": 8,

    "title_wrap_width": 42,
    "subtitle_wrap_width": 72,
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
    "subtitle_y": 0.855,

    "footer_left_x": 0.10,
    "footer_right_x": 0.90,
    "footer_y": 0.075,

    "plot_top": 0.74,
    "plot_bottom": 0.18,
    "plot_left": 0.16,
    "plot_right": 0.88,

    "vertical_gridlines": True,

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "output_file": "output/world_cup_chart_02_final_timeline.png"
}