CHART_CONFIG = {
    "data_file": "data/fuel_prices_diesel_pct_leq_zero.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Diesel_pct_change_y",
    "y_col": "Country",
    "series_col": None,
    "value_col": None,

    "title": "Flat wasn’t falling",
    "subtitle": "Most countries with no diesel price rise saw no change at all, while Russia and Barbados were the clear fallers.",
    "source_text": "Source: User-provided fuel price dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_comparison",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_axis": {
        "min": -10,
        "max": 0.5,
        "tick_interval": 2,
        "format": "percent"
    },

    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    "line_width": 2.6,
    "marker_size": 58,
    "show_markers": True,
    "auto_end_labels": False,
    "sort_descending": False,

    "sort": {
        "by": "Diesel_pct_change_y",
        "ascending": True
    },

    "reference_lines": [
        {
            "axis": "x",
            "value": 0,
            "label": "No change",
            "color": "#7A7A7A",
            "linestyle": "--",
            "linewidth": 1.0
        }
    ],

    "highlight_points": [
        {
            "x": -8.2,
            "y": "Russia",
            "label": "Russia: -8.2%",
            "color": "#C44E52"
        },
        {
            "x": -3.1,
            "y": "Barbados",
            "label": "Barbados: -3.1%",
            "color": "#C44E52"
        }
    ],

    "annotate_points": [],
    "end_labels": [],

    "dot_style": {
        "color": "#1F8FA8",
        "size": 58,
        "alpha": 0.75
    },

    "highlight_style": {
        "color": "#C44E52",
        "size": 82,
        "alpha": 1.0
    },

    "label_style": {
        "enabled": False,
        "label_col": "Diesel_pct_change_y",
        "label_format": "{:.1f}%",
        "position": "right",
        "fontsize": 8
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

    "fig_width": 8.0,
    "fig_height": 8.0,
    "dpi": 200,

    "title_fontsize": 22,
    "subtitle_fontsize": 12,
    "tick_label_fontsize": 10,
    "axis_label_fontsize": 10,
    "footer_fontsize": 10,

    "title_wrap_width": 42,
    "subtitle_wrap_width": 82,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,

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

    "output_file": "output/diesel_pct_change_filtered_dot.png"
}