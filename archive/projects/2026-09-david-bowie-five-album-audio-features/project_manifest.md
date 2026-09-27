# Project manifest: Bowie five-album audio profiles

## Status

- Started: 27 September 2026
- Working branch: `project/2026-09-david-bowie-five-album-audio-features`
- Scope: five albums associated with David Bowie's five most-streamed canonical studio tracks in the 25 September 2026 snapshot
- Visual template: **duration + tempo + energy + valence + acousticness**
- Analysis status: **complete**
- Publication package: **complete; site packaging next**
- PR: #80
- Publication status: not merged / not live

## Five-album scope

1. *The Rise and Fall of Ziggy Stardust and the Spiders from Mars* (1972)
2. *Heroes* (1977)
3. *Space Oddity* (1969)
4. *Diamond Dogs* (1974)
5. *Hunky Dory* (1971)

These albums contain the five most-streamed canonical Bowie studio compositions in the existing 25 September 2026 dataset: *Starman*, *“Heroes”*, *Space Oddity*, *Rebel Rebel* and *Life on Mars?*.

## Parent data

The source spine reuses the validated Bowie track dataset:

`archive/projects/2026-09-david-bowie-track-length-success/data/david_bowie_tracks_success.csv`

## Final enriched dataset

`data/five_album_audio_features.csv`

- 53 canonical tracks
- 51 confident ReccoBeats audio-feature matches
- Missing feature rows: *Neuköln* and *(Don’t Sit Down)*
- Missing rows retain canonical duration; no feature values are imputed

Coverage:
- Ziggy Stardust: 11/11
- Diamond Dogs: 11/11
- Hunky Dory: 11/11
- Heroes: 9/10
- Space Oddity: 9/10

## Source strategy

- Canonical sequence/duration: validated MusicBrainz-based parent dataset
- Current streams: Spotify/Kworb snapshot dated 25 September 2026
- Audio features: ReccoBeats Spotify-style descriptors
- Matching hierarchy:
  1. validated Spotify/Kworb version identity when resolvable;
  2. positively identified ReccoBeats album tracklist;
  3. strict David Bowie artist-catalogue title/duration fallback.

## Locked chart template

- rows = tracks in original album order
- bar length = canonical track duration
- bar colour = Tempo
- compact horizontal global Tempo key
- right-side dots = Energy, Valence, Acousticness
- red dot beside label = most-streamed matched track on the album
- missing audio-feature rows = duration retained, feature marks blank

## Final charts

- `output/ziggy_stardust_audio_profile.png`
- `output/heroes_audio_profile.png`
- `output/space_oddity_audio_profile.png`
- `output/diamond_dogs_audio_profile.png`
- `output/hunky_dory_audio_profile.png`

## Editorial route

**Can one Bowie song tell you the whole album?**

The hit is sometimes surprisingly central (*Starman*), sometimes structurally unusual but sonically typical (*“Heroes”*), and sometimes a poor guide to the album around it (*Rebel Rebel*).

## Next gate

Copy the exact final charts into site assets, add the feature image and Jekyll post, run Pages/Jekyll QA, then hand PR #80 to Adam for final approval before merge.
