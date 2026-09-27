# Publication package: Can one Bowie song tell you the whole album?

## Editorial recommendation

Publish as the next Bowie follow-on after:

- *Bowie never needed the three-minute rule*
- *Every Bowie album has a shape*

This project starts with Bowie's five most-streamed canonical studio tracks and opens the albums behind them. Each chart keeps track length as the primary comparison, colours duration bars by Tempo, and adds Energy, Valence and Acousticness as aligned 0–1 feature strips.

The repeated red dot asks one question:

**How representative is the song everyone knows of the album around it?**

The answer is deliberately not binary. *Starman* is strikingly central on Energy and Valence; *Rebel Rebel* is much more energetic and much less acoustic than the median *Diamond Dogs* track; *“Heroes”* is a huge length outlier but sits exactly on its album's median Tempo and Valence.

## Published headline

**Can one Bowie song tell you the whole album?**

## Standfirst / excerpt

Start with Bowie's five most-streamed studio tracks, then open the albums behind them. Track length, tempo, energy, valence and acousticness show when the hit is a useful guide — and when it really isn't.

## Site post

`site/_posts/2026-09-27-can-one-bowie-song-tell-you-the-whole-album.md`

## Site asset folder

`site/assets/migrated/david-bowie-five-album-audio-profiles/`

Expected assets:

- `feature.svg`
- `ziggy-stardust.png`
- `heroes.png`
- `space-oddity.png`
- `diamond-dogs.png`
- `hunky-dory.png`

## Chart sequence

### 1. Inside Ziggy Stardust

**Editorial point:** *Starman* is longer and slower than the median track, but lands exactly on Ziggy's median Energy (0.449) and Valence (0.549), with Acousticness close to the album median.

**Caption:** *Starman* is the album's most-streamed track, but its Energy and Valence sit exactly at the Ziggy median. The red dot is an entry point, not an automatic outlier.

**Alt text:** Horizontal track-by-track profile of David Bowie's Ziggy Stardust album. Bar length shows duration and bar shade shows tempo; aligned dots show Energy, Valence and Acousticness. Starman is marked with a red dot as the most-streamed track. Its Energy and Valence align with the album median while its duration is longer and tempo slower than the typical track.

### 2. Inside Heroes

**Editorial point:** *“Heroes”* is 6:10 against a 3:48 album median, yet its Tempo (112.1 BPM) and Valence (0.435) are exactly at the album medians.

**Caption:** The title track is structurally unusual in length, but much less unusual in the album's wider sound profile.

**Alt text:** Horizontal profile of the Heroes album. The six-minute title track is the longest and is marked red as the most-streamed song. Its tempo and valence sit at the album medians. Neuköln has duration shown but blank audio-feature marks because no confident ReccoBeats match was available.

### 3. Inside Space Oddity

**Editorial point:** The title track is longer than the album median and close to its typical Tempo, but is lower-energy and less acoustic than the median matched track.

**Caption:** *Space Oddity* matches the album's pace better than its Energy or Acousticness profile.

**Alt text:** Horizontal profile of the Space Oddity album. The title track is marked red and runs 5 minutes 16 seconds. Cygnet Committee is the longest track at 9 minutes 36 seconds. Don’t Sit Down retains its 44-second duration but has blank audio-feature marks because no separate confident ReccoBeats match was available.

### 4. Inside Diamond Dogs

**Editorial point:** *Rebel Rebel* is one of the clearest non-typical hits: longer than the album median, more energetic (0.686 vs 0.476) and much less acoustic (0.209 vs 0.624).

**Caption:** The biggest track is close to the album's Tempo and Valence, but it is not a typical *Diamond Dogs* track on Energy or Acousticness.

**Alt text:** Horizontal profile of Diamond Dogs. Rebel Rebel is marked red as the most-streamed song. It is longer and more energetic than the album median and its acousticness is much lower than the album median. All eleven tracks have matched audio features.

### 5. Inside Hunky Dory

**Editorial point:** *Life on Mars?* is close to the album median in length and Tempo, but is less positive on Valence and more acoustic.

**Caption:** *Life on Mars?* looks typical in pace, less typical in mood.

**Alt text:** Horizontal profile of Hunky Dory. Life on Mars? is marked red as the most-streamed track. Its duration and tempo are close to the album centre, while its valence is lower and acousticness higher than the album medians.

## Feature-image metaphor

**One red entry point opens into five different sound paths.**

