---
layout: behind-the-build
title: "Interwoven — From football data to a virtual art gallery"
description: "How an entire football season became something we could hang on a wall."
permalink: /about/behind-the-build/how-we-made-it/interwoven/
collection_label: How we made it
article_number: "06"
last_reviewed: 2026-11-26
social_image: /assets/gallery/interwoven/gallery.jpg
---

## The idea

Having explored the Premier League season through an interactive visualisation, I wanted to do something quite different with exactly the same numbers.

What if we removed the familiar club colours, league tables and conventional charts?

Could we create something that people might initially appreciate as a piece of art, before discovering the information hidden within it?

That was the starting point for Interwoven.

{% include behind-interwoven-media.html kind="gallery" %}

## The challenge

There are 380 matches, 20 clubs and 1,045 goals in our dataset.

The challenge wasn't simply to make those numbers look attractive. It was to develop a visual language that remained faithful to the football results whilst creating something with a very different aesthetic.

And then, rather ambitiously, we decided to put it in a gallery.

{% include behind-diagram.html name="interwoven-experiences" alt="One dataset leads to a Python-rendered artwork, a simulated gallery film and a JavaScript interactive explorer." caption="One dataset. Three experiences. Conceptual illustrations, not actual match plots." %}

## How it works

Each club has its own horizontal thread.

Every fixture creates two glass-like spheres, connected vertically. Home performances sit above their club's thread and away performances below.

The area of each sphere increases with goals scored, with a minimum size for zero. A halo celebrates a victory. Dashed connections identify draws, whilst brighter connections indicate matches with more goals.

Illuminated ribbons identify runs of five or more consecutive victories.

From a distance, the result is an abstract monochrome composition. Move closer and the individual stories begin to emerge.

{% include behind-interwoven-media.html kind="artwork" %}

{% include behind-interwoven-demo.html %}

## Under the bonnet

Python reads the original football dataset and calculates the position, size and appearance of every mark.

Using a library called Pillow, we build the artwork in layers: background, club threads, match connections, winning streaks, glass spheres and labels.

The finished canvas measures 6,000 by 2,000 pixels.

To create the gallery experience, we place that artwork onto a simulated gallery wall.

We then define a series of camera positions and calculate the movement between them, creating the impression of approaching the artwork and travelling along its surface.

Six hundred and ninety individual frames become a continuous 23-second film.

{% include behind-diagram.html name="interwoven-camera" alt="Four conceptual camera framings: establish the gallery scene, approach the canvas, move across the detail and return to the opening view." caption="The artwork stays still. The camera moves. Conceptual diagram of the camera journey; 23 seconds at 30 frames per second gives 690 frames." %}

The gallery scene is composed first. Key camera positions are defined at different times, intermediate positions are calculated for smooth movement, and each frame is rendered. FFmpeg assembles those frames into an MP4.

{% include behind-interwoven-media.html kind="video" %}

The interactive edition uses JavaScript to reconstruct the visual language in the browser, allowing us to select individual clubs and fixtures.

## What didn't work

A piece of artwork designed for a large wall presents a rather different challenge on a small phone screen.

The full canvas is difficult to explore at that scale. Individual spheres become too small to distinguish.

We introduced a detail mode, retained the club labels and made selected spheres more prominent.

Rather than compromise the original composition, we gave the reader a different way to experience it.

## What we learnt

The same dataset can serve considerably different purposes.

Premier League Unfolded encourages analytical exploration. Interwoven encourages curiosity through a different visual experience.

Neither required us to invent new numbers.

The creative opportunity came from changing the way we represented them, and the environment in which we experienced them.

{% include behind-diagram.html name="interwoven-comparison" alt="Symbolic comparison of Premier League Unfolded's monthly win draw loss results and Interwoven's connected monochrome club threads." caption="The same data, a completely different experience. Symbolic illustrations, not actual season results." %}

## Try it yourself

Visit [Interwoven in The Gallery](/gallery/interwoven/).

Watch the film, explore the complete canvas and then select an individual club or fixture in the [interactive edition](/gallery/interwoven/explore/).

It's worth experiencing the artwork in each of its three forms.

For the curious: [Premier League Unfolded — A season in a single view](/about/behind-the-build/how-we-made-it/premier-league-unfolded/), [the original Interwoven story](/stories/interwoven-when-data-becomes-art/), [the archived data](https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-11-epl-2526-unfolded/data/matches_2526.csv) and [the Python artwork renderer](https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-11-interwoven/render_interwoven.py).

## TL;DR

One football season. One dataset. Three experiences.

Sometimes the most interesting thing we can do with data is give ourselves permission to see it differently.
