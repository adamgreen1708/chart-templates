CHART_CONFIG = {
    "data_file": "data/arsenal_vs_top10.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Points",
    "y_col": "Opponent",
    "series_col": None,
    "value_col": None,

    "title": "Arsenal handled the top half unevenly",
    "subtitle": "Ordered by final league position, Arsenal took six points from Brighton but only one from City and Liverpool.",
    "source_text": "Source: Football-Data.co.uk, Premier League 2025/26 results",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_comparison",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_axis": {
        "min": 0,
        "max": 7,
        "tick_interval": 1,
        "format": None
    },

    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    "sort": {
        "by": "FinalPosition",
        "ascending": True
    },
    "sort_descending": False,

    "line_width": 2.6,
    "marker_size": 60,
    "show_markers": True,
    "auto_end_labels": False,

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

    "reference_lines": [],

    "highlight_points": [
        {"column": "Opponent", "value": "Manchester City"},
        {"column": "Opponent", "value": "Liverpool"},
        {"column": "Opponent", "value": "Brighton & Hove Albion"}
    ],

    "annotate_points": [],

    "end_labels": [],

    "label_style": {
        "enabled": True,
        "label_col": "Points",
        "label_format": "{:.0f}",
        "position": "right",
        "fontsize": 8
    },

    "title_fontsize": 22,
    "subtitle_fontsize": 12,
    "tick_label_fontsize": 10,
    "axis_label_fontsize": 10,
    "footer_fontsize": 10,

    "title_wrap_width": 40,
    "subtitle_wrap_width": 72,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,

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
    "plot_left": 0.30,
    "plot_right": 0.88,

    "vertical_gridlines": False,

    "dpi": 200,
    "output_file": "output/chart.png"
}