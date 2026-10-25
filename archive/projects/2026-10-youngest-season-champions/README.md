# Youngest season-long champions — Coffeetableviz

**Stage:** Research-to-production review (25 October 2026, Europe/London). No site publication and no approval of final images implied.

## Editorial question

How young were athletes when they reached the top of a full season's competition? Starting with the F1 youngest-champion record, compare a tightly defined selection of senior season-long sporting achievements.

## Eligible titles

Include a senior **season-long** championship, overall World Cup/tour standings, or officially recognised year-end No. 1 rankings, earned through multiple events. Include season-plus-finals structures if progression depends on regular-season results. This includes ATP/WTA year-end No. 1 and golf season titles. Exclude majors, Olympic individual medals, isolated races and tournament-only world championships.

## Source files

- `data/youngest_season_champions.csv`: 13 independently identified **examples**, not a comprehensive census and not necessarily each sport's all-time record. One primary source URL for every row.
- `data/f1_youngest_record_progression.csv`: confirmed 1972–2010 youngest-age record changes and a separately conditional 2026 Antonelli scenario.
- `scripts/render_charts.py`: deterministic standalone Python chart rendering (Matplotlib) to `output/`.

To reproduce (from repository root): `python -m pip install matplotlib` then `python archive/projects/2026-10-youngest-season-champions/scripts/render_charts.py`.

The standard `src/render_538.py` supports conventional line/dot/scatter/bar charts but these bespoke step/leader/three-panel compositions use a project-specific Matplotlib renderer following `spec/538_template_rules.md`. The shared renderer is deliberately unchanged. Any final generated PNG must be visually checked, not assumed valid because the script runs.

## Three-chart editorial narrative

1. **F1's age record could fall again** — confirmed youngest world-champion-age step records; hollow *conditional* Antonelli point for 25 October 2026.
2. **A champion at 13. Another at 23.** — ranked dot plot of 13 season-long title examples; F1 red, motorcycling/rallying blue, all others grey.
3. **Three ways to win a season** — same examples grouped by annual standings, season-plus-finals and race-points championships; athlete names carry sports in brackets.

## Editorial and data QA caveats

- Exact ages use completed years plus days since last birthday, with decimal age for dot placement.
- **Comparison is selected examples, not a claim that one sport reliably produces younger champions.** Do not calculate representative sport-level means without a full census.
- 2013 ski jumping and 1971 alpine skiing ages are measured at the season's final event, not necessarily the earliest mathematical clinch.
- Official WTA 1997 ranking dated **24 November 1997** is the reference used for Hingis; distinguish this from when she *first* reached No. 1.
- DP World Tour supplies the age **19y 250d** for Seve Ballesteros; award-date field is intentionally blank rather than invented.
- The World Snowboard Tour was a historical tour-ranking system; its overall crown differs from FIS overall World Cup titles.
- ATP/WTA year-end rankings are rolling ranking-points systems; race points and season-plus-finals are separately flagged.
- **Antonelli has not been recorded as 2026 world champion** in this data; refresh his status from Formula 1 after the relevant race before any publication.
- Check final exported pixels for clipping, leader-line overlap, colour consistency, status footnotes, title/subtitle and margins on desktop and mobile.
- Some claimed champion ages in older sources disagree by a day. These data rely on one consistent reference date per record, documented in CSV.

## Delivery and approval

This branch is for peer/editorial review. Do not publish the blog post or merge without review and the user's approval. The first rendered previews were shared in chat; the repository renderer script and its output need their own execution and pixel QA before images are marked publication-ready.
