# coffeetableviz site prototype

This folder is the source for the GitHub Pages prototype.

## Content model

- `_posts/` contains the Markdown master copy for published stories.
- `assets/charts/` contains publication-ready chart outputs.
- `_layouts/` and `_includes/` define the reusable site shell.
- `about/` and `archive/` contain the supporting pages.

## Local preview

From the repository root:

```bash
bundle install
bundle exec jekyll serve --source site --baseurl ""
```

The GitHub Pages workflow builds from `site/` and deploys only after changes are merged to `main`.

