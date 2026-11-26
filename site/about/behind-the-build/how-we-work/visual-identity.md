---
layout: behind-the-build
title: "Building a visual identity"
description: "Creating something recognisably Coffeetableviz."
permalink: /about/behind-the-build/how-we-work/visual-identity/
collection_label: How we work
article_number: "11"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/identity-vocabulary.svg
---

## The idea

I've always admired publications such as the Financial Times and FiveThirtyEight for their distinctive approach to data visualisation.

There's something rather nice about recognising where a chart comes from before you've read the source.

I wanted Coffeetableviz to develop its own visual identity.

{% include behind-diagram.html name="identity-vocabulary" alt="A light-grey square editorial illustration with the words Simple charts. Clear stories. and a grid of illustrative grey, blue and red dots." caption="Less, but with purpose." %}

## The challenge

Working with AI makes it incredibly easy to experiment with different visual styles.

Perhaps a little too easy.

Without some consistency, a collection of individually attractive charts can feel like a collection of unrelated pieces.

## How it works

Our charting framework is built around a relatively simple visual language.

A light-grey canvas. A restrained colour palette. Clear typography. Generous margins. A consistent approach to titles and source references.

The intention is to give the information room to breathe.

{% include behind-identity-palette.html %}

## Under the bonnet

We've established a square format for our statistical charts, particularly with mobile readers in mind.

Blue typically directs attention. Red provides emphasis or distinguishes an important comparison. Grey allows the surrounding information to remain visible without competing for attention.

Those colours need to have meaning, rather than simply making things look attractive.

{% include behind-identity-colour.html %}

Our creative studios and gallery experiments have more freedom. They don't all need to look like our statistical charts.

## What didn't work

A chart that looks great on a laptop doesn't necessarily work on a phone.

We've gradually increased the size of our typography, refined our margins and reconsidered how much information we try to fit into a single image.

Those lessons became part of our shared rendering framework.

{% include behind-identity-typography.html %}

## What we learnt

Consistency doesn't mean repetition.

A visual identity should accommodate different subjects, chart types and creative ideas without losing its character.

Perhaps the most important part of our house style isn't the colour palette or typography.

It's knowing what to leave out.

{% include behind-identity-examples.html %}

## Try it yourself

Experiment with colour, emphasis and typography in the examples above.

Notice how relatively small design decisions change what attracts your attention.

For the curious: [approved house style](https://github.com/adamgreen1708/chart-templates/blob/main/spec/538_template_rules.md), [renderer style profiles](https://github.com/adamgreen1708/chart-templates/blob/main/src/chart_style.py), [website stylesheet](https://github.com/adamgreen1708/chart-templates/blob/main/site/assets/css/site.css) and [The recipe for a chart](/about/behind-the-build/how-we-work/chart-recipe/).

## TL;DR

A visual identity is more than a collection of colours and fonts.

It's a consistent way of helping people see what matters.

Simple charts. Clear stories.

<script defer src="{{ '/assets/behind-the-build/identity-demo.js' | relative_url }}?v=1"></script>
