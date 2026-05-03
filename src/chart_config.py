CHART_CONFIG = {
    "data_file": "data/forbes_most_valuable_sports_team",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Value_USD_Billion",
    "y_col": "Sport",
    "series_col": None,
    "value_col": None,

    "title": "Different sports, different economics",
    "subtitle": "NFL teams cluster tightly at high values, while football and the NBA show wider spreads and higher ceilings.",
    "source_text": "Source: Forbes",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "comparison",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_label": "Team value, USD billions",
    "y_label": "Sport",

    "x_axis": {
        "min": 5,
        "max": 14,
        "tick_interval": 1,
        "format": "billions"
    },

    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    "sort": None,
    "sort_descending": False,

    "line_width": 2.6,
    "marker_size": 60,
    "show_markers": True,
    "auto_end_labels": False,

    "dot_style": {
        "color": "#D9D9D9",
        "size": 42,
        "alpha": 0.55
    },

    "highlight_style": {
        "color": "#1F8FA8",
        "size": 70,
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

    # Highlight sports groups for emphasis
    "highlight_points": [
        {"Sport": "American football"},
        {"Sport": "Basketball"}
    ],

    "annotate_points": [
        {
            "x": 10.5,
            "y": "American football",
            "label": "NFL: high floor, tight spread",
            "xytext": (8, 0),
            "ha": "left",
            "va": "center",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None
        },
        {
            "x": 10.0,
            "y": "Basketball",
            "label": "NBA: higher peaks",
            "xytext": (8, 0),
            "ha": "left",
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
    "tick_label_fontsize": 10,
    "axis_label_fontsize": 10,
    "footer_fontsize": 10,

    "title_wrap_width": 40,
    "subtitle_wrap_width": 74,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,

    "fig_width": 8.0,
    "fig_height": 6.5,

    "title_x": 0.10,
    "title_y": 0.92,
    "subtitle_x": 0.10,
    "subtitle_y": 0.86,

    "footer_left_x": 0.10,
    "footer_right_x": 0.90,
    "footer_y": 0.08,

    "plot_top": 0.75,
    "plot_bottom": 0.18,
    "plot_left": 0.20,
    "plot_right": 0.90,

    "vertical_gridlines": True,

    "dpi": 200,
    "output_file": "output/forbes_05_sport_structure.png"
}