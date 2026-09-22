# Project manifest: Brad Pitt quotability

## Status

- Status: Story discovery / expanded pilot
- Started: 23 September 2026
- Last updated: 23 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-brad-pitt-quotability`
- Branch: `feat/brad-pitt-quotability`
- Draft PR: #58

## Story

- Working title: Brad Pitt quotability
- Recommended argument: Brad Pitt's most quotable character is Tyler Durden, using IMDb character-page quote-entry counts as a measurable proxy for user-curated quotability.
- Important limitation: this is not screenplay dialogue volume, screen time or an objective cultural-impact measure.

## Existing source reused

- `archive/projects/2026-09-brad-pitt-imdb-list/data/brad_pitt_imdb_films.csv`
- 54-film IMDb list already used by the published Brad Pitt story.
- Reuse year, title, tconst and IMDb rating rather than rebuilding those fields.

## New source

IMDb character pages for Brad Pitt (`nm0000093`) under each title:
`https://www.imdb.com/title/{tconst}/characters/nm0000093/`

Values were checked on 23 September 2026 from indexed IMDb character-page results. Counts are mutable and must be frozen/rechecked before final publication.

## Data files

| File | Purpose | Status |
|---|---|---|
| `data/brad_pitt_quote_counts_pilot.csv` | Quote-entry enrichment for 44 films | Expanded pilot; 10 source-list films unresolved |

## Content

| File | Purpose | Status |
|---|---|---|
| `content/story_plan.md` | Story options, recommended 3-chart route, provisional relationship test and QA risks | Ready for editorial review |

## Current evidence

Verified quote-entry leaders:
1. Tyler Durden / *Fight Club* — 105
2. Louis / *Interview with the Vampire* — 60
3. Billy Beane / *Moneyball* — 53
4. Achilles / *Troy* — 50
5. Sonny Hayes / *F1* — 46
6. Mills / *Seven* — 45
7. Rusty Ryan / *Ocean's Eleven* — 42

Verified-sample relationship:
- n = 44
- Pearson quote-count vs IMDb-rating correlation = 0.54
- Spearman rank correlation = 0.46
- Treat as descriptive only.

Ocean's recurring-character check:
- *Ocean's Eleven* — 42
- *Ocean's Twelve* — 13
- *Ocean's Thirteen* — 17

## QA / caveats

- Quote count verified for 44 of the 54 rows in the existing film list.
- Ten films remain unresolved after indexed-source checks.
- Unresolved films are unknown, not zero.
- Counts can change as IMDb users edit quote pages.
- Counts may be influenced by role size, fandom and page activity.
- Correlation does not imply causation and is confounded by role size.
- Film ratings are reused from the existing Brad Pitt list and inherit its source-scope caveat.
- No chart configs, renderer changes or live-site publication are part of this stage.

## Next gate

Resolve or explicitly audit the remaining ten titles, freeze coverage, then build the three derived datasets and chart configs only after the story/coverage gate is accepted.
