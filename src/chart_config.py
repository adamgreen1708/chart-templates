CHART_CONFIG = {
    "data_file": "data/fuel_prices_low_low_quadrant.csv",
    "data_format": "wide",
    "chart_type": "bar",

    "x_col": "Country",
    "y_col": "Diesel_USD_per_litre",
    "series_col": None,
    "value_col": None,

    "title": "Where diesel prices did not rise",
    "subtitle": "Current diesel price in countries where diesel price change was zero or negative.",
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

    "x_label": "",
    "y_label": "Current diesel price, USD per litre",

    "y_axis": {
        "min": 0,
        "max": None,
        "tick_interval": None,
        "format": "currency"
    },

    "bar_style": {
        "color": "#1F8FA8",
        "alpha": 0.9
    },

    "label_style": {
        "enabled": True,
        "label_col": "Diesel_USD_per_litre",
        "label_format": "${:.2f}",
        "position": "end",
        "fontsize": 8
    },

    "highlight_points": [],

    "output_file": "outputs/diesel_current_price_no_increase_bar.png"
}