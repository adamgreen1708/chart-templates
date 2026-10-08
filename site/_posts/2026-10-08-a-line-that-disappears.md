---
title: "A line that disappears"
date: 2026-10-08 20:00:00 +0100
slug: a-line-that-disappears
permalink: /icons-of-data/minard/
description: "In 1869 Charles Joseph Minard turned Napoleon's disastrous Russian campaign into a line that shrank. The clever bit? Width became information."
category: Icons of Data
read_time: 3 minute read
---

<p class="eyebrow"><a href="{{ '/resources/icons-of-data/' | relative_url }}">Icons of Data · Edition 01</a></p>

Napoleon's invasion of Russia in 1812 didn't exactly go to plan.

An enormous army marched east towards Moscow. A considerably smaller one made it back.

Historians have spent rather a lot of time explaining what went wrong. Battles, disease, hunger, exhaustion and, of course, the Russian winter.

In 1869, French engineer Charles Joseph Minard decided to tell the story rather differently.

He drew a map.

And made the line shrink.

## Not your usual route map

At first glance, Minard's famous illustration looks like a map of Napoleon's journey across Russia.

The pale band follows the army towards Moscow. The dark one traces the retreat.

But look a little closer.

**The width of each band represents the estimated number of men in the army.**

As the numbers fall, the line narrows. By the time it heads back west, there's precious little width left.

You don't need to know much about military history to appreciate that things have gone rather badly.

<figure class="story-chart full-bleed">
  <a href="https://commons.wikimedia.org/wiki/File:Minard.png">
    <img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Minard.png"
         alt="Charles Joseph Minard's original 1869 French diagram of Napoleon's Russian campaign. A wide pale band travels east to Moscow, a thinner dark band returns west, and a temperature trace sits beneath the routes."
         width="2003" height="955" loading="lazy">
  </a>
  <figcaption>Minard's original, 1869. Public domain, via <a href="https://commons.wikimedia.org/wiki/File:Minard.png">Wikimedia Commons</a>. Open the image to inspect its original French labels.</figcaption>
</figure>

## One line. Several jobs.

What makes this remarkable isn't simply the shrinking line.

Minard manages to combine geography, troop numbers, direction, place names and dates. Beneath the map, he even plots temperatures recorded during the retreat.

And those temperatures make for fairly uncomfortable reading.

{% assign image_two = site.static_files | where: "path", "/assets/icons-of-data/minard/02_shrinking_army.png" | first %}
{% if image_two %}
<figure class="story-chart full-bleed">
  <img src="{{ '/assets/icons-of-data/minard/02_shrinking_army.png' | relative_url }}"
       alt="Coffeetableviz reconstruction of Minard's three group routes. Pale bands mark the advance; black bands mark the retreat, with line width proportional to estimated troop counts. Beneath is a red temperature trace in degrees Réaumur."
       width="1920" height="1920" loading="lazy">
  <figcaption>Our reconstruction from the digitised source tables. The lines encode estimated troop strength, not a precise death toll; temperature stays in the original Réaumur units.</figcaption>
</figure>
{% else %}
<p><em>Visual 2 — One journey. A shrinking army. Approved chart awaiting its original PNG asset in GitHub before publication.</em></p>
{% endif %}

The clever part is how naturally the different pieces fit together.

The route tells us **where** the army travelled. The width tells us **how many** men remained in Minard's estimates. The temperature chart adds another layer of context to an already disastrous journey.

Each element tells us something different, but together they tell one story.

All on a single sheet of paper.

In 1869.

{% assign image_three = site.static_files | where: "path", "/assets/icons-of-data/minard/03_decode_the_icon.png" | first %}
{% if image_three %}
<figure class="story-chart full-bleed">
  <img src="{{ '/assets/icons-of-data/minard/03_decode_the_icon.png' | relative_url }}"
       alt="Decode the Icon: four panels isolate position, changing width, colour for advance and retreat, and temperature annotations. Each encoding does a different job."
       width="1920" height="1920" loading="lazy">
  <figcaption>Decode the Icon: geography locates the journey, width carries troop numbers, colour separates directions and the temperature graph provides context.</figcaption>
</figure>
{% else %}
<p><em>Visual 3 — Decode the Icon. Approved chart awaiting its original PNG asset in GitHub before publication.</em></p>
{% endif %}

## But there's always a catch

As compelling as the illustration is, it isn't a perfect historical record.

Minard worked with estimates and made deliberate simplifications about the movement of different army units.

The shrinking line doesn't mean everyone who disappeared from the count died. Nor does the temperature chart prove that the cold caused every loss.

Those distinctions matter.

A brilliant visualisation can tell a powerful story without telling us absolutely everything.

## TLDR

Most lines on maps tell us where something goes.

Minard made the width of his line tell us how much remained.

He combined several different ways of encoding information into one extraordinary illustration.

More than 150 years later, it's still a rather good lesson in visual storytelling.

Sometimes the cleverest thing you can do with a line is make it thinner.

<aside class="method-note">
  <h2>Source and method</h2>
  <p>Charles Joseph Minard, <em>Carte figurative des pertes successives en hommes de l'Armée Française dans la campagne de Russie 1812–1813</em> (1869). The troop counts are historical estimates, and temperatures on the original are expressed in degrees Réaumur. Our reconstructions use the digitised <a href="https://friendly.github.io/HistData/reference/Minard.html">HistData Minard tables</a> (51 troop-route records in three groups, 20 places, nine temperature observations). One temperature date is missing and has not been invented. See the <a href="https://commons.wikimedia.org/wiki/File:Minard.png">public-domain original and original legend</a>. The HistData help text contains an erroneous reference to 1815; the campaign here was 1812–1813.</p>
</aside>

<p><a href="{{ '/resources/icons-of-data/' | relative_url }}">Explore more Icons of Data →</a></p>

<p class="sign-off"><strong>simple charts clear stories.</strong></p>
