# Project manifest: Brad Pitt quotability

## Status

- Status: Story discovery / pilot data
- Started: 23 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-brad-pitt-quotability`
- Branch: `feat/brad-pitt-quotability`

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

Pilot values were checked on 23 September 2026 from indexed IMDb character-page results. Counts are mutable and must be rechecked before final publication.

## Data files

| File | Purpose | Status |
|---|---|---|
| `data/brad_pitt_quote_counts_pilot.csv` | First-pass quote-entry enrichment for 35 films | Pilot; non-exhaustive |

## Content

| File | Purpose | Status |
|---|---|---|
| `content/story_plan.md` | Story options, recommended 3-chart route and QA risks | Ready for editorial review |

## Current evidence

Pilot quote-entry leaders:
1. Tyler Durden / *Fight Club* — 105
2. Louis / *Interview with the Vampire* — 60
3. Billy Beane / *Moneyball* — 53
4. Achilles / *Troy* — 50
5. Sonny Hayes / *F1* — 46
6. Mills / *Seven* — 45
7. Rusty Ryan / *Ocean's Eleven* — 42

Ocean's recurring-character check:
- *Ocean's Eleven* — 42
- *Ocean's Twelve* — 13
- *Ocean's Thirteen* — 17

## QA / caveats

- Pilot includes 35 of the 54 rows from the existing film list.
- Missing films are unknown/not-yet-checked, not zero.
- Counts can change as IMDb users edit quote pages.
- Counts may be influenced by role size, fandom and page activity.
- Film ratings are reused from the existing Brad Pitt list and inherit its source-scope caveat.
- No chart configs or renderer changes should be made until the 54-film enrichment and story check are complete.

## Next gate

Complete the 54-film quote-count dataset, calculate coverage, test the rating relationship, then confirm or revise the recommended 3-chart route before creating configs.
