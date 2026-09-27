---
title: "Bowie never needed the three-minute rule"
date: 2026-09-27 08:22:00 +0100
slug: bowie-never-needed-the-three-minute-rule
permalink: /2026/09/27/bowie-never-needed-the-three-minute-rule/
description: "Across 275 David Bowie studio-album tracks, song length changes with the catalogue's musical eras — but shorter tracks do not show a clear streaming advantage."
category: Music
read_time: 4 minute read
card_image: /assets/migrated/david-bowie-track-length-success/feature.svg
hero_image: /assets/migrated/david-bowie-track-length-success/feature.svg
hero_alt: "Black-and-charcoal editorial illustration on a light-grey background showing an audio ribbon changing shape as it passes through and stretches beyond a stopwatch, with one muted-red timing mark on the stopwatch rim."
---

Three minutes is one of those numbers that hangs around pop music.

Long enough to do something interesting. Short enough not to annoy anyone too much.

David Bowie seems to have treated it more as a suggestion.

I rebuilt his lifetime solo studio catalogue at track level: **275 canonical album tracks across 26 albums**, from the 1967 debut to *Blackstar* in 2016.

Then I added three things: album-level AllMusic Styles, a current Spotify-stream snapshot, and UK singles-chart history.

The useful story is not that Bowie made long songs.

It is that **the shape of the songs keeps changing — and shorter tracks do not seem to have a simple advantage.**

## Bowie stretched the song

Start with the albums.

The 1967 debut has a median track length of just **2:49**.

By *Station to Station* in 1976, the median is **6:02**.

Then it drops again.

Then rises again.

<figure class="story-chart full-bleed">
  <img src="{{ '/assets/migrated/david-bowie-track-length-success/album-medians.png' | relative_url }}" alt="Line chart showing median track length for David Bowie's 26 lifetime solo studio albums in release order. The 1967 debut begins at 2 minutes 49 seconds, Station to Station is highlighted at 6 minutes 2 seconds, and later albums continue to move above and below the 4 minute 10 second career median." loading="lazy">
  <figcaption>Median track length changes sharply across Bowie's 26 lifetime solo studio albums, peaking at 6:02 on <em>Station to Station</em>.</figcaption>
</figure>

Across the whole catalogue, the median track is **4:10**.

But the album medians move around that number constantly.

*Pin Ups* sits at 2:50.  
*Low* at 3:03.  
*Let's Dance* at 4:59.  
*Earthling* at 5:00.  
*The Buddha of Suburbia* at 5:24.

So this is not a tidy “songs got longer over time” story.

Bowie keeps changing the shape of the record.

## Style changed the clock

That becomes more interesting when the AllMusic Styles are added.

These are **album-level** labels, and they overlap heavily, so I am not treating them as mutually exclusive song genres.

The better question is narrower:

**when an album carries a particular style label, what do its tracks tend to look like in length?**

<figure class="story-chart full-bleed">
  <img src="{{ '/assets/migrated/david-bowie-track-length-success/style-lengths.png' | relative_url }}" alt="Ranked dot plot of median track duration for seven recurring AllMusic album Styles in David Bowie's catalogue. Blue-Eyed Soul is highest at 4 minutes 45 seconds, followed by Dance-Rock and Art Rock, while Glam Rock is 3 minutes 29 seconds and Singer/Songwriter 3 minutes 24 seconds. Track and album counts are shown beside each style." loading="lazy">
  <figcaption>Tracks on albums carrying different recurring AllMusic Styles have different length profiles; the categories overlap and are album-level labels rather than mutually exclusive song genres.</figcaption>
</figure>

The contrast is substantial.

Tracks on Blue-Eyed Soul-tagged albums have a median length of **4:45**.

Dance-Rock: **4:24**.  
Art Rock: **4:18**.  
Glam Rock: **3:29**.  
Singer/Songwriter: **3:24**.

That does not mean style *caused* the song length.

But it does show that Bowie's changing musical vocabulary coincides with changing track structures.

The reinvention is not just in the labels.

It is also in the clock.

## The hits weren't short

Then comes the obvious assumption.

If shorter songs are easier to consume, perhaps they should be more popular.

The current catalogue does not give that idea much help.

Across **237 matched studio compositions**, the relationship between album-track duration and log current Spotify streams is only **r = 0.11**.

That is very little linear relationship.

<figure class="story-chart full-bleed">
  <img src="{{ '/assets/migrated/david-bowie-track-length-success/streams-vs-length.png' | relative_url }}" alt="Scatter plot of album-track length against current Spotify streams on a logarithmic scale for 237 matched David Bowie studio compositions. A four-minute reference line divides the plot. UK-charted compositions are red. Starman, Heroes and Let's Dance are labelled among the most-streamed longer tracks, while Moonage Daydream is labelled as a high-streaming track with no main UK chart match." loading="lazy">
  <figcaption>Album-track length has little linear relationship with current Spotify streams in the matched catalogue; red dots identify compositions with a main UK Official Singles Chart entry.</figcaption>
</figure>

And the most-streamed end is hardly dominated by short songs.

*Starman*: **4:10**.  
*“Heroes”*: **6:10**.  
*Space Oddity*: **5:16**.  
*Rebel Rebel*: **4:34**.  
*Let's Dance*: **7:37**.

In fact, **15 of the current top 20 matched studio compositions are at least four minutes long**.

There is a comparability wrinkle worth being explicit about: these are canonical **album-track lengths**. A historical single may have used a shorter edit. The UK chart data tells us whether the composition appeared on the main singles chart; it does not pretend that the plotted album version was always the exact version bought at the time.

That wrinkle actually makes the story better.

Bowie could make a seven-minute album track, cut it for radio, and still leave the long version as part of the catalogue people stream today.

## TLDR

Across **275 canonical studio-album tracks**, David Bowie's songs keep changing shape.

The catalogue median is **4:10**, but individual albums swing from well under three minutes to around six.

Those length differences also line up with different AllMusic album Styles.

But shorter tracks do not show a clear current-streaming advantage: across 237 matched compositions, duration vs log streams is only **r = 0.11**, and **15 of the top 20** run four minutes or longer.

Three minutes was useful.

Bowie just did not seem to regard it as compulsory.

<aside class="method-note">
  <h2>Method note</h2>
  <p>The lifetime solo studio scope contains 26 albums and 275 canonical album tracks from the 1967 debut through <em>Blackstar</em> in 2016. Track identity and duration come from MusicBrainz, with album-by-album track-count QA used to avoid shortened regional editions, bonus material and duplicated multi-layer programmes. AllMusic Styles are album-level, overlapping classifications inherited by the tracks on those albums; they are not mutually exclusive song genres. Current popularity uses a Spotify/Kworb snapshot dated 25 September 2026 and is deduplicated to 237 matched compositions. Historic UK success uses the main Official Singles Chart from Official Charts. Chart 3 compares canonical album-track duration with composition-level success; some historical singles used shorter edits. Downloads are deliberately not used as a whole-career success measure because the commercial download era covers only a small fraction of Bowie's career. The reported r = 0.11 is Pearson correlation between track duration and log10 current streams in the matched catalogue and is descriptive, not causal.</p>
</aside>

<p class="sign-off"><strong>simple charts clear stories.</strong></p>
