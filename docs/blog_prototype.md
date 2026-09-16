# coffeetableviz GitHub Pages prototype

The prototype extends the repository from chart production into publication without changing the renderer.

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

## Deliberately unchanged

- WordPress remains live and untouched.
- Existing chart renderers and workflows are unchanged.
- No WordPress archive content has been migrated.
- No custom domain has been configured.

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

