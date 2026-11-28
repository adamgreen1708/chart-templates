---
layout: behind-the-build
title: "From GitHub to website"
description: 'What actually happens when I say "push"?'
permalink: /about/behind-the-build/how-we-work/github-to-website/
collection_label: How we work
article_number: "13"
last_reviewed: 2026-11-27
social_image: /assets/behind-the-build/publish-workshop.svg
---

## The idea

One of the things I find particularly satisfying about our setup is how little manual publishing is involved.

I can develop an article with ChatGPT, review the charts, make a few changes and, when I'm happy, simply say "push".

But there's quite a lot happening behind that little instruction.

{% include behind-diagram.html name="publish-workshop" alt="ChatGPT prepares content and code, GitHub stores and versions the files, GitHub Actions checks and builds the website, and GitHub Pages deploys it to coffeetableviz.com. Changes are reviewed before merging and deployment." caption="From workshop to shop window. Simplified overview: changes are reviewed before they are merged and deployed." %}

## The challenge

I wanted publishing to be straightforward without giving AI unrestricted permission to change the live website.

We needed somewhere to develop ideas, review changes and check that everything still worked.

That's where GitHub comes in.

## How it works

Think of a repository as a project folder with a memory.

It contains our website files, charts, code and instructions, along with a history of the changes we've made.

Rather than immediately change the main version, we create a separate working version called a branch.

Changes are recorded as commits.

When they're ready, we create a pull request: essentially a proposal to bring those changes into the main version.

{% include behind-publish-glossary.html %}

## Under the bonnet

GitHub Actions runs our automated checks.

Jekyll then assembles the website from our articles, templates and supporting files.

Once the changes have passed the checks and received my approval, we merge them into the main branch.

That triggers another build, followed by deployment to GitHub Pages, which hosts Coffeetableviz.

{% include behind-publish-record.html %}

## What didn't work

The distinction between a successful build and a successful publication is important.

A website can build successfully whilst containing a poorly designed page.

Equally, merging our changes doesn't necessarily mean the new article is already visible to readers.

We need to check the finished website too.

## What we learnt

The value of this approach isn't simply automation. It's control.

*Explore our scheduled workflows and safeguards in [Putting things on autopilot](/about/behind-the-build/how-we-work/autopilot/).*

We can develop something without disturbing the existing website, inspect exactly what has changed and retain a record of the decisions we've made.

And if something needs correcting, we have a history to work from.

## Try it yourself

Follow the interactive publishing example below.

Create a branch, record a change, run the checks and approve its publication.

Notice that the public website remains unchanged until deployment succeeds.

{% include behind-publish-demo.html %}

For the curious: [actual publishing workflow](https://github.com/adamgreen1708/chart-templates/blob/main/.github/workflows/publish-blog.yml), [process documentation](https://github.com/adamgreen1708/chart-templates/blob/main/docs/coffeetableviz_process_flow.md) and [HTML and CSS — Giving everything a home](/about/behind-the-build/how-we-work/html-css/).

## TL;DR

ChatGPT helps prepare the changes. GitHub records and checks them. Jekyll builds the website. GitHub Pages makes it available to readers.

A surprisingly straightforward way of publishing, with a few rather important safeguards.

<script defer src="{{ '/assets/behind-the-build/publish-demo.js' | relative_url }}?v=1"></script>
