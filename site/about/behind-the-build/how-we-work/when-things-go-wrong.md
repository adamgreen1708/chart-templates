---
layout: behind-the-build
title: "When things go wrong"
description: "Making our mistakes useful."
permalink: /about/behind-the-build/how-we-work/when-things-go-wrong/
collection_label: How we work
article_number: "15"
last_reviewed: 2026-11-27
social_image: /assets/behind-the-build/mistakes-cycle.svg
---

## The idea

If you've ever created something with AI, you'll probably recognise the experience.

Something works beautifully. You make a seemingly minor change. Something else stops working.

We've had our fair share of those moments at Coffeetableviz.

{% include behind-diagram.html name="mistakes-cycle" alt="A continuous improvement cycle: identify the problem, understand its cause, correct and test it, then retain the lesson." caption="Fixing the immediate problem is only half the job." %}

## The challenge

Not all problems are immediately obvious.

Broken code is relatively easy to identify. Incorrect calculations, misleading headlines and poorly positioned labels can be considerably more subtle.

Sometimes everything appears to work, yet the result simply isn't good enough.

## How it works

When something goes wrong, we try to establish where the problem originates.

Is it the data? The analysis? The chart configuration? The rendering code? Or the website itself?

Understanding the cause helps us avoid fixing the wrong thing.

## Under the bonnet

Our Premier League Unfolded project provides a nice little example.

Whilst reviewing the visualisation on my phone, I noticed that the West Ham home results for August were sitting too close to the month label.

The solution was remarkably simple: eight pixels of additional clearance.

But rather than just correct the appearance, we added a browser test to check that the problem didn't return.

{% include behind-mistakes-gap.html %}

## What didn't work

Even this reference library has provided a few lessons.

The original About page article list looked rather messy on my phone.

We revised how the styling was loaded and separated the article titles from their descriptions, making the list more resilient even if the styling failed.

A small problem with a useful wider lesson.

## What we learnt

There's a difference between correcting a mistake and preventing it from happening again.

A particular chart may need a small adjustment. A recurring problem may need a change to our shared framework.

Knowing which is which is an important part of the process.

*Explore the reader's experience in [Designing for everyone](/about/behind-the-build/how-we-work/designing-for-everyone/).*

{% include behind-diagram.html name="mistakes-fix-scope" alt="Decide whether a correction is specific to a chart or a reusable lesson. Correct the individual configuration or improve the shared framework, and test the correction." caption="Improve the system where appropriate, without unnecessarily changing previously approved charts." %}

## Try it yourself

Become the reviewer for a moment.

Look for potential problems in the examples below and decide how you would approach them.

{% include behind-mistakes-quiz.html %}

For the curious: [Premier League QA history](https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-11-epl-2526-unfolded/qa_report.md), [browser regression test](https://github.com/adamgreen1708/chart-templates/blob/main/scripts/qa/epl_2526_browser_test.py), [About page correction](https://github.com/adamgreen1708/chart-templates/pull/245), [chart QA checklist](https://github.com/adamgreen1708/chart-templates/blob/main/docs/chart_qa_checklist.md) and [Keeping AI honest](/about/behind-the-build/how-we-work/keeping-ai-honest/).

## TL;DR

Things will go wrong.

Identify the problem, understand its cause, correct it and retain the lesson.

Then make something better.

<script defer src="{{ '/assets/behind-the-build/mistakes-demo.js' | relative_url }}?v=1"></script>
