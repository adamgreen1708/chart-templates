# Dr Seuss word invention — QA report

## Result

**PASS — ready for Adam visual/editorial review.**

The first three-chart build was rendered through the repository's archived-project workflow and inspected as finished PNG output.

Final render workflow run: `36187074206` — success.

## Data QA

- Dataset path exists: `data/dr_seuss_word_invention_metrics.csv`.
- 12 aggregate observations are present.
- No mock data or invented source values are used.
- Part-of-speech published shares: 61%, 27%, 5%, 4%, 3% — sum = 100%.
- Sound-influence published shares: 48%, 19%, 17%, 16% — sum = 100%.
- Derived noun share: 61% + 27% = 88%.
- Derived rhyme/alliteration influence: 48% + 19% + 17% = 84%.
- Z share comparison: 4.42% / 0.10% = 44.2×.
- The paper's rounded percentages remain labelled as such in the research documentation.
- Letter-frequency comparisons use percentage shares rather than raw counts because the comparison lists differ in size.

## Config QA

All three configs:

- point to the real aggregate CSV;
- use exact existing columns;
- use explicit metric filters;
- use a zero baseline for horizontal bars;
- use percent formatting consistently;
- use concise source text;
- use descriptive archived output paths;
- require no renderer-specific workaround.

## Visual QA

### Chart 1 — Seuss mostly invented things

- horizontal ranking reads high to low;
- values and category labels are legible;
- 61% focus highlight supports the noun-heavy opening;
- title/subtitle stay inside safe margins;
- x-axis title and footer are separated;
- no clipping detected.

### Chart 2 — The nonsense follows the sound

- four mutually exclusive published categories remain visible;
- no single category is falsely highlighted as the whole 84% story;
- labels clearly preserve the rhyme + alliteration overlap category;
- title/subtitle stay inside safe margins;
- x-axis title and footer are separated;
- no clipping detected.

### Chart 3 — Z does much more work in Seuss

- Seuss 4.42% is highlighted against 1.02% and 0.10% comparison shares;
- reader-facing label uses “invented words” while research notes preserve the technical “type-2 nonce words” terminology;
- all three comparison labels are visible;
- 0% baseline is visible;
- title/subtitle stay inside safe margins;
- x-axis title and footer are separated;
- no clipping detected.

## Reusable template improvement

The first render exposed a general layout weakness: the documented default `plot_bottom=0.14` and `footer_y=0.08` allowed an x-axis title to collide vertically with the footer.

This branch therefore updates the shared system to:

- `plot_bottom=0.18`;
- `footer_y=0.055`;
- require concise `source_text` in the chart footer.

Updated reusable files:

- `spec/538_template_rules.md`;
- `src/chart_config_template.py`;
- `docs/chart_config_prompt.txt`;
- `src/render_538.py`;
- `src/chart_538.py`.

The final Seuss renders confirm that the revised defaults resolve the observed collision.

## Known limitations

- Teuber's 377-word dataset is a defined linguistic sample, not a complete census of every unusual word in Seuss's oeuvre.
- Published part-of-speech and sound-influence shares are rounded whole percentages.
- The three Z comparison lists have different sizes and constructions.
- The charts show patterns in the study; they do not claim that nouns, rhyme or Z alone define Seuss's writing style.

## Publication gate

No live Jekyll post, site assets, social package or feature artwork has been created.

Next gate: Adam reviews the exact three charts and editorial route. Publication work starts only after approval.
