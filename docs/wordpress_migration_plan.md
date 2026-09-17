# WordPress selected-post migration

This document tracks the curated launch archive being moved from
`coffeetableviz.wordpress.com` to `coffeetableviz.com`.

## Migration rules

- Preserve the original publication date, title and date-based path.
- Keep a `legacy_url` in front matter for provenance.
- Store required images in the repository rather than depending on WordPress media URLs.
- Re-encode migrated images to remove embedded metadata.
- Add useful alt text rather than carrying over empty WordPress alt attributes.
- Keep Tableau Public links where the interactive version adds value.
- Do not migrate WordPress comments into the static site.
- Give older posts a light editorial and factual QA pass before publication.

## Pilot

| Original date | Post | Format | Status |
|---|---|---|---|
| 2026-09-12 | 007 Villains of Age | Chart template | Migrated in pilot |
| 2026-09-08 | IMDb Brad Pitt film ratings, popcorn & a boys night in | Chart template | Migrated in pilot |
| 2026-06-11 | World Cup finals: a tiny winners’ club, a growing taste for drama | Chart template | Migrated in pilot |
| 2026-02-04 | Truchet Tiles: Small Shapes, Long Shadows | Legacy / Tableau | Migrated in pilot |
| 2024-12-31 | Running in Shapes: A Bauhaus-Inspired Journey Through Data | Legacy / Tableau | Migrated in pilot |

## Remaining chart-template posts

| Original date | Post | Status |
|---|---|---|
| 2026-06-10 | The story to glory, A 22 year wait | Queued |
| 2026-06-07 | The World’s Highest Paid Athletes | Queued |
| 2026-05-21 | The wee dram, a small sip with lingering notes | Queued |
| 2026-05-03 | Forbes’ most valuable sports teams | Queued |
| 2026-05-02 | More Articles Are Now Created by AI Than Humans | Queued |
| 2026-04-30 | The UK’s hottest years are also shining through | Queued |
| 2026-04-29 | The UK’s rapeseed rollercoaster | Queued |
| 2026-04-26 | How is war shaping fuel prices | Queued |

## Remaining legacy and evergreen posts

| Original date | Post | Status |
|---|---|---|
| 2026-01-13 | Tables & Visualisations — A delicate dance in the grand data opera | Queued |
| 2025-07-24 | ZERO: The Rarest Number in Football | Queued |
| 2025-07-16 | Sinner vs Alcaraz, Wimbledon 2025: A triangle tale | Queued |
| 2025-07-07 | Who Rules the Road | Queued; review dated predictions |
| 2025-01-17 | Shades of Heroism | Queued; editorial accuracy review required |
| 2024-11-13 | Creating for fun | Queued; large image gallery |
| 2024-10-10 | How to Find stories in Data: channelling our inner journo | Queued |
| 2024-07-19 | Colour Bank No.6 — Tom Hanks Filmography | Queued |

## Cutover approach

The WordPress site remains online as a read-only legacy archive. Selected posts are
published at their matching date-based path on `coffeetableviz.com`; future posts are
created directly in this repository.
