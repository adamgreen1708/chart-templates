CHART_CONFIG = {
    "data_file": "data/fuel_prices_trimmed_correct_pct_clean.csv",
    "data_format": "wide",
    "chart_type": "scatter",
    "output_slug": "diesel_rose_harder_than_petrol",

    "x_col": "Gasoline_pct_change_y",
    "y_col": "Diesel_pct_change_y",
    "series_col": None,
    "value_col": None,

    "title": "Diesel rose harder",
    "subtitle": "Most countries sit above parity, showing diesel prices often rose faster than petrol during the shock.",
    "source_text": "Source: GlobalPetrolPrices.com, user-compiled dataset",
    "footer_left": "Adam Green | coffeetableviz",
    "footer_right": "Change from 23 Feb to 20 Apr 2026",

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
        "linewidth": 1.5,
        "alpha": 0.65
    },

    "reference_lines": [
        {
            "axis": "diagonal",
            "value": "y_equals_x",
            "label": "Diesel = petrol rise",
            "color": "#7A7A7A",
            "linewidth": 1.2,
            "linestyle": "--",
            "alpha": 0.85
        }
    ],

    "axis_equal": True,
    "x_limits": [-10, 170],
    "y_limits": [-10, 170],

    "highlight_points": [
        {
            "x": 101.1,
            "y": 161.4,
            "label": "Burma (Myanmar)"
        },
        {
            "x": 35.8,
            "y": 149.7,
            "label": "Laos"
        },
        {
            "x": 57.6,
            "y": 118.4,
            "label": "Philippines"
        },
        {
            "x": 19.7,
            "y": 35.2,
            "label": "United Kingdom"
        }
    ],

    "annotate_points": [
        {
            "x": 101.1,
            "y": 161.4,
            "text": "Myanmar: +161% diesel",
            "xytext": [-12, -12],
            "ha": "right"
        },
        {
            "x": 35.8,
            "y": 149.7,
            "text": "Laos: diesel shock",
            "xytext": [18, 0],
            "ha": "left"
        },
        {
            "x": 19.7,
            "y": 35.2,
            "text": "UK above parity",
            "xytext": [18, -10],
            "ha": "left"
        }
    ],

    "x_axis_label": "Gasoline price change (%)",
    "y_axis_label": "Diesel price change (%)",

    "x_tick_format": "{x:.0f}%",
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