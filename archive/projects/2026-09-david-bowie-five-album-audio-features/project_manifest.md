# Project manifest: Bowie five-album audio profiles

## Status

- Started: 27 September 2026
- Working branch: `project/2026-09-david-bowie-five-album-audio-features`
- Scope: five albums associated with David Bowie's five most-streamed canonical studio tracks in the 25 September 2026 snapshot
- Visual template: **duration + tempo + energy + valence + acousticness**
- Analysis status: **complete**
- Publication package: **complete**
- PR: #80
- Site packaging: **complete; final PR validation pending**
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
- *Space Oddity* limitation: title-track features resolve to the 2009 remaster; the remaining accepted feature rows resolve to ReccoBeats 2019 Mix equivalents where exact 2015-remaster feature records were unavailable

Coverage:
- Ziggy Stardust: 11/11
- Diamond Dogs: 11/11
- Hunky Dory: 11/11
- Heroes: 9/10
- Space Oddity: 9/10

## Source strategy

- Canonical identity/duration: validated MusicBrainz-based parent dataset
- Running order: checked against official David Bowie album pages; *Heroes* corrected to the original 1977 sequence before final render
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

## Site package

- `site/_posts/2026-09-27-can-one-bowie-song-tell-you-the-whole-album.md`
- `site/assets/migrated/david-bowie-five-album-audio-profiles/feature.svg`
- five final chart PNGs under the same asset folder
- final site PNGs are copied from the approved project outputs; *Heroes* was resynced after the running-order correction

## Final QA

- temporary order-rebuild workflow removed
- five site chart PNGs match their final project-output Git blob SHAs exactly
- final site-content PR workflow passed in run `36344254770`
- Blockbuster Quote validator passed
- Data Lens validator passed
- Jekyll build passed
- Pages artifact upload passed

## Next gate

Adam reviews PR #80 and approves the merge. After merge, verify the main-branch Pages deployment and live URL before calling the post published.
