CHART_CONFIG = {
    "data_file": "fuel_prices_low_low_quadrant.csv",
    "data_format": "wide",
    "chart_type": "scatter",

    "x_col": "Diesel current price",
    "y_col": "Diesel pct change",
    "series_col": None,
    "value_col": None,

    "title": "Diesel’s quiet corner",
    "subtitle": "Among markets where both petrol and diesel price changes are zero or negative, this shows whether cheaper diesel also came with bigger falls.",
    "source_text": "Source: User-provided fuel price dataset",
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

    "highlight_points": [
        {
            "label_col": "Country",
            "match_col": "Country",
            "match_value": "United Kingdom",
            "label": "UK",
            "color": "#C44E52"
        }
    ],

    "reference_lines": [
        {
            "axis": "y",
            "value": 0,
            "label": "No diesel price rise",
            "color": "#7A7A7A",
            "linestyle": "--"
        }
    ],

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
        "label_col": "Country",
        "auto_label": "highlight_only",
        "fontsize": 9
    },

    "output_file": "outputs/diesel-current-price-vs-pct-change.png"
}