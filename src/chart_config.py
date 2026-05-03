CHART_CONFIG = {
    "data_file": "data/forbes_most_valuable_sports_team",
    "data_format": "wide",
    "chart_type": "bar",

    "x_col": "Team",
    "y_col": "Value_USD_Billion",
    "series_col": None,
    "value_col": None,

    "title": "The top 15, stacked at the top",
    "subtitle": "The most valuable teams are tightly grouped at the top, led clearly by the Dallas Cowboys.",
    "source_text": "Source: Forbes",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_comparison",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 45,

    "x_label": "",
    "y_label": "Team value, USD billions",

    "x_axis": {
        "min": None,
        "max": None,
        "tick_interval": None,
        "format": None
    },

    "y_axis_min": 0,
    "y_axis_max": 14,
    "y_tick_interval": 2,
    "y_tick_format": "billions",

    "sort": {
        "by": "Value_USD_Billion",
        "ascending": False
    },
    "sort_descending": False,

    "filters": [
        {
            "column": "Rank",
            "operator": "<=",
            "value": 15
        }
    ],

    "line_width": 2.6,
    "marker_size": 60,
    "show_markers": False,
    "auto_end_labels": False,

    "bar_style": {
        "color": "#D9D9D9",
        "alpha": 0.9
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

    "reference_lines": [],

    "highlight_points": [
        {"Team": "Dallas Cowboys"}
    ],

    "annotate_points": [
        {
            "x": "Dallas Cowboys",
            "y": 13.0,
            "label": "$13bn",
            "xytext": (0, 8),
            "ha": "center",
            "va": "bottom",
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

    "title_fontsize": 22,
    "subtitle_fontsize": 12,
    "tick_label_fontsize": 8,
    "axis_label_fontsize": 10,
    "footer_fontsize": 10,

    "title_wrap_width": 40,
    "subtitle_wrap_width": 74,
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
    "plot_bottom": 0.20,
    "plot_left": 0.12,
    "plot_right": 0.90,

    "vertical_gridlines": False,

    "dpi": 200,
    "output_file": "output/forbes_06_top15_bar.png"
}
