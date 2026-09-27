# Ziggy Stardust prototype findings

## Coverage

- 11 canonical album tracks in the parent dataset.
- 10/11 have confident ReccoBeats Spotify-style audio-feature matches.
- The 10 accepted rows match the 2012-remaster title used in the existing streaming spine.
- *Moonage Daydream* is deliberately not assigned audio features: the closest available ReccoBeats title/duration fallback differed by 11.8 seconds, which fails the tightened alternate-version QA rule.
- Its canonical MusicBrainz duration remains visible in the chart, with audio-feature marks left blank.

## Prototype visual

**Title:** Inside Ziggy Stardust

Primary encoding:
- horizontal bar length = canonical track duration;
- bar colour = ReccoBeats tempo;
- red outline = most-streamed track on the album (*Starman*).

Right-hand feature panels:
- Energy
- Valence
- Danceability

## What the data is saying

### Tempo has real spread

Among matched tracks:
- *Ziggy Stardust*: 160.5 BPM
- *Five Years*: 152.5 BPM
- *Suffragette City*: 142.6 BPM
- *Soul Love*: 72.9 BPM

That makes tempo a useful colour encoding because the album contains a broad pace range.

### Energy and valence are highly discriminating

Energy:
- highest: *Suffragette City* 0.888
- *Star* 0.856
- *Hang On to Yourself* 0.788
- lowest: *It Ain’t Easy* 0.279

Valence:
- highest: *Hang On to Yourself* 0.936
- *Suffragette City* 0.793
- *Soul Love* 0.709
- lowest: *It Ain’t Easy* 0.177

### Danceability is comparatively compressed

Matched-track danceability runs only from:
- 0.434 (*Ziggy Stardust*)
- to 0.593 (*Lady Stardust*)

It is valid data, but it creates less visual separation than the other features.

### Acousticness may be a better third mini-panel

Acousticness ranges from:
- 0.017 (*It Ain’t Easy*)
- to 0.615 (*Lady Stardust*)

That is much stronger visual variation than danceability and may tell a more useful album-structure story.

Liveness also varies materially (0.045–0.540), but its interpretation is less immediately intuitive for a general audience.

## Recommendation before scaling to the other albums

Keep:
1. duration as the dominant encoding;
2. tempo as bar colour;
3. energy;
4. valence.

For the third mini-panel, compare:
- **Danceability** — familiar and intuitive, but compressed on Ziggy;
- **Acousticness** — much stronger variation on Ziggy and potentially more revealing.

Do not enrich/render the other four albums until Adam has reviewed this prototype and chosen the final mini-panel set.
