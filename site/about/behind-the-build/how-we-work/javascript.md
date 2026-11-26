---
layout: behind-the-build
title: "JavaScript — Bringing things to life"
description: "What actually happens when we say JavaScript builds the interactive visualisation?"
permalink: /about/behind-the-build/how-we-work/javascript/
collection_label: How we work
article_number: "05"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/javascript-action.svg
---

## The idea

There's something rather satisfying about tapping a square in Pixel Art Studio and watching it change colour.

Or selecting a football club and seeing an entire season rearrange itself.

These interactions feel almost instantaneous. But behind each of them is a collection of instructions waiting for something to happen.

That's where JavaScript comes in.

## The challenge

A chart saved as an image is perfectly capable of telling a story.

But what if we want the reader to explore that story? Select a club, change a colour, adjust the size of a circle or create something of their own?

We need our website to respond to the reader, rather than simply present information.

## How it works

JavaScript is a programming language that, amongst other things, allows us to run instructions inside a web browser.

Imagine opening Pixel Art Studio.

Behind the artwork is a collection of numbers representing the colours of the individual squares.

When we select a colour and tap a square, JavaScript identifies which square we've selected, changes its stored colour value and updates the display.

The browser isn't asking ChatGPT to create another picture every time we paint a pixel.

It's following instructions that we've already written.

{% include behind-diagram.html name="javascript-action" alt="A tap selects a square, instructions update its stored colour value, and the browser redraws the square in blue." caption="An action, an instruction and a response. All within your browser." %}

## Under the bonnet

There are three particularly useful concepts behind our interactive projects.

**An event** is something that happens. A click, a tap or a change to a slider.

**State** is the information that describes what is currently happening. Which colour is selected? Which club are we looking at? What values make up our artwork?

**Rendering** is the process of translating that information into something we can see.

These three concepts work together.

{% include behind-javascript-paint.html %}

These two instructions are taken directly from our Pixel Art Studio code.

{% include behind-javascript-code.html example="pixel" %}

The first instruction changes the stored colour value of the selected square. The second tells the studio to update what we see.

{% include behind-diagram.html name="javascript-state" alt="A white square becomes blue when its stored colour value changes from zero to two and the display is rendered again." caption="Change the information. Change the picture. The actual Pixel Art Studio colour values." %}

In Premier League Unfolded, JavaScript loads the prepared JSON file, identifies the selected club and creates the individual result circles.

Choose another club and the instructions run again using a different set of records.

{% include behind-javascript-code.html example="football" %}

It tells the browser to listen for a change in the club selector and respond by running the instructions for the newly selected team.

The underlying football results haven't changed. We're simply asking the browser to present a different part of them.

Two very different products. The same underlying principle.

## What didn't work

Designing an interaction for someone using a mouse doesn't necessarily mean it will work well for someone using a phone.

Hovering over a result is useful on a desktop computer, but we can't rely on that behaviour on a touchscreen.

Our interactive visualisations therefore need to respond to different ways of interacting, including taps, clicks and keyboard controls.

We've also learnt that changing what appears on screen isn't always enough. The underlying information needs to stay consistent, particularly when we introduce features such as undo, redo and saved artwork.

## What we learnt

One of the most interesting things about JavaScript is how much we can achieve without continually communicating with a server.

Once Pixel Art Studio has loaded, its painting instructions can run directly in the browser.

We can experiment, make mistakes, undo our changes and create something entirely new.

ChatGPT helps us develop the instructions. GitHub stores them. The browser executes them.

It's this combination that has allowed us to turn relatively simple ideas into surprisingly capable little creative tools.

{% include behind-javascript-workflow.html %}

*Want to understand how? Read [HTML and CSS — Giving everything a home](/about/behind-the-build/how-we-work/html-css/).*

## Try it yourself

Experiment with the miniature painting example and watch what happens to the underlying information every time you change a square.

The drawing example below takes the same principle one step further. Change a few instructions and see how the browser draws a circle.

*Explore the drawing techniques in [Drawing with code — When numbers become pictures](/about/behind-the-build/how-we-work/drawing-with-code/).*

{% include behind-javascript-shape.html %}

Then visit [Pixel Art Studio](/resources/8x8-pixel-art-builder/) or [Premier League Unfolded](/resources/epl-2026-27-unfolded/) and look at those interactions a little differently.

Behind every click is another set of instructions.

For the curious: [Python — Making sense of the numbers](/about/behind-the-build/how-we-work/python/), [Pixel Art Studio — 256 little squares](/about/behind-the-build/how-we-made-it/pixel-art-studio/), [Premier League Unfolded — A season in a single view](/about/behind-the-build/how-we-made-it/premier-league-unfolded/), [Pixel Art Studio JavaScript](https://github.com/adamgreen1708/chart-templates/blob/main/site/assets/js/pixel-art-builder.js) and [Premier League JavaScript](https://github.com/adamgreen1708/chart-templates/blob/main/site/assets/js/epl-2627-unfolded.js).

## TL;DR

JavaScript listens for something to happen, updates the relevant information and changes what we see.

It turns our website from something we read into something we can explore.
