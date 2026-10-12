---
title: "The map that put a pump on trial"
date: 2026-10-12 20:01:00 +0100
slug: the-map-that-put-a-pump-on-trial
permalink: /icons-of-data/john-snow-cholera-map/
description: "John Snow's 1855 map made a striking pattern of cholera deaths visible. Why the Broad Street pump mattered — and why the map alone could not settle the case."
category: Icons of Data
read_time: 3 minute read
card_image: /assets/icons-of-data/john-snow/02_the_pattern_mapped.png
social_image: /assets/icons-of-data/john-snow/02_the_pattern_mapped.png
---

<div class="eyebrow"><a href="{{ '/resources/icons-of-data/' | relative_url }}">Icons of Data · Edition 06</a></div>

The most suspicious object in a London neighbourhood in 1854 wasn't a person.

It was a water pump.

And John Snow had a rather compelling map to go with his suspicions.

## One death. One black mark.

In late August and September 1854, cholera spread through Soho, leaving many families devastated.

Snow was already investigating the idea that cholera could travel through contaminated drinking water. When people became ill around Broad Street, he examined their addresses, asked where they obtained water and looked for explanations that fitted the evidence.

His map, published in **1855**, placed the fatal attacks he could trace on a street plan. Short black bars stood at affected houses. Several bars at an address meant several deaths.

He also marked the neighbourhood's public water pumps.

And the concentration of black marks around the Broad Street pump was difficult to ignore.

<figure class="story-chart full-bleed">
  <a href="https://commons.wikimedia.org/wiki/File:Map_showing_deaths_from_Cholera_in_Broad_Street..._Wellcome_L0063431.jpg" aria-label="View John Snow's original 1855 Broad Street map and image credit">
    <img src="{{ '/assets/icons-of-data/john-snow/01_snow_original_wellcome_L0063431_review.jpg' | relative_url }}"
         alt="John Snow's authentic 1855 printed map of Soho around Broad Street, showing individual black fatal-attack bars grouped at buildings and several public water pumps. Dense clusters of black bars appear around Broad Street and Golden Square."
         width="1600" height="1534" loading="lazy" decoding="async">
  </a>
  <figcaption>John Snow, <em>Map showing deaths from Cholera in Broad Street, Golden Square and the neighbourhood</em> (from the second edition of <em>On the Mode of Communication of Cholera</em>, <strong>1855</strong>; the mapped outbreak occurred in <strong>1854</strong>). Digital reproduction: <a href="https://commons.wikimedia.org/wiki/File:Map_showing_deaths_from_Cholera_in_Broad_Street..._Wellcome_L0063431.jpg">Wellcome Collection, L0063431</a>, <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. The digital scan has been proportionally resized for the website, without cropping or recolouring. This is Snow's book map, not the separate St James parish inquiry plate.</figcaption>
</figure>

## Location is doing the talking

On a table, an address is just another row.

On a map, it has neighbours.

The short bars show **where** fatal attacks were recorded. The pumps introduce a possible explanation for the pattern. The streets matter because the nearest pump in a straight line wasn't necessarily the easiest to reach on foot.

<figure class="story-chart full-bleed">
  <a href="{{ '/assets/icons-of-data/john-snow/02_the_pattern_mapped.png' | relative_url }}">
    <img src="{{ '/assets/icons-of-data/john-snow/02_the_pattern_mapped.png' | relative_url }}"
         alt="Modern square reconstruction of Snow's cholera map, showing 578 dark plotted fatal-attack marks distributed along Soho streets, 12 other pump positions indicated in teal and the Broad Street pump singled out by a red diamond. The mapped fatal attacks concentrate near the highlighted pump."
         width="1920" height="1920" loading="lazy" decoding="async">
  </a>
  <figcaption><strong>The pattern, mapped:</strong> a reconstruction from published <code>HistData</code> digitisation: <strong>578 mapped fatal-attack marks, 13 water pump locations and 528 street polylines</strong>. These are source map-drawing coordinates, <strong>not GPS locations</strong>. Squares replace Snow's original bars and modern colours highlight pump positions; the Broad Street pump is a <strong>red annotation added by us</strong>. The 578 rows are <em>not</em> an estimate of the outbreak's complete death toll, nor are they mortality rates.</figcaption>
