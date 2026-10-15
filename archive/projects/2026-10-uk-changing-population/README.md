# UK population: 2026–2050 — Coffeetableviz (draft)

Editorial story: **The UK is getting older. But not all at once.**

## Review status

The article copy and chart sequence were approved on 15 October 2026. This branch stages the copy and supporting verified ONS CSVs **for a draft PR**, not for publication.

**BLOCKER — approved images not yet committed to this branch. Do not merge.** The ChatGPT GitHub connection currently accepts UTF-8 text files but not direct upload of PNG bytes. The approved assets exist in the review pack shared in the ChatGPT conversation and must be copied unchanged into the following exact paths:

- \`site/assets/charts/uk_ageing_feature.png\` (single-scene, approved Westminster Bridge illustration)
- \`site/assets/charts/01_uk_age_profile_2026.png\`
- \`site/assets/charts/02_uk_age_shares_to_2050.png\`
- \`site/assets/charts/03_uk_85plus_growth_2050.png\`

The asset paths must be verified on the PR branch before marking ready for review. Until then the page references are broken.

## Data

- \`data/uk_population_by_age_2026.csv\`: one row per individual age category; UK 2024-based ONS principal projection, mid-2026.
- \`data/uk_population_projection_2026_2050.csv\`: yearly UK total, ages 0–14, ages 65+, ages 85+ and their shares, derived from the same principal scenario.

The associated Matplotlib rendering script and chart PNGs are in the approved local review ZIP but are not committed yet. The local renderer was not the production \`src/render_538.py\`; confirm QA against \`spec/538_template_rules.md\` and \`docs/chart_qa_checklist.md\` before merge.

## Source

- https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/datasets/z1zippedpopulationprojectionsdatafilesuk
- https://commonslibrary.parliament.uk/the-uks-changing-population/

Both 2026 and 2050 are projections. Historical dates are editorial reference points, not explanations for population peaks.
