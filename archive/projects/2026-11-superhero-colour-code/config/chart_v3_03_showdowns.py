# Alternative 3-chart editorial redesign. Costume coding is PROVISIONAL.
# Secondary-colour squares mirror at x=.326 (hero) and x=.652 (villain).
# Villain secondary text is right-anchored at x=.895, matching villain names.
# All information is generated from the real 24-character project dataset.
CHART_CONFIG = {
    "chart_type": "palette_story",
    "render_profile": "social_square",
    "fig_width": 8,
    "fig_height": 8,
    "dpi": 200,
    "x_col": None,
    "y_col": None,
    "series_col": None,
    "value_col": None,
    "sort": None,
    "sort_descending": False,
    "filters": [],
    "footer_left": "Adam Green | coffeetableviz",
    "source_text": "Source: Marvel/DC · curated 24",
    "data_file": "archive/projects/2026-11-superhero-colour-code/data/chart_v2_03_colour_twins.csv",
    "layout_variant": "comic_showdowns",
    "title": "Same paint. Different morals.",
    "subtitle": "Five matched colours. Five very different showdowns.",
    "output_file": "output/superhero_v3_03_showdowns.png",
}
