CHART_CONFIG = {
    "data_file": "data/self-reported-trust-attitudes.csv",
    "data_format": "long",
    "chart_type": "line",
    "title": "Trust collapsed — then quietly recovered",
    "subtitle": "UK trust in others fell sharply after the 1990s but has since rebounded to a modern high",
    "source_text": "Source: Our World in Data",
    "footer_left": "Adam Green | coffeetableviz",
    "vertical_gridlines": True,
    "x_col": "Year",
    "y_col": None,
    "series_col": "Entity",
    "value_col": "Trust in others",
    "xlim_right_pad": 1,
    "sort_descending": False,
    "series_style": {
        "United Kingdom": {"color": "#1F8FA8", "linewidth": 2.5}
    },
    "series_overrides": {},
    "reference_lines": [],
    "highlight_points": [
        {
            "x": 1998,
            "y": 30.44983,
            "label": "Sharp drop begins",
            "color": "#C44E52",
            "dx": 0,
            "dy": -15,
            "ha": "center",
            "size": 9
        },
        {
            "x": 2022,
            "y": 43.31179,
            "label": "Highest level recorded",
            "color": "#C44E52",
            "dx": 0,
            "dy": 10,
            "ha": "center",
            "size": 9
        }
    ],
    "auto_end_labels": True,
    "end_labels": []
}