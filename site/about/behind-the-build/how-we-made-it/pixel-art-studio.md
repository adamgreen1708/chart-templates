---
layout: behind-the-build
title: "Pixel Art Studio — 256 little squares"
description: "How a Tableau experiment became an interactive creative playground."
permalink: /about/behind-the-build/how-we-made-it/pixel-art-studio/
collection_label: How we made it
article_number: "01"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/pixel.svg
---

## The idea

Back in January 2023, I built a little drawing tool in Tableau. An 8×8 grid, a selection of colours and the ability to paint individual squares.

It wasn't intended to solve a business problem or communicate a particularly important piece of information.

It was simply an opportunity to play with data and see what was possible.

A few years later, I wondered whether we could recreate it directly on Coffeetableviz.

## The challenge

Could we take something originally built using Tableau parameters and dashboard actions and turn it into a standalone tool that anyone could use in their browser?

And whilst we were at it, could we make it a little better?

## How it works

The principle behind Pixel Art Studio is remarkably simple.

Every square has a position and a colour. Give each colour a number and suddenly a picture becomes a collection of values.

An 8×8 picture needs 64 values. A 16×16 picture needs 256.

When you paint a square, you're simply changing one of those values. The browser then displays the corresponding colour.

You're effectively editing data, even if it feels like you're just drawing a little frog.

{% include behind-diagram.html name="pixel" alt="The actual 8 by 8 frog design shown as 64 colour codes and as coloured squares, with its colour key." caption="A picture is just a set of numbers. Original Frog design and palette." %}

## Under the bonnet

The studio uses three familiar web technologies.

HTML provides the structure. CSS determines how everything looks. JavaScript makes it interactive.

ChatGPT helped develop the code, whilst GitHub stores it and GitHub Pages makes the studio available through the website.

One of my favourite features is the ability to share a drawing.

Rather than uploading an image somewhere, we encode the colour of every square into the website address. When somebody opens that link, the studio reads those values and reconstructs the artwork.

They can then paint straight over it and create something of their own.

The same principle powers the Tiny Pixel Zoo and Pixel Universe galleries.

{% include behind-pixel-demo.html %}

## What didn't work

Eight squares across doesn't give you much room for artistic expression.

Some of our early attempts at animals required a considerable amount of imagination to recognise what they were supposed to be.

Introducing the 16×16 canvas gave us four times as many squares, allowing more detail without losing the simplicity of the original idea.

We also needed to ensure that adding new colours and canvas sizes didn't break the artwork people had already created.

The original 8×8 design links still work.

## What we learnt

Not every data visualisation needs to look like a chart.

A collection of numbers can become a picture, a drawing tool or an entire gallery of little creatures.

Perhaps more importantly, revisiting an old creative experiment with new technology can open up possibilities that weren't there the first time around.

## Try it yourself

Explore [Pixel Art Studio](/resources/8x8-pixel-art-builder/), paint something, save it or share it with somebody else.

Alternatively, visit the [Tiny Pixel Zoo](/resources/pixel-art-gallery/), borrow one of our little creatures and make it your own.

See the [original Tableau experiment](https://public.tableau.com/app/profile/adam.green4310/viz/8x8PixelArtBuilder/8X8PIXELART), the [JavaScript implementation](https://github.com/adamgreen1708/chart-templates/blob/main/site/assets/js/pixel-art-builder.js) and the [gallery data](https://github.com/adamgreen1708/chart-templates/blob/main/site/_data/pixel_art_gallery.yml). The original experiment credited [Ant Pulley's Paint Your Own Bob Ross](https://consult-ant.uk/2020/12/18/makeover-monday-2020-week-50/) as inspiration.

## TL;DR

Every pixel is a value. Every picture is a collection of data.

With a little JavaScript, some curiosity and a helping hand from AI, those values become a rather enjoyable creative playground.
