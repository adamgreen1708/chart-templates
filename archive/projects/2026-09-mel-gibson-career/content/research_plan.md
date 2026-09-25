# Mel Gibson career project — research plan

## Recommended route

**Source research and data acquisition → story discovery → three-chart editorial plan.**

This project should reuse the repo's IMDb actor-project pattern but extend it so the same reproducible dataset captures both principal acting credits and feature-film directing credits.

## Why this route

The question is not simply "which Mel Gibson films rated highest?". Adam's nostalgia anchors — *Lethal Weapon* and *Braveheart* — sit either side of an important career change. *Lethal Weapon* represents the mainstream acting-star phase; *Braveheart* is also a directing milestone.

A one-lane actor filmography would therefore miss the most interesting part of the question: **the job changed**.

## Verified starting evidence

These facts are strong enough to define the research question, but not to replace the downloadable-data pass:

- IMDb identifies Mel Gibson as `nm0000154` and currently lists him as actor, producer and director.
- IMDb describes *Lethal Weapon* (1987) as the start of his signature series.
- The Academy records *Braveheart* (1995) with 10 nominations and 5 wins, including Directing for Mel Gibson and Best Picture shared by Gibson, Alan Ladd Jr. and Bruce Davey.
- IMDb's current directing credits show released feature films including *The Man Without a Face* (1993), *Braveheart* (1995), *The Passion of the Christ* (2004), *Apocalypto* (2006), *Hacksaw Ridge* (2016) and *Flight Risk* (2025).
- The Academy records Gibson as a 2017 Directing nominee for *Hacksaw Ridge*.
- Reuters reported in 2016 that Gibson had kept a low profile with a handful of small acting roles after his 2006 arrest and antisemitic outburst, describing *Hacksaw Ridge* as a career rebound. This is contextual evidence only; a chart should not infer causation from chronology.
- The Numbers currently lists Gibson with more than US$4.6bn worldwide box office across 56 leading roles. This is useful scale context, not the main metric for the story.

## Acquisition design

Use IMDb's official non-commercial exports:

- `name.basics.tsv.gz`
- `title.principals.tsv.gz`
- `title.basics.tsv.gz`
- `title.ratings.tsv.gz`
- `title.crew.tsv.gz`

Process:

1. Resolve exact-name Mel Gibson in `name.basics`; verify `nm0000154` from the source rather than hard-coding it as truth.
2. Filter `title.principals` to Gibson's actor/actress principal credits.
3. Stream `title.crew` and capture any title where Gibson appears in the directors field, plus crew rows needed for acting titles.
4. Join the union of acting and directing title IDs to `title.basics` and `title.ratings`.
5. Restrict the analytical set to released `movie` titles with a year, rating and a disclosed minimum-vote floor.
6. Preserve every excluded title/reason in an audit CSV.
7. Derive transparent flags only from source fields: `acted`, `directed`, and `career_lane` (`acting`, `directing`, `acting + directing`).
8. Store source URLs, access time, upstream run dates where available, join coverage and row-count validation.

## Story tests to run after acquisition

- Acting-title count and mean/median IMDb rating by five-year period.
- Acting output before and after the mid-2000s.
- Directed-feature chronology and ratings.
- Titles where Gibson both acted and directed versus acted only.
- Gaps between acting releases and between directing releases.
- Whether the apparent post-*Braveheart* shift is visible in credit mix rather than being a handful of famous examples.
- Whether the 2016 directing return genuinely stands out in rating/awards context.
- Sensitivity to the IMDb vote floor.

## Comparability rules

- IMDb ratings describe the title, not Gibson's performance.
- Vote counts vary substantially; show or disclose sample size and vote-floor rules.
- Acting and directing title counts measure credits, not workload or creative control.
- Box office is optional context only; do not mix nominal grosses across decades as if inflation-adjusted.
- Public controversy can be marked as a sourced timeline event, but the data cannot by itself prove it caused a change in film opportunities.

## Stop gate

Do not create chart configs from this research note. Run and validate the acquisition script first, inspect the resulting data, then rewrite the story plan with exact dataset statistics.
