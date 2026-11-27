---
layout: behind-the-build
title: "Premier League Unfolded — A season in a single view"
description: "How we turned a collection of football results into an interactive story."
permalink: /about/behind-the-build/how-we-made-it/premier-league-unfolded/
collection_label: How we made it
article_number: "05"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/epl-fixture-perspectives.svg
---

## The idea

A league table is a remarkably efficient way of summarising a football season.

But it tells us relatively little about the journey each club has taken to get there.

Back in 2020–21, I created a Tableau visualisation that arranged football results by calendar month, with home games above and away games below.

I wanted to revisit that idea and give it a new home on Coffeetableviz.

## The challenge

Twenty clubs. Thirty-eight games each. Three hundred and eighty matches across an entire season.

How could we present all that information without overwhelming the reader?

Rather than showing everything at once, we decided to make individual clubs the focus, whilst retaining the wider league as context.

## How it works

Every circle represents a completed match.

A win uses a representative club colour, a draw is light grey and a defeat is darker grey.

The position of each circle tells us when the match took place and whether it was played at home or away.

Tap a circle and the underlying details appear: the opponent, score, date and cumulative points.

A shared points scale allows us to move between clubs and explore their different journeys.

{% include behind-epl-demo.html %}

## Under the bonnet

The starting point is a dataset containing the actual completed fixtures.

*Explore how we choose and verify our sources in [Where do the numbers come from?](/about/behind-the-build/how-we-work/data-sources/).*

Python transforms each match into two records, one from the perspective of each participating club.

*Want to understand how? Read [Python — Making sense of the numbers](/about/behind-the-build/how-we-work/python/).*

A home win becomes an away defeat. A draw gives both clubs a point.

{% include behind-diagram.html name="epl-fixture-perspectives" alt="Arsenal beat Leeds five nil on 23 August 2025: Arsenal's home record is a win worth three points; Leeds' away record is a loss worth zero points." caption="One match. Two perspectives. Actual archived 2025–26 result." %}

We calculate results, goals, points and cumulative totals from those records, then package the information into a file that the website can read.

JavaScript builds the interactive visualisation directly from that data.

*Explore the drawing techniques in [Drawing with code — When numbers become pictures](/about/behind-the-build/how-we-work/drawing-with-code/).*

*Want to understand how? Read [JavaScript — Bringing things to life](/about/behind-the-build/how-we-work/javascript/).*

For the ongoing season, GitHub also has a scheduled process that checks for new completed results. Data updates must pass validation and browser tests before they can be published automatically.

The website displays the latest included result date rather than simply assuming the information is current.

*Explore our scheduled workflows and safeguards in [Putting things on autopilot](/about/behind-the-build/how-we-work/autopilot/).*

{% include behind-diagram.html name="epl-refresh" alt="Daily scheduled results check, followed by validation and browser tests for changed data, then guarded data-only publication or an issue if checks fail." caption="Automated, but not unchecked. The automatic publishing permission is restricted to the two season data files, not design, code or editorial changes. No new results means no new data publication." %}

## What didn't work

Our earlier attempt focused primarily on cumulative points.

Technically it worked, but it lost much of what made the original Tableau visualisation interesting: the monthly rhythm and the contrast between home and away performances.

We returned to the original visual structure.

There was also a surprisingly important little detail on mobile: the home-result circles sat too close to the month labels.

A small spacing adjustment made the distinction much clearer.

Sometimes the smallest changes make a considerable difference to how we read a visualisation.

## What we learnt

A good interactive visualisation doesn't necessarily need to display more information.

It needs to make the right information available at the right moment.

We also have to be careful about how we compare clubs during an unfinished season. Teams don't always complete the same number of matches on the same dates.

The cumulative points comparison therefore uses each club's own completed match number, rather than pretending that rearranged fixtures happened together.

## Try it yourself

Explore the [completed 2025–26 season](/stories/premier-league-season-unfolded-2025-26/) or follow the [unfolding 2026–27 season](/resources/epl-2026-27-unfolded/).

Choose your club, tap a result and see whether the patterns tell you something the league table doesn't.

See how we used the same dataset to create [Interwoven — From football data to a virtual art gallery](/about/behind-the-build/how-we-made-it/interwoven/).

For the curious: [original Tableau visualisation](https://public.tableau.com/app/profile/adam.green4310/viz/EPL202021SeasonUnfolded/202021EPLSeason), [project methodology](https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-11-epl-2526-unfolded/README.md), [QA history](https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-11-epl-2526-unfolded/qa_report.md) and [daily refresh workflow](https://github.com/adamgreen1708/chart-templates/blob/main/.github/workflows/epl-2627-refresh.yml).

## TL;DR

Every match becomes a dot. Every dot has a story.

Put them together and a football season becomes something we can explore, rather than simply summarise.
