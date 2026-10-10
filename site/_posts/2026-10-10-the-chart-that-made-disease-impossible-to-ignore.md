---
title: "The chart that made disease impossible to ignore"
date: 2026-10-10 18:00:00 +0100
slug: the-chart-that-made-disease-impossible-to-ignore
permalink: /icons-of-data/nightingale-mortality/
description: "Florence Nightingale made a case for healthier military hospitals with a striking 1858 mortality diagram. What its blue areas revealed — and what they could not prove."
category: Icons of Data
read_time: 3 minute read
card_image: /assets/icons-of-data/nightingale/02_what_the_numbers_reveal.png
social_image: /assets/icons-of-data/nightingale/02_what_the_numbers_reveal.png
---

<div class="eyebrow"><a href="{{ '/resources/icons-of-data/' | relative_url }}">Icons of Data · Edition 04</a></div>

A war has a fairly obvious suspect when soldiers die.

You'd probably guess battle wounds.

Florence Nightingale had some figures that made that answer rather awkward.

In 1858, she published a diagram showing what had killed British soldiers during the Crimean War. It wasn't designed simply to look pretty.

It was designed to make a point.

## The biggest problem was blue

Her diagram divided deaths into three categories.

Blue represented what she called *preventable or mitigable zymotic diseases* — a decidedly Victorian way of grouping illnesses such as cholera, dysentery and fever. Red meant wounds. Black covered other causes.

And blue dominated.

In a later transcription of the army's returns, **about 84% of recorded deaths in the first twelve months** fell into the disease category.

Not quite the picture of war you might expect.

<figure class="story-chart full-bleed">
  <a href="https://commons.wikimedia.org/wiki/File:Diagram_of_the_causes_of_mortality_in_the_army_Wellcome_L0041105.jpg" aria-label="View the original Florence Nightingale diagram at Wellcome through Wikimedia Commons">
    <img src="{{ '/assets/icons-of-data/nightingale/01_nightingale_1858_wellcome.jpg' | relative_url }}"
         alt="Original 1858 two-circle polar-area diagram by Florence Nightingale. The large right-hand circle represents monthly mortality causes between April 1854 and March 1855 and the smaller left-hand circle covers April 1855 to March 1856. Broad blue sectors dominate the first period; narrower red and dark sectors represent wounds and other causes."
         width="1536" height="1000" loading="lazy" decoding="async">
  </a>
  <figcaption>Florence Nightingale, <em>Diagram of the Causes of Mortality in the Army in the East</em> (1858). Digital scan: <a href="https://commons.wikimedia.org/wiki/File:Diagram_of_the_causes_of_mortality_in_the_army_Wellcome_L0041105.jpg">Wellcome Collection, L0041105</a>, <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. Original scan proportionally resized for the website; no crop or editorial recolouring. The first year is on the <strong>right</strong>, the second on the <strong>left</strong>. The blues, reds and dark marks follow Nightingale's historical cause categories.</figcaption>
</figure>

## A rose with a rather sharp point

The diagram looks a little like a flower. But it's not an ordinary pie chart.

Each month gets the same angle. The **area** of each coloured section represents a mortality **rate**, not a headcount — or simply the distance from the centre.

That last detail matters. Double a wedge's radius and its area quadruples. Nightingale's design accounted for that.

There are two circles: the first year of the war on the right, and the second on the left. The later blue areas are dramatically smaller.

<figure class="story-chart full-bleed">
  <a href="{{ '/assets/icons-of-data/nightingale/02_what_the_numbers_reveal.png' | relative_url }}">
    <img src="{{ '/assets/icons-of-data/nightingale/02_what_the_numbers_reveal.png' | relative_url }}"
         alt="Line chart of annualised monthly British Army mortality rates per 1,000 soldiers from April 1854 to March 1856, starting at zero. The blue disease line rises sharply to 1,022.8 in January 1855, then falls across the second period. Red wounds and charcoal other-causes lines remain much lower. A dashed divider marks April 1855."
         width="1920" height="1920" loading="lazy" decoding="async">
  </a>
  <figcaption>Same historical returns, modern view: 24 monthly records, plotted as <strong>annualised rates per 1,000 troops</strong>, not counts of deaths. The disease peak of 1,022.8 in January 1855 is an annualised rate based on 2,761 recorded disease deaths and estimated army strength 32,393 for that month. Source: <code>HistData::Nightingale</code>, digitised from nineteenth-century military records. A decline is observable; this plot does not assign a cause.</figcaption>
