# David Bowie track length, style and success — research plan

## Editorial question

Does Bowie's success obey a simple pop rule — short tracks, familiar styles, bigger audience — or does the catalogue tell a messier story?

## Why this is a separate project

The earlier Bowie reinvention project worked at album level. This project changes the unit of analysis to the **track**, while reusing the already validated 26-album lifetime studio scope.

## Dataset design

Planned canonical columns:

- `album_sequence`
- `album_year`
- `album_title`
- `track_number`
- `disc_number`
- `track_title`
- `duration_ms`
- `duration_seconds`
- `duration_display`
- `decade`
- `allmusic_album_styles`
- `allmusic_album_style_count`
- `style_granularity` = `album` for the base dataset
- `musicbrainz_release_group_id`
- `musicbrainz_release_id`
- `musicbrainz_recording_id`
- `spotify_streams` (dated snapshot; nullable)
- `spotify_daily` (dated snapshot; nullable)
- `spotify_snapshot_date`
- `uk_chart_best_peak` (nullable)
- `uk_chart_total_weeks` (nullable)
- `uk_chart_entry_count`
- `uk_charted_flag`
- `success_data_note`

## Source rules

### Track lengths

Use MusicBrainz because it is reproducible and exposes recording/track lengths. Resolve David Bowie rather than guessing the artist identifier. Match the 26 validated album titles to Bowie's release groups, then choose an original official release with a preference for the earliest dated UK release where available.

Do not silently mix bonus tracks from later deluxe editions into the canonical album tracklist.

### AllMusic Styles

The existing album spine already contains AllMusic Styles for 25 of 26 albums; *The Next Day* has no comparable album Styles field.

A useful discovery from fresh research is that AllMusic also exposes **song-level Styles**. However, duplicate song entities can exist for the same title and can carry different metadata. Therefore:

- the base full-catalogue dataset uses the validated album-level style set;
- song-level Styles may be added later;
- any song-level enrichment must follow the song link from the correct album track listing, not a global title search;
- missing song-level Styles remain missing rather than being imputed.

### Popularity and success

Use two separate concepts rather than one blended score.

**Current catalogue popularity**
- Spotify streams and daily streams from a dated Kworb snapshot.
- Treat remaster text as a version label, not a distinct composition where a clean canonical match is possible.
- Keep the snapshot date because current streams change continuously.

**Historic UK commercial success**
- Official Charts peak, weeks and chart runs.
- Aggregate repeat chart runs carefully.
- Do not interpret an album track with no singles-chart entry as a zero-quality or zero-popularity observation.

### Why not downloads?

Downloads are not a fair whole-career metric: commercial download charts arrived decades after Bowie's first releases. They can be retained as a later-era appendix if a reliable source adds editorial value, but they should not drive the main comparison.

## QA risks

1. **Remaster duplication:** current streaming services expose many versions of the same composition.
2. **Single edit vs album version:** e.g. a successful radio edit may be much shorter than the album track. Preserve both concepts rather than overwriting one with the other.
3. **AllMusic duplicate song IDs:** use album-linked song entities only for song-level Styles.
4. **Multi-label style categories:** a track can inherit multiple AllMusic album Styles; style analysis should be exploded carefully and should not double-count tracks in totals.
5. **Era effects:** stream counts measure current listening, while Official Charts measures historic release-period performance.
6. **Cover versions:** *Pin Ups* contains covers; songwriter identity is not the analytical unit here, but the track remains part of Bowie's studio-album catalogue.
7. **Instrumentals/interludes:** especially relevant in *Low*, *Heroes*, *1. Outside* and *The Buddha of Suburbia*; very short or long pieces should not be treated as data errors without review.

## Build order

1. Freeze canonical studio-album tracklist and durations.
2. Inspect duration distribution by year, album and style.
3. Match Official Charts success.
4. Match current Spotify stream snapshot.
5. Compare current popularity with original UK chart success.
6. Run story discovery.
7. Present the recommended three-chart editorial route.
8. Only then create chart configs.
