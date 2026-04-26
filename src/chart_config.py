CHART_CONFIG = {
    "data_file": "data/fuel_prices_diesel_pct_leq_zero.csv",
    "data_format": "wide",
    "chart_type": "dot",

    "x_col": "Diesel_pct_change_y",
    "y_col": "Country",
    "series_col": None,
    "value_col": None,

    "title": "Only a handful of countries saw diesel prices fall",
    "subtitle": "Most saw no change at all — with just a few experiencing meaningful declines.",
    "source_text": "Source: User-provided fuel price dataset",
    "footer_left": "Adam Green | coffeetableviz",

    "story_angle": "ranked_comparison",

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
        "alpha": 0.7
    },

    "highlight_points": [
        {
            "x": -8.2,
            "y": "Russia",
            "label": "Russia: sharpest fall",
            "color": "#C44E52"
        },
        {
            "x": -3.1,
            "y": "Barbados",
            "label": "Barbados: notable drop",
            "color": "#C44E52"
        },
        {
            "x": 0,
            "y": "Algeria",
            "label": "Many countries: no change",
            "color": "#C44E52"
        }
    ],

    "highlight_style": {
        "color": "#C44E52",
        "size": 90,
        "alpha": 1.0
    },

    "label_style": {
        "enabled": True,
        "label_col": "Diesel_USD_per_litre",
        "label_format": "${:.2f}",
        "position": "right",
        "fontsize": 8
    },

    "reference_lines": [
        {
            "axis": "x",
            "value": 0,
            "label": "No change",
            "color": "#7A7A7A",
            "linestyle": "--"
        }
    ],

    "output_file": "outputs/diesel_pct_change_filtered_dot.png"
}