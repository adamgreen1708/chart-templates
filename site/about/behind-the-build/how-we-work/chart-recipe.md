---
layout: behind-the-build
title: "The recipe for a chart"
description: "How we tell the computer what to draw."
permalink: /about/behind-the-build/how-we-work/chart-recipe/
collection_label: How we work
article_number: "10"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/recipe-anatomy.svg
---

## The idea

One of the things I enjoy about Tableau is the ability to separate information from the way it's presented.

We've adopted a similar principle at Coffeetableviz.

Our numbers live in a dataset. Our presentation instructions live in something we call CHART_CONFIG.

## The challenge

Rather than continually explaining our preferred colours, typography and layouts to ChatGPT, we've established a reusable framework.

For each new chart, we concentrate on the decisions that make it different.

## How it works

CHART_CONFIG is essentially a collection of named instructions.

Which dataset should we use? Which columns contain the information? What should we draw? What should we highlight?

ChatGPT helps translate our editorial decisions into these instructions.

Our Python renderer reads them and creates the finished chart.

{% include behind-diagram.html name="recipe-anatomy" alt="Six groups of chart instructions: data, chart type, story, highlights, layout and output." caption="Anatomy of a chart recipe." %}

## Under the bonnet

Take our David Bowie project exploring track lengths.

We wanted to understand how the length of his songs changed across albums, how it differed between musical styles and whether shorter songs enjoyed greater streaming success.

Three different questions.

Three different configurations.

One shared renderer.

Each configuration identifies the relevant dataset, chart type, measurements, highlights and layout.

{% include behind-recipe-explorer.html %}

These original September 2026 configurations predate our current social_square house profile. We're exploring the actual historical recipes, not presenting them as today's default settings.

## What didn't work

Different charts require different amounts of space.

Our comparison of musical styles needed more room for category names and explanatory labels than the album trend chart.

Rather than create a separate renderer, we adjusted the layout instructions.

The framework remained the same.

{% include behind-recipe-layout.html %}

## What we learnt

The configuration allows us to distinguish between a design decision for an individual chart and a design rule that applies across our collection.

We can experiment without losing consistency.

## Try it yourself

Explore the three Bowie chart recipes above.

Notice which instructions change and which remain consistent.

Then experiment with the layout to understand how we allocate space to different elements.

For the curious: [Bowie never needed the three-minute rule](/2026/09/27/bowie-never-needed-the-three-minute-rule/), [original configurations](https://github.com/adamgreen1708/chart-templates/tree/main/archive/projects/2026-09-david-bowie-track-length-success/config), [current configuration template](https://github.com/adamgreen1708/chart-templates/blob/main/src/chart_config_template.py) and [house rules](https://github.com/adamgreen1708/chart-templates/blob/main/spec/538_template_rules.md).

## TL;DR

The data provides the ingredients. CHART_CONFIG provides the recipe.

The renderer follows the instructions.

We concentrate on finding something worth communicating.

<script defer src="{{ '/assets/behind-the-build/recipe-demo.js' | relative_url }}?v=1"></script>
