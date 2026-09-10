CHART_CONFIG = {
    "data_file": "archive/projects/2026-09-james-bond-villains/data/bond_villains_chart_04_imdb_companion.csv",
    "data_format": "wide",
    "chart_type": "dot",
    "orientation": None,

    "x_col": "imdb_rating",
    "y_col": "villain_label",
    "series_col": None,
    "value_col": None,

    "filters": [],

    "title": "Le Chiffre got the best Bond film to be evil in",
    "subtitle": "IMDb rating of the Bond film featuring each film's first-listed villain. Film ratings are context, not villain scores.",
    "source_text": "Source: IMDb title pages, snapshot 9 Sep 2026",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_comparison",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "all",

    "x_is_datetime": False,
    "x_tick_rotation": 0,
    "x_label": "IMDb film rating",
    "y_label": "",
    "x_margin": 0.08,

    "x_axis": {
        "min": 5.9,
        "max": 8.2,
        "tick_interval": 0.5,
        "format": ".1f"
    },

    "y_axis": {
        "min": None,
        "max": None,
        "tick_interval": None,
        "format": None
    },
    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    "sort": {
        "by": "imdb_rating",
        "ascending": False
    },
    "sort_descending": False,

    "line_width": 2.6,
    "marker_size": 60,
    "show_markers": True,
    "auto_end_labels": False,

    "dot_style": {
        "color": "#D9D9D9",
        "size": 50,
        "alpha": 0.72
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
        "color": "#C44E52",
        "size": 92,
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

    "trend_line": {
        "enabled": False,
        "color": "#7A7A7A",
        "linewidth": 1.4,
        "linestyle": "-",
        "alpha": 0.8
    },

    "highlight_points": [
        {"villain_name": "Le Chiffre"}
    ],

    "annotate_points": [],
    "end_labels": [],

    "label_style": {
        "enabled": True,
        "label_col": "imdb_rating",
        "label_format": "{:.1f}",
        "position": "right",
        "fontsize": 7
    },

    "title_fontsize": 20,
    "subtitle_fontsize": 10,
    "tick_label_fontsize": 7,
    "axis_label_fontsize": 9,
    "footer_fontsize": 9,

    "title_wrap_width": 42,
    "subtitle_wrap_width": 76,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,

    "fig_width": 8.0,
    "fig_height": 8.0,

    "title_x": 0.08,
    "title_y": 0.94,
    "subtitle_x": 0.08,
    "subtitle_y": 0.855,

    "footer_left_x": 0.08,
    "footer_right_x": 0.92,
    "footer_y": 0.07,

    "plot_top": 0.74,
    "plot_bottom": 0.14,
    "plot_left": 0.46,
    "plot_right": 0.91,

    "vertical_gridlines": False,

    "dpi": 200,
    "output_file": "output/bond_villains_imdb_companion.png"
}
