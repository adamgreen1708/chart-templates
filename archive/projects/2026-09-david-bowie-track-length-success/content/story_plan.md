# David Bowie track length, style and success — story plan

## Dataset read

The final canonical dataset contains **275 original studio-album tracks across 26 lifetime David Bowie solo studio albums**, from the 1967 debut through *Blackstar* (2016).

QA status:

- 26/26 validated studio albums represented;
- 275 canonical album-track rows;
- 0 missing track durations;
- original-album track counts enforced album by album;
- 239/275 album-track rows matched to a current Spotify/Kworb composition;
- Spotify snapshot date: **25 September 2026**;
- 49/275 album-track rows match at least one David Bowie entry on the main UK Official Singles Chart;
- Official Charts reissues with year-labelled titles are folded back to the same composition;
- AllMusic Styles are currently the validated **album-level** taxonomy inherited by each track, not a claim of song-level style classification.

The release-selection QA caught and fixed two important errors before story work: the shortened 12-track US edition of the 1967 debut and a multi-layer *Reality* SACD that duplicated the album programme.

## Strongest analytical findings

### 1. Bowie tracks got longer — but not in a straight line

Median studio-album track length by decade:

| Decade | Median |
|---|---:|
| 1960s | 3:09 |
| 1970s | 3:39 |
| 1980s | 4:19 |
| 1990s | 4:49 |
| 2000s | 4:16 |
| 2010s | 4:10 |

Album medians show the variation more clearly:

- *David Bowie* (1967): 2:49;
- *Pin Ups* (1973): 2:50;
- *Low* (1977): 3:03;
- *Let's Dance* (1983): 4:59;
- *Earthling* (1997): 5:00;
- *The Buddha of Suburbia* (1993): 5:24;
- *Station to Station* (1976): 6:02.

So the career is not a simple drift toward longer songs. Bowie repeatedly changes the shape of an album as well as its sound.

### 2. The AllMusic style labels line up with very different track-length profiles

Using the complete album-level AllMusic Styles taxonomy and describing these correctly as **tracks on albums tagged with a style**:

| AllMusic album Style | Track rows | Median track length |
|---|---:|---:|
| Blue-Eyed Soul | 43 | 4:45 |
| Dance-Rock | 134 | 4:24 |
| Art Rock | 238 | 4:18 |
| Album Rock | 160 | 4:02 |
| Proto-Punk | 111 | 3:37 |
| Glam Rock | 64 | 3:29 |
| Singer/Songwriter | 22 | 3:24 |

These categories overlap heavily and are album-level metadata, so they must not be presented as mutually exclusive song genres or as causal explanations. The useful story is that Bowie's stylistic eras coincide with noticeably different song structures.

### 3. Shorter did not mean more successful

Among the 237 unique canonical compositions with a current matched Spotify stream count, the Pearson correlation between album-track duration and log10 current streams is only **r = 0.11**.

Other useful checks point in the same direction:

- the median album version of a track that reached the main UK Official Singles Chart is **4:34**;
- the median for tracks without a main UK singles-chart match is **4:02**;
- **15 of the current top 20 matched studio compositions are at least four minutes long**;
- the top 10 matched compositions account for about **62.8%** of streams within the matched canonical studio-track set.

Examples:

| Track | Album version | Current streams | Best UK main-chart peak |
|---|---:|---:|---:|
| Starman | 4:10 | 829.9m | 10 |
| “Heroes” | 6:10 | 739.8m | 12 |
| Space Oddity | 5:16 | 517.4m | 1 |
| Rebel Rebel | 4:34 | 462.5m | 5 |
| Life on Mars? | 3:54 | 406.1m | 3 |
| Let's Dance | 7:37 | 403.4m | 1 |

Important comparability note: the duration is the canonical **album version**, while historical chart success belongs to the composition/single release. Some singles used shorter edits. That difference is editorially useful, but it must be explained rather than hidden.

## Recommended story route

**Bowie’s songs changed shape as often as they changed style — and he never needed the three-minute rule to make them successful.**

This is stronger than a simple “long songs are successful” claim. The data does not support that. Instead it supports three connected observations:

