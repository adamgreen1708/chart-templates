---
layout: behind-the-build
title: "A memory outside ChatGPT"
description: "Building something that learns from its previous projects."
permalink: /about/behind-the-build/how-we-work/external-memory/
collection_label: How we work
article_number: "13"
last_reviewed: 2026-11-27
social_image: /assets/behind-the-build/memory-projects.svg
---

## The idea

One of the frustrations I encountered when working with AI was repeatedly explaining things we'd already agreed.

Our preferred chart style. How we check the numbers. How we structure a project. Even how we publish an article.

I wanted those decisions to become part of the way we work, rather than something confined to a conversation.

## The challenge

Conversations are a useful place to explore ideas.

They're not necessarily the best place to maintain a set of instructions that evolves over time.

Rather than rely entirely on ChatGPT remembering previous discussions, we started documenting our decisions in GitHub.

## How it works

Our repository contains considerably more than code and data.

It contains instructions for ChatGPT, charting standards, publishing processes, quality checklists and lessons from previous projects.

When we begin something new, ChatGPT can consult these documents.

We're no longer starting with a blank piece of paper.

{% include behind-diagram.html name="memory-projects" alt="Experience from three projects is captured as instructions, design standards, lessons and reusable code in GitHub, giving the next project a better starting point." caption="Every project informs the next." %}

{% include behind-memory-context.html %}

## Under the bonnet

One particularly useful file is called AGENTS.md.

Think of it as an induction document for an AI joining our project.

It explains how we work, identifies the important instructions and establishes some boundaries around what can be changed.

Other documents provide more detailed guidance.

Together, they form a reference library that supports our day-to-day creative work.

{% include behind-memory-library.html %}

## What didn't work

When we introduced a new chart style, we didn't want every previously published chart to change automatically.

We documented the new design standards alongside the requirement to preserve older charts until their replacements had been reviewed and approved.

That decision became part of our framework, rather than something I needed to remember to mention every time.

{% include behind-memory-decision.html %}

## What we learnt

Whenever a project reveals something useful, we have an opportunity to improve the next one.

Sometimes that means changing a piece of code. Sometimes it's a new check or a better instruction.

The important thing is capturing the lesson somewhere we can find it again.

## Try it yourself

Explore the difference between starting a project with a simple request and starting with an established set of instructions.

Then explore the documents that sit behind our own framework.

## TL;DR

ChatGPT helps us develop ideas.

GitHub helps us retain the instructions, decisions and lessons behind them.

The next project should benefit from the last.

<script defer src="{{ '/assets/behind-the-build/memory-demo.js' | relative_url }}?v=1"></script>
