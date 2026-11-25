---
layout: post
title: "Interwoven: When data becomes art"
slug: interwoven-when-data-becomes-art
date: 2026-11-25 00:00:00 +0000
author: Adam Green
category: Sport
description: "20 clubs. 380 matches. 1,045 goals. One canvas. An experiment in turning an entire football season into data art."
read_time: "3 minute read"
card_image: /assets/gallery/interwoven/card.jpg
social_image: /assets/gallery/interwoven/gallery.jpg
tags: [premier-league, football, data-art, gallery, interactive, data-visualisation]
published: true
---

<figure class="story-chart gallery-inline"><img src="{{ '/assets/gallery/interwoven/gallery.jpg' | relative_url }}" width="1600" height="900" alt="Interwoven displayed as a panoramic monochrome artwork in a modern gallery with oak flooring."></figure>

What if a football season could hang on a gallery wall?

Not a league table, a dashboard or a collection of charts. Something that might catch your eye as you walk past, encouraging you to stop, move closer and discover what's hidden within.

That was the idea behind Interwoven.

## Finding beauty in the numbers

Using every Premier League result from the 2025/26 season, I wanted to explore the relationship between data visualisation and art.

Club colours were stripped away, leaving a monochrome collection of glass-like spheres, delicate threads and illuminated halos.

Nothing is there purely for decoration.

The size of each sphere represents goals scored. A halo celebrates a victory. Home performances sit above the horizontal thread, away performances below it. Vertical connections bring opposing teams together.

The season unfolds from left to right.

<figure class="story-chart gallery-inline"><a href="{{ '/assets/gallery/interwoven/artwork.png' | relative_url }}"><img src="{{ '/assets/gallery/interwoven/artwork.png' | relative_url }}" width="6000" height="2000" loading="lazy" alt="The full Interwoven artwork, with 20 club rows, match connections, glass spheres and winning streak ribbons."></a><figcaption>Select the canvas for the full-resolution artwork.</figcaption></figure>

## Look a little closer

From a distance, it's an abstract composition. Up close, the football stories begin to emerge.

Aston Villa's eight consecutive victories produce the most prominent individual streak. Arsenal, the eventual champions, illuminate three separate five-game winning runs.

Tottenham recorded more than twice as many wins away from home as they did at home (seven versus three). Wolves didn't win away at all.

Hidden amongst the glass and light are the highs and lows of an entire season.

<figure class="story-chart gallery-inline"><img src="{{ '/assets/gallery/interwoven/detail.png' | relative_url }}" width="1780" height="695" loading="lazy" alt="Close-up of the opening fixtures and the top-ranked club labels, showing the glass spheres, victory halos and opponent connections."></figure>

## From canvas to gallery

Creating the artwork wasn't enough. I wanted to explore how it might feel to encounter data visualisation in a different environment.

So why not build a virtual gallery?

A contemporary exhibition space, a panoramic canvas and a camera that invites you to walk past, move closer and explore.

<figure class="gallery-inline"><video class="gallery-video" controls playsinline loop preload="metadata" width="1600" height="900" poster="{{ '/assets/gallery/interwoven/gallery.jpg' | relative_url }}" aria-label="Interwoven gallery walkthrough"><source src="{{ '/assets/gallery/interwoven/walkthrough.mp4' | relative_url }}" type="video/mp4"><a href="{{ '/assets/gallery/interwoven/walkthrough.mp4' | relative_url }}">Watch the gallery walkthrough</a></video><figcaption>The 23-second virtual gallery walkthrough uses the original artwork.</figcaption></figure>

There's also an interactive edition. Select a club, reveal a connection or discover the score behind an individual sphere.

**[Explore Interwoven interactively →]({{ '/gallery/interwoven/explore/' | relative_url }})**

The artwork becomes something you can explore rather than simply observe.

## Creating for the sake of creating

Not every visualisation needs to solve a business problem or answer an urgent question.

Sometimes curiosity is enough.

Interwoven is an experiment in what happens when we give ourselves permission to do something a little different with data.

And it's the first exhibit in a new Coffeetableviz collection: **[The Gallery]({{ '/gallery/' | relative_url }})**.

## TL;DR

An entire Premier League season transformed into an interactive piece of data art. Every sphere, halo and connection is grounded in real match results.

*Simple charts. Clear stories. Occasionally, a little art.*

---

### A note on the numbers

The [frozen match-level dataset](https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-11-epl-2526-unfolded/data/matches_2526.csv) contains all 380 full-time results (38 per club, 19 home and 19 away), 1,045 goals and 104 draws. The remaining 276 fixtures each have one winner. Winning ribbons denote maximal runs of five or more consecutive matches won by the same club. The horizontal sequence follows fixture dates, with same-date games in source-file order, not assumed kickoff order. The gallery scene is simulated; the data artwork is generated from the actual results.
