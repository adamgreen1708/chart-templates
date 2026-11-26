---
layout: behind-the-build
title: "Drawing with code — When numbers become pictures"
description: "How a collection of instructions becomes something we can see."
permalink: /about/behind-the-build/how-we-work/drawing-with-code/
collection_label: How we work
article_number: "07"
last_reviewed: 2026-11-26
social_image: /assets/behind-the-build/drawing-methods.svg
---

## The idea

As someone who has spent years creating visualisations in Tableau, I've become accustomed to dragging information onto a canvas and watching a picture emerge.

But beneath that seemingly simple experience, a computer is making decisions about position, size, shape and colour.

At Coffeetableviz, we've been exploring how to give the computer those instructions ourselves.

## The challenge

Not everything we create requires the same approach to drawing.

A chart accompanying a blog article needs to be accurate, consistent and reproducible.

An interactive visualisation needs to respond to the reader.

A creative studio might need to redraw an entire artwork as someone adjusts a slider.

We've therefore found ourselves using several different drawing technologies.

## How it works

Imagine asking a computer to draw a circle.

We need to tell it where the centre should be, how large the circle should be and what colour to use.

Those simple instructions can be repeated, combined and driven by information from a dataset.

A number becomes a position. Another becomes a size. A category becomes a colour.

Put enough of these instructions together and we have a visualisation.

{% include behind-diagram.html name="drawing-methods" alt="Three identical-looking circles: SVG describes vector geometry, Canvas paints a pixel surface, and our Python workflow saves an image as PNG." caption="Three ways to draw a circle. Conceptual illustration; Python can also produce vector graphics." %}

## Under the bonnet

We use three particularly interesting approaches.

**SVG — describing shapes.**

SVG stands for Scalable Vector Graphics. Rather than storing every individual pixel, it describes geometric objects.

Our Premier League visualisation uses SVG to draw its interactive points comparison. Each club's marker has a calculated position, appearance and associated information.

This instruction creates an SVG element:

<div class="btb-py-code"><p>ACTUAL PREMIER LEAGUE JAVASCRIPT</p><pre><code>const e = document.createElementNS(svgNS, tag);</code></pre></div>

The surrounding instructions assign its position, dimensions, colour and other attributes. A simplified SVG circle looks like this:

<div class="btb-py-code"><p>ILLUSTRATIVE SVG</p><pre><code>&lt;circle cx="80" cy="80" r="35"
        fill="#1F8FA8" /&gt;</code></pre></div>

The browser interprets that description and draws the circle.

**Canvas — painting onto a surface.**

Canvas gives JavaScript a digital drawing surface.

In Truchet Tile Studio, we calculate the position and orientation of each triangle, then instruct the browser to draw it.

<div class="btb-py-code"><p>ACTUAL TRUCHET DRAWING INSTRUCTIONS</p><pre><code>ctx.moveTo(px,py);
ctx.lineTo(px+s,py);
ctx.lineTo(px,py+s);</code></pre></div>

Move to the starting point, draw to the second point, then draw to the third point. The surrounding code closes and fills the shape.

{% include behind-drawing-triangle.html %}

Change the pattern and the browser redraws the artwork.

**Python — generating finished images.**

Our chart renderer uses a Python library called Matplotlib to create our statistical charts from actual datasets and configuration files.

<div class="btb-py-code"><p>ACTUAL MATPLOTLIB INSTRUCTION</p><pre><code>fig, ax = plt.subplots(figsize=figsize)</code></pre></div>

This creates the figure and the area where we'll draw our data. Further instructions determine which chart type to use, what data to plot and how to apply our house style. Finally, `plt.savefig()` saves the finished image.

{% include behind-diagram.html name="drawing-render" alt="Actual data and CHART_CONFIG feed the Python Matplotlib renderer executed in GitHub, producing a PNG for visual quality assurance." caption="From numbers to a finished chart." %}

<figure class="btb-figure"><img src="{{ '/assets/charts/patrick-stewart/patrick_stewart_1.png' | relative_url }}" loading="lazy" alt="Patrick Stewart films ranked by IMDb votes, with Xavier roles blue, Picard red and other work grey."><figcaption>Existing GitHub-rendered chart, reproduced unchanged from the Patrick Stewart project. <a href="https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-10-patrick-stewart/config/chart_1.py">View its configuration.</a></figcaption></figure>

Interwoven uses another Python library, Pillow, to produce its much more elaborate panoramic artwork.

Both approaches allow us to generate finished images using repeatable instructions.

## What didn't work

One of the lessons from creating our interactive studios is that an artwork can look perfectly acceptable on screen, yet become less satisfactory when exported or enlarged.

A small drawing surface is useful for experimentation, but it doesn't necessarily produce a particularly good print.

Our creative studios therefore include separate export instructions, creating artwork at a defined resolution rather than simply taking a screenshot of the browser.

{% include behind-drawing-raster.html %}

We've also had to think carefully about how shapes represent numbers.

If we double the radius of a circle, its area becomes four times larger.

That matters when the circle is supposed to communicate a quantity.

{% include behind-drawing-area.html %}

This is why our Bauhaus Art Studio uses area-based sizing for its geometric shapes.

## What we learnt

The interesting part isn't simply learning how to draw a circle or a triangle.

It's deciding what that shape should represent.

The technology gives us the ability to draw almost anything. Our responsibility is to make sure the resulting picture communicates what we intend.

And for our statistical charts, those instructions must remain connected to the actual data.

{% include behind-drawing-tools.html %}

## Try it yourself

Experiment with the examples above.

Compare a vector shape with a pixel-based image. Explore the relationship between a circle's radius and its area.

Then revisit one of our creative studios and consider how its artwork is constructed from relatively simple drawing instructions.

For the curious: [Matplotlib renderer](https://github.com/adamgreen1708/chart-templates/blob/main/src/render_538.py), [Truchet drawing instructions](https://github.com/adamgreen1708/chart-templates/blob/main/site/assets/js/truchet-tile-studio.js), [Premier League SVG implementation](https://github.com/adamgreen1708/chart-templates/blob/main/site/assets/js/epl-2627-unfolded.js), [Interwoven Python renderer](https://github.com/adamgreen1708/chart-templates/blob/main/archive/projects/2026-11-interwoven/render_interwoven.py) and [Bauhaus Art Studio](/about/behind-the-build/how-we-made-it/bauhaus-art-studio/).

## TL;DR

A picture can be a collection of instructions.

Combine those instructions with data, geometry and a little creativity, and we can create everything from a simple dot plot to an entire virtual gallery.

<script defer src="{{ '/assets/behind-the-build/drawing-demo.js' | relative_url }}?v=1"></script>
