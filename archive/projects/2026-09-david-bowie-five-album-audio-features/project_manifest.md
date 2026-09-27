# Project manifest: Bowie five-album audio profiles

## Status

- Started: 27 September 2026
- Working branch: `project/2026-09-david-bowie-five-album-audio-features`
- Scope: five albums associated with David Bowie's five most-streamed canonical studio tracks in the 25 September 2026 snapshot
- Prototype gate: enrich and render **Ziggy Stardust only** before rolling the visual across the other four albums
- Publication status: research/prototype only

## Five-album scope

1. *The Rise and Fall of Ziggy Stardust and the Spiders from Mars* (1972)
2. *Heroes* (1977)
3. *Space Oddity* (1969)
4. *Diamond Dogs* (1974)
5. *Hunky Dory* (1971)

These albums are selected because their tracks contain the five most-streamed canonical Bowie compositions in the existing dataset: *Starman*, *“Heroes”*, *Space Oddity*, *Rebel Rebel* and *Life on Mars?*.

## Parent data

The source spine reuses the validated Bowie track dataset:

`archive/projects/2026-09-david-bowie-track-length-success/data/david_bowie_tracks_success.csv`

The new project does not reacquire duration or stream-count data.

## Audio-feature source

Spotify's own Audio Features / Audio Analysis endpoints are unavailable to new or development-mode API applications. For this project, the prototype uses **ReccoBeats Spotify-style audio features** with explicit source attribution rather than claiming the values are newly retrieved from Spotify.

ReccoBeats documents the following features:

- acousticness
- danceability
- energy
- instrumentalness
- liveness
- loudness
- speechiness
- tempo
- valence

## Prototype question

Can one album graphic make track sequence, song length, pace and mood readable at the same time?

## Ziggy prototype encoding

- rows: album tracks in original order
- primary comparison: canonical track duration
- bar colour: tempo
- right-side mini-panels: energy, valence and danceability on 0–1 scales
- contextual emphasis: most-streamed track on the album
- retain streams in the dataset but do not use them as a second quantitative axis

## Next gate

Run the ReccoBeats enrichment for all 11 *Ziggy Stardust* tracks. If coverage and matching QA pass, render one prototype chart and inspect whether tempo colour plus three feature dots is legible. Do not enrich/render the other four albums yet.
