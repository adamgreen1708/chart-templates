---
title: "How do you measure a chameleon?"
date: 2026-09-23 21:00:00 +0100
slug: how-do-you-measure-a-chameleon
permalink: /2026/09/23/how-do-you-measure-a-chameleon/
description: "David Bowie released 26 lifetime solo studio albums across six named decades. A simple style-reset score shows repeated change — and the limits of trying to measure reinvention."
category: Music
read_time: 4 minute read
card_image: /assets/migrated/david-bowie-reinvention/feature.svg
hero_image: /assets/migrated/david-bowie-reinvention/feature.svg
hero_alt: "Black-and-charcoal stencil chameleon stretched across a measuring ruler on a light-grey background, with segmented body tones suggesting change and one muted-red measurement mark breaking the regular scale."
---

David Bowie is one of those artists routinely described as endlessly reinventing himself.

The phrase feels right. It is also suspiciously difficult to measure.

So I tried.

This story starts with Bowie's lifetime solo studio catalogue: **26 albums**, from the 1967 debut to *Blackstar* in 2016. That is a 49-year difference between the first and last album years, spread across **six named calendar decades**.

The interesting question is not whether Bowie was creative, influential or important. A chart is not going to settle that.

The question is narrower: **can the catalogue data show repeated changes in musical direction — and what happens when we try to reduce those changes to one number?**

## Six decades. Twenty-six albums.

Start with the uncomplicated bit.

<figure class="story-chart full-bleed">
  <img src="{{ '/assets/migrated/david-bowie-reinvention/six-decades.png' | relative_url }}" alt="Chronological dot plot of David Bowie's 26 lifetime solo studio albums from 1967 to 2016, with every album labelled and the ten-year gap between Reality and The Next Day highlighted." loading="lazy">
  <figcaption>Bowie's lifetime solo studio catalogue runs from 1967 to <em>Blackstar</em> in 2016, with a ten-year gap between <em>Reality</em> and <em>The Next Day</em>.</figcaption>
</figure>

Twenty-six records is a lot of opportunities to change course.

The chronology also has its own rhythm. The 1970s are packed. The 1980s and 1990s keep moving. Then there is the ten-year pause between *Reality* in 2003 and *The Next Day* in 2013 before *Blackstar* closes the sequence in 2016.

Longevity, though, is not the same thing as reinvention.

For that, we need to look inside the labels attached to the albums.

## The labels rarely sit still

Rather than force every album into one genre, I used the album-level **Styles** listed by AllMusic and tracked how the distinctive labels appear across the chronology.

<figure class="story-chart full-bleed">
  <img src="{{ '/assets/migrated/david-bowie-reinvention/style-matrix.png' | relative_url }}" alt="Album-by-style dot matrix showing distinctive AllMusic style tags across David Bowie's solo studio albums. Labels such as Glam Rock, Blue-Eyed Soul, Dance-Rock, Post-Punk and Alternative/Indie Rock appear in different parts of the chronology." loading="lazy">
  <figcaption>Distinctive AllMusic style tags appear, disappear and return across the catalogue; the three near-universal umbrella labels are omitted from the display only.</figcaption>
</figure>

Across the 25 albums with comparable AllMusic Styles metadata, there are **24 distinct style labels**.

Some are so broad that they appear almost everywhere: Contemporary Pop/Rock on 24 of those 25 albums, Art Rock on 23, and Experimental Rock on 22. I left those three near-universal labels out of the display so they do not swamp the more distinctive movement underneath.

What remains is much more interesting.

Glam Rock clusters early. Blue-Eyed Soul and Dance-Rock arrive later. Post-Punk appears around *Scary Monsters*. Alternative/Indie Rock becomes part of the later vocabulary.

The labels are imperfect, but they plainly do not sit still.

Which raises the dangerous question.

Could we score the movement?

## A reinvention score gets awkward

I used a deliberately simple measure.

For every adjacent pair of albums, I compared their complete AllMusic Styles sets using **Jaccard similarity** — shared labels divided by all labels present across the pair — then flipped it:

**style reset score = 1 − similarity**

Higher means less overlap.

Twenty-six albums create **25 possible album-to-album moves**. The debut itself does not get a score because there is no previous album to compare it with.

AllMusic currently exposes comparable Styles data for 25 of the 26 albums. *The Next Day* is the exception, so the two moves touching it cannot be scored consistently. They stay in the chart as grey missing-data rows rather than being quietly turned into zero.

<figure class="story-chart full-bleed">
  <img src="{{ '/assets/migrated/david-bowie-reinvention/reinvention-score.png' | relative_url }}" alt="Dot plot showing style-reset scores for 25 album-to-album moves in David Bowie's solo studio catalogue. Twenty-three transitions have measured scores; The Next Day and Blackstar are retained as grey missing-data rows because The Next Day lacks comparable AllMusic Styles metadata. Space Oddity has the largest measured reset at 89%, while Low is highlighted at 33%." loading="lazy">
  <figcaption>Twenty-six albums create 25 transitions. Twenty-three have comparable style data; the two moves involving <em>The Next Day</em> are shown as grey missing-data rows rather than zero scores.</figcaption>
</figure>

The largest measured reset is the 1967 debut → *Space Oddity* at **89%**.

*Tonight* → *Never Let Me Down* reaches **75%**.  
*Diamond Dogs* → *Young Americans* lands at **67%**.  
*Scary Monsters* → *Let's Dance* reaches **60%**.

Then the score gets awkward.

*Station to Station* → *Low* lands at only **33%** — exactly around the median measured reset.

Why? Because six broad AllMusic labels remain shared between the two records.

That is not a failure of the chart. It is the point of it.

The metric is measuring **taxonomy turnover**, not creativity, intent or artistic significance. Broad labels can survive while the music underneath them changes considerably.

So the data gives us two useful things at once.

It shows a catalogue that repeatedly changes its descriptive vocabulary.

And it shows the limit of pretending those labels are the same thing as the art.

## TLDR

David Bowie released **26 lifetime solo studio albums** from 1967 to 2016, spanning **six named calendar decades**.

Distinctive style labels repeatedly enter, disappear and return across the catalogue. A simple adjacent-album reset score captures some of that movement, with the debut → *Space Oddity* transition scoring **89%**.

But *Station to Station* → *Low* scores only **33%** because broad labels remain shared.

The score is useful.

It just cannot become the art.

<aside class="method-note">
  <h2>Method note</h2>
  <p>The lifetime solo studio scope contains 26 albums from the 1967 debut through <em>Blackstar</em> in 2016. Album identity and chronology were built from MusicBrainz release-group data and cross-checked against the official David Bowie catalogue. <em>The Buddha of Suburbia</em> is included under the official Bowie studio-album classification; <em>Toy</em> is excluded from the lifetime sequence because its standalone release was posthumous. Album-level AllMusic Styles are used for the like-for-like style comparison. AllMusic currently exposes Styles for 25 of the 26 scoped albums; <em>The Next Day</em> has no comparable Styles values, so the two adjacent transitions touching it remain missing. Reset score is 1 minus Jaccard similarity of the complete observed style sets. It measures metadata turnover, not creativity, quality, influence or intent.</p>
</aside>

<p class="sign-off"><strong>simple charts clear stories.</strong></p>
