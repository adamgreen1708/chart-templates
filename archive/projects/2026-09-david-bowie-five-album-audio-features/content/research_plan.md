# Source and matching plan

## Existing canonical spine

The five-album input file contains **53 tracks** from the validated parent Bowie dataset.

Album counts:

- Ziggy Stardust: 11
- Heroes: 10
- Space Oddity: 10
- Diamond Dogs: 11
- Hunky Dory: 11

## Why ReccoBeats

Spotify announced that new Web API use cases and development-mode apps cannot access Audio Features or Audio Analysis. Existing extended-access apps may retain access, but this repo does not assume such access.

The prototype therefore uses ReccoBeats, a no-auth API that exposes Spotify-style audio descriptors.

## Matching approach

1. Search ReccoBeats for the exact artist name **David Bowie**.
2. Require a unique exact artist-name result.
3. Retrieve the artist's ReccoBeats track catalogue with pagination.
4. Normalise track titles to remove common remaster/mix suffixes and punctuation differences.
5. Match the canonical *Ziggy Stardust* title.
6. If multiple ReccoBeats versions match, choose the candidate with duration closest to the canonical album duration.
7. Preserve ReccoBeats track ID, returned title, returned duration and absolute duration difference for QA.
8. Reject a match if title normalisation fails or the closest candidate differs by more than 12 seconds.
9. Fetch the nine documented audio-feature values for the accepted ReccoBeats track ID.

## QA gates

- exactly 11 canonical Ziggy rows
- no duplicated canonical track title
- at least 10/11 tracks with accepted ReccoBeats matches before rendering
- every accepted match has a documented source ID
- duration-difference field retained
- tempo must be > 0 where present
- 0–1 fields must be within range
- loudness retained in dB and not normalised silently
- no interpolation or invented values for missing tracks

## Attribution

Call these **ReccoBeats Spotify-style audio features**, not “Spotify audio features from Spotify”.
