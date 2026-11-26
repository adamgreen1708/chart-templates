---
layout: behind-the-build
title: "Bauhaus Art Studio — Geometry with purpose"
description: "How a collection of numbers becomes a piece of geometric art."
permalink: /about/behind-the-build/how-we-made-it/bauhaus-art-studio/
collection_label: How we made it
article_number: "04"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/bauhaus-form-data.svg
---

## The idea

I've always been drawn to the simplicity of Bauhaus-inspired design.

Circles, squares, triangles, strong colours and an appreciation of how these relatively simple elements can work together.

My earlier Hidden Miles Tableau artwork explored this relationship between running, data and geometric design.

I wanted to revisit that idea, but this time create something that would allow other people to explore their own data in a similarly creative way.

## The challenge

Could we build something that allows people to create freely with geometric shapes, whilst also giving those shapes a genuine connection to data?

There's an important distinction between creating something that looks like data visualisation and creating something that actually represents data.

I wanted the studio to accommodate both.

## How it works

Bauhaus Art Studio has two different approaches.

The first is creative freedom. Choose a pattern, select a palette, paint individual shapes and experiment with the arrangement.

The second is driven by data.

Upload a CSV file, select the numbers you want to explore and decide how those numbers should influence the artwork.

Larger values might produce larger circles, longer stripes or bigger rectangles.

The data provides the measurements. The design provides the personality.

{% include behind-diagram.html name="bauhaus-form-data" alt="Three illustrative running values become circles whose areas are proportional to the values." caption="Form follows data. The three running values come from the studio's illustrative sample; colours are decorative." %}

{% include behind-bauhaus-demo.html %}

## Under the bonnet

The studio reads the selected data directly in the browser. You can use a local CSV file or load data from a public GitHub repository.

JavaScript converts the numbers into geometric measurements and Canvas draws the resulting composition.

*Want to understand how? Read [JavaScript — Bringing things to life](/about/behind-the-build/how-we-work/javascript/).*

One of the most important decisions concerns the size of the shapes.

If one value is twice another, its circle should have twice the area, not twice the diameter.

*Explore the drawing techniques in [Drawing with code — When numbers become pictures](/about/behind-the-build/how-we-work/drawing-with-code/).*

The mathematics behind each shape is therefore slightly different, but the principle remains consistent.

{% include behind-diagram.html name="bauhaus-area" alt="For illustrative values of 50 and 100, correct proportional-area circles double the area, whereas doubling the diameter quadruples the area." caption="Twice the value. Not twice the diameter. The studio calculates dimensions from the required filled area." %}

We've also developed four different poster families: Data Mosaic, Typographic Broadside, Stripe Study and Circle Study.

Each provides a different way to communicate the same underlying information.

## What didn't work

One of the challenges with combining art and data is knowing where decoration ends and measurement begins.

Making every visual difference meaningful can restrict creative freedom. Making everything decorative can undermine the integrity of the data.

We've separated those decisions.

Colours can be meaningful or purely decorative. Shape areas can represent actual values, whilst an alternative contrast setting deliberately emphasises differences.

That distinction is explained rather than hidden.

Missing or invalid numbers are excluded, not treated as zero. Limits on the number of displayed records are also made explicit.

## What we learnt

Data visualisation doesn't always have to look like data visualisation.

There is room for creativity, experimentation and even a little artistic indulgence, provided we're clear about what the visual elements represent.

Perhaps the most enjoyable part of building this studio has been exploring how the same numbers can produce such different compositions.

The numbers haven't changed. Our interpretation of them has.

{% include behind-bauhaus-studios.html %}

## Try it yourself

Visit [Bauhaus Art Studio](/resources/bauhaus-art-studio/).

Start with the illustrative running dataset or bring along some numbers of your own. Experiment with the shapes, colours and poster styles.

See how many different ways you can express the same information.

Explore the original [Hidden Miles Tableau artwork](https://public.tableau.com/app/profile/adam.green4310/viz/HiddenMiles/Bauhausrunningtotal), the [Running in Shapes article](/2024/12/31/running-in-shapes-a-bauhaus-inspired-journey-through-data/) or the [studio implementation](https://github.com/adamgreen1708/chart-templates/blob/main/site/resources/bauhaus-art-studio/index.html).

## TL;DR

Data determines the measurements. Design determines the composition.

Somewhere between the two sits an opportunity to create something rather interesting.
