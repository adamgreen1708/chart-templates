CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "archive/projects/2026-05-world-cup-finals/data/world_cup_chart_03_home_winners.csv",
    "data_format": "wide",
    "chart_type": "line",  # line | bar | dot | scatter

    "x_col": "year",
    "y_col": "cumulative_host_wins",
    "series_col": None,
    "value_col": None,

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "Home glory has gone quiet",
    "subtitle": "Six host nations have won the World Cup final, but none since France in 1998.",
    "source_text": "Source: Wikipedia- List of FIFA World Cup finals",
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
    "y_label": "Cumulative host-nation wins",
    "x_margin": 0.08,

    "x_axis": {
        "min": 1930,
        "max": 2022,
        "tick_interval": 8,
        "format": None
    },

    "y_axis_min": 0,
    "y_axis_max": 7,
    "y_tick_interval": 1,
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
    "line_width": 3.2,
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
        "size": 100,
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
    # ANNOTATIONS
    # ---------------------------
    "reference_lines": [
        {
            "axis": "x",
            "value": 1998,
            "label": "Last host winner",
            "color": "#7A7A7A",
            "linestyle": "--",
            "linewidth": 1.0,
            "alpha": 0.7
        }
    ],

    "highlight_points": [
        {
            "column": "host_winner",
            "value": 1,
            "color": "#C44E52",
            "size": 100,
            "alpha": 1.0
        }
    ],

    "annotate_points": [
        {
            "x": 1930,
            "y": 1,
            "text": "Uruguay (1930)",
            "xytext": (6, -14),
            "fontsize": 8
        },
        {
            "x": 1934,
            "y": 2,
            "text": "Italy (1934)",
            "xytext": (6, 10),
            "fontsize": 8
        },
        {
            "x": 1966,
            "y": 3,
            "text": "England (1966)",
            "xytext": (6, -14),
            "fontsize": 8
        },
        {
            "x": 1974,
            "y": 4,
            "text": "West Germany (1974)",
            "xytext": (6, 10),
            "fontsize": 8
        },
        {
            "x": 1978,
            "y": 5,
            "text": "Argentina (1978)",
            "xytext": (6, -14),
            "fontsize": 8
        },
        {
            "x": 1998,
            "y": 6,
            "text": "France (1998)",
            "xytext": (8, 10),
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
    "title_fontsize": 22,
    "subtitle_fontsize": 12,
    "tick_label_fontsize": 10,
    "axis_label_fontsize": 10,
    "footer_fontsize": 10,

    "title_wrap_width": 40,
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
    "subtitle_y": 0.86,

    "footer_left_x": 0.10,
    "footer_right_x": 0.90,
    "footer_y": 0.045,

    "plot_top": 0.75,
    "plot_bottom": 0.19,
    "plot_left": 0.12,
    "plot_right": 0.90,

    "vertical_gridlines": False,

    # ---------------------------
    # OUTPUT
    # ---------------------------
    "dpi": 200,
    "output_file": "output/chart.png"
}
