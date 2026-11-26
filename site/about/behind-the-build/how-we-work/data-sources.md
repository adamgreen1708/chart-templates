---
layout: behind-the-build
title: "Where do the numbers come from?"
description: "Why finding a dataset is only the beginning."
permalink: /about/behind-the-build/how-we-work/data-sources/
collection_label: How we work
article_number: "08"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/data-source-check.svg
---

## The idea

Most of my Coffeetableviz projects begin with a question.

Sometimes it's prompted by something I've read, a film I've watched or a conversation I've had.

Before we can explore that curiosity through a visualisation, we need to find some information.

And that's where things become interesting.

## The challenge

Finding numbers has arguably never been easier.

Finding numbers that genuinely answer the question we're asking is a rather different matter.

A dataset might be incomplete, outdated or measure something subtly different from what we had imagined.

AI can help us discover potential sources, but a confidently written answer isn't necessarily evidence.

We need to establish where the information originated.

{% include behind-diagram.html name="data-source-check" alt="Published data, APIs and source records lead to checks of origin, meaning, completeness and suitability. Suitable evidence is retained; unresolved issues require investigation or rejection." caption="Every number has a history. Accuracy starts before the first chart." %}

## How it works

We acquire data in several different ways.

Sometimes we download an existing dataset, often in the form of a CSV file.

Sometimes we use an API, which provides a way for one piece of software to request information from another.

And sometimes we need to combine several sources to build a dataset that doesn't already exist.

Our Patrick Stewart project is a good example. IMDb provided film information, ratings and votes, whilst additional documented credits helped establish which titles belonged in our selection.

The dataset was built around the question rather than simply accepting the first collection of numbers we found.

**Understanding an API**

API stands for Application Programming Interface. Think of it as an agreed way of asking another computer system for information.

{% include behind-diagram.html name="data-source-api" alt="Python in GitHub requests 2026–27 match results from football-data.org. The API responds with JSON, which must be validated before use." caption="Asking for information. Receiving data isn't the same as trusting it." %}

This is the actual endpoint used by our ongoing Premier League project:

<div class="btb-py-code"><p>ACTUAL API ENDPOINT</p><pre><code>https://api.football-data.org/v4/competitions/PL/matches?season=2026</code></pre></div>

The request identifies the competition and season. The service returns structured information that our Python instructions can process. The authenticated request runs in GitHub, not in the reader's browser.

Our workflow also checks that previously recorded results have not unexpectedly disappeared or changed, and excludes incomplete or unplayed fixtures.

## Under the bonnet

Finding the source is only part of the process.

We need to understand what each row represents, what period the information covers, which units are being used and whether anything is missing.

We also need to check whether the source permits the intended use.

For our completed 2025–26 Premier League project, we retained a dated copy of the match results and documented where those results originated.

The original data, transformed information and processing instructions are stored together in GitHub.

This gives us something called data provenance: a record of where our numbers came from and how they reached the finished visualisation.

{% include behind-data-passport.html %}

## What didn't work

A particularly interesting challenge emerged during our Patrick Stewart project.

We had documented 70 films, but only 68 had available IMDb ratings and votes.

The other two weren't necessarily unpopular or poorly rated. We simply didn't have those measurements.

Replacing the missing values with zero would have introduced information that wasn't present in the source.

{% include behind-data-missing.html %}

We also had to be careful about what IMDb votes actually represent.

They tell us about voting activity around a film, not how many people watched it or how much they appreciated a particular actor.

The distinction matters.

## What we learnt

A reliable source doesn't automatically produce a reliable conclusion.

We still need to understand the definitions, limitations and context of the information.

There is considerable value in retaining the original dataset rather than simply keeping the finished chart.

It allows us to revisit the numbers, challenge our assumptions and understand why we reached a particular conclusion.

Occasionally, the available information simply isn't sufficient to tell the story we initially imagined.

That's a perfectly good reason to change the question.

## Try it yourself

Explore the examples below and consider which questions our different datasets can genuinely answer.

{% include behind-data-evidence.html %}

Then look at the source references beneath one of our charts.

Behind that little line of text should be a much bigger story about where the information came from.

For the curious: [Premier League archived source and methodology](https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-11-epl-2526-unfolded/README.md), [current-season API and validation documentation](https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-11-epl-2627-unfolded/README.md), [Patrick Stewart archived film dataset](https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-10-patrick-stewart/data/films_expanded.csv), [editorial judgement standard](https://github.com/adamgreen1708/chart-templates/blob/main/docs/editorial_judgement_standard.md) and [Python — Making sense of the numbers](/about/behind-the-build/how-we-work/python/).

## TL;DR

Good data visualisation starts with good evidence.

Find it. Question it. Understand it. Retain it.

Only then should we start drawing.

<script defer src="{{ '/assets/behind-the-build/data-sources-demo.js' | relative_url }}?v=1"></script>
