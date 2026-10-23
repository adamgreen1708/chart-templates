---
title: "I spent hours building 64 squares. AI rebuilt them in minutes."
date: 2026-10-23 22:15:00 +0100
slug: i-spent-hours-on-64-squares-ai-rebuilt-them-in-minutes
description: "My 8×8 pixel-art builder took hours and hours to make in Tableau. ChatGPT rebuilt it for coffeetableviz in minutes. I'm delighted. I'm also a little sad."
category: Technology
read_time: 5 minute read
card_image: /assets/pixel-art-builder/ai-rebuild-feature.svg
hero_image: /assets/pixel-art-builder/ai-rebuild-feature.svg
social_image: /assets/pixel-art-builder/ai-rebuild-feature.svg
hero_alt: "Two 8×8 pixel grids: a dark tangled design becomes a clean red pixel heart, symbolising the original hours-long Tableau build and the rapid AI-assisted rebuild."
---

I've built some fairly unusual things in Tableau over the years. Some involved serious data. Some involved music, films or the occasional questionable creative decision.

And one involved **64 little squares**.

Back in 2023, I made [Greeny's 8×8 Pixel Art Builder](https://public.tableau.com/app/profile/adam.green4310/viz/8x8PixelArtBuilder/8X8PIXELART) on Tableau Public. You chose from eight colours and clicked squares to paint a picture. Click a coloured square again and it turned white.

That's it. No KPIs. No business question. Just a tiny drawing tool hiding inside a data visualisation platform.

**It took me hours and hours to build.**

I spent those hours stretching Tableau beyond what I'd normally ask of it: thinking through the grid, the interactions and how to make the whole thing behave like a little drawing app. I loved that challenge. It's why I still enjoy making things just for fun.

## Then I asked a rather dangerous question

This week I sent ChatGPT a link to my original and asked:

> Can you build this for my coffeetableviz blog?

Not a lengthy technical specification. Not a blueprint. Just the original idea and a request to bring it onto my GitHub Pages site.

**Minutes later, there was a working version.**

Eight colours. Sixty-four squares. And a few extras: drag-to-paint, undo and redo, ready-made designs, PNG export and a link that lets someone else open your exact creation.

I opened it on my iPhone and started tapping.

It worked.

*Oh my freaking gosh.*

I was genuinely delighted. And then, almost immediately, a little deflated.

Because something I'd poured hours into had apparently become a few minutes of conversation.

**I'm both happy and sad.** And I don't think those feelings cancel each other out.

<div class="image-grid">
  <figure>
    <img src="{{ '/assets/migrated/creating-for-fun/8x8-pixel-art.jpg' | relative_url }}" alt="The original 8×8 pixel-art experiment featured in my Creating for fun article." loading="lazy">
    <figcaption>The original Tableau experiment — a lot more work than 64 squares would suggest. <a href="https://public.tableau.com/app/profile/adam.green4310/viz/8x8PixelArtBuilder/8X8PIXELART">Open it on Tableau Public →</a></figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/pixel-art-builder-card.svg' | relative_url }}" alt="A red pixel-art heart on an 8×8 grid, representing the new coffeetableviz builder." loading="lazy">
    <figcaption>The new browser version, with extra features. <a href="{{ '/resources/8x8-pixel-art-builder/' | relative_url }}">Have a go →</a></figcaption>
  </figure>
</div>

## How did AI do it so quickly?

Here's the important bit: **it didn't convert my Tableau workbook into a website**.

It took an idea that already existed, inspected my publicly shared example and the coffeetableviz site structure, then built the same interaction using tools that browsers already understand.

In Tableau, I'd been persuading a visual analytics application to behave like a drawing program.

In the new version, the browser is doing something much closer to its day job.

The mechanics are surprisingly small:

- **HTML** creates 64 buttons in an eight-by-eight grid.
- **CSS** makes them look like neat little pixels, including on a phone.
- **JavaScript** keeps track of which colour belongs to each square and changes it when you paint.

In fact, the entire starting canvas is this one line:

`let pixels = new Array(64).fill(0);`

There are 64 positions. Each holds a number: **0 means white**, and **1 to 8** represent the eight paint colours.

When you touch a square, JavaScript changes that number and redraws the corresponding colour. Undo keeps previous copies of the 64 numbers. Your design can be saved in the browser, or encoded into a shareable link as 64 digits. And PNG export draws those same colours onto a larger image.

No database. No server-side drawing engine. **No AI model running every time someone paints a pixel.** Once published, it's an ordinary little web application.

The AI's role was in **writing and assembling the code**, making the GitHub changes and helping check the behaviour. I reviewed the result, approved the pull request and tested it on my phone. It wasn't magic, and it wasn't a flawless one-click conversion. But the speed still caught me rather off guard.

## So were all those Tableau hours wasted?

No. Although I confess, for a moment, they felt a little less valuable.

The original was about far more than the finished picture. It was about getting curious, learning what a tool could do and finding creative ways around its limits. It taught me things. It gave me something original to share.

And, rather importantly, **there wouldn't have been anything to recreate without that original idea**.

The AI version was faster partly because the difficult creative decisions had already been made. The grid size, the concept, the interaction and the reason it should exist were sitting there, ready to be understood.

That doesn't diminish what the technology achieved. Writing, styling and wiring up a responsive app in minutes is extraordinary.

But it does change where I spend my time.

Perhaps a few less hours wrestling with the mechanics. A few more asking **what would be fun, interesting or useful to make next?** And then testing whether it actually works, rather than assuming a confident-looking piece of code must be correct.

## A slightly uncomfortable, rather exciting conclusion

I can admire what AI made without pretending I feel nothing about how quickly it made it.

I can also be proud of the hours I spent in Tableau without insisting everyone else should have to spend those hours too.

Maybe that's the change: not that curiosity, judgement or creativity have become irrelevant, but that the distance between an idea and something you can actually use has become very, very short.

As someone who enjoys the *making* as much as the *finished thing*, I'm still working out how I feel about that.

Probably with another tiny experiment.

**[Try the new 8×8 Pixel Art Builder →]({{ '/resources/8x8-pixel-art-builder/' | relative_url }})**

And if you'd like to compare, here's [the original Tableau Public version](https://public.tableau.com/app/profile/adam.green4310/viz/8x8PixelArtBuilder/8X8PIXELART). Same little idea. Very different route to getting there.

## TLDR

I spent hours making a 64-square drawing tool in Tableau. ChatGPT rebuilt the idea as a working web app in minutes.

**I'm impressed. I'm a bit sad. I'm still proud of those hours.**

All three can be true.

<aside class="method-note">
  <h2>Behind the build</h2>
  <p>The new builder is plain HTML, CSS and JavaScript, hosted on GitHub Pages. You can inspect the <a href="https://github.com/adamgreen1708/chart-templates/blob/main/site/assets/js/pixel-art-builder.js">drawing code</a> and <a href="https://github.com/adamgreen1708/chart-templates/pull/146">the original pull request</a>. This was a reimplementation based on the public example and the existing site, <strong>not</strong> a line-by-line translation of the Tableau workbook. This article was drafted with ChatGPT using my original project, reaction and editorial direction. The original project, reaction and editorial decisions are mine.</p>
</aside>

<p class="sign-off"><strong>simple charts. clear stories. and occasionally, 64 squares.</strong></p>
