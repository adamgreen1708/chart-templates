# Icons of Data — Edition 07: Ed Hawkins' Warming Stripes

**Started:** 20 October 2026
**Working headline:** How the world changed colour
**Editorial category:** Making the invisible visible
**Historic object:** Ed Hawkins / University of Reading, Warming Stripes, developed 2018. The specific archival comparison artefact proposed is the University of Reading Art Collection's *Climate Stripes: Warming Stripes, Global 2020* (digital edition 2021, collection UAC/11018), depicting 1850–2020.
**State (20 October 2026):** Editorial direction approved. A pinned Met Office snapshot, edition-specific renderer, authentic original and two modern visuals were generated and hash-QA'd on GitHub Actions; full GitHub PNGs visually inspected. All output remains under edition archive on draft PR #138. Exact final image approval **pending**; no site post, Resources change, merge or GitHub Pages publication.

## Working editorial argument
Removing scales, labels and numbers makes a century-spanning temperature pattern immediately legible; the same decision makes precise magnitudes, uncertainty and reference periods much harder to inspect. Colour replaces nearly all the furniture of a conventional chart.

## Review deliverables
- `content/hawkins_07_draft.md`: conversational approximately 350–400 word manuscript with three image placements and TLDR.
- `content/hawkins_07_visual_plan.md`: historical original -> independently sourced modern stripes/temperature view -> four-panel encoding decoder.
- `research/hawkins_07_sources.md`: University of Reading primary records, data/licence sources, dates and caveats.

## Explicit gates before rendering
1. Confirm the exact original source asset and reproduction rights for the art-collection Global 2020 edition. University gallery indicates wide reuse, but check rights attached to the exact image file. Do not AI-generate a fake historical original.
2. Download **HadCRUT.5.2.0.0** annual global mean series directly from the Met Office and preserve the original source. Do not invent rows/values or assume 2026 partial-year observations constitute a completed year. Prefer completed years only (through 2025 if present).
3. Document data provenance, version, exact period, year count and the published HadCRUT5 baseline of **1961–1990**. If rebasing to a **1961–2010** mean to resemble the University diagram, calculate the adjustment from identical annual source values; document that it is a distinct dataset and not a pixel-exact recreation.
4. Check Met Office Open Government Licence v3 attribution including download date/version and Morice et al. (2021). Berkeley Earth data are BY-NC 4.0, not interchangeable rights.
5. Compose **modern Figures 02 and 03 only** as 1:1 square visuals on #F3F4F6; show **Figure 01 in its original 1200×675 aspect without Coffeetableviz framing** using house fonts and generous safe margins. Use historically meaningful blue-red temperature colour encoding as a justified palette exception; avoid misleading a viewer with arbitrary house teal/red for a source-faithful stripe view.
6. Text/pixel QA at full resolution and at 390/320px; meaningful image descriptions, contrast checks, precise time labels and reference-period notes.

## Author approval gates
A. Approve editorial hook/headline/working article and visual storyboard.
B. Independently research/download/validate data; render authentic original + two deterministic graphics, visually QA and show to author.
C. Only after exact image approval, stage Jekyll and Resources website preview on a review PR and perform desktop/mobile/site-link checks.
D. Separate explicit approval to merge/deploy; verify Pages and live URL. Do not publish from this research draft PR.

No site, renderer, CSS or active workflows changed in this kickoff.


## GitHub-hosted review production — 20 October 2026
Successful final GitHub workflow run: https://github.com/adamgreen1708/chart-templates/actions/runs/39505109952 . Final source-data integrity, original, three 1920 square images, all hash values, author-review links, visual inspection and remaining image/site approval requirements are documented in `content/hawkins_07_visual_review.md` and `qa/render_manifest.json`.

**Temporary workflow must be removed after successful review render; keep the edition-specific Python renderer so the images can be regenerated through GitHub when requested.** Website remains untouched. Exact GH-generated image approval required before staging site content.

## Author correction: historical image and the reference years (20 October 2026)

The author correctly rejected Figure 01 as a 1920px Coffeetableviz frame, since Icons of Data shows the untouched original object. The framed file and 320/390/600 previews were deleted from the draft branch. Correct first figure is `qa/visuals/01_reading_global_2020_original_unmodified.jpg`, **1200×675**, SHA-256 `64ac4a7b3ed36fc7448b107caa4b6c222005013862ecf017947e24ad4d16f07f`. Modern Figures 02/03 remain separate, square Coffeetableviz interpretations. Renderer updated not to frame the historical artwork.

Authoritative Hawkins first-person 2024 source confirms the **2023** baseline change from **1971–2000** to **1961–2010**, to handle exceptionally high 2023 values along with palette changes; the original Global 2020 artefact precedes that update. Our Met Office HadCRUT5 data instead use **1961–1990**. Verified correction and source integrity in GitHub Actions https://github.com/adamgreen1708/chart-templates/actions/runs/39506769249 . Author image and site publication approval still pending. 
