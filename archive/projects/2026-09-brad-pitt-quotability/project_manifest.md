# Project manifest: Brad Pitt quotability

## Status

- Status: Publication package staged; official PNGs committed; feature asset awaiting approval
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
| config/chart_01_top_roles.py | Fury started it. Tyler Durden owns the answer. | Local render QA passed |
| config/chart_02_quotes_vs_rating.py | Ratings help. They don't explain the quotes. | Local render QA passed |
| config/chart_03_oceans.py | Rusty did most of his talking on the first job | Local render QA passed |

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
- Local visual QA produced three 1600 × 1600 outputs.
- First-pass title/subtitle/footer collisions were resolved solely through project config spacing and shorter source text.
- Second-pass visual QA found no clipping or collisions.
- No live-site publication is part of this stage.

- Workflow retrigger: corrected archived-render output-path handling after PR #59 validation failure.

## Publication staging

- Official GitHub Actions renders are committed on main.
- Site post staged at `site/_posts/2026-09-23-fury-started-it-tyler-durden-owns-the-answer.md`.
- Official chart blobs copied into `site/assets/migrated/brad-pitt-quotability/`.
- Publication package staged at `content/publication_package.md`.
- Feature illustration generated for Adam review; exact feature asset is intentionally not committed until approved.
- Publication PR must remain draft until the exact feature asset is committed and all site references pass.

## Next gate

Adam reviews the generated feature illustration. If approved, commit that exact asset as `site/assets/migrated/brad-pitt-quotability/feature.webp`, run final site-reference QA, then mark the publication PR ready for review.
