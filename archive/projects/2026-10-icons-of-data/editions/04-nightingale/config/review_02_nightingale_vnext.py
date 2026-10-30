"""Review-only Nightingale replacement, awaiting author visual approval.

The intended production config will be promoted to the normal archive
project config path and rendered to the approved site image only after sign-off.
"""
CHART_CONFIG = {
    "data_file": "archive/projects/2026-10-icons-of-data/editions/04-nightingale/data/nightingale_24_months.csv",
    "data_format": "wide",
    "chart_type": "nightingale_rates",
    "x_col": "Date",
    "y_col": "Disease.rate",
    "series_col": None,
    "value_col": None,
    "filters": [],
    "render_profile": "social_square",
    "profile_overrides": {},
    "title": "The biggest problem was blue.",
    "subtitle": "Annualised deaths per 1,000 soldiers · 1854–56",
    "source_text": "Source: HistData · 24 months",
    "footer_left": "Adam Green | coffeetableviz",
    "fig_width": 8.0,
    "fig_height": 8.0,
    "dpi": 200,
    "output_file": "output/nightingale_vnext_preview.png",
}
