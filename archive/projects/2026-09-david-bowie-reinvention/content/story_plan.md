# David Bowie reinvention — story plan

## Dataset read

The focus dataset now contains **26 lifetime David Bowie studio albums** from the 1967 debut through *Blackstar* in 2016.

Scope decisions are explicit:

- include *The Buddha of Suburbia* (1993): the official Bowie store identifies it as the 19th studio album even though MusicBrainz also classifies it as a soundtrack;
- exclude *Toy* from the lifetime chronology: Bowie's official archive describes it as previously unreleased, with its standalone release arriving in 2022;
- exclude live albums, compilations and *David Bowie Narrates Prokofiev's Peter and the Wolf*;
- keep Tin Machine outside Bowie's solo studio-album sequence.

AllMusic exposes album-level Styles metadata for **25 of the 26** scoped albums. Its current *The Next Day* page exposes no Styles values. MusicBrainz genres for *The Next Day* are retained as supplemental context but are deliberately not mixed into the AllMusic similarity calculation.

That leaves **23 of 25 adjacent album transitions** with a like-for-like AllMusic style-reset score.

## What the data says

- 26 studio albums.
- 1967 to 2016: a 49-year difference between first and last album years.
- Albums appear in six named calendar decades: 1960s through 2010s.
- The longest album-year gap in the scoped chronology is 10 years, from *Reality* (2003) to *The Next Day* (2013).
- Across the 25 albums with AllMusic Styles metadata there are 24 distinct style labels.
- The three most ubiquitous AllMusic labels are very broad: Contemporary Pop/Rock appears on 24 of 25 tagged albums, Art Rock on 23, and Experimental Rock on 22.
- Median adjacent-album style reset across the 23 measurable transitions is 0.3333.
- The highest measured reset is the 1967 debut -> *Space Oddity* (0.8889).
- Other large measured resets include *Tonight* -> *Never Let Me Down* (0.7500), *Diamond Dogs* -> *Young Americans* (0.6667), *Let's Dance* -> *Tonight* (0.6250), *Scary Monsters* -> *Let's Dance* (0.6000), and *The Buddha of Suburbia* -> *1. Outside* (0.6000).

The metric also exposes a limitation that is editorially useful: the famous *Station to Station* -> *Low* shift scores only 0.3333 because broad AllMusic umbrella labels remain shared. The data detects taxonomy turnover; it does not directly measure artistic daring.

## Ranked story options

### 1. How do you measure a chameleon? — recommended

**Core argument:** Bowie's catalogue plainly changes across six decades, but a transparent attempt to quantify “reinvention” shows both the movement and the limits of genre metadata.

**Why it works:** it combines music, data and visualisation rather than producing a subjective “most reinvented artist” league table. The surprising part is not merely that Bowie changes; it is that the measurement itself has something to teach us.

**Data required:** the 26-album chronology, AllMusic Styles sets, the adjacent-album Jaccard calculation, and the explicit missing-data flag for *The Next Day*.

**Risk / weakness:** readers must understand that the reset score describes metadata overlap, not creativity or quality.

### 2. Six decades, repeated pivots

**Core argument:** Bowie repeatedly moved into and out of style families across a 49-year album chronology.

**Why it works:** direct, recognisable and visually rich.

**Risk / weakness:** without the measurement caveat it can overstate what style labels prove.

### 3. Long careers are not the same as reinvention

**Core argument:** use Bowie alongside Dylan, Elton John, Cher, Neil Young, Paul McCartney, Springsteen and the Rolling Stones to separate longevity from stylistic change.

**Why it is third:** the peer cohort is valuable context, but current discography rules become inconsistent quickly (solo vs band work, collaborative albums, soundtracks, posthumous releases and very recent 2026 releases). It is better as a later extension than as the first Bowie story.

## Recommended three-chart narrative

### Chart 1 — Six decades. Twenty-six albums.

- **Role:** Set the scene.
- **Story question:** What does Bowie's lifetime studio-album chronology actually look like?
- **Chart type:** timeline dot plot / album strip.
- **Data needed:** sequence, year, title.
- **Key stat:** 26 albums from 1967 to 2016 across six named decades; the longest gap is 10 years.
- **Why this chart matters:** establishes the longevity and cadence before attempting to measure change.
- **Potential issue / QA risk:** multiple albums share years; title labels need selective annotation to avoid crowding.

### Chart 2 — The labels rarely sit still

- **Role:** Build the tension.
- **Story question:** Which style descriptors appear, disappear and return across the album sequence?
- **Chart type:** album-by-style dot matrix.
- **Data needed:** long-form album/style rows derived from `david_bowie_studio_albums.csv`.
- **Key stat:** 24 distinct AllMusic style labels across 25 tagged albums.
- **Recommended display rule:** show the distinctive descriptors in the main matrix and treat the three near-ubiquitous umbrella labels as context, not as the visual story.
- **Why this chart matters:** lets the reader see glam, soul/dance, alternative and other labels moving through the chronology without reducing Bowie to a single genre per album.
- **Potential issue / QA risk:** the display filter must be explicitly documented and must not alter the underlying reset calculation.

### Chart 3 — A reinvention score gets awkward

- **Role:** Land the aha moment.
- **Story question:** What happens when we reduce adjacent-album style change to one transparent number?
- **Chart type:** timeline / lollipop of Jaccard style-reset scores by destination album.
- **Data needed:** `david_bowie_style_transitions.csv`.
- **Key stat:** 23 measurable transitions; median reset 0.3333. The largest is debut -> *Space Oddity* at 0.8889, while *Station to Station* -> *Low* is only 0.3333.
- **Why this chart matters:** it gives us the Bowie story and the data-story punchline. Reinvention is visible, but taxonomy is not artistic truth.
- **Potential issue / QA risk:** the two transitions involving *The Next Day* must be shown as missing rather than zero, and the title/subtitle must not imply an objective creativity score.

## Recommended story route

**How do you measure a chameleon?** David Bowie gives us 26 studio albums across six named decades. Style metadata shows repeated movement, but the attempt to score “reinvention” also reveals how much the answer depends on the labels we use.

## Next build step

Await Adam's editorial approval of this route. After approval:

1. derive the long album/style dataset for Chart 2;
2. derive the chart-specific transition dataset for Chart 3;
3. create the three locked 538 configs;
4. render and run the chart QA checklist;
5. only then move to publication copy and feature artwork.

No chart configs or renders should be created before this approval gate.