</figure>

## A chart isn't a verdict

Sanitary improvements were made during the war, and Nightingale wanted officials to recognise the importance of preventable illness.

But the chart alone can't tell us exactly why the death rates fell. The seasons, army strength, conditions and military campaign changed too.

Nor did she invent the polar-area chart from scratch.

What she did was make an uncomfortable comparison extremely difficult to miss.

<figure class="story-chart full-bleed">
  <a href="{{ '/assets/icons-of-data/nightingale/03_decode_the_icon.png' | relative_url }}">
    <img src="{{ '/assets/icons-of-data/nightingale/03_decode_the_icon.png' | relative_url }}"
         alt="Decode the Icon four-panel explainer. Panel one shows twelve equal 30-degree monthly sectors. Panel two illustrates fixed-angle sector areas of one and four, with radius doubled for the larger. Panel three separates disease, wounds and other causes into three distinct illustrations to explain Nightingale's shared-centre overlap rather than stacked bands. Panel four distinguishes observed declines in mortality from unproven explanations for those declines."
         width="1920" height="1920" loading="lazy" decoding="async">
  </a>
  <figcaption>Decode the Icon: equal monthly angles, <strong>area proportional to mortality rate</strong>, three colour-coded causes and the limits of a two-period comparison. All drawn wedges in the decoder are <strong>explanatory schematics</strong>, not reconstructions of particular historical months.</figcaption>
</figure>

## TLDR

Nightingale didn't just organise numbers. She organised an argument.

The colours caught your eye.

The data asked what could have been prevented.

And sometimes that's precisely what a good chart needs to do.

<aside class="method-note">
  <h2>Source and method</h2>
  <p>The historical source is Florence Nightingale's <em>Notes on Matters Affecting the Health, Efficiency, and Hospital Administration of the British Army</em> (1858). The original digitised plate is <a href="https://wellcomecollection.org/works/sz9sms2m">Wellcome L0041105</a>, independently available from <a href="https://commons.wikimedia.org/wiki/File:Diagram_of_the_causes_of_mortality_in_the_army_Wellcome_L0041105.jpg">Wikimedia Commons</a> under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>, credited above with resizing disclosed. The 1858 plate should not be confused with later editions of the diagram.</p>
  <p>For the modern chart, the <a href="https://search.r-project.org/CRAN/refmans/HistData/html/Nightingale.html">HistData Nightingale</a> transcription contains 24 months from April 1854 to March 1856, with recorded deaths and estimated army strength. Annualised cause-specific mortality rates are calculated as <strong>monthly recorded deaths ÷ estimated army strength × 12,000</strong>, yielding annualised deaths per 1,000 soldiers, not actual monthly deaths per 1,000. The original data transcription and <a href="https://github.com/adamgreen1708/chart-templates/tree/main/archive/projects/2026-10-icons-of-data/editions/04-nightingale/data">QA summary</a> are in this project's source archive. In the first period, 11,157 of 13,294 recorded deaths (about 84%) were categorised as disease; that count proportion is not itself a radial chart rate.</p>
  <p>Nightingale's colours label nineteenth-century cause categories; “zymotic” is not an exact modern medical diagnostic category. A striking before-and-after pattern does <strong>not prove</strong> how much any one sanitary intervention contributed to the changes.</p>
</aside>

<p><a href="{{ '/resources/icons-of-data/' | relative_url }}">Explore more Icons of Data →</a></p>

<p class="sign-off"><strong>simple charts clear stories.</strong></p>
