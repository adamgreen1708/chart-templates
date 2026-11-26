---
layout: behind-the-build
title: "Python — Making sense of the numbers"
description: "What actually happens when we say Python transforms the data?"
permalink: /about/behind-the-build/how-we-work/python/
collection_label: How we work
article_number: "04"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/python-transform.svg
---

## The idea

Throughout Behind the build, we've made several references to Python.

Python prepares our data. Python calculates the numbers. Python renders our charts.

All very reassuring, but what does that actually mean?

At its simplest, Python is a language that allows us to write instructions for a computer.

And much of what we do at Coffeetableviz involves giving a computer rather specific instructions about what to do with some numbers.

## The challenge

Data rarely arrives in precisely the format we need.

Take our Premier League dataset. Each row describes a football match, including the date, home team, away team and final score.

That's perfectly useful if we're interested in individual matches.

But our interactive visualisation is designed around individual clubs. We want to know how each club performed at home and away, how many points it earned and how those points accumulated throughout the season.

The information is there. It just needs reorganising.

## How it works

Think of Python as a particularly obedient assistant with a written set of instructions.

Open this file. Read each row. Identify the home and away teams. Calculate the result from each team's perspective. Award the appropriate points.

Repeat.

Our original 380 match records become 760 club-level records.

We haven't created new football matches. We've simply changed the way the information is organised.

This allows us to answer questions that were rather more awkward to answer using the original dataset.

{% include behind-diagram.html name="python-transform" alt="380 match rows enter a Python transformation and become 760 club-level records stored in JSON." caption="Data doesn't prepare itself. One match becomes two club perspectives." %}

## Under the bonnet

Python reads our CSV file, which is essentially a table stored as plain text.

We write rules to extract the relevant information, convert text into numbers and perform calculations.

For example, a win earns three points, a draw earns one and a defeat earns none.

This is an actual line from our archived Python script:

{% include behind-python-code.html %}

{% include behind-diagram.html name="python-points" alt="A win adds three points, a draw adds one point, and a loss adds zero points." caption="One line of code. Three possible outcomes. The += instruction adds the points earned to the club's existing total." %}

Once we've processed every match, we arrange each club's results chronologically and calculate its cumulative points.

The finished information is saved as a JSON file.

Unlike a flat table, JSON allows us to organise information into groups. In our example, each club contains its own collection of matches and season totals.

JavaScript can then read that information and bring the interactive visualisation to life.

{% include behind-python-transform.html %}

## What didn't work

Computers are wonderfully obedient, which is also one of their greatest weaknesses.

If we give Python the wrong instructions, it can calculate the wrong answer remarkably efficiently.

What happens if a fixture appears twice? Or a score is missing? Or the stated result contradicts the number of goals scored?

These are precisely the sorts of things our validation rules are designed to catch.

For the ongoing Premier League season, our process also checks that previously published results haven't unexpectedly disappeared or changed.

If the data fails those checks, we want the process to stop rather than quietly publish unreliable information.

{% include behind-python-validation.html %}

## What we learnt

One of the greatest advantages of using Python isn't simply that it saves time.

It's that the instructions remain available.

We can revisit the code, examine the calculations, change a rule or repeat the process using the same dataset.

ChatGPT helps us write and review those instructions. GitHub gives us somewhere permanent to keep and execute them.

But understanding what we're asking the computer to do remains our responsibility.

{% include behind-python-workflow.html %}

## Try it yourself

Work through the examples above and follow a football result from its original row of data to the information used by our interactive visualisation.

Then deliberately introduce a mistake and see why validation matters.

You don't need to know how to write Python to understand the process.

Explore the [original CSV](https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-11-epl-2526-unfolded/data/matches_2526.csv), [Python instructions](https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-11-epl-2526-unfolded/scripts/build_data.py) and [finished JSON file](https://github.com/adamgreen1708/chart-templates/blob/main/site/assets/data/epl-2526-unfolded.json). See how these feed into [Premier League Unfolded](/about/behind-the-build/how-we-made-it/premier-league-unfolded/), [Interwoven](/about/behind-the-build/how-we-made-it/interwoven/) and [Building a chart factory](/about/behind-the-build/how-we-work/building-a-chart-factory/).

## TL;DR

Python isn't magic.

It's a collection of instructions that tell a computer how to read, transform, calculate and check information.

The quality of the result depends on the quality of those instructions.
