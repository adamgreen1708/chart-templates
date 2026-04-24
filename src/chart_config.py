CHART_CONFIG = {
    "data_file": "data/fuel_prices_trimmed_correct_pct_clean.csv",
    "data_format": "wide",
    "chart_type": "scatter",

    "x_col": "Gasoline_USD_per_litre",
    "y_col": "Gasoline_pct_change_y",
    "series_col": None,
    "value_col": None,

    "title": "Cheap fuel still spiked",
    "subtitle": "Countries with lower petrol prices were not protected from sharp rises between 23 Feb and 20 Apr 2026. Malaysia stands out as the biggest break from the trend.",
    "source_text": "Source: GlobalPetrolPrices.com, user-compiled dataset",
    "footer_left": "Adam Green | coffeetableviz",
    "footer_right": "20 Apr 2026 prices; change since 23 Feb 2026",

    "story_angle": "relationship",

    "focus_series": None,
    "secondary_series": None,

    "context_style": {
        "color": "#D9D9D9",
        "linewidth": 0.8,
        "alpha": 0.25,
        "zorder": 1
    },

    "focus_style": {
        "color": "#1F8FA8",
        "linewidth": 3.5,
        "alpha": 1.0,
        "zorder": 5
    },

    "secondary_style": {
        "color": "#7A7A7A",
        "linewidth": 2.0,
        "alpha": 0.9,
        "zorder": 4
    },

    "point_style": {
        "color": "#1F8FA8",
        "alpha": 0.55,
        "size": 42
    },

    "highlight_style": {
        "color": "#C44E52",
        "alpha": 1.0,
        "size": 95,
        "zorder": 6
    },

    "regression_line": {
        "show": True,
        "color": "#7A7A7A",
        "linewidth": 1.6,
        "alpha": 0.75
    },

    "reference_lines": [
        {
            "axis": "y",
            "value": 0,
            "label": "No change",
            "color": "#B8B8B8",
            "linewidth": 1.0,
            "linestyle": "--",
            "alpha": 0.8
        }
    ],

    "highlight_points": [
        {
            "x": 1.017,
            "y": 58.3,
            "label": "Malaysia"
        }
    ],

    "annotate_points": [
        {
            "x": 1.017,
            "y": 58.3,
            "text": "Malaysia: +58.3%",
            "xytext": [18, 16],
            "ha": "left"
        }
    ],

    "x_axis_label": "Gasoline price, USD per litre",
    "y_axis_label": "Gasoline price change since 23 Feb 2026",

    "x_tick_format": "${x:.2f}",
    "y_tick_format": "{x:.0f}%",

    "fig_width": 8.0,
    "fig_height": 8.0,

    "title_fontsize": 22,
    "subtitle_fontsize": 13,
    "tick_label_fontsize": 12,
    "footer_fontsize": 10,

    "title_wrap_width": 30,
    "subtitle_wrap_width": 58,
    "title_max_lines": 2,
    "subtitle_max_lines": 2,

    "title_x": 0.11,
    "title_y": 0.94,
    "subtitle_x": 0.11,
    "subtitle_y": 0.865,

    "footer_left_x": 0.11,
    "footer_right_x": 0.89,
    "footer_y": 0.075,

    "plot_top": 0.70,
    "plot_bottom": 0.16,
    "plot_left": 0.11,
    "plot_right": 0.89,

    "plot_padding": {
        "x": 0.08,
        "y": 0.10
    }
}