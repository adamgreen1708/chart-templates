# Bauhaus Gallery v2 — implemented typography and Ink refinement

This is a focused follow-up to merged PR #179, governed by `docs/bauhaus-gallery-v2-revision-brief.md`.

## Gallery Paper and other poster finishes — text safety

The new `posterSafeText` renderer measures text using Canvas metrics, wraps words and unbroken strings, and fits each editable field into a separate reserved region:

- Headline: x=82, y=110–203, 793px maximum width, 2 lines, 30–43px font.
- Explanation: x=83, y=211–275, 793px maximum width, 2 lines, 14–17px font.
- Source: x=83, y=849–915, 792px maximum width, 2 lines, 12–14px font.

Overflow after fitting is clipped **textually with ellipsis**, retaining full source text in the editable controls. Measured shapes remain inside the centre artwork band; no changes to values, filters or image export.

## Ink Study — lighter hero panel

The former full-width filled black block in Broadside is removed in Ink Study. Hero numbers are dark-on-stone, the rule and circular construction marks use a red accent, and every bar is drawn as a thin horizontal mark. Length still starts at zero and is proportional to the original value; the accent highlights all tied maxima.

Other finishes keep their existing hero panel. The gallery styles remain a *finish*, not a new data mapping.

## Checks completed

- Embedded JS compiles.
- Real GitHub Bowie CSV with 14 tracks on 1967 album; all 14 Broadside bars render.
- Ink draws no opaque, full-width hero block, while Paper/Colour remain visually distinct.
- Deliberately long headline, deck and source strings render within dedicated bands and do not reach into the central artwork or off the canvas in simulated Canvas test.
- Automatic caption restore still works.
- No source data, chart renderer or site publishing workflow files were altered.

## Checks still required before merging

- Actual final PNG/pixel inspection, including long unbroken identifiers, the thinnest red/black stripes, safe margins and all palettes.
- Mobile Safari interactions with 320–430 CSS-pixel layout, saved PNG and category changes. A simulated Canvas check does not establish real-device QA.

The next dependent PR adds **Stripe Study** and **Circle Study** as separate *poster composition engines* rather than expanding these finishes with more visual-only controls.
