---
layout: behind-the-build
title: "Putting things on autopilot"
description: "Automating the routine without losing control."
permalink: /about/behind-the-build/how-we-work/autopilot/
collection_label: How we work
article_number: "14"
last_reviewed: 2026-11-27
social_image: /assets/behind-the-build/automation-flow.svg
---

## The idea

I enjoy creating things considerably more than I enjoy maintaining them.

Refreshing datasets, checking for updates and producing regular reports are all useful activities. They're also reasonably predictable.

So why not get the computer to do some of that work?

## The challenge

Automation is relatively easy when everything goes to plan.

The interesting bit is deciding what should happen when it doesn't.

A missing dataset, an unavailable source or an unexpected change shouldn't result in incorrect information appearing on the website.

{% include behind-diagram.html name="automation-flow" alt="A scheduled task executes instructions and validates its results. A failed check leads to stopping and investigating; successful checks allow work to continue within approved rules." caption="Automation needs to know when to stop, as well as when to start." %}

## How it works

We use two different types of automation.

ChatGPT's scheduled tasks can help prepare content, review information and deliver summaries.

GitHub Actions can run code at predetermined times, retrieve data, perform calculations and build outputs.

The two can complement one another.

{% include behind-automation-levels.html %}

## Under the bonnet

Our Premier League Unfolded visualisation is a good example.

Each morning, GitHub is scheduled to check for newly completed matches. If there are new results, it updates the dataset, runs validation checks and tests the visualisation.

Only verified updates to two specific data files are eligible for automatic publication.

Our Daily Pulse works slightly differently. GitHub prepares a report on the previous day's website activity, which ChatGPT can then summarise for me.

## What didn't work

Our website analytics source has occasionally been unavailable when a scheduled report has attempted to run.

Rather than assume the numbers were zero, we introduced retries and a second opportunity to generate a missing report later in the day.

Sometimes the most useful automation is the one that recognises it hasn't succeeded.

{% include behind-automation-pulse.html %}

## What we learnt

Not everything needs to be fully automated.

I'm comfortable allowing verified football results to update automatically within strict controls.

I'm considerably less comfortable allowing AI to decide what editorial content should appear under my name without reviewing it.

Different tasks require different levels of autonomy.

## Try it yourself

Follow our simulated Premier League update below.

Introduce a problem and see what happens when one of the checks fails.

{% include behind-automation-epl.html %}

{% include behind-automation-records.html %}

For the curious: [Premier League Unfolded](/about/behind-the-build/how-we-made-it/premier-league-unfolded/), [football refresh workflow](https://github.com/adamgreen1708/chart-templates/blob/main/.github/workflows/epl-2627-refresh.yml), [independent football QA](https://github.com/adamgreen1708/chart-templates/blob/main/.github/workflows/epl-2627-qa.yml), [Daily Pulse workflow](https://github.com/adamgreen1708/chart-templates/blob/main/.github/workflows/daily-site-pulse.yml) and [daily editorial commands](https://github.com/adamgreen1708/chart-templates/blob/main/spec/DAILY_RUN_COMMANDS.md).

## TL;DR

Automate the predictable. Retain control over the important decisions.

And make sure the system knows when to stop.

<script defer src="{{ '/assets/behind-the-build/automation-demo.js' | relative_url }}?v=1"></script>
