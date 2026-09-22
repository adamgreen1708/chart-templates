# Project manifest: Brad Pitt quotability

## Status

- Status: Final chart specs / configs staged; render QA pending
- Started: 23 September 2026
- Last updated: 23 September 2026
- Owner: Adam Green
- Repo project slug: 2026-09-brad-pitt-quotability
- Branch: feat/brad-pitt-quotability
- Draft PR: #58

## Story

- Working title: Brad Pitt quotability
- Editorial trigger: Adam was watching Fury.
- Recommended argument: Fury starts the question, but Tyler Durden in Fight Club leads the verified film-role quote-count ranking.
- Fury treatment: Don 'Wardaddy' Collier is a required highlighted point in Charts 1 and 2 and anchors the eventual feature-art concept.
- Important limitation: this is not screenplay dialogue volume, screen time or an objective cultural-impact measure.

## Existing source reused

- archive/projects/2026-09-brad-pitt-imdb-list/data/brad_pitt_imdb_films.csv
- 54-film IMDb list already used by the published Brad Pitt story.
- Reuse year, title, tconst and IMDb rating rather than rebuilding those fields.

## New source

IMDb character pages for Brad Pitt (nm0000093) under each title.

Values were checked on 23 September 2026 from indexed IMDb character-page results. Counts are mutable and must be frozen/rechecked before final publication.

## Data files

| File | Purpose | Status |
|---|---|---|
| data/brad_pitt_quote_counts_pilot.csv | Quote-entry enrichment for 44 films | Expanded verified snapshot |
| data/brad_pitt_quote_counts_unresolved.csv | Audit of ten unresolved source-list films | Complete for this stage |
| data/brad_pitt_chart_01_top_roles.csv | Top 12 film-role ranking | Ready for render |
| data/brad_pitt_chart_02_quotes_vs_rating.csv | 44-film-role scatter dataset | Ready for render |
| data/brad_pitt_chart_03_oceans.csv | Rusty Ryan Ocean's sequence | Ready for render |

## Chart configs

| File | Chart | Status |
|---|---|---|
| config/chart_01_top_roles.py | Fury started the question. Tyler Durden owns the answer. | Ready for renderer QA |
| config/chart_02_quotes_vs_rating.py | Ratings help. They don't explain the quotes. | Ready for renderer QA |
| config/chart_03_oceans.py | Rusty did most of his talking on the first job | Ready for renderer QA |

## Content

| File | Purpose | Status |
|---|---|---|
| content/story_plan.md | Agreed Fury-led story route and data definition | Updated |
| content/chart_specs.md | Final production specification for all three charts | Complete |

## Current evidence

Verified quote-entry leaders:
1. Tyler Durden / Fight Club — 105
2. Louis / Interview with the Vampire — 60
3. Billy Beane / Moneyball — 53
4. Achilles / Troy — 50
5. Sonny Hayes / F1 — 46
6. Mills / Seven — 45
7. Rusty Ryan / Ocean's Eleven — 42
8. Don 'Wardaddy' Collier / Fury — 40

Verified-sample relationship:
- n = 44 film-role pages
- Pearson quote-count vs IMDb-rating correlation = 0.536
- Spearman rank correlation = 0.464
- Treat as descriptive only.

Ocean's recurring-character check:
- Ocean's Eleven — 42
- Ocean's Twelve — 13
- Ocean's Thirteen — 17

## QA / caveats

- Quote count verified for 44 of the 54 rows in the existing film list.
- Ten films remain unresolved and are unknown, not zero.
- The unit is a film-role page, not a unique character across multiple films.
- Counts can change as IMDb users edit quote pages.
- Counts may be influenced by role size, fandom and page activity.
- Correlation does not imply causation.
- Film ratings inherit the existing Brad Pitt source-scope caveat.
- Renderer and template files remain untouched.
- No live-site publication is part of this stage.

## Next gate

Run all three configs through the locked renderer, inspect the resulting 1600 × 1600 PNGs, correct only project-level annotation/layout issues where possible, then present the three charts for Adam's visual approval before publication work.
