CHART_CONFIG = {
    "data_file": "data/uk_mean_temperature_top20.csv",
    "data_format": "wide",
    "chart_type": "bar",

    "x_col": "Annual mean temperature (°C)",
    "y_col": "Year",
    "series_col": None,
    "value_col": None,

    "title": "The UK’s warmest years are all recent",
    "subtitle": "The top 10 warmest years by annual mean temperature all come from the 21st century, with 2025 at the top.",
    "source_text": "Source: https://www.metoffice.gov.uk",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_comparison",
    "focus_series": None,
    "secondary_series": None,
    "label_strategy": "focus_only",

    "x_is_datetime": False,
    "x_tick_rotation": 0,

    "x_axis": {
        "min": 8.5,
        "max": 10.5,
        "tick_interval": 0.5,
        "format": ".1f"
    },

    "y_axis_min": None,
    "y_axis_max": None,
    "y_tick_interval": None,
    "y_tick_format": None,

    "sort": {
        "by": "Annual mean temperature (°C)",
        "ascending": False
    },
    "sort_descending": False,

    "filters": [
        {
            "column": "Rank",
            "operator": "<=",
            "value": 10
        }
    ],

    "line_width": 2.6,
    "marker_size": 60,
    "show_markers": False,
    "auto_end_labels": False,

    "bar_style": {
        "color": "#D9D9D9",
        "alpha": 0.85
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

    "reference_lines": [
        {
            "axis": "x",
            "value": 8.5,
            "label": "Series average",
            "rotation": 0,
            "color": "#7A7A7A",
            "linewidth": 1.0,
            "linestyle": "--",
            "alpha": 0.7
        }
    ],

    "highlight_points": [
        {"Year": 2025}
    ],

    "annotate_points": [
        {
            "x": 10.09,
            "y": 2025,
            "label": "Warmest year",
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
    "tick_label_fontsize": 10,
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
    "plot_left": 0.20,
    "plot_right": 0.90,

    "vertical_gridlines": False,

    "dpi": 200,
    "output_file": "output/uk_temperature_top10_horizontal_bar.png"
}