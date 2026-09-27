# Publication package: Every Bowie album has a shape

## Editorial recommendation

Publish this as a short follow-on to **Bowie never needed the three-minute rule**.

The previous post deliberately used album medians to compare the catalogue cleanly. This mini-post asks what that summary hides by plotting all **275 canonical studio-album tracks across 26 albums**.

The main editorial point is:

**The most famous track is not necessarily the most representative track.**

Mean, median, formal duration outliers and the album's most-streamed matched track all sit on the same distribution, so the chart does the analytical work rather than requiring a second companion visual.

## Published headline

**Every Bowie album has a shape**

## Standfirst / excerpt

An album average gives you one number. Plot every David Bowie studio-album track and the catalogue looks much less tidy: long tails, short interludes, famous outliers, and albums where the most-streamed song is not especially representative of the album around it.

## Story sequence

1. **Distribution is the story**  
   Plot every one of the 275 canonical tracks rather than collapsing each album to one median.

2. **Mean and median can disagree for a reason**  
   *Blackstar* has a 5:53 mean versus a 4:52 median; *1. Outside* reverses the pattern at 3:56 versus 4:22.

3. **The famous track is not always typical**  
   *Let's Dance* is 7:37 against a 4:59 album median; *“Heroes”* is 6:10 against 3:48; *Golden Years* is 4:01 against *Station to Station*'s 6:02 median.

4. **Outliers are part of the album shape**  
   13 of 26 albums contain at least one formal Tukey track-length outlier.

## Site post

`site/_posts/2026-09-27-every-bowie-album-has-a-shape.md`

## Site assets

- `site/assets/migrated/david-bowie-track-distributions/feature.svg`
- `site/assets/migrated/david-bowie-track-distributions/bowie-track-distribution-01.png`

## Feature-image metaphor

**The distribution itself becomes the illustration.**

Several horizontal album-like rows contain clusters of small grey track dots. Blue median ticks and charcoal mean crosses sit near each row's centre, while a single muted-red dot is deliberately displaced from the cluster on the hero row. The image communicates the specific approved tension: a summary centre can look tidy while an important track sits somewhere else in the distribution.

No Bowie likeness, lightning bolt, album artwork, logos or text.

## Feature alt text

Editorial illustration on a light-grey background showing several horizontal track distributions made of grey dots, with blue median marks, charcoal mean crosses and one muted-red standout dot sitting away from the centre.

## Blog excerpt

Averages are useful. They also hide things. Plot all 275 canonical Bowie studio-album tracks and the catalogue turns into a set of very different shapes — including albums where the most-streamed song sits nowhere near the middle.

## LinkedIn

Averages are useful. They are also sneaky.

For the Bowie track-length project, the first post used album medians. Helpful, clean, readable.

But I wanted to see what the averages were hiding.

So I plotted **every canonical studio-album track** across Bowie's **26 solo studio albums** — **275 tracks** in total — then added the album mean, median and most-streamed track.

A few things jump out:

- **13 of 26 albums** contain at least one formal duration outlier
- *Blackstar* has a **4:52** median but a **5:53** mean
- *1. Outside* goes the other way: **4:22** median, **3:56** mean
- *“Heroes”* and *Let's Dance* both have their most-streamed song sitting well away from the album centre
- *Golden Years* is the most-streamed track on *Station to Station*, even though it is much shorter than that album's median

The most famous song is not always the most representative one.

That is why distribution matters.

Full chart and write-up on **coffeetableviz.com**.

## Instagram

Every Bowie album has a shape.

This follow-on chart plots **all 275 canonical studio-album tracks** across **26 albums**.

Grey dots = tracks  
Blue mark = median  
Black × = mean  
Red dot = the album's most-streamed track

The useful bit: the famous song is not always the typical one.

- *Let's Dance*: **7:37** vs album median **4:59**
- *“Heroes”*: **6:10** vs **3:48**
- *Golden Years*: **4:01** vs *Station to Station* median **6:02**

Distribution is the story.

Full post on **coffeetableviz.com**.

## X / short social

Every Bowie album has a shape.

I plotted all **275 canonical studio-album tracks** across **26 albums**.

Grey = tracks  
Blue = median  
× = mean  
Red = album's most-streamed track

The best-known song is not always the most representative one.

More on coffeetableviz.com.

## Chart caption

Each row is an album. Grey dots are tracks, blue marks show the median, charcoal × marks the mean, and red highlights the album's most-streamed matched track.

## Chart alt text

Distribution chart of David Bowie album track lengths. Each row is one studio album, each grey dot is a track, blue vertical marks show album medians, charcoal crosses show means, and red dots show the most-streamed matched track on each album. Selected grey labels mark formal duration outliers. The chart shows that several famous tracks sit well away from their album's centre.

## Method / comparability notes

- Reuses the validated **275-track / 26-album** canonical dataset from the parent Bowie project.
- Track durations are the canonical album versions from the MusicBrainz-based parent dataset.
- Mean and median are calculated within each album.
- Formal duration outliers use Tukey's **1.5 × IQR** rule within each album.
- **13 of 26 albums** contain at least one formal duration outlier under that rule.
- The red point is the most-streamed matched track **within that album**, using the existing Spotify/Kworb snapshot dated **25 September 2026**.
- Streaming is contextual annotation only; the chart does not claim duration caused popularity.
- Short segues and interludes remain in the distribution when they are part of the validated canonical album release.
- The full chart labels all 26 red points and selectively labels the most extreme non-red outliers to preserve legibility.

## QA checklist

- [x] Uses the validated 275-track parent dataset.
- [x] 26 album distributions shown chronologically.
- [x] Mean visible on every album row.
- [x] Median visible on every album row.
- [x] All 26 most-streamed red points labelled.
- [x] Grey outlier labels reduced to preserve hierarchy.
- [x] Wider 14.5 × 17.5 chart passes visual QA.
- [x] No title/subtitle clipping.
- [x] Source and stream snapshot date visible.
- [x] Feature concept matches the approved distribution story.
- [x] Feature follows the locked #F3F4F6 / black-charcoal / one-muted-red palette.
- [ ] Exact approved chart copied byte-for-byte into site assets.
- [ ] Exact feature asset referenced by the Jekyll post.
- [ ] GitHub Pages/Jekyll PR build passes.
- [ ] PR merged.
- [ ] Live page and assets verified after deployment.
