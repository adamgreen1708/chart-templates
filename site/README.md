# coffeetableviz site prototype

This folder is the source for the GitHub Pages prototype.

## Content model

- `_posts/` contains the Markdown master copy for published stories.
- `_data_lens/` contains verified daily Data Lens editions.
- `data-lens/resources/` contains evergreen Data Lens guides.
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
