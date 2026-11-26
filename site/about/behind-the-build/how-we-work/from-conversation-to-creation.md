---
layout: behind-the-build
title: "From conversation to creation"
description: "How ChatGPT, GitHub and a little curiosity power Coffeetableviz."
permalink: /about/behind-the-build/how-we-work/from-conversation-to-creation/
collection_label: How we work
article_number: "01"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/ecosystem.svg
---

## The idea

A question I keep getting asked is how I actually create the things that appear on Coffeetableviz.

How does a conversation with ChatGPT turn into a chart, an interactive art studio or even a virtual gallery?

It's not quite as simple as typing a prompt and pressing a button. Over time, we've built something a little more structured.

And when I say *we*, I mean me, ChatGPT and GitHub.

## The challenge

I enjoy exploring data and creating things. What I enjoy considerably less is repeatedly setting up files, formatting charts, moving images around and doing all the administrative bits that sit between an idea and its publication.

Could we make that process easier without compromising the quality of what we produce?

More importantly, could we build something that remembers how we like to work?

## How it works

I tend to think of our setup as three tools with three very different jobs.

**ChatGPT is my creative and analytical partner.** Somewhere to explore ideas, challenge assumptions, investigate data, develop code and draft articles.

**GitHub is our workshop.** It's where we keep the data, code, instructions and rules that govern how things are made.

**GitHub Pages is our shop window.** It takes the approved website files and makes them available for others to explore at coffeetableviz.com.

The distinction is important. ChatGPT helps us develop the product, but the finished product doesn't need to live inside ChatGPT.

## Under the bonnet

{% include behind-diagram.html name="ecosystem" alt="Human direction leads to ChatGPT and the GitHub repository, with a review loop before publication through GitHub Pages." caption="Three tools. Three different jobs." %}

When we start a project, ChatGPT can access our GitHub repository and read the instructions we've previously written.

Rather than explaining everything again, I can ask it to start a new project using our existing framework.

It can inspect the available data, develop an approach and prepare the files needed to build the product.

GitHub Actions then runs the relevant code and checks. I review the results, challenge anything that doesn't quite work and, when I'm happy, approve publication.

The website is built using Jekyll, which turns our content, templates and supporting files into the pages you see.

It's a series of relatively simple steps that collectively achieve something quite powerful.

## What didn't work

One of the limitations of relying entirely on conversations with AI is consistency.

A new conversation can introduce a slightly different interpretation of an instruction. A chart might look different, a previously agreed rule might be missed, or a lesson learnt on one project might not carry through to the next.

Moving our instructions, configurations and decisions into GitHub gives us a permanent reference point.

## What we learnt

The real value isn't necessarily in the individual tools. It's in how we've connected them.

We've created a shared environment in which ideas can become tangible products, improvements can be retained and future projects can benefit from previous ones.

I'm still responsible for deciding what is worth creating and what is good enough to publish.

The technology simply gives me more opportunities to do it.

## Try it yourself

Explore the [Coffeetableviz GitHub repository](https://github.com/adamgreen1708/chart-templates) and see how the data, instructions, code and website files sit alongside one another.

## TL;DR

ChatGPT helps develop the ideas. GitHub holds the instructions and provides the machinery. GitHub Pages shares the results.

Human curiosity and judgement remain at the centre of it all.
