CHART_CONFIG = {
    "data_file": "data/forbes_most_valuable_sports_team",
    "data_format": "wide",
    "chart_type": "bar",
    "orientation": "horizontal",

    "x_col": "Value_USD_Billion",
    "y_col": "Team",
    "series_col": None,
    "value_col": None,

    "title": "The top 15, stacked at the top",
    "subtitle": "The Cowboys sit clear of a chasing pack packed with NFL and NBA money.",
    "source_text": "Source: Forbes",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_comparison",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_label": "Team value, USD billions",
    "y_label": "",

    "x_axis": {
        "min": 0,
        "max": 14,
        "tick_interval": 2,
        "format": "billions"
    },

    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    "sort": {
        "by": "Value_USD_Billion",
        "ascending": True
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

    "highlight_points": [
        {"Team": "Dallas Cowboys"}
    ],

    "reference_lines": [],

    "annotate_points": [
        {
            "x": 13.0,
            "y": "Dallas Cowboys",
            "label": "Dallas Cowboys: $13bn",
            "xytext": (-8, 0),
            "ha": "right",
            "va": "center",
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
    "tick_label_fontsize": 9,
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
    "plot_bottom": 0.14,
    "plot_left": 0.34,
    "plot_right": 0.90,

    "vertical_gridlines": True,

    "dpi": 200,
    "output_file": "output/forbes_06_top15_bar.png"
}