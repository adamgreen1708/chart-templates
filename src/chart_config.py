CHART_CONFIG = {
    "data_file": "data/fuel_prices_low_low_quadrant.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Diesel_USD_per_litre",
    "y_col": "Country",
    "series_col": None,
    "value_col": None,

    "title": "Flat isn’t the same as falling",
    "subtitle": "Among countries where diesel prices didn’t rise, those with no change stand apart from those with actual declines.",
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
        "by": "Diesel_USD_per_litre",
        "ascending": False
    },

    "x_label": "Current diesel price, USD per litre",
    "y_label": "",

    "x_axis": {
        "min": 0,
        "max": None,
        "tick_interval": None,
        "format": "currency"
    },

    "dot_style": {
        "color": "#1F8FA8",
        "size": 65,
        "alpha": 0.7
    },

    "highlight_points": [
        {
            "label_col": "Country",
            "match_col": "Diesel_pct_change_y",
            "match_value": 0,
            "label": "No change",
            "color": "#C44E52"
        }
    ],

    "highlight_style": {
        "color": "#C44E52",
        "size": 85,
        "alpha": 1.0
    },

    "label_style": {
        "enabled": True,
        "label_col": "Diesel_USD_per_litre",
        "label_format": "${:.2f}",
        "position": "right",
        "fontsize": 8
    },

    "output_file": "outputs/diesel_current_price_zero_vs_negative_dot.png"
}