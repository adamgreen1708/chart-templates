CHART_CONFIG = {
    # ---------------------------
    # DATA
    # ---------------------------
    "data_file": "data/world_cup_chart_03_home_winners.csv",
    "data_format": "wide",
    "chart_type": "scatter",

    "x_col": "year",
    "y_col": "host_winner",
    "series_col": None,
    "value_col": None,

    # ---------------------------
    # STORY
    # ---------------------------
    "title": "Home advantage is rare, but it sticks",
    "subtitle": "Only six World Cup finals ended with the host nation lifting the trophy.",
    "source_text": "Source: Wikipedia- List of FIFA World Cup finals",
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
    "x_label": "World Cup year",
    "y_label": "Host nation lifted the trophy (1=yes)",

    "x_axis": {
        "min": 1928,
        "max": 2024,
        "tick_interval": 8,
        "format": None
    },

    "y_axis_min": -0.15,
    "y_axis_max": 1.15,
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
    "line_width": 2.6,
    "marker_size": 60,
    "show_markers": True,
    "auto_end_labels": False,

    # ---------------------------
    # STYLING
    # ---------------------------
    "dot_style": {
        "color": "#D9D9D9",
        "size": 52,
        "alpha": 0.75
    },

    "highlight_style": {
        "color": "#C44E52",
        "size": 92,
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
            "axis": "y",
            "value": 0,
            "label": "No",
            "color": "#B0B0B0",
            "linestyle": "--",
            "linewidth": 0.8,
            "alpha": 0.8
        },
        {
            "axis": "y",
            "value": 1,
            "label": "Yes",
            "color": "#B0B0B0",
            "linestyle": "--",
            "linewidth": 0.8,
            "alpha": 0.8
        }
    ],

    "highlight_points": [
        {"column": "host_winner", "value": 1}
    ],

    "annotate_points": [
        {
            "x": 1930,
            "y": 1,
            "text": "Uruguay",
            "xytext": (6, 10),
            "fontsize": 8
        },
        {
            "x": 1934,
            "y": 1,
            "text": "Italy",
            "xytext": (6, -14),
            "fontsize": 8
        },
        {
            "x": 1966,
            "y": 1,
            "text": "England",
            "xytext": (6, 10),
            "fontsize": 8
        },
        {
            "x": 1974,
            "y": 1,
            "text": "West Germany",
            "xytext": (6, -14),
            "fontsize": 8
        },
        {
            "x": 1978,
            "y": 1,
            "text": "Argentina",
            "xytext": (6, 10),
            "fontsize": 8
        },
        {
            "x": 1998,
            "y": 1,
            "text": "France",
            "xytext": (6, -14),
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
    "output_file": "output/chart.png"
}