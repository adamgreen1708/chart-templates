# David Bowie track length, style and success — early story scan

This is a **discovery pass**, not the final three-chart plan. It uses the current top-nine solo Spotify tracks plus the previously validated album-level AllMusic Styles. The complete canonical track table still needs to be built and inspected before chart configs are created.

## Early finding 1 — the biggest catalogue songs are not especially short

For the current nine leading solo tracks in the Spotify/Kworb ranking:

- 7 of 9 are at least four minutes long;
- the median duration is **4:39**;
- the mean is about **4:59**;
- *Let's Dance* is 7:37 in the album version and *Heroes* is 6:11 in the current Spotify artist-page version.

That immediately weakens a simple “shorter song = bigger song” hypothesis.

### Story potential

**Working angle:** *Bowie did not need three minutes to make a hit.*

The more interesting follow-up is likely not a straight correlation. It is the distinction between:
- original album length;
- shorter single/radio edits;
- historic chart success;
- current streaming of the longer canonical/remastered versions.

This could produce a strong before/after or dumbbell story for songs such as *Let's Dance*, *Heroes* and *Young Americans*.

## Early finding 2 — current listening is highly concentrated

The nine leading solo tracks sum to about **4.21 billion streams**, roughly **50%** of the 8.38 billion solo streams shown on the same Kworb artist snapshot.

That makes “the catalogue is huge, but current listening clusters around a relatively small canon” a plausible scene-setting story.

### Story potential

**Working angle:** *Half the streams live in nine songs.*

We should verify the share again when the canonical-version matching is complete, because Kworb counts individual Spotify track versions and remasters separately.

## Early finding 3 — the streaming afterlife may be more interesting than original chart success

Several heavily streamed catalogue tracks were not straightforward contemporary UK singles hits.

Examples already visible in the current ranking include:
- *Moonage Daydream* — roughly 294m streams;
- *Five Years* — roughly 72m;
- *Queen Bitch* — roughly 49m;
- *Lady Stardust* — roughly 45m;
- *Soul Love* — roughly 43m.

The likely story is not “the charts were wrong”. It is that **release-period commercial success and long-run catalogue popularity are different measures**.

### Story potential

**Working angle:** *Some Bowie songs became hits after the charts had stopped counting them.*

This becomes much stronger once every canonical album track is joined to Official Charts data and a current stream snapshot.

## Early finding 4 — style may explain length better than success

The AllMusic metadata suggests plausible structural differences between eras and style families:
- early theatrical/psychedelic material contains many short tracks;
- art/experimental eras include very short instrumentals as well as long pieces;
- dance-oriented 1980s albums contain long album versions that were often shortened for singles.

A single average by style will probably hide this. Distribution plots or within-album comparisons are likely better.

## Song-level AllMusic Styles: useful, but a QA trap

Fresh research confirms AllMusic has song-level Styles. That is promising, but global title searches surfaced duplicate song entities for some Bowie titles with different style sets.

Therefore the robust method is:
1. start from the correct album page;
2. follow that album's exact track link;
3. capture Styles from that specific song entity;
4. retain the AllMusic song URL/ID in the dataset.

Until that enrichment is complete, album-level Styles remain the reproducible full-catalogue baseline.

## Provisional story routes

### Route A — strongest at present: **Long songs, short edits, big hits**
Core argument: Bowie's most durable songs often have substantial album runtimes; commercial single edits shortened some of them, but today's listeners still stream long versions at scale.

Likely chart sequence:
1. Track-length distribution across the 26-album catalogue.
2. Album version vs single-edit length for charting songs.
3. Current streams vs original UK chart success, highlighting long-form catalogue giants.

### Route B — **The afterlife of a hit**
Core argument: current streaming popularity is only partly explained by original UK singles-chart performance.

Likely chart sequence:
1. Original UK singles success.
2. Current Spotify stream ranking for canonical album tracks.
3. Biggest “afterlife” gaps: album tracks/non-hits that now outperform many original singles.

### Route C — **Bowie by the minute**
Core argument: track length changes as Bowie moves between style eras, but not in a tidy linear direction.

Likely chart sequence:
1. Track length through time.
2. Distribution by AllMusic style family / album style.
3. Outliers: very short and very long tracks, annotated with success and era.

## Current recommendation

Build the full canonical track-duration table and the UK-chart join, then re-run story discovery. At this point **Route A** is the most promising because it connects all three requested ingredients — length, success and style/era — without forcing a dubious single “popularity score”.