1. track length changed substantially across Bowie's catalogue;
2. those shifts coincide with different AllMusic style eras;
3. there is very little evidence that shorter album tracks have a current-streaming advantage.

## Recommended three-chart story

### Chart 1 — **Bowie stretched the song**

**Role:** Set the scene.

**Story question:** How did the typical length of a Bowie album track change across his career?

**Chart type:** Connected dot/line timeline of median track duration by studio album, with individual-track range or subtle distribution context where readable.

**Data needed:** Album, year, median duration, track count; optional min/max or quartiles.

**Key stats:** Career median 4:10; decade medians rise from 3:09 in the 1960s to 4:49 in the 1990s before easing back. *Station to Station* has a 6:02 album median.

**Why it matters:** It establishes that “Bowie track length” is not a fixed characteristic. The structure of the records changes markedly through the catalogue.

**QA risk:** Albums with interludes or instrumentals can produce unusual distributions. Use medians rather than means and show album track count/context.

### Chart 2 — **Style changed the clock**

**Role:** Build the tension.

**Story question:** Do Bowie's AllMusic style eras coincide with different typical track lengths?

**Chart type:** Ranked dot plot of median track duration for selected recurring AllMusic album Styles.

**Data needed:** Exploded album Style × canonical track rows; style track count and number of albums represented.

**Key stats:** Tracks on albums tagged Blue-Eyed Soul have a 4:45 median; Dance-Rock 4:24; Glam Rock 3:29; Singer/Songwriter 3:24.

**Why it matters:** It connects the new track-length dataset directly to the AllMusic taxonomy from the earlier Bowie project and shows that reinvention changed the *shape* of the songs, not just their labels.

**QA risk:** Styles overlap and are currently album-level. Wording must be “tracks on albums tagged…” rather than “songs in the style…”. Prefer styles represented on at least two albums and show n.

### Chart 3 — **The hits weren't short**

**Role:** Land the aha moment.

**Story question:** Are shorter Bowie album tracks more popular now?

**Chart type:** Scatter plot: album-track duration on x, log current Spotify streams on y. Distinguish compositions that have / have not appeared on the main UK Official Singles Chart. Label only the strongest story points.

**Data needed:** Canonical duration, matched streams, UK chart flag/peak, title/year.

**Key stat:** Duration vs log current streams **r = 0.11** — essentially little linear relationship in this catalogue. Fifteen of the current top 20 matched studio tracks are at least four minutes long.

**Highlight candidates:** *Starman*, *“Heroes”*, *Space Oddity*, *Let's Dance*, *Moonage Daydream*.

**Why it matters:** It overturns the tempting “short songs win” assumption without replacing it with another overclaim.

**QA risk:** Current streams are a 2026 snapshot, not original-era popularity. Historical chart status is composition-level and sometimes refers to shorter single edits. Both distinctions belong in the subtitle/method note.

## Strong spin-off story — **The afterlife of a hit**

This should be retained as a fourth-chart or later-post candidate rather than weakening the main length/style story.

Highest-streamed matched studio tracks with **no main UK Official Singles Chart match for the canonical title** include:

- *Moonage Daydream* — 294.1m;
- *The Man Who Sold the World* — 159.2m;
- *Suffragette City* — 89.7m;
- *Five Years* — 71.6m;
- *Oh! You Pretty Things* — 71.3m;
- *Rock ’n’ Roll Suicide* — 63.5m.

That suggests a separate story about how streaming has created a Bowie canon that is not identical to the contemporary singles chart.

## Single-edit extension

There is also a strong small-multiple/dumbbell extension comparing album versions with commercial single edits.

Two verified examples already make the point:

- *Let's Dance*: album form is over seven minutes; AllMusic notes it was edited for single release.
- *“Heroes”*: the current remastered album version is 6:11, while Rhino lists the remastered single version at 3:35.

This is likely better as an annotated sidebar or fourth chart unless a complete, reliably sourced single-edit dataset can be built.

## Next build step

Create only the three derived chart datasets above, then create the three chart configs under the locked 538 template and render/QA them.

Do **not** publish a site post yet. The next gate is Adam's review of the three rendered charts.
