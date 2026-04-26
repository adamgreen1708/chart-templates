CHART_CONFIG = {
    "data_file": "data/fuel_prices_low_low_quadrant.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Diesel_pct_change_y",
    "y_col": "Country",
    "series_col": None,
    "value_col": None,

    "title": "Flat isn’t the same as falling",
    "subtitle": "Countries where diesel prices were flat or falling, ranked by the size of the price change.",
    "source_text": "Source: User-provided fuel price dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_comparison",

    "filters": [
        {
            "column": "Diesel_pct_change_y",
            "operator": "<=",
            "value": 0
        }
    ],

    "sort": {
        "by": "Diesel_pct_change_y",
        "ascending": True
    },

    "x_label": "Diesel price change (%)",
    "y_label": "",

    "x_axis": {
        "min": -10,
        "max": 0,
        "tick_interval": 2,
        "format": "percent"
    },

    "dot_style": {
        "color": "#1F8FA8",
        "size": 65,
        "alpha": 0.75
    },

    "highlight_points": [],

    "label_style": {
        "enabled": True,
        "label_col": "Diesel_USD_per_litre",
        "label_format": "${:.2f}",
        "position": "right",
        "fontsize": 8
    },

    "output_file": "outputs/diesel_pct_change_no_increase_dot.png"
}