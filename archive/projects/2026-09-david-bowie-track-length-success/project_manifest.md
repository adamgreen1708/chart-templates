# Project manifest: David Bowie track length, style and success

## Status

- Status: **dataset build and story discovery complete; three-chart plan ready for Adam review**
- Started: 27 September 2026
- Last updated: 27 September 2026
- Owner: Adam Green
- Repo project slug: `2026-09-david-bowie-track-length-success`
- Working branch: `project/2026-09-david-bowie-track-length-success`
- Draft PR: #78
- Publication status: research/story-planning only; no chart configs or live site publication yet

## Core question

What happens when David Bowie's studio catalogue is viewed track by track rather than album by album: are his more successful songs shorter, do track lengths change with musical style, and does today's streaming popularity tell a different story from original UK chart success?

## Scope

- Reuse the previously validated 26 lifetime solo studio albums from the 1967 debut through *Blackstar* (2016).
- Include *The Buddha of Suburbia* under the previously validated official Bowie studio-album scope.
- Exclude *Toy*, live albums, compilations, *Peter and the Wolf* and Tin Machine.
- Unit of analysis: original studio-album track.
- Alternate mixes, live versions, demos, remasters and reissues are excluded from the canonical album spine unless used only to identify present-day consumption for the matching composition.

## Final dataset QA

- **275 canonical studio-album tracks**
- **26/26 albums**
- **0 missing durations**
- album-by-album canonical track-count assertions pass
- 1967 debut corrected to the 14-track UK original
- *Reality* corrected to the 11-song album rather than duplicated SACD layers
- **239/275** album tracks matched to a current Spotify/Kworb composition
- Spotify snapshot: **25 September 2026**
- **49/275** album tracks match at least one David Bowie entry on the main UK Official Singles Chart
- Official Charts year-labelled reissues are folded back into the same composition
- AllMusic Styles remain explicitly labelled as **album-level** metadata in the full-catalogue dataset

## Source strategy

1. **Track identity and duration:** MusicBrainz, with canonical album track-count QA and original-release selection.
2. **Style:** AllMusic album-level Styles inherited by each canonical track. Song-level Styles remain a possible later enrichment and must be reached from the correct album track entity.
3. **Current popularity:** dated Spotify stream snapshot from Kworb, matched at composition level while preserving the matched Spotify title and candidate count.
4. **Historic UK success:** Official Charts main Official Singles Chart history, aggregating repeated chart entries/reissues for the composition.
5. **Downloads:** not used as the main success metric because the download era covers only a small fraction of Bowie's career.

## Key findings

- Overall canonical track median: **4:10**.
- Median track duration rises from **3:09 in the 1960s** to **4:49 in the 1990s**, then eases back.
- *Station to Station* has the longest album median at **6:02**.
- Among recurring AllMusic album Styles, Blue-Eyed Soul-tagged albums have a **4:45** track median versus **3:29** for Glam Rock-tagged albums.
- Duration vs log current streams: **Pearson r = 0.11** — little linear relationship.
- Tracks with a main UK singles-chart match have a median album duration of **4:34**, versus **4:02** for tracks without one.
- **15 of the current top 20 matched studio compositions are at least four minutes long.**
- The top 10 matched studio compositions account for about **62.8%** of streams within the matched canonical studio-track set.
- Strong current-streaming non-main-chart examples include *Moonage Daydream* (294.1m), *The Man Who Sold the World* (159.2m) and *Suffragette City* (89.7m).

## Files

### Data

- `data/source_album_spine.csv` — reused validated Bowie album scope and AllMusic album Styles.
- `data/spotify_top9_discovery_snapshot.csv` — initial discovery snapshot retained for audit history.
- `data/david_bowie_tracks_core.csv` — final canonical track/duration spine.
- `data/david_bowie_tracks_streams.csv` — canonical tracks plus current stream matching.
- `data/david_bowie_tracks_success.csv` — final joined analysis dataset with stream and UK chart fields.

### Scripts

- `scripts/build_track_length_dataset.py` — MusicBrainz track builder with release and album-count QA.
- `scripts/enrich_current_streams.py` — dated current-stream enrichment.
- `scripts/enrich_uk_official_charts.py` — main Official Singles Chart enrichment and reissue normalisation.

### Content

- `content/research_plan.md` — source, matching and QA rules.
- `content/early_story_scan.md` — pre-build story hypotheses.
- `content/story_plan.md` — final dataset-led three-chart editorial plan.

## Recommended story

**Bowie's songs changed shape as often as they changed style — and he never needed the three-minute rule to make them successful.**

Recommended sequence:

1. **Bowie stretched the song** — album median track length through the career.
2. **Style changed the clock** — recurring AllMusic album Styles versus median track duration.
3. **The hits weren't short** — duration versus current streams, with UK main-chart status as context.

Strong spin-off: **The afterlife of a hit** — high-streaming album tracks whose canonical title has no main UK Official Singles Chart match.

## Next gate

Adam reviews the recommended story route. If approved, create the three derived chart datasets, then the three locked-538 chart configs, render and QA them.

Do not publish a live site post yet.
