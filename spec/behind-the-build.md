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
Published collection: From conversation to creation; Building a chart factory; Keeping AI honest; Pixel Art Studio; Truchet Tile Studio; The Dot Studio; Bauhaus Art Studio; Premier League Unfolded; Interwoven; Python — Making sense of the numbers; JavaScript — Bringing things to life; HTML and CSS — Giving everything a home; Drawing with code — When numbers become pictures; Where do the numbers come from?; Finding the story; The recipe for a chart; Building a visual identity; From GitHub to website; A memory outside ChatGPT; Putting things on autopilot (20 articles: 14 How we work and 6 How we made it). See the approved Phase 2 and Phase 3 roadmap below.

Capture methodology, decisions and lessons at completion of substantial projects, then draft the relevant reference article for review. Keep site/about/behind-the-build and site/assets/behind-the-build separate from normal blog content.

## Navigation and spacing (26 November 2026)
- Both collections and their direct article links appear on About under Behind the build. The dedicated index remains available for existing links, using the same shared include; do not require an intermediate page to reach an article. Article breadcrumbs return directly to the About section. Keep About highlighted within the collection.
- Use the scoped compact hero and prose rules in the Behind the build stylesheet; do not inherit the generous 4rem heading margins and 8rem section padding. Preserve the original site-wide blog styles. Review phone and desktop rhythm; do not confuse generous breathing room with large empty gaps.

## Stylesheet delivery and resilient index
Load the Behind the build stylesheet in the shared HTML head only for About routes, after site.css; bump its version query on CSS changes to prevent stale Safari cache. Index entries must have explicit whitespace, separate link titles and description paragraphs so they remain readable even if styles do not load. Validate built markup and CSS and inspect live phone view before describing visual QA as complete.

- Truchet explainer uses the full studio's radial rule, reflection mappings and seeded noise on a fixed 8×8 grid. Preserve repeatability, static no-JS artwork, native keyboard-accessible slider and reset. Art is procedural, not a statistical chart.

- Dot Studio explainer uses a labelled procedural landscape, the original brightness and size rules at 80% variation, and eight-tone greyscale. Reference the original Tableau artwork in place. Keep the demo distinct from the full photographic and halftone engine; preserve native accessible controls and static fallback.

- Bauhaus explainer uses the actual built-in illustrative running values (not personal running records), studio palettes, area formulas and explicit zero-based versus min–max scale. Keep colour meanings explicit, decorative sequence labelled, native controls and no-JS fallback. Simplified layout and upright triangle orientation are intentional.

## Demystifying the code — approved follow-on roadmap
Develop these How we work articles in order, with the established editorial review and approval gate:
- 04. Python — Making sense of the numbers (published): show actual inputs, a small source-grounded transformation, validation and outputs.
- 05. JavaScript — Bringing things to life (published): show how the browser reads data, creates marks, responds to events and updates the display.
- 06. HTML and CSS — Giving everything a home (published): explain markup, typography, layout and responsive design.
- 07. Drawing with code — When numbers become pictures (published): compare SVG, Canvas and deterministic Python rendering.
Write for non-coders, not as full coding tutorials. Use plain-English step-by-step explanations, actual code excerpts, small interactive examples and links back to product stories. Once published, add contextual links from existing articles where they use these technologies. Do not add dead links before publication.

- Premier League teaching example uses the archived 2025–26 JSON, four clubs and August–October only. Check all scores, W/D/L, cumulative and venue totals against the frozen dataset. Keep the production season data, scoring code and scheduled refresh workflow unchanged; describe the configured automation rather than guaranteeing a current result.

- Editorial challenges should teach the reader something about the creative or analytical process; omit incidental delivery problems from public articles while retaining technical records and provenance internally.
- Interwoven explainer uses four verified archived fixtures and the source sphere-radius, winner-halo and connection-brightness rules, with enlarged marks and simplified spacing. Reuse the existing exhibit media by reference; no changes to approved artwork, film, data, explorer or validation manifests. Distinguish conceptual diagrams and browser gradients from the full artwork.

- Python explainer uses three actual archived fixtures, the exact scoring instruction and two browser-based teaching simulations. Clearly distinguish points earned in a fixture from cumulative points in the production JSON; label simplified output and intentional errors. Link contextually from the chart factory, Premier League Unfolded and Interwoven. No changes to production data or Python scripts.

- JavaScript explainer uses the original six selected pixel palette entries and same-colour tap-to-erase rule on a reduced 3×3 grid, with explicit event/state/render readout and a conceptual shape drawing demo. Retain exact source code excerpts; contextual links in Python and all six product articles. No modifications to product implementations.

