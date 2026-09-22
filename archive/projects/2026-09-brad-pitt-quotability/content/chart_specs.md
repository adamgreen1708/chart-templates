# Brad Pitt quotability — final three-chart specification

## Editorial definition

The unit in Charts 1 and 2 is a Brad Pitt film-role page on IMDb: one film + one Brad Pitt character-page quote count.

This is intentionally not described as a ranking of unique characters because recurring characters such as Rusty Ryan have separate quote counts for each film.

Current evidence base:
- 54 films in the existing Brad Pitt source list.
- 44 film-role pages with a verified IMDb quote-entry count.
- 10 unresolved titles retained in the audit as unknown, not zero.
- Snapshot date: 23 September 2026.

Fury is the editorial trigger and must be visibly featured, but the data is allowed to deliver a different headline.

## Chart 1 — Fury started it. Tyler Durden owns the answer.

Role: set the scene.

Question: Which verified Brad Pitt film roles have accumulated the most IMDb quote entries?

Chart type: ranked dot plot.

Display set: top 12 of the 44 verified film-role pages.

Key facts:
- Tyler Durden / Fight Club: 105.
- Wardaddy / Fury: 40.
- Wardaddy ranks 8th in the verified sample.
- The next-highest page after Fight Club is Louis / Interview with the Vampire at 60.

Visual treatment:
- all ordinary points in coffeetableviz blue;
- Fury / Wardaddy highlighted in muted red;
- annotate Tyler Durden and Wardaddy only;
- use film + role labels on the categorical axis;
- x-axis begins at zero;
- vertical gridlines on to support magnitude reading.

Dataset:
archive/projects/2026-09-brad-pitt-quotability/data/brad_pitt_chart_01_top_roles.csv

Config:
archive/projects/2026-09-brad-pitt-quotability/config/chart_01_top_roles.py

Output:
archive/projects/2026-09-brad-pitt-quotability/output/brad_pitt_01_top_roles.png

QA risk:
Do not call these screenplay lines, total dialogue, unique quotes across a career or an objective cultural-impact score.

## Chart 2 — Ratings help. They don't explain the quotes.

Role: build the tension.

Question: Do more highly rated Brad Pitt films also accumulate more quote entries for his role?

Chart type: scatter plot with a simple linear trend line.

Coverage: all 44 verified film-role pages.

Key facts:
- Pearson correlation: r = 0.536, shown editorially as 0.54.
- Spearman rank correlation: rho = 0.464, retained in the method notes rather than cluttering the chart.
- Fury: 40 quote entries, IMDb rating 7.6.

Required labels:
- Fury / Wardaddy — primary red highlight.
- Fight Club / Tyler Durden — high/high extreme.
- 12 Years a Slave — high rating, very few Pitt quote entries.
- The Big Short — high rating, very few Pitt quote entries.
- Sinbad — relatively high quote count at a middling rating.

Visual treatment:
- all context points grey;
- Fury in muted red;
- Fight Club annotation in blue;
- simple grey linear trend line;
- no causal wording.

Dataset:
archive/projects/2026-09-brad-pitt-quotability/data/brad_pitt_chart_02_quotes_vs_rating.csv

Config:
archive/projects/2026-09-brad-pitt-quotability/config/chart_02_quotes_vs_rating.py

Output:
archive/projects/2026-09-brad-pitt-quotability/output/brad_pitt_02_quotes_vs_rating.png

QA risk:
Role size, fandom and IMDb participation are confounders. Correlation is descriptive only.

## Chart 3 — Rusty did most of his talking on the first job

Role: land the aha moment with a controlled recurring-character example.

Question: How does the same Brad Pitt character's IMDb quote count change across the Ocean's trilogy?

Chart type: ordered three-point line.

Key facts:
- Ocean's Eleven: 42.
- Ocean's Twelve: 13.
- Ocean's Thirteen: 17.

Visual treatment:
- one blue line;
- zero baseline on quote-count axis;
- annotate all three points directly;
- no claim that three observations form a general trend.

Dataset:
archive/projects/2026-09-brad-pitt-quotability/data/brad_pitt_chart_03_oceans.csv

Config:
archive/projects/2026-09-brad-pitt-quotability/config/chart_03_oceans.py

Output:
archive/projects/2026-09-brad-pitt-quotability/output/brad_pitt_03_oceans.png

## Publication framing

Suggested opening idea:

I was watching Fury and wondering where Don 'Wardaddy' Collier would actually land if you tried to measure Brad Pitt's most quotable film roles.

Feature-art direction:
- symbolic tank / commander-hatch silhouette;
- quote-burst or speech-fragment motif;
- light grey #F3F4F6 background;
- charcoal/black artwork;
- one muted red accent;
- no Brad Pitt likeness required.

## Render gate

These configs have passed a local locked-renderer visual QA pass; repository PNGs are still pending the GitHub render/commit step.

QA completed locally against the locked renderer behaviour:
1. all three outputs rendered at 1600 × 1600;
2. first pass exposed title/subtitle and footer collisions;
3. fixes were made only in the three project configs: title sizing/wrapping, title/subtitle spacing, footer spacing and shorter source text;
4. second pass showed no clipping or title/subtitle/footer collisions;
5. Fury remains the red focus point in Charts 1 and 2;
6. Chart 3 retains a zero baseline and direct labels;
7. renderer and template files remain unchanged.

Next gate: create the repository PNG outputs through the GitHub archived-project render path, then present the exact committed images for Adam's approval.