Create a square editorial illustration on the locked light-grey background. At the left, one restrained muted-red circular marker acts as the “hit”. From it, five black-and-charcoal waveform/ribbon paths fan out horizontally, each developing a different length, density and rhythm. The red marker is the only accent; the five divergent paths represent the albums that cannot be reduced to the entry-point song.

No text, Bowie likeness, lightning-bolt face paint, album artwork, logos or copyrighted imagery.

## Feature alt text

Square editorial illustration on a light-grey background showing one muted-red entry-point dot opening into five different black-and-charcoal waveform paths, representing five Bowie albums that develop differently beyond their best-known song.

## Method / comparability notes

- Five albums selected because they contain Bowie's five most-streamed canonical studio tracks in the **25 September 2026 Spotify/Kworb snapshot**.
- Canonical track identity, sequence and duration reuse the validated MusicBrainz-based Bowie parent dataset.
- Current streams reuse the dated Spotify/Kworb snapshot.
- Audio descriptors are **ReccoBeats Spotify-style audio features**, not newly retrieved Spotify Web API Audio Features.
- ReccoBeats features retained in the dataset include acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo and valence.
- Publication charts use Tempo, Energy, Valence and Acousticness.
- 51 of 53 canonical tracks have confident audio-feature matches.
- Missing: *Neuköln* on *Heroes* and *(Don’t Sit Down)* on *Space Oddity*. Their durations remain plotted and their feature marks are blank.
- No missing audio-feature values are imputed.
- The Tempo colour scale is global across all five charts; Energy, Valence and Acousticness use fixed 0–1 scales.
- ReccoBeats values are descriptive model-derived audio descriptors. They should not be treated as objective judgements about artistic quality, mood or genre.
- Streams are contextual only. The charts do not claim that any audio feature caused a track's popularity.

## LinkedIn

Can one song tell you what an album sounds like?

I started with David Bowie's five most-streamed canonical studio tracks:

Starman. “Heroes”. Space Oddity. Rebel Rebel. Life on Mars?

Then I opened the albums around them — **53 tracks in total** — and added track length, tempo, Energy, Valence and Acousticness.

The red dot in each chart is the song most people currently stream.

A few things surprised me:

- *Starman* lands **exactly on Ziggy's median Energy and Valence**
- *“Heroes”* is a 6:10 length outlier, but its Tempo and Valence sit exactly at the album medians
- *Rebel Rebel* is much more energetic and far less acoustic than the typical *Diamond Dogs* track
- *Life on Mars?* is close to *Hunky Dory* in pace, but lower in Valence and more acoustic
- *Heroes* is the highest-energy and least-acoustic album of the five by median feature values

So the biggest song can be a good guide to one part of an album and a terrible guide to another.

Five albums. Five entry points. A lot more going on behind the red dot.

Full story on **coffeetableviz.com**.

## Instagram

Can one Bowie song tell you the whole album?

I took his five most-streamed canonical studio tracks and opened the albums behind them.

**53 tracks. Five albums.**

Each chart shows:
- length
- tempo
- Energy
- Valence
- Acousticness

Red dot = the album's most-streamed track.

My favourite contrast:

*Starman* sits exactly on Ziggy's median Energy and Valence.

*Rebel Rebel* does the opposite — much more energetic and much less acoustic than the typical *Diamond Dogs* track.

The hit is an entry point. It isn't always the album.

Full story on **coffeetableviz.com**.

## X / short social

Can one Bowie song tell you the whole album?

5 biggest studio tracks → 5 albums → 53 songs.

Length + tempo + Energy + Valence + Acousticness.

*Starman* is surprisingly typical.
*Rebel Rebel* really isn't.

Five album profiles on coffeetableviz.com.

## QA checklist

- [x] Five-album canonical spine contains 53 tracks.
- [x] Final audio-feature coverage is 51/53.
- [x] Ziggy Stardust 11/11 matched.
- [x] Diamond Dogs 11/11 matched.
- [x] Hunky Dory 11/11 matched.
- [x] Heroes 9/10 matched.
- [x] Space Oddity 9/10 matched.
- [x] Missing rows are shown transparently with blank feature marks.
- [x] All five final charts use the locked visual template.
- [x] Tempo colour scale is global across the five charts.
- [x] Energy, Valence and Acousticness use consistent 0–1 scales.
- [x] Red most-streamed marker is consistent and restrained.
- [x] No chart title, subtitle or track label clipping found in visual QA.
- [ ] Exact final chart PNGs copied byte-for-byte into site assets.
- [ ] Feature image committed and referenced by Jekyll post.
- [ ] Pages/Jekyll PR build passes.
- [ ] Adam approves final publication package before merge.
