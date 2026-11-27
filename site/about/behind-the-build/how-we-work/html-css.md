---
layout: behind-the-build
title: "HTML and CSS — Giving everything a home"
description: "How we turn a collection of content into a website with its own identity."
permalink: /about/behind-the-build/how-we-work/html-css/
collection_label: How we work
article_number: "06"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/html-css-structure.svg
---

## The idea

One of the things I wanted Coffeetableviz to have was a recognisable visual identity.

Not just within the charts themselves, but throughout the website.

Consistent typography, colours, spacing and layouts that make everything feel as though it belongs together.

That's where HTML and CSS come in.

## The challenge

Our website contains a rather eclectic collection of things.

Articles, charts, interactive studios, a virtual gallery and now a reference library explaining how everything works.

Each has different requirements, but I didn't want them to feel like entirely separate websites.

We needed a common structure and a shared set of design rules, with enough flexibility to accommodate the more creative projects.

## How it works

HTML describes the structure of a webpage.

It identifies the headings, paragraphs, images, links, buttons and other elements that make up the content.

CSS describes how those elements should appear.

It determines the colours, typography, spacing, alignment and dimensions.

JavaScript, as we explored in the [previous article](/about/behind-the-build/how-we-work/javascript/), adds the behaviour.

Think of HTML as the architecture, CSS as the interior design and JavaScript as the things that move.

{% include behind-diagram.html name="html-css-structure" alt="The same heading, paragraph and link presented first as simple structured content and then with editorial typography, colour and spacing." caption="Same content. Different presentation. Conceptual example." %}

{% include behind-html-css-style.html %}

## Under the bonnet

Rather than write an entirely new webpage for every article, we use shared layouts.

Our Behind the build articles, for example, all use the same underlying layout. Each article supplies its own title, description and content.

**Where does Jekyll fit in?**

Imagine having to recreate the website's navigation, header, footer and article layout every time we publish a new story.

That would become rather tedious.

Jekyll is what's known as a static site generator. It takes our written content, reusable page layouts and shared components and assembles them into finished webpages.

We write our articles in Markdown, a simple way of formatting text without having to write HTML.

Jekyll converts that content into HTML and inserts it into the appropriate page layout.

GitHub Pages then makes the finished website available to our readers.

*Follow the publication process in [From GitHub to website](/about/behind-the-build/how-we-work/github-to-website/).*

Write the content once. Define the layout once. Reuse it throughout the website.

{% include behind-diagram.html name="html-css-jekyll" alt="Markdown content and HTML layouts feed Jekyll, which assembles the HTML pages alongside CSS, JavaScript and other assets. GitHub Pages serves the finished files." caption="The website assembly line. Jekyll builds the pages; GitHub Pages hosts the finished website." %}

This is a genuine extract from our shared article layout. The first line identifies the article heading. The second identifies its introductory description. The placeholders tell Jekyll where to insert the information belonging to each article.

{% include behind-html-css-template.html %}

Our shared CSS stylesheet then applies the visual rules.

We can also create additional rules for specific sections of the website without changing everything else.

This means we can improve the appearance of an entire collection by adjusting a few instructions in one place.

## What didn't work

When we first introduced Behind the build, the pages inherited the generous spacing we'd established for our main blog.

It worked reasonably well for individual stories, but made the reference library feel unnecessarily stretched out.

There were large gaps between headings and paragraphs, and the article index wasn't particularly easy to scan on a phone.

Rather than redesign every page, we introduced a separate set of spacing and layout rules for the collection.

The content remained the same. Its presentation improved considerably.

It's a useful reminder that consistency doesn't mean everything has to look identical.

This is an actual rule from our Behind the build stylesheet:

<div class="btb-py-code"><p>ACTUAL CSS INSTRUCTION</p><pre><code>.prose-page.btb-article {
  padding-bottom: 3rem;
}</code></pre></div>

Our original global rule specified 8rem. One small instruction. A change applied throughout the collection.

{% include behind-html-css-spacing.html %}

## What we learnt

Separating the content from its appearance gives us considerable flexibility.

We can change the size of a heading, tighten the spacing or rearrange a layout without rewriting the underlying article.

We can also tell the browser to behave differently depending on the available screen width.

This is known as responsive design.

It's particularly important for Coffeetableviz, where an article or interactive visualisation needs to be just as enjoyable on a phone as it is on a larger screen.

A media query is essentially a conditional instruction to the browser: when the screen becomes sufficiently narrow, apply a different layout.

{% include behind-html-css-responsive.html %}

{% include behind-diagram.html name="html-css-browser" alt="HTML provides structure, CSS provides appearance and JavaScript provides behaviour. All three contribute to the browser experience." caption="Three technologies. Three complementary jobs." %}

## Try it yourself

Experiment with the examples above.

Remove the styling, change the spacing and switch between a wider screen and a narrower one.

Notice that the underlying content doesn't change.

The browser is simply following a different collection of presentation rules.

For the curious: [shared article layout](https://github.com/adamgreen1708/chart-templates/blob/main/site/_layouts/behind-the-build.html), [website stylesheet](https://github.com/adamgreen1708/chart-templates/blob/main/site/assets/css/site.css), [Behind the build stylesheet](https://github.com/adamgreen1708/chart-templates/blob/main/site/assets/behind-the-build/style.css), [Pixel Art Studio](/about/behind-the-build/how-we-made-it/pixel-art-studio/) and [From conversation to creation](/about/behind-the-build/how-we-work/from-conversation-to-creation/).

## TL;DR

HTML gives our content a structure. CSS gives it a visual identity.

Together, they allow us to build a website that feels consistent without restricting our creativity.

<script defer src="{{ '/assets/behind-the-build/html-css-demo.js' | relative_url }}?v=1"></script>
