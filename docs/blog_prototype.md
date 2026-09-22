# coffeetableviz GitHub Pages prototype

> Historical prototype record. The site has since cut over fully to the repository/Jekyll/GitHub Pages publishing model. WordPress and Jetpack are not active publishing systems. For the current workflow, use `docs/coffeetableviz_process_flow.md`.

The prototype extended the repository from chart production into publication without changing the renderer.

## Publishing flow

```text
dataset -> story discovery -> chart configs -> render and QA -> Markdown post -> GitHub Pages
```

## Pilot scope

- chart-led homepage;
- About page;
- archive page;
- reusable post layout;
- one complete real article using the archived James Bond charts;
- responsive styling for desktop and mobile;
- GitHub Pages deployment workflow.

## Historical prototype assumptions

At the prototype stage:

- the legacy WordPress site was still live and untouched;
- existing chart renderers and workflows were unchanged;
- WordPress archive content had not yet been migrated;
- the custom domain had not yet been configured.

These statements describe the prototype stage only and are not current publishing instructions.

## Post front matter

Each story starts as Markdown in `site/_posts/` and carries the publication metadata the site needs:

```yaml
---
title: Story title
slug: readable-story-slug
description: One-sentence excerpt
category: Sport
read_time: 3 minute read
card_image: /assets/charts/chart-name.png
hero_image: /assets/charts/chart-name.png
hero_alt: Accessible description of the opening chart
---
```

## Prototype decision gate

Before migrating the WordPress archive, validate:

1. mobile reading experience;
2. image sharpness and page weight;
3. Markdown authoring from an iPhone;
4. chart-to-post path checks;
5. navigation and URL structure;
6. whether the visual identity feels recognisably coffeetableviz.

