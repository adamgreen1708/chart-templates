---
layout: behind-the-build
title: "Keeping AI honest"
description: "Why a successfully generated chart isn't necessarily a good chart."
permalink: /about/behind-the-build/how-we-work/keeping-ai-honest/
collection_label: How we work
article_number: "03"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/controls.svg
---

## The idea

AI makes it remarkably easy to create things.

That doesn't necessarily make it easier to create good things.

Working in analytics, I've spent a considerable amount of time thinking about the difference between presenting information and genuinely helping someone understand it.

I see no reason why using AI should change that.

## The challenge

AI can produce something that looks convincing, reads well and appears entirely plausible.

Unfortunately, none of those qualities guarantee that it's correct.

The challenge isn't just preventing invented numbers. It's also making sure we're asking interesting questions, drawing reasonable conclusions and communicating what the data actually tells us.

## How it works

We've gradually built a set of controls into the way we create things for Coffeetableviz.

There are documented rules covering how we acquire data, explore potential stories, configure charts, render images and publish content.

*Explore how we choose and verify our sources in [Where do the numbers come from?](/about/behind-the-build/how-we-work/data-sources/).*

These instructions live in GitHub. They're available to ChatGPT whenever we start a new project.

We also have automated checks that help identify technical problems.

*Explore how we correct problems and retain the lessons in [When things go wrong](/about/behind-the-build/how-we-work/when-things-go-wrong/).*

But perhaps the most important control is recognising that different things need different types of checking.

A piece of code can run successfully while producing a misleading chart. A chart can be entirely accurate while being thoroughly uninteresting.

## Under the bonnet

{% include behind-diagram.html name="controls" alt="Evidence, editorial, visual and human checks lead to approval, with a return loop if checks fail." caption="Trust is built into the process." %}

I think of our checks in four different ways.

**Evidence:** Are the numbers real? Do the calculations make sense? Are we comparing like with like?

**Editorial:** What are we actually telling the reader? Does the evidence support our headline?

**Visual:** Are the labels readable? Do the colours have meaning? Does the chart work on a phone?

**Human:** Am I comfortable putting my name against it?

Only once those questions have been satisfactorily addressed should something reach the website.

{% include behind-diagram.html name="tests" alt="Technical checks such as code runs and image created contrast with editorial questions about interest, accuracy and readability." caption="A successful build is not an editorial approval." %}

## What didn't work

A recent example was our Robert Pattinson project.

The initial charts were technically competent, but they weren't particularly interesting. One grouped his career into broad periods and compared IMDb ratings. Another plotted ratings against votes.

They summarised information, but they didn't reveal much.

Revisiting the analysis led us towards the relationships between Pattinson's films and the people who had played James Bond.

A rather more interesting human connection.

We documented the experience in GitHub, including the limitations that remained, and strengthened our editorial guidance for future projects.

*Explore how we retain those lessons in [A memory outside ChatGPT](/about/behind-the-build/how-we-work/external-memory/).*

One of the resulting rules is particularly simple: don't make three charts just because we normally make three charts.

Every chart should earn its place.

*Continue with [Finding the story](/about/behind-the-build/how-we-work/finding-the-story/).*

## What we learnt

The most useful thing about documenting mistakes is that they can improve more than the project that exposed them.

A new rule, a better test or an improved instruction becomes part of the framework we use next time.

It doesn't mean we'll get everything right. But it does give us a mechanism for learning.

AI can help us do more. It shouldn't encourage us to think less.

## Try it yourself

Our [quality assurance checklist](https://github.com/adamgreen1708/chart-templates/blob/main/docs/chart_qa_checklist.md) and [editorial judgement standard](https://github.com/adamgreen1708/chart-templates/blob/main/docs/editorial_judgement_standard.md) are available in GitHub. Read the [Pattinson retrospective](https://github.com/adamgreen1708/chart-templates/blob/main/docs/lessons/2026-11-19-pattinson-editorial-retrospective.md) for the detailed case.

## TL;DR

Automation helps us check the work. Documented rules help us retain what we've learnt. Neither replaces curiosity, critical thinking or human judgement.

A good chart still needs to earn its place.
