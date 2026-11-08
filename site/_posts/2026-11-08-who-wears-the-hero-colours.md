---
layout: post
title: "Who wears the hero colours?"
slug: who-wears-the-hero-colours
date: 2026-11-08 12:43:00 +0000
author: Adam Green
category: Culture
description: "The superhero dress code looks simple: primaries for the good guys, green and purple for the villains. Twenty-four comic costumes and five unlikely colour twins complicate the picture."
read_time: "4 minute read"
card_image: /assets/charts/superhero-colour-code/superhero_v3_01_comic_lineup.png
hero_image: /assets/charts/superhero-colour-code/superhero_v3_01_comic_lineup.png
social_image: /assets/charts/superhero-colour-code/superhero_v3_01_comic_lineup.png
hero_alt: "Twelve selected Marvel and DC comic costumes, shown as equal main, supporting and accent colour chips in side-by-side hero and villain columns; chips describe hues rather than fabric proportions."
tags: [superheroes, comics, marvel, dc, colour, culture, data-visualisation]
published: false
---

# Who wears the hero colours?

You probably know the comic-book dress code, even if nobody gave you a copy.

Superman gets blue and red. The Joker gets purple and green. Green Goblin looks as though he got dressed in an abandoned chemistry lab.

The old shorthand is simple: **red, yellow and blue for the heroes; green, purple and orange for the villains**. It's the colourful argument behind [Tim Leong's *Super Graphic*](https://www.wired.com/gallery/excerpt-visual-guide-to-the-comic-book-universe/), and an idea I first played with in my [Shades of Heroism Tableau visualisation](https://public.tableau.com/app/profile/adam.green4310/viz/Shadesofheroism/shadesofheroism).

This time the challenge was to look past the colours in isolation. **Does the whole costume give away which side someone is on?**

## A case of wardrobe identity

The colour line-up above shows 12 recognisable costumes from Marvel and DC, recreated as colour fingerprints. The chips are ordered **main → supporting → accent**, rather than pretending we've measured exactly how many square inches of spandex are red.

On the heroes' side, the Flash is red and yellow. Superman is blue, red and yellow. The villains seem to have raided the green and purple aisles.

But look closer. Green Lantern is green. Magneto is red. The neat divide is already showing cracks.

## Three villains missed the dress-code memo

<figure class="story-chart full-bleed">
  <img src="{{ '/assets/charts/superhero-colour-code/superhero_v3_02_colour_wheels.png' | relative_url }}" alt="Two wheels with 12 equal character slices each: eight of twelve selected heroes and three of twelve selected villains are coded as having red, yellow or blue dominant costumes, with DC and Marvel subsets labelled." width="1600" height="1600" loading="lazy">
  <figcaption>Every equal slice is one selected character. The central numbers count traditional primary-dominant costumes, not areas of fabric.</figcaption>
</figure>

Across the **24 costume versions selected for this study**, eight of 12 heroes have a red, yellow or blue *main* colour.

So do **three of 12 villains**.

Each wheel has **12 equal slices**, one for each selected character. The first six in each wheel are DC characters, followed by six Marvel characters clockwise. DC's six chosen heroes split three primaries to three other hues, while five of Marvel's six selected heroes use primaries. That's a feature of **this deliberately picked group**, not proof that one publisher has a stronger moral colour code.

Each slice is a character, **not a percentage of costume fabric**.

### Who's behind the colour wheels?

Here's the cast behind the slices. The entries are in the same order as the wheels, with the first six DC and next six Marvel on each side. Rows are a compact reference list, **not hero–villain match-ups**. Colours in **bold** are traditional red, yellow and blue primaries.

| Role | DC character · main hue | Marvel character · main hue |
|:--|:--|:--|
| Hero | Superman · **blue** | Captain America · **blue** |
| Hero | The Flash · **red** | Daredevil · **red** |
| Hero | Wonder Woman · **red** | Iron Man · **red** |
| Hero | Aquaman · orange | Spider-Man · **red** |
| Hero | Batman · grey | Wolverine · **yellow** |
| Hero | Green Lantern · green | Black Panther · black |
| Villain | Sinestro · **yellow** | Magneto · **red** |
| Villain | Black Manta · black | Thanos · **blue** |
| Villain | Lex Luthor · green | Doctor Doom · green |
| Villain | Poison Ivy · green | Green Goblin · green |
| Villain | The Joker · purple | Loki · green |
| Villain | The Riddler · green | Venom · black |

*Character roles and costume hues are provisional, pending issue-specific artwork verification.*

## A colourful identity crisis

<figure class="story-chart full-bleed">
  <img src="{{ '/assets/charts/superhero-colour-code/superhero_v3_03_showdowns.png' | relative_url }}" alt="Five paired hero-villain character comparisons with the same coded main colour: Flash and Magneto red, Superman and Thanos blue, Wolverine and Sinestro yellow, Green Lantern and Green Goblin green, and Black Panther and Venom black. Both supporting colours appear as symmetric swatches." width="1600" height="1600" loading="lazy">
  <figcaption>Matching main hues, different characters. Supporting swatches add context; these are qualitative costume labels, not measured proportions.</figcaption>
</figure>

Now the fun bit.

The Flash and Magneto both wear red. Superman and Thanos share blue. Wolverine and Sinestro share yellow.

And there's a green-versus-green confrontation waiting between Green Lantern and Green Goblin.

Even the black suits tell two stories: Black Panther on one side and Venom, in his classic adversary guise, on the other.

**Five pairs, five matching leading colours, ten very different characters.**

The supporting colours change the look, while the characters' histories change what we read into it. If you judged a comic-book universe only by the first colour you saw, you'd be wrong rather quickly.

## How the data was assembled

This is an **illustrative set of 24 characters**, balanced as six heroes and six villains from DC and from Marvel. Each character has one specified comic-book costume or era; character identity and costume coding aren't assumed to stay fixed forever. The colours are editorial classifications from publisher references, not percentages of fabric captured from images.

That matters. A costume may change by issue, writer or artist, and some characters have switched sides. The full issue-specific art review is still outstanding, so the colour coding remains provisional.

## TLDR

The comic-book colour code exists as a design tradition, and you can spot echoes of it here. But a hero can wear green, a villain can wear blue, and nobody owns red.

Maybe the best thing a costume does isn't tell you who's good.

**It's give you someone to recognise.**

*simple charts, clear stories*

<aside class="method-note">
  <h2>Behind the colours</h2>
  <p>This is a deliberately chosen line-up, not a random or complete Marvel/DC character sample. Each character has a selected traditional comic-book portrayal. Main, supporting and accent colours are manually coded descriptive labels, not measured costume-area percentages. Hair and skin are excluded. The traditional artist's primaries are red, yellow and blue; black, grey and gold are kept separate. Some characters switch sides and some costumes change by issue. Individual full-body comic-art verification is still in progress, so this is a <strong>provisional analysis</strong>, not a publisher-wide statistical conclusion. See the <a href="https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-11-superhero-colour-code/data/publication_source_review_2026-11-08.csv">24-character source review</a> and the <a href="https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-11-superhero-colour-code/METHODOLOGY.md">full methodology</a>.</p>
</aside>

### Sources and inspiration
- [Tim Leong's *Super Graphic*, *Wired* (2013)](https://www.wired.com/gallery/excerpt-visual-guide-to-the-comic-book-universe/)
- [DC's explanation of the classic Superman costume](https://www.dc.com/blog/2023/05/04/super-looks-the-man-of-steels-ever-changing-wardrobe)
- [DC on the Riddler's two familiar costumes](https://www.dc.com/blog/2021/09/09/clothes-make-the-superman-d-cs-best-costume-upgrades)
- [Marvel's guide to Wolverine's many suits](https://www.marvel.com/articles/comics/wolverine-logan-james-howlett-every-costume-list)
- [Marvel on Iron Man's classic colours](https://www.marvel.com/articles/comics/iron-man-of-the-80s-the-silver-centurion)
- [Original *Shades of Heroism* on Tableau Public](https://public.tableau.com/app/profile/adam.green4310/viz/Shadesofheroism/shadesofheroism)

<p class="sign-off"><strong>simple charts clear stories.</strong></p>
