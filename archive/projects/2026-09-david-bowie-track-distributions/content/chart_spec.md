# Chart spec: Every Bowie album has a shape

## Core chart

**Title:** Every Bowie album has a shape

**Subtitle:** Each dot is a track. Median and mean show the centre; red marks the most-streamed track. Labels call out formal duration outliers and selected streaming standouts.

## Layout

- Tall horizontal distribution plot.
- One row per studio album, chronological from 1967 to 2016.
- X-axis: canonical album-track duration in minutes.
- Y-axis: album year + album title.
- Every canonical track plotted at its exact duration.
- Target roughly 12 × 16–18 inches so 26 rows remain readable.

## Encoding

- **All tracks:** small light-grey circles.
- **Median:** short blue vertical tick.
- **Mean:** charcoal × or diamond.
- **Most-streamed track:** muted-red filled dot.
- **Tukey duration outlier:** thin charcoal outline or annotation.
- If the most-streamed track is also an outlier, label once.

## Labelling rule

Do not label all 26 most-streamed tracks.

Label:
1. every Tukey outlier where space permits;
2. a most-streamed track when it is at least 60 seconds from its album median;
3. selected editorial anchors.

Priority anchors:
- *Cygnet Committee* — 9:36
- *The Width of a Circle* — 8:09
- *Station to Station* — 10:14
- *Golden Years* — 4:01, most streamed on an album with a 6:02 median
- *Warszawa* — 6:24
- *“Heroes”* — 6:10, most streamed + outlier
- *Let's Dance* — 7:37, most streamed + outlier
- *Loving the Alien* — 7:11
- *Bring Me the Disco King* — 7:45
- *★* — 9:57

## Outlier rule

Use Tukey's 1.5 × IQR rule within each album.

Current result: **13 of 26 albums** contain at least one formal duration outlier.

Mean and median are both descriptive summaries. The chart should show when they diverge and why, not imply one is universally better.

## QA

- Keep the 0:44 “(Don’t Sit Down)” on *Space Oddity*: it is part of the validated canonical release.
- Keep the short *1. Outside* segues: they are part of the album distribution and explain the mean/median difference.
- Most-streamed status uses the existing 25 September 2026 Spotify/Kworb snapshot and is album-relative.
- Streaming is annotation/context, not causal evidence.
- Distribution must remain the visual hierarchy.

## Optional companion

If the primary chart becomes too dense, add a small ranked dumbbell of **mean vs median duration by album**.
