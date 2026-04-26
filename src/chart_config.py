CHART_CONFIG = {
    "data_file": "data/fuel_prices_low_low_quadrant.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Diesel_USD_per_litre",
    "y_col": "Country",
    "series_col": None,
    "value_col": None,

    "title": "Diesel prices where costs didn’t rise",
    "subtitle": "Countries where diesel prices were flat or falling, ranked by current price per litre.",
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
        "size": 70,
        "alpha": 0.9
    },

    "label_style": {
        "enabled": True,
        "label_col": "Diesel_USD_per_litre",
        "label_format": "${:.2f}",
        "position": "right",
        "fontsize": 8
    },

    "highlight_points": [],

    "output_file": "outputs/diesel_current_price_no_increase_dot.png"
}