</figure>

It's a beautifully economical encoding. A reader can see the neighbourhood pattern almost immediately, where a list of addresses might take far longer to explain.

But a convincing cluster is not the same as an answer.

## What isn't on the map?

The black marks don't tell us how many people lived at each address. They don't show everyone who became ill, where water was actually consumed or when each exposure happened.

The map is a *distribution of recorded fatal attacks*, not a map of infection risk.

There's also a detail that tends to get misplaced in retellings.

Snow persuaded officials to remove the Broad Street pump handle on **8 September 1854**. The outbreak was **already declining**. The map didn't magically solve the epidemic with one decisive flourish.

<figure class="story-chart full-bleed">
  <a href="{{ '/assets/icons-of-data/john-snow/03_decode_the_icon.png' | relative_url }}">
    <img src="{{ '/assets/icons-of-data/john-snow/03_decode_the_icon.png' | relative_url }}"
         alt="Four-part Decode the Icon diagram: multiple short bars denote multiple fatal attacks at an address; plotted pumps provide spatial context but not confirmed water use; deaths without a population denominator cannot yield a mortality rate; and the map has no individual dates, while the Broad Street pump handle was removed on 8 September 1854 after the outbreak had begun declining."
         width="1920" height="1920" loading="lazy" decoding="async">
  </a>
  <figcaption><strong>Decode the Icon:</strong> stacked marks, pump geography, the difference between <strong>counts and rates</strong>, and what a single map cannot show about timing. The little diagrams and example figures are <strong>schematic illustrations</strong>, not additional observations from the 1854 outbreak.</figcaption>
</figure>

## TLDR

Snow made a geographical pattern easier to see.

He also did the less photogenic work: questions, comparisons and checking unusual cases.

The map helped make his argument.

It wasn't the whole argument.

<aside class="method-note">
  <h2>Source and method</h2>
  <p>Historical work: John Snow, <a href="https://wellcomecollection.org/works/uqa27qrt"><em>On the Mode of Communication of Cholera</em>, second edition (1855)</a>. The specific book-map photograph is <a href="https://commons.wikimedia.org/wiki/File:Map_showing_deaths_from_Cholera_in_Broad_Street..._Wellcome_L0063431.jpg">Wellcome L0063431</a>, reproduced under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a> with the disclosed resize. The outbreak was in 1854; the edition and image were published in 1855. Related 1855 parish inquiry maps are separate artefacts.</p>
  <p>Our spatial reconstruction draws the <a href="https://rdrr.io/rforge/HistData/man/Snow.html"><code>HistData</code> Snow datasets</a>: 578 digitised mark positions, 13 pump positions and 1,241 street vertices forming 528 separate polylines. The verified source CSVs and <a href="https://github.com/adamgreen1708/chart-templates/tree/main/archive/projects/2026-10-icons-of-data/editions/06-john-snow/data">validation summary</a> are archived with the project. Coordinates are local map drawing coordinates, not measured household GPS. The <code>case</code> identifiers are not dates.</p>
  <p>Neither chart gives the population at risk at each location, records every cholera infection, proves specific water exposure or distinguishes causal mechanisms by itself. The <a href="https://epi-snow.ph.ucla.edu/Stream2_BSPoutbreak_e.html">historical account of the pump-handle removal</a> shows that cases were already declining before 8 September 1854. That does not prove the intervention had no possible effect; it means the map and the popular story cannot alone establish how much it changed the outcome.</p>
</aside>

<p><a href="{{ '/resources/icons-of-data/' | relative_url }}">Explore more Icons of Data →</a></p>

<p class="sign-off"><strong>simple charts clear stories.</strong></p>
