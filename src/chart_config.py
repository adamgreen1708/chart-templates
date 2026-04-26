CHART_CONFIG = {
    "data_file": "data/fuel_prices_low_low_quadrant.csv",
    "data_format": "wide",
    "chart_type": "scatter",

    "x_col": "diesel_current_price",
    "y_col": "diesel_pct_change",
    "series_col": None,
    "value_col": None,

    "title": "Where diesel is cheapest, falls are sharper",
    "subtitle": "In markets with flat or falling fuel prices, lower diesel prices tend to coincide with larger percentage declines.",
    "source_text": "Source: User-provided fuel price dataset (low-low quadrant)",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "relationship",

    "x_label": "Current diesel price",
    "y_label": "Diesel price change (%)",

    "x_axis": {
        "min": None,
        "max": None,
        "tick_interval": None,
        "format": "currency"
    },

    "y_axis": {
        "min": -10,
        "max": 0,
        "tick_interval": 2,
        "format": "percent"
    },

    "reference_lines": [
        {
            "axis": "y",
            "value": 0,
            "label": "No price increase",
            "color": "#7A7A7A",
            "linestyle": "--"
        }
    ],

    "highlight_points": [],

    "point_style": {
        "color": "#1F8FA8",
        "alpha": 0.75,
        "size": 55
    },

    "highlight_style": {
        "color": "#C44E52",
        "alpha": 1.0,
        "size": 90
    },

    "label_style": {
        "enabled": True,
        "label_col": "country",
        "auto_label": "all",
        "fontsize": 8
    },

    "output_file": "outputs/diesel_price_vs_change_low_quadrant.png"
}