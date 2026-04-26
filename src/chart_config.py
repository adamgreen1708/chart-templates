CHART_CONFIG = {
    "data_file": "data/fuel_prices_low_low_quadrant.csv",
    "data_format": "wide",
    "chart_type": "scatter",

    "x_col": "Diesel_USD_per_litre",
    "y_col": "Diesel_pct_change_y",
    "series_col": None,
    "value_col": None,

    "title": "Cheap diesel didn’t mean small falls",
    "subtitle": "Among countries where both fuel prices fell or stayed flat, current diesel price and diesel percentage change do not move neatly together.",
    "source_text": "Source: User-provided fuel price dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "relationship",

    "x_label": "Current diesel price, USD per litre",
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
            "label": "No diesel price increase",
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

    "label_style": {
        "enabled": True,
        "label_col": "Country",
        "auto_label": "all",
        "fontsize": 8
    },

    "output_file": "outputs/diesel_price_vs_pct_change_low_quadrant.png"
}