- HTML/CSS explainer includes Jekyll as the static site generator and GitHub Pages as the host. Use actual layout placeholders, source CSS spacing values and 420px media-query rule, and the existing frog. Four scoped browser demos: styling, template assembly, spacing and responsive layout. Label all as teaching previews, not live Jekyll execution or site screenshots. Preserve actual website-wide styling; reserve deployment detail for the GitHub-to-website article.

- Drawing explainer compares SVG geometry, simulated raster pixels and the actual Python-to-PNG process. Same magnification in both previews; use the four original Truchet paths and area versus radius on illustrative values only. Embed the existing Patrick Stewart PNG unchanged. Add contextual links to related articles; no production renderer or data changes.

## Extended editorial roadmap — approved 26 November 2026

Finish How we work before returning to individual product stories. Review each article with Adam before publishing; retain the interactive, source-grounded reference approach.

### Phase 2 — How we work
- 08. Where do the numbers come from? (published): source discovery, API, provenance, missing values and suitability for a question.
- 09. Finding the story (published): one dataset, competing hypotheses, editorial judgement and rejecting weak narratives.
- 10. The recipe for a chart (published): CHART_CONFIG and rendering rules.
- 11. Building a visual identity (published): palette, typography, layout and consistent visual language.
- 12. From GitHub to website (published): repositories, branches, commits, pull requests, Actions and Pages.
- 13. A memory outside ChatGPT (published): versioned prompts, standards, decisions and lessons.
- 14. Putting things on autopilot (published): scheduling, automated data updates and controlled publication.
- 15. When things go wrong: tests, failure detection, debugging and lessons.
- 16. Designing for everyone: mobile readability, accessibility, contrast and interaction.

### Phase 3 — How we made it
- 07. Tiny Pixel Zoo & Pixel Universe
- 08. Blockbuster Quote
- 09. Today's Data Lens
- 10. Icons of Data
- 11. Daily Pulse

Target 27 articles across the two collections. Creating for fun remains a separate personal editorial piece, not part of the numbered library.

Article 08 uses verified archived football provenance and five actual film records; missing ratings are preserved by default, with deliberately incorrect zero substitution labelled. The evidence quiz distinguishes film votes from audience or cultural importance. The data passport is an illustrative documentation format, not an adopted formal source standard. No changes to source data or refresh workflows.

Article 09 deliberately uses the approved shorter copy (~300 words), one conceptual diagram, two interactive editorial examples and the three original published Pattinson chart PNGs without changes. Avoid repeating the editorial-control diagram from Keeping AI honest. The 14 film-pair connections and six verified performers are documented retrospective findings, not independently recalculated source records; do not imply an exhaustive search or causal casting explanation.

Article 10 uses the three genuine September Bowie track-length recipes, not Patrick Stewart. Reuse the original published PNGs unchanged (verify archive/published blob equality); the chart-type diagrams and layout previews are explicitly conceptual. Preserve legacy configuration values rather than presenting them as current social_square defaults. Compare actual plot widths 78% and 48%. No changes to chart data, configs, renderer or published Bowie story.

Article 11 uses the actual house palette and legacy/current typography profiles. Colour attention and mobile type previews use illustrative marks only; preserve original Kipchoge, Gary and superhero chart PNGs unchanged. Show source-defined colour exceptions and distinguish illustrative SVG previews from actual rendered PNGs. No production CSS, renderer or chart changes; only Behind the build scoped styles.

Article 12 uses actual PR #258, premerge build 45911674835 (deploy skipped) and postmerge deployment 45911725116 (success), checked 27 November 2026. The seven-stage teaching simulation distinguishes branch, commit, pull request, validation, human approval, merge and deployment, and blocks progress on a deliberately failed check. Human approval may precede PR creation; it must precede merge. No publishing workflow changes or actual GitHub operations occur in the browser demo.

Article 13 uses six genuine document extracts (verified against source), the documented 30 October house-profile migration decision, and three teaching simulations: fresh brief vs repository context, document explorer, and recording a decision. No measured AI performance comparison or claim of automatic compliance; controls make no changes to GitHub. No changes to production guidance, renderer or workflows.

Article 14 uses the actual EPL DST-gated schedule and restricted data-only publication path, Daily Pulse UTC schedule, retries and recovery logic, and 27 November historical run records 46048994673 and 46047348222. Two teaching simulations distinguish failed checks, no-change runs, paused publishing and independent summary/report generation. Successful no-change football run is not proof of an automatic merge. No production workflow, schedule, data or permission changes.
