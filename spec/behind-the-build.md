# Behind the build — editorial and visual standard v1.0

Approved direction: 26 November 2026. An evergreen reference library within About, not chronological posts.

## Editorial
- Two collections: How we work (the framework) and How we made it (individual products).
- Read it. See it. Play with it. Explore it.
- UK English; personal, conversational and curious; assume no technical knowledge. Use 'we' for Adam, ChatGPT and GitHub collaboration. Aim for 400–700 words.
- Consistent structure: The idea; The challenge; How it works; Under the bonnet; What didn't work; What we learnt; Try it yourself; TL;DR.
- Inspect current repo source, actual data and retrospective before writing. Distinguish historical facts, interpretation and proposals; never invent implementation details or failures. Link to original projects, code and data. Include author and last-reviewed date.
- Two or three purposeful visuals where helpful; diagrams may be non-square for clarity. Use responsive SVG, light-grey #F3F4F6, focus #1F8FA8, accent #C44E52, charcoal and neutral greys. Use accessible labels, adequate contrast and mobile readability. Explain any conceptual schematic.
- Interactive examples teach one concept, not duplicate the full product; no external libraries required for the first demo. Provide keyboard access, reset, meaningful labels, a non-JS fallback and a link to the product. Preserve real-data GitHub-only chart rendering; use actual pre-rendered outputs for any chart comparison, never fake statistical charts.
- Keep approved article copy and assets intact through PR review, inspect phone sizes, verify links, interactions and Pages build. No direct main changes. Confirm the live URL after deployment.

## Roadmap
Published collection: From conversation to creation; Building a chart factory; Keeping AI honest; Pixel Art Studio; Truchet Tile Studio; The Dot Studio. Future: recipe/config deep dive, finding the story, identity, GitHub to Pages, repo memory, automation, failures, Bauhaus, EPL, Interwoven, Tiny Pixel Zoo and Pixel Universe, Data Lens, Blockbuster Quote, Icons of Data and Daily Pulse.

Capture methodology, decisions and lessons at completion of substantial projects, then draft the relevant reference article for review. Keep site/about/behind-the-build and site/assets/behind-the-build separate from normal blog content.

## Navigation and spacing (26 November 2026)
- Both collections and their direct article links appear on About under Behind the build. The dedicated index remains available for existing links, using the same shared include; do not require an intermediate page to reach an article. Article breadcrumbs return directly to the About section. Keep About highlighted within the collection.
- Use the scoped compact hero and prose rules in the Behind the build stylesheet; do not inherit the generous 4rem heading margins and 8rem section padding. Preserve the original site-wide blog styles. Review phone and desktop rhythm; do not confuse generous breathing room with large empty gaps.

## Stylesheet delivery and resilient index
Load the Behind the build stylesheet in the shared HTML head only for About routes, after site.css; bump its version query on CSS changes to prevent stale Safari cache. Index entries must have explicit whitespace, separate link titles and description paragraphs so they remain readable even if styles do not load. Validate built markup and CSS and inspect live phone view before describing visual QA as complete.

- Truchet explainer uses the full studio's radial rule, reflection mappings and seeded noise on a fixed 8×8 grid. Preserve repeatability, static no-JS artwork, native keyboard-accessible slider and reset. Art is procedural, not a statistical chart.

- Dot Studio explainer uses a labelled procedural landscape, the original brightness and size rules at 80% variation, and eight-tone greyscale. Reference the original Tableau artwork in place. Keep the demo distinct from the full photographic and halftone engine; preserve native accessible controls and static fallback.
