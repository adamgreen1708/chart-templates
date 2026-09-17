---
title: "Truchet Tiles: Small Shapes, Long Shadows"
date: 2026-02-04 20:48:55 +0000
slug: truchet-tiles-small-shapes-long-shadows
permalink: /2026/02/04/truchet-tiles-small-shapes-long-shadows/
description: One tile, a few rotations and a reminder that very simple rules can produce endless visual complexity.
category: Design
read_time: 5 minute read
card_image: /assets/migrated/truchet-tiles/feature.png
hero_image: /assets/migrated/truchet-tiles/feature.png
hero_alt: "A monochrome grid of square Truchet tiles whose rotated black and pale triangles form a complex geometric pattern."
legacy_url: https://coffeetableviz.wordpress.com/2026/02/04/truchet-tiles-small-shapes-long-shadows/
---

Some ideas shout. Others whisper, and for as long as I can remember **Truchet tiles** have whispered sweet nothings to me, seducing me with order, chaos and complexity.

Sometimes the simplest visual ingredients have the most enduring charm. Truchet tiles can be simple or complex, but they are always mesmerising.

So I set about creating the first version of my [Truchet Tile generator in Tableau](https://public.tableau.com/views/Truchettiles/TRUCHET?) along with this accompanying post.

## A short history (ish)

In 1704, Sébastien Truchet published *Mémoire sur les combinaisons*, exploring how decorative patterns could be constructed from variations of a simple geometric tile.

The original Truchet tile is absurdly simple: a square divided diagonally into two triangles, one black and one white.

- **The magic:** rotate the square and four different orientations appear.
- **The chaos:** assemble those squares into a grid and the triangles create continuous lines, labyrinths and unexpected patterns.

What matters is not only the tile itself, but how it relates to its neighbours. Three centuries later, the idea still feels mesmerising — to me, anyway.

## More than pretty pictures

Because they are algorithmic, Truchet tiles have become a favourite device in generative art and data visualisation. Within the Tableau community, Neil Richards has written an excellent [introduction to how they work](https://questionsindataviz.com/2021/03/03/what-are-truchet-tiles/).

The underlying idea also appears in unexpected places. Researchers have described a metal-organic framework, TRUMOF-1, whose structure resembles a three-dimensional Truchet tiling.

Below are four screenshots from my Tableau generator, ranging from quiet order to complex and slightly off-symmetrical mess.

<div class="image-grid" aria-label="Four Truchet tile patterns">
  <figure><img src="{{ '/assets/migrated/truchet-tiles/pattern-1.png' | relative_url }}" alt="Monochrome Truchet tile pattern forming a large pale rounded-square shape within a dark field." loading="lazy"></figure>
  <figure><img src="{{ '/assets/migrated/truchet-tiles/pattern-2.png' | relative_url }}" alt="Dense monochrome Truchet tile pattern made from irregularly rotated black and pale triangles." loading="lazy"></figure>
  <figure><img src="{{ '/assets/migrated/truchet-tiles/pattern-3.png' | relative_url }}" alt="Monochrome Truchet tile pattern with diagonal fragments creating interlocking paths and patches." loading="lazy"></figure>
  <figure><img src="{{ '/assets/migrated/truchet-tiles/pattern-4.png' | relative_url }}" alt="Monochrome Truchet tile pattern combining diagonal paths, blocks and chevrons in an irregular grid." loading="lazy"></figure>
</div>

## How it works (ish)

I will not pretend I crafted this in Tableau alone. I leaned on ChatGPT to build the framework, spreadsheet scaffold and calculations. It got things wrong; we iterated; eventually we reached a working first version.

Broadly speaking, the method is:

1. Give every tile a binary choice: which way should the diagonal run?

```text
OrientationFlag = ([X] + [Y]) % 2
```

2. Change the rule and the whole pattern shifts.
3. Repeat the rule, not the outcome. Each tile applies the same local logic at a different position, allowing a global structure to emerge.
4. Use distance from the centre to create radial symmetry.

```text
RadiusBand = INT(
  SQRT( ([X]-CenterX)^2 + ([Y]-CenterY)^2 )
)
```

5. Let colour follow the same system rather than treating it as decoration.

```text
TileColour =
IF ABS(HASH(STR([RadiusBand]))) % 2 = 0
THEN "Black" ELSE "White" END
```

## Why they are still charming

You can understand the entire system in seconds, yet stare at the results for minutes. Paths appear. Loops form. Shapes seem to rotate even when nothing is moving.

They reward attention without demanding it. In an age of increasing complexity, Truchet tiles remind me that constraint can be creative, repetition can be expressive, and complexity does not require complexity as an input.

## TLDR

- Truchet’s published exploration dates to the early 18th century.
- The patterns rely on rotation, repetition and constraint.
- Complex results emerge from very simple local rules.
- Their charm lies in what they do not try to do.

**One tile. A few rotations. Endless quiet fascination.**

Hope you enjoy.

Adam
