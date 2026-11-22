---
layout: post
title: "The Premier League unfolded — one match at a time"
slug: premier-league-season-unfolded-2025-26
date: 2026-11-22 00:00:00 +0000
author: Adam Green
category: Sport
description: "Twenty clubs, 380 matches and ten months of wins, draws and losses. A new interactive take on my original Premier League Tableau visual."
read_time: "3 minute read"
card_image: /assets/features/epl-2526-season-unfolded-editorial.svg
hero_image: /assets/features/epl-2526-season-unfolded-editorial.svg
social_image: /assets/features/epl-2526-season-unfolded-editorial.svg
hero_alt: "Editorial illustration of a charcoal results board, with large red W, light-grey D and dark-grey L circles, representing win, draw and loss. Not actual match data."
tags: [premier-league, football, sport, interactive, tableau, data-visualisation]
published: true
---

Thirty-eight games per club. Ten months. Hundreds of little decisions, missed chances, late goals and the odd inexplicable result.

Then, at the end of it all, we compress the lot into one league table.

Useful, certainly. But it makes twenty very different journeys look rather tidy.

Back in **2020–21**, I made a [Tableau visualisation](https://public.tableau.com/app/profile/adam.green4310/viz/EPL202021SeasonUnfolded/202021EPLSeason) that arranged the Premier League results month by month, with home games above the dates and away games below.

I rather liked that way of looking at football. So I've brought it up to date for **2025–26** — and turned it into an interactive Coffeetableviz page.

## The result is just one dot

Each circle is a real match. A club-coloured **W** for a win, light grey **D** for a draw, darker grey **L** for a defeat.

Home results stack upwards from the month. Away results stack downwards. In each case, the earliest fixture sits nearest the month label.

Choose a club. Tap a dot. See the opponent, score and date. There's also a little cumulative-points chart tucked into the translucent tooltip, with the other nineteen clubs kept quietly in the background.

**[Explore the interactive Premier League season →]({{ '/resources/epl-2025-26-unfolded/' | relative_url }})**

## Same league. Rather different home comforts.

Arsenal finished champions on **85 points**, seven clear of Manchester City. That much the final table tells us.

But the home and away split reveals some more interesting quirks.

Take **Tottenham**. They finished seventeenth with 41 points, yet **26 of them came away from home**, compared with just **15 at home**. A rather unusual way to scrape through the season.

**Fulham** went the other way: **35 points at home**, but only **17 away** — the largest home-over-away points difference of any club in the dataset.

And **Chelsea**? Absolutely even. **26 home points and 26 away**, down to matching records of seven wins, five draws and seven defeats in each.

The final positions don't reveal those differences. The rows of dots make you curious enough to look.

## Have a little play

The bottom of the interactive puts all twenty clubs on one shared final-points scale. Select another club and the ten-month calendar redraws.

Then try a result tooltip. The small line chart plots cumulative points for every team after **its own** first, second, third and eventually thirty-eighth league match. The coloured line follows your selected club; the rest provide context.

It's not claiming the teams played those matches on the same dates. Rearranged fixtures make that distinction worth keeping.

What began as a Tableau experiment has become a touch-friendly browser visualisation, with the data, design and code kept together on GitHub.

A few more ways to explore what happened between August and May. And, hopefully, an excuse to spend another five minutes looking at football.

**[Open the 2025–26 Season Unfolded interactive]({{ '/resources/epl-2025-26-unfolded/' | relative_url }})**

## TL;DR

The Premier League doesn't unfold in neat table rows. This interactive shows all **380 matches** as home and away results by calendar month, with every score, opponent and club's points journey a tap away. Tottenham, Fulham and Chelsea offer three rather different examples of why the home/away split matters.

*Simple charts. Clear stories.*

---

### A note on the numbers

All **380 full-time matches** in the 2025–26 Premier League are included, with **38 per club** (19 home and 19 away). The season dataset comes from [Football-Data.co.uk](https://www.football-data.co.uk/mmz4281/2526/E0.csv), via a [pinned historical source snapshot](https://github.com/qhtexas/football-dataset/blob/9ec38fd9149216e3110d8b6edb1c0e8457d3016b/datasets/premier-league/season-2526.csv). The results and calculated points were checked against the [Premier League's final standings](https://www.premierleague.com/en/tables/premier-league/2025-26).

The monthly calendar uses actual fixture **calendar months**, not assumed official matchweeks. The miniature line chart's horizontal axis shows each club's **own nth match completed**, not simultaneous fixtures on the same date. All home/away points and the differences in the article are derived from the saved match-level data. The cover illustration is symbolic, not a statistical chart.

This is a new browser interpretation inspired by [my original 2020–21 Tableau version](https://public.tableau.com/app/profile/adam.green4310/viz/EPL202021SeasonUnfolded/202021EPLSeason), not a direct conversion of the workbook.
