# Project manifest: Bowie five-album audio profiles

## Status

- Started: 27 September 2026
- Working branch: `project/2026-09-david-bowie-five-album-audio-features`
- Scope: five albums associated with David Bowie's five most-streamed canonical studio tracks in the 25 September 2026 snapshot
- Template approved: **duration + tempo + energy + valence + acousticness**
- Publication status: five-album build in progress

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

Spotify's own Audio Features / Audio Analysis endpoints are unavailable to new or development-mode API applications. This project therefore uses **ReccoBeats Spotify-style audio features** with explicit attribution.

Available features retained in the enriched dataset:

- acousticness
- danceability
- energy
- instrumentalness
- liveness
- loudness
- speechiness
- tempo
- valence

The publication visuals use **tempo, energy, valence and acousticness**.

## Locked visual template

- rows = album tracks in original order
- primary comparison = canonical track duration
- bar colour = tempo
- compact horizontal tempo key
- right-side mini-panels = energy, valence, acousticness
- red dot beside track label = most-streamed matched track on the album
- missing audio-feature rows retain duration and show blank feature marks
- tempo colour scale = global across all five albums
- feature scales = fixed 0–1

## Next gate

Build and QA the full five-album enrichment, render all five charts, then write the dataset-led publication package. The temporary project-specific workflow must be removed before merge.
