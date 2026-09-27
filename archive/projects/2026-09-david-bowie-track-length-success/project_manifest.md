# Project manifest: David Bowie track length, style and success

## Status

- Status: kickoff complete; core data build staged; early story scan completed
- Started: 27 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-david-bowie-track-length-success`
- Working branch: `project/2026-09-david-bowie-track-length-success`
- Publication status: research only; no chart configs or site publication yet

## Core question

What happens when David Bowie's studio catalogue is viewed track by track rather than album by album: are his more successful songs shorter, do track lengths change with musical style, and does today's streaming popularity tell a different story from original UK chart success?

## Scope

- Reuse the previously validated 26 lifetime solo studio albums from the 1967 debut through *Blackstar* (2016).
- Include *The Buddha of Suburbia* under the previously validated official Bowie studio-album scope.
- Exclude *Toy*, live albums, compilations, *Peter and the Wolf* and Tin Machine.
- Initial unit of analysis: original studio-album track.
- Keep alternate mixes, live versions, demos, remasters and reissues out of the canonical track spine unless they are only being used to identify current streaming consumption for the matching composition.

## Source strategy

1. **Track identity and duration:** MusicBrainz, using the validated album spine and an original-release preference.
2. **Style:** AllMusic. The first full-catalogue field is album-level Styles inherited by each canonical track. Song-level AllMusic Styles are a planned enrichment, but only when the song entity is reached from the correct album track link because AllMusic can expose duplicate song entities with different metadata.
3. **Current popularity:** dated Spotify stream snapshots from Kworb, matched to the canonical composition/remaster.
4. **Historic UK success:** Official Charts chart history, preserving peak, weeks and repeat chart runs rather than treating an uncharted album track as a failed single.
5. **Downloads:** deliberately not used as the main success metric because the download era covers only a small fraction of Bowie's career.

## Current files

- `data/source_album_spine.csv` — reused validated Bowie album scope and AllMusic album Styles.
- `data/spotify_top9_discovery_snapshot.csv` — first-pass current-streaming evidence for the nine leading solo tracks in the current Spotify ranking.
- `scripts/build_track_length_dataset.py` — reproducible MusicBrainz track/duration builder.
- `content/research_plan.md` — source, matching and QA rules.
- `content/early_story_scan.md` — story candidates before chart config work.

## Current recommendation

Build the complete canonical track-length table first, then enrich it with historic UK chart performance and a dated current-streaming snapshot. Do not create chart configs until the joined dataset has been inspected under the repository's story-discovery flow.
