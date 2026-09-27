# Source and matching plan

## Existing canonical spine

The five-album input file contains **53 tracks** from the validated parent Bowie dataset.

Album counts:

- Ziggy Stardust: 11
- Heroes: 10
- Space Oddity: 10
- Diamond Dogs: 11
- Hunky Dory: 11

## Audio-feature source

Spotify's own Web API Audio Features / Audio Analysis access is restricted for new/development-mode applications, so this project uses **ReccoBeats Spotify-style audio features** with explicit attribution.

Retained fields:
- acousticness
- danceability
- energy
- instrumentalness
- liveness
- loudness
- speechiness
- tempo
- valence

Publication visuals use Tempo, Energy, Valence and Acousticness.

## Final matching approach

1. Reuse exact canonical track identity, title, duration and current stream version from the validated parent Bowie dataset.
2. Parse the dated Kworb Bowie table for Spotify track IDs where available.
3. Attempt ReccoBeats track resolution from the validated Spotify version identity.
4. Search ReccoBeats for the exact album and fetch its tracklist.
5. Choose the album candidate with the strongest canonical title coverage and closest duration agreement.
6. Match within the positively identified album tracklist, allowing up to 12 seconds of mastering-duration drift.
7. Only then fall back to the wider David Bowie artist catalogue, where non-exact title matches use a stricter 5-second duration tolerance.
8. Preserve match method, ReccoBeats track ID, returned title, candidate count and duration difference in the output.

## Final QA

- 53 canonical rows.
- 51 confident feature matches.
- 2 intentionally blank feature rows:
  - *Neuköln* — no confident ReccoBeats title match.
  - *(Don’t Sit Down)* — no separate confident ReccoBeats title match.
- No missing values imputed.
- Every matched row has Tempo > 0.
- Energy, Valence, Acousticness and other 0–1 features stay within range.
- Loudness remains in dB.
- The global Tempo scale spans the actual matched five-album range.
- All five charts retain original album order.

## Attribution language

Use **ReccoBeats Spotify-style audio features**.

Do not describe the values as freshly retrieved Spotify Web API Audio Features.
