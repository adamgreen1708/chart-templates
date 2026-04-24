CHART_CONFIG = {
    "data_file": "data/fuel_prices_trimmed_correct_pct_clean.csv",
    "data_format": "wide",
    "chart_type": "dot",
    "output_slug": "fuel_price_quadrants",

    "x_col": "Diesel_minus_gasoline_USD_per_litre",
    "y_col": "Country",
    "series_col": None,
    "value_col": None,

    "title": "Diesel carries the pain",
    "subtitle": "In many countries diesel was markedly more expensive than petrol, with Singapore showing the biggest gap.",
    "source_text": "Source: GlobalPetrolPrices.com, user-compiled dataset",
    "footer_left": "Adam Green | coffeetableviz",
    "footer_right": "20 Apr 2026",

    "story_angle": "ranking",

    "focus_series": None,
    "secondary_series": None,

    "sort_by": "Diesel_minus_gasoline_USD_per_litre",
    "sort_order": "descending",
    "limit": 25,

    "point_style": {
        "color": "#1F8FA8",
        "alpha": 0.65,
        "size": 48
    },

    "highlight_style": {
        "color": "#C44E52",
        "alpha": 1.0,
        "size": 90,
        "zorder": 6
    },

    "reference_lines": [
        {
            "axis": "x",
            "value": 0,
            "label": "Diesel = petrol",
            "color": "#B8B8B8",
            "linewidth": 1.0,
            "linestyle": "--",
            "alpha": 0.8
        }
    ],

    "highlight_points": [
        {
            "x": 0.847,
            "y": "Singapore",
            "label": "Singapore"
        },
        {
            "x": 0.454,
            "y": "United Kingdom",
            "label": "United Kingdom"
        }
    ],

    "annotate_points": [
        {
            "x": 0.847,
            "y": "Singapore",
            "text": "Singapore: diesel +$0.85/L",
            "xytext": [18, 0],
            "ha": "left"
        },
        {
            "x": 0.454,
            "y": "United Kingdom",
            "text": "UK: +$0.45/L",
            "xytext": [18, 0],
            "ha": "left"
        }
    ],

    "x_axis_label": "Diesel premium over gasoline, USD per litre",
    "y_axis_label": "",

    "x_tick_format": "${x:.2f}",
    "y_tick_format": "{x}",

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
    "plot_left": 0.24,
    "plot_right": 0.89,

    "plot_padding": {
        "x": 0.08,
        "y": 0.04
    }
}