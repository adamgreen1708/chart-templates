# Mel Gibson career arc — research plan

## Recommended route

Use **source research/data acquisition -> story discovery -> 3-chart editorial plan**.

Do not create chart configs yet.

## Why

The user's hook is nostalgic — *Lethal Weapon* and *Braveheart* — but the useful analytical question is not simply "what were his best films?" It is "how did the shape of the career change?"

That requires three distinct evidence layers:

1. **Role chronology** — acting, directing, writing and producing.
2. **Title-level reception** — official IMDb ratings/vote counts, with a disclosed vote floor.
3. **Commercial scale/context** — selective box-office enrichment, with clear current-lifetime/nominal-dollar caveats.

## Discovery sources already checked

### Film role chronology

Current public filmography table: https://en.wikipedia.org/wiki/Mel_Gibson_filmography

Discovery extraction:
- 72 released feature-film rows from 1977 through 2025.
- 65 rows with an acting credit.
- 6 rows with a directing credit.
- 14 rows with a producing credit.
- 3 rows with a writing credit.
- Unreleased *The Resurrection of the Christ* parts dated 2027 and 2028 are excluded from the released dataset.

These counts are for discovery only. The final actor/rating dataset must be rebuilt from IMDb's official non-commercial exports following `docs/imdb_actor_project_prompt.md`.

### Directing snapshot

The six released feature directing credits are:
- *The Man Without a Face* (1993)
- *Braveheart* (1995)
- *The Passion of the Christ* (2004)
- *Apocalypto* (2006)
- *Hacksaw Ridge* (2016)
- *Flight Risk* (2025)

The Numbers current lifetime worldwide totals in the companion CSV range from about $24.8m to $622.3m. They are nominal current-lifetime figures, not inflation-adjusted comparisons. *The Passion of the Christ* total includes 2026 re-release activity.

### Career context

Variety reported in 2024 that Gibson's Hollywood career "nosedived" after his 2006 DUI arrest and antisemitic remarks, and that although he kept acting, it was rarely in major Hollywood tentpoles or studio films. This is contextual reporting; the filmography counts alone cannot establish cause.

Variety reported in 2026 that *Flight Risk* marked a return to studio filmmaking and that the two-part *The Resurrection of the Christ* is planned for 2027 and 2028.

## Required next acquisition

Before configs:

1. Adapt the existing Simon Pegg official-IMDb streaming workflow for Mel Gibson rather than scraping IMDb pages.
2. Resolve the exact Mel Gibson `nconst` against `name.basics.tsv.gz`; do not assume it from a web page.
3. Join principal acting credits to basics, ratings and crew.
4. Keep released `titleType=movie` titles with a disclosed minimum-vote threshold.
5. Preserve exclusions and unmatched rows in an audit CSV.
6. Calculate annual acting-credit counts and career-era summaries from the verified IMDb set.
7. Only if Chart 2 still needs "scale" rather than activity, enrich a reproducible subset with The Numbers box office/theatre data. Do not infer blockbuster status from title recognition alone.

## Stop gate

No CHART_CONFIG, render, feature art or live-site files until the official IMDb pass confirms or materially revises the story route.
