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
- Use an extended wide canvas (current draft: 14.5 × 17.5 inches) so all 26 red labels fit without clipping.

## Encoding

- **All tracks:** small light-grey circles.
- **Median:** short blue vertical tick.
- **Mean:** charcoal × or diamond.
- **Most-streamed track:** muted-red filled dot.
- **Tukey duration outlier:** thin charcoal outline or annotation.
- If the most-streamed track is also an outlier, label once.

## Labelling rule

Label **all 26 album-level most-streamed tracks** in muted red.

To keep the distribution readable, grey outlier labels are selective rather than exhaustive:
1. every red most-streamed track is labelled;
2. if a red track is also a Tukey outlier, add “outlier” to the red label;
3. for other Tukey outliers, label only the single most extreme non-red outlier per album;
4. place grey labels on the opposite vertical side from the red label where possible.

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
