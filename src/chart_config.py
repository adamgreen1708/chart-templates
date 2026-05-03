CHART_CONFIG = {
    "data_file": "data/forbes_most_valuable_sports_team_clean.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Rank_Change",
    "y_col": "Team",
    "series_col": None,
    "value_col": None,

    "title": "Movement was rare",
    "subtitle": "Most teams barely shifted, but Kansas City climbed seven places while Barcelona slid 22.",
    "source_text": "Source: Forbes",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_comparison",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_label": "Rank change, places gained or lost",
    "y_label": "",

    "x_axis": {
        "min": -25,
        "max": 10,
        "tick_interval": 5,
        "format": ".0f"
    },

    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    "sort": {
        "by": "Rank_Change",
        "ascending": True
    },
    "sort_descending": False,

    "line_width": 2.6,
    "marker_size": 60,
    "show_markers": True,
    "auto_end_labels": False,

    "dot_style": {
        "color": "#D9D9D9",
        "size": 42,
        "alpha": 0.60
    },

    "highlight_style": {
        "color": "#C44E52",
        "size": 76,
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

    "reference_lines": [
        {
            "axis": "x",
            "value": 0,
            "label": "No rank change",
            "rotation": 0,
            "color": "#7A7A7A",
            "linewidth": 1.0,
            "linestyle": "--",
            "alpha": 0.7
        }
    ],

    "highlight_points": [
        {"Team": "Kansas City Chiefs"},
        {"Team": "FC Barcelona"},
        {"Team": "Liverpool"}
    ],

    "annotate_points": [
        {
            "x": 7,
            "y": "Kansas City Chiefs",
            "label": "Chiefs: +7",
            "xytext": (8, 0),
            "ha": "left",
            "va": "center",
            "fontsize": 8,
            "color": "#333333",
            "arrowprops": None
        },
        {
            "x": -22,
            "y": "FC Barcelona",
            "label": "Barcelona: -22",
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
    "tick_label_fontsize": 8,
    "axis_label_fontsize": 10,
    "footer_fontsize": 10,

    "title_wrap_width": 40,
    "subtitle_wrap_width": 74,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,

    "fig_width": 8.0,
    "fig_height": 10.0,

    "title_x": 0.10,
    "title_y": 0.94,
    "subtitle_x": 0.10,
    "subtitle_y": 0.89,

    "footer_left_x": 0.10,
    "footer_right_x": 0.90,
    "footer_y": 0.06,

    "plot_top": 0.80,
    "plot_bottom": 0.12,
    "plot_left": 0.34,
    "plot_right": 0.90,

    "vertical_gridlines": True,

    "dpi": 200,
    "output_file": "output/forbes_03_rank_movement.png"
}