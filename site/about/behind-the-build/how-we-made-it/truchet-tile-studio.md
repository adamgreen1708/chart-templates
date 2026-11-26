---
layout: behind-the-build
title: "Truchet Tile Studio — Order from chaos"
description: "How one simple geometric shape becomes an almost endless creative playground."
permalink: /about/behind-the-build/how-we-made-it/truchet-tile-studio/
collection_label: How we made it
article_number: "02"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/truchet-rotations.svg
---

## The idea

I've always enjoyed the relationship between data, mathematics and design.

Sometimes the most interesting visualisations aren't those that communicate a particular number, but those that reveal what happens when we apply a simple rule repeatedly.

Truchet tiles are a rather lovely example of this.

Take a square, divide it diagonally into two colours and rotate it. That's essentially our entire building block.

What happens next is considerably more interesting.

## The challenge

Having previously explored Truchet tiles in Tableau, I wanted to create something more interactive on Coffeetableviz.

Rather than simply displaying geometric patterns, could we give people the tools to create their own?

And could we explore what happens somewhere between perfect symmetry and complete disorder?

## How it works

Every tile has four possible orientations.

We give each orientation a value from zero to three. By arranging those values across a grid, we can create a surprisingly diverse collection of patterns.

{% include behind-diagram.html name="truchet-rotations" alt="Four diagonal tiles rotated by zero, ninety, one hundred and eighty, and two hundred and seventy degrees, followed by a mirrored eight by eight pattern." caption="One tile. Four rotations. Repeat, reflect, rotate." %}

The interesting bit is deciding which value each square should contain.

We can use rules based on alternating positions, distance from the centre or mathematical waves. Each produces a different visual character, despite using exactly the same geometric shape.

The tiles haven't changed. The instructions have.

## Under the bonnet

The studio uses JavaScript to calculate the rotation of each tile and a browser technology called Canvas to draw the resulting pattern.

*Explore the drawing techniques in [Drawing with code — When numbers become pictures](/about/behind-the-build/how-we-work/drawing-with-code/).*

*Want to understand how? Read [JavaScript — Bringing things to life](/about/behind-the-build/how-we-work/javascript/).*

To create symmetry, we generate the underlying pattern for one quarter of the artwork and reflect it across the other three.

The chaos slider then progressively introduces independently selected rotations, disrupting that symmetry.

Those rotations are generated using a repeatable mathematical process. Moving the slider back to an earlier position can therefore restore the same arrangement, provided the other settings and edits haven't changed.

This is important. We wanted people to explore the transition between structure and disorder, rather than simply generate a completely different image every time they moved a slider.

{% include behind-truchet-demo.html %}

## What didn't work

One of the design challenges was balancing creative freedom with the rules that make the artwork interesting.

If every tile behaves independently, it's easy to lose the symmetry. If everything remains perfectly linked, it's harder to introduce individual variations.

Our solution was to give the user both options.

Rotate a single tile, or link it to its three mirrored partners and watch a small change echo across the artwork.

## What we learnt

Complexity doesn't necessarily require a complicated starting point.

Sometimes a simple shape, a handful of instructions and a little repetition are all that's needed.

It's a principle that extends well beyond geometric artwork. The rules we apply to data can be just as interesting as the data itself.

{% include behind-diagram.html name="truchet-pixel-comparison" alt="The actual Pixel Art Studio frog uses values for colours, while a mirrored Truchet pattern uses values for tile rotations." caption="Same principle. Different instructions. Both are creative interpretations of data." %}

## Try it yourself

Visit [Truchet Tile Studio](/resources/truchet-tile-studio/). Start with a symmetrical pattern, gradually introduce chaos and see where you find the most interesting balance.

There's no correct answer. That's rather the point.

Explore the [original Tableau visualisation](https://public.tableau.com/app/profile/adam.green4310/viz/Truchettiles/TRUCHET), the [JavaScript implementation](https://github.com/adamgreen1708/chart-templates/blob/main/site/assets/js/truchet-tile-studio.js) or our companion article, [Pixel Art Studio — 256 little squares](/about/behind-the-build/how-we-made-it/pixel-art-studio/).

## TL;DR

One square. Four rotations. A handful of mathematical rules.

Combine them and you have a creative playground somewhere between mathematics, data and art.
