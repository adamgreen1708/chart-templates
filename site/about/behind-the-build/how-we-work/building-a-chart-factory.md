---
layout: behind-the-build
title: "Building a chart factory"
description: "Why we don't ask ChatGPT to draw our charts."
permalink: /about/behind-the-build/how-we-work/building-a-chart-factory/
collection_label: How we work
article_number: "02"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/factory.svg
---

## The idea

One of the things I've always appreciated about good data visualisation is consistency.

Look through a collection of charts from an established publication and you'll often recognise where they came from before reading the source.

The colours, typography, layout and editorial style give them an identity.

I wanted Coffeetableviz to have something similar.

## The challenge

Asking AI to create a new chart every time might seem like the obvious solution. But what happens when the colours change, the labels move, the numbers are misrepresented or the chart looks completely different from the previous one?

Rather than repeatedly asking for the same thing, why not build a reusable system that already knows how to make our charts?

So that's what we did.

## How it works

Our charting system has three main ingredients.

**The dataset.** The actual numbers we want to communicate. These typically sit in a CSV file, which is essentially a simple table of information.

**The configuration.** A set of instructions describing what we want to create. Which columns to use, which chart type to choose, what to highlight and what the headline should say.

**The renderer.** A reusable piece of Python code that reads those instructions and produces the chart.

Think of it like cooking. The data provides the ingredients, the configuration provides the recipe and the renderer does the cooking.

Our house style provides the standards that hold everything together.

*Explore our design principles in [Building a visual identity](/about/behind-the-build/how-we-work/visual-identity/).*

## Under the bonnet

{% include behind-diagram.html name="factory" alt="Dataset, configuration and house rules feed a Python renderer which produces a chart image for review." caption="The recipe and the ingredients." %}

When we develop a new data story, we first explore the dataset and decide what we're trying to communicate.

ChatGPT then helps write a configuration file, which we call CHART_CONFIG.

It tells the renderer which data to use, how to present it and where to apply particular design decisions.

Most of our charts share the same underlying visual framework: a light-grey background, a consistent palette, familiar typography, source references and a square canvas designed to work on a phone.

GitHub Actions runs the Python renderer, which produces the actual image.

*Explore the drawing techniques in [Drawing with code — When numbers become pictures](/about/behind-the-build/how-we-work/drawing-with-code/).*

*Want to understand how? Read [Python — Making sense of the numbers](/about/behind-the-build/how-we-work/python/).*

ChatGPT doesn't draw our statistical charts. The code does, using the real data.

That distinction gives us something particularly useful: repeatability.

If we use the same data, instructions and rendering environment, we should be able to reproduce the result.

{% include behind-config.html %}

*Explore the actual configuration instructions in [The recipe for a chart](/about/behind-the-build/how-we-work/chart-recipe/).*

## What didn't work

Building the renderer has been an iterative process.

We've encountered titles that don't fit, labels that overlap, charts that look great on a large screen but become unreadable on a phone, and layouts that simply don't suit the story.

The important thing is what happens next.

If a problem is unique to one chart, we can adjust its configuration. If it's something likely to happen again, we improve the shared renderer, rules or tests.

The next project benefits from the previous one.

## What we learnt

Separating the data, configuration and renderer makes it easier to experiment without starting from scratch.

It also means our visual identity doesn't depend on an AI remembering what we asked it to do last week.

We've built a small chart factory.

But the factory doesn't decide which charts are worth making. That's still the interesting part of the process.

## Try it yourself

Explore our [chart template rules](https://github.com/adamgreen1708/chart-templates/blob/main/spec/538_template_rules.md) or the [Python renderer](https://github.com/adamgreen1708/chart-templates/blob/main/src/render_538.py).

## TL;DR

Real data provides the ingredients. A configuration file describes the recipe. A reusable Python renderer produces the chart.

Consistency is something we've built into the process, rather than something we hope AI remembers.
