CHART_CONFIG = {
    "data_file": "data/uk-mean-temperature.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Annual mean temperature (°C)",
    "y_col": "Year",
    "series_col": None,
    "value_col": None,

    "title": "The heat is moving up the table",
    "subtitle": "The UK’s ten warmest annual mean temperatures in this dataset all come from 2006 onwards, with 2025 sitting at the top.",
    "source_text": "Source: User-provided UK mean temperature dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_comparison",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_axis": {
        "min": 7.0,
        "max": 10.3,
        "tick_interval": 0.5,
        "format": ".1f"
    },

    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    "sort": "Annual mean temperature (°C)",
    "sort_descending": True,

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
            "value": 8.50,
            "label": "Series average: 8.5°C",
            "color": "#7A7A7A",
            "linewidth": 1.0,
            "linestyle": "--",
            "alpha": 0.7
        }
    ],

    "highlight_points": [
        {"Year": 2025},
        {"Year": 2022},
        {"Year": 2023},
        {"Year": 2024},
        {"Year": 2014}
    ],

    "annotate_points": [
        {
            "x": 10.09,
            "y": 2025,
            "label": "2025: warmest in the series",
            "xytext": (12, 0),
            "ha": "left"
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
    "subtitle_wrap_width": 80,

    "fig_width": 8.0,
    "fig_height": 8.0,

    "title_x": 0.10,
    "title_y": 0.88,
    "subtitle_x": 0.10,
    "subtitle_y": 0.825,

    "footer_left_x": 0.10,
    "footer_right_x": 0.90,
    "footer_y": 0.08,

    "plot_top": 0.70,
    "plot_bottom": 0.16,
    "plot_left": 0.18,
    "plot_right": 0.86,

    "dpi": 200,
    "output_file": "output/uk_mean_temperature_ranked.png"
}