CHART_CONFIG = {
    "data_file": "data/fuel_prices_trimmed_correct_pct_clean.csv",
    "data_format": "wide",
    "chart_type": "dot",
    "output_slug": "diesel_rose_harder",

    "x_col": "Diesel_pct_change_minus_gasoline_pct_change",
    "y_col": "Country",
    "series_col": None,
    "value_col": None,

    "title": "Diesel rose harder",
    "subtitle": "In many countries diesel prices increased faster than petrol between Feb and Apr 2026.",
    "source_text": "Source: GlobalPetrolPrices.com, user-compiled dataset",
    "footer_left": "Adam Green | coffeetableviz",
    "footer_right": "20 Apr 2026; change since 23 Feb",

    "story_angle": "ranking",

    "sort_by": "Diesel_pct_change_minus_gasoline_pct_change",
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
            "label": "Equal change",
            "color": "#B8B8B8",
            "linewidth": 1.0,
            "linestyle": "--",
            "alpha": 0.8
        }
    ],

    "highlight_points": [],

    "annotate_points": [],

    "x_axis_label": "Diesel rise minus petrol rise (percentage points)",
    "y_axis_label": "",

    "x_tick_format": "{x:.0f}pp",
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
    "title_y": 0.93,
    "subtitle_x": 0.11,
    "subtitle_y": 0.855,

    "footer_left_x": 0.11,
    "footer_right_x": 0.89,
    "footer_y": 0.075,

    "plot_top": 0.75,
    "plot_bottom": 0.17,
    "plot_left": 0.24,
    "plot_right": 0.89,

    "plot_padding": {
        "x": 0.08,
        "y": 0.04
    }
}
