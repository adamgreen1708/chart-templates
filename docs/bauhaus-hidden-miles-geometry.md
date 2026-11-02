# Hidden Miles cutout geometry

## Reference and intended result

This note governs the **free-play Cutout brush** and **Hidden Miles** starting pattern in the Bauhaus Art Studio.

Source visual: the existing Coffeetableviz **Hidden Miles** artwork, used on the Resources page at \`site/assets/migrated/running-in-shapes/hidden-miles.png\` and in the Running in Shapes post. Keep the studio motif recognisable rather than accidentally introducing a different diagonal and inset.

## The tile

The tile is a square of side \`s\`, with origin at its top-left. Its red (primary) polygon consists of six vertices, in order:

\`\`\`text
(0, .5s) → (.5s, 0) → (.5s, .5s)
         → (s, .5s) → (.5s, s) → (0, s) → close
\`\`\`

A contrasting **cream top-right square** covers \`x ∈ [.5s, s]\`, \`y ∈ [0, .5s]\`; the lower-right diagonal is exposed background (yellow). All geometry uses exact half-tile coordinates, so there are no small offsets or inconsistent slopes. A continuous pattern repeats without randomly rotating or recolouring the motif.

With the **Hidden Miles palette**:
- Background: \`#F3DD00\` yellow
- Main polygon: \`#CB3E2A\` red
- Upper-right cutout: \`#FAEEC4\` cream

The individually paintable **Cutout** shape is intentionally palette-aware, so users can experiment with other combinations. It rotates by 90° on repeated taps, like other manual brushes; this does **not** change the unedited Hidden Miles preset.

## Preset arrangement

- Hidden Miles is fixed **3 columns × 4 rows** with identical orientation and colour.
- The reference is shown on a square canvas with a small bottom-right \`HIDDEN MILES\` signature, no oversized editorial banner across the motif.
- Grid-size / chaos sliders are disabled in the reference preset, where they would otherwise imply changes that do not occur.
- User can still paint, erase, rotate, reset, undo, export PNG and share a design link. Switching to another creative mode restores the normal \`n × n\` interactive grid.
- The brush instruction explicitly explains that users should pick the Hidden Miles palette or preset to match the original screenshot.

## QA

- JavaScript syntax, canvas draw calls and change handlers.
- Verify exactly 12 red polygons, 12 cream squares, 0 random rotations on the preset.
- Compare clean geometry against source art: midpoints, red diagonal, cream quadrant, exposed yellow triangle, spacing.
- Test one Cutout tap, second tap rotates, undo, PNG export and normal-mode regression.
- Inspect the actual hosted result on mobile Safari before merging if possible; programmatic canvas-command checks and mock-up images do not establish successful on-device visual QA.
