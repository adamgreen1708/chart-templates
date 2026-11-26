---
layout: behind-the-build
title: "The Dot Studio — Every dot is a data point"
description: "How a photograph becomes a dataset and a dataset becomes a piece of art."
permalink: /about/behind-the-build/how-we-made-it/dot-studio/
collection_label: How we made it
article_number: "03"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/dot-image-data-art.svg
---

## The idea

Some of my favourite creative experiments in Tableau have involved using data to recreate images.

My Aladdin Sane portrait of David Bowie is one such example. Rather than displaying a photograph, the artwork is constructed from individual coloured dots plotted on a coordinate canvas.

Stand back and you see a portrait. Look closely and you see the individual marks that make it possible.

I wanted to revisit that idea and make the process accessible to anyone.

<figure class="btb-figure">
  <img src="{{ '/assets/migrated/creating-for-fun/aladdin-sane_high-res.png' | relative_url }}" alt="Original David Bowie Aladdin Sane portrait built from coloured Tableau dots." width="1000" height="1000" loading="lazy">
  <figcaption>David Bowie — Aladdin Sane. Original Tableau pointillism study by Adam Green. <a href="{{ '/2024/11/13/creating-for-fun/' | relative_url }}">See the earlier creative experiments.</a></figcaption>
</figure>

## The challenge

Could we take any photograph, extract the information we need and recreate it using nothing more than circles?

And could we give people some creative control over how those circles behave?

## How it works

The Dot Studio divides an image into a grid.

For each sampled position, we extract information about the colour and brightness of the image.

That information helps determine the position, colour and size of a dot.

Increase the number of dots and more detail begins to emerge. Reduce the number and the image becomes increasingly abstract.

The interesting thing is how much information we can remove whilst still recognising the original subject.

{% include behind-diagram.html name="dot-image-data-art" alt="Illustrative landscape sampled into positions, colours and sizes, then reconstructed as circles." caption="From image to data to art. Conceptual illustration of the conversion." %}

{% include behind-dot-demo.html %}

## Under the bonnet

JavaScript reads the image using a browser technology called Canvas.

*Want to understand how? Read [JavaScript — Bringing things to life](/about/behind-the-build/how-we-work/javascript/).*

We can then apply different rules to the sampled information. Limit the available colours, increase the size of dots in darker areas or recreate the appearance of a printed comic book.

We've also introduced a CMYK halftone treatment inspired by traditional colour printing.

Rather than assigning one colour to each grid position, it creates four overlapping layers of coloured dots, representing cyan, magenta, yellow and black.

The size of each dot reflects how much of that ink is required.

{% include behind-diagram.html name="dot-ink-layers" alt="Four overlapping ink screens: cyan 15 degrees, magenta 75 degrees, yellow zero degrees and black 45 degrees." caption="Illustrative screens using the actual ink angles and colours. Larger dots represent greater ink coverage; overlapping colours are blended in the browser." %}

Perhaps my favourite feature, however, is that we can export the underlying data.

Every dot has coordinates, a colour and a size. Export those values into a CSV file and we can recreate a version of the artwork in Tableau.

We've effectively turned an image back into a dataset.

{% include behind-dot-tableau.html %}

## What didn't work

One of the challenges is that different visualisation tools interpret colour and size differently.

Tableau can reproduce the individual coloured marks, but overlapping ink colours and dot sizes won't necessarily appear exactly as they do in the browser.

Our halftone treatment is also a creative simulation of printing, rather than a colour-managed printing process.

Recognising those limitations is part of understanding what we've created.

## What we learnt

An image contains an extraordinary amount of information.

By deliberately restricting the number of colours, the number of marks and the way those marks behave, we can create something with an entirely different visual character.

Sometimes working with less information gives us more creative freedom.

## Try it yourself

Visit [The Dot Studio](/resources/dot-studio/), choose your own photograph and experiment with the different colour treatments.

If you're a Tableau enthusiast, download the underlying data and see what you can create with it.

Explore the [studio implementation](https://github.com/adamgreen1708/chart-templates/blob/main/site/resources/dot-studio/index.html), or compare the approach with [Pixel Art Studio](/about/behind-the-build/how-we-made-it/pixel-art-studio/) and [Truchet Tile Studio](/about/behind-the-build/how-we-made-it/truchet-tile-studio/).

## TL;DR

Every dot has a position, a colour and a size.

Those are simply data values. Put enough of them together and something rather wonderful begins to emerge.
