---
layout: behind-the-build
title: "Designing for everyone"
description: "Making our creations easier to see, understand and use."
permalink: /about/behind-the-build/how-we-work/designing-for-everyone/
collection_label: How we work
article_number: "12"
last_reviewed: 2026-11-27
social_image: /assets/behind-the-build/inclusive-devices.svg
---

## The idea

A visualisation is only useful if someone can actually use it.

It's something I spend a fair amount of time thinking about in my working life, and Coffeetableviz is no different.

The challenge isn't simply making things look good.

It's making them work for other people.

{% include behind-diagram.html name="inclusive-devices" alt="A desktop screen and a phone present the same illustrative information in different arrangements." caption="Different devices. Different needs. The same opportunity to explore." %}

## The challenge

We don't all experience information in the same way.

We use different devices. We see colours differently. Some of us navigate with a keyboard rather than a mouse.

Something that feels perfectly intuitive to the person who created it might be considerably less obvious to someone else.

## How it works

We've gradually introduced design principles that make our creations easier to explore.

Readable typography, meaningful colours, clear labels and layouts that adapt to smaller screens.

Where possible, we provide more than one way to access the information.

{% include behind-inclusive-labels.html %}

## Under the bonnet

Our Premier League visualisation automatically adjusts the club heading colour when it doesn't provide sufficient contrast against the dark background.

The individual match results also contain descriptive labels and can be explored using a mouse, touch or keyboard.

{% include behind-inclusive-contrast.html %}

Our Pixel Art Studio allows people to move between squares using the arrow keys.

Small details, perhaps, but useful alternatives to relying entirely on a mouse.

{% include behind-inclusive-grid.html %}

## What didn't work

Designing on a large screen can be rather deceptive.

A beautifully arranged chart can become almost unreadable when reduced to the width of a phone.

We now require our statistical charts to be reviewed at 320px and 390px as well as their original size.

*Try the screen-width and typography comparison in [Building a visual identity](/about/behind-the-build/how-we-work/visual-identity/#btb-identity-type).*

## What we learnt

Accessibility isn't something we can simply declare finished.

There are always opportunities to improve, and automated checks don't tell us everything about someone's actual experience.

Good design means considering those experiences from the beginning.

Comprehensive accessibility and screen-reader testing remain opportunities for improvement.

## Try it yourself

Experiment with colour contrast, additional labels and screen sizes in the examples above.

Notice how small changes can make information easier to interpret.

For the curious: [football visualisation code](https://github.com/adamgreen1708/chart-templates/blob/main/site/assets/js/epl-2627-unfolded.js), [Pixel Art Studio code](https://github.com/adamgreen1708/chart-templates/blob/main/site/assets/js/pixel-art-builder.js), [chart QA checklist](https://github.com/adamgreen1708/chart-templates/blob/main/docs/chart_qa_checklist.md) and [chart design standard](https://github.com/adamgreen1708/chart-templates/blob/main/spec/538_template_rules.md).

## TL;DR

Design for the reader, not just the screen in front of you.

Simple charts. Clear stories.

<script defer src="{{ '/assets/behind-the-build/inclusive-demo.js' | relative_url }}?v=1"></script>
