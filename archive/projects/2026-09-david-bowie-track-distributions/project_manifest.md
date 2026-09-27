# Project manifest: David Bowie track distributions

## Status

- Status: distribution dataset and editorial route drafted
- Started: 27 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-david-bowie-track-distributions`
- Working branch: `project/2026-09-david-bowie-track-distributions`
- Publication status: spin-off mini-post; separate from “Bowie never needed the three-minute rule”

## Core question

What gets hidden when David Bowie's album track lengths are reduced to one average?

## Source

Reuse the validated 275-track canonical dataset from:
`archive/projects/2026-09-david-bowie-track-length-success/data/david_bowie_tracks_success.csv`

## Recommended editorial angle

**Every Bowie album has a shape.**

Plot every track rather than only the album median. Show mean and median together, then use the most-streamed track and formal duration outliers to reveal where the famous song is — or is not — representative of the album around it.

## Current findings

- 26 albums / 275 canonical tracks.
- 13 of 26 albums contain at least one Tukey track-length outlier.
- *Blackstar*: mean 5:53 vs median 4:52 because the 9:57 title track pulls the mean upward.
- *1. Outside*: mean 3:56 vs median 4:22; short segues pull the mean downward.
- *Let's Dance*: the most-streamed track is 7:37 versus a 4:59 album median.
- *“Heroes”*: the most-streamed track is 6:10 versus a 3:48 album median and is also a Tukey outlier.
- *Station to Station*: the most-streamed track, *Golden Years*, is 4:01 versus a 6:02 album median — the opposite pattern.

## Files

- `data/bowie_track_distribution_rows.csv` — 275 track rows with album statistics and label flags.
- `scripts/build_distribution_dataset.py` — reproducible derivation from the validated parent dataset.
- `content/chart_spec.md` — visual specification.
- `content/mini_post_angle.md` — editorial structure.

## Next gate

Render one tall distribution chart, review label density and legibility, then decide whether the mini-post needs only this chart or a small mean-vs-median companion.
