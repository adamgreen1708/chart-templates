# Edition 02 — Visual storyboard and build gates
**Working headline:** The map that put connections first
**Central argument:** Beck didn't simply tidy a map. He changed the information readers were meant to prioritise — the stations and connections, not the ground between them.

This is an Icons of Data editorial three-visual narrative, NOT a conventional three statistical chart dataset story. Follow original source -> honest comparison -> Encode/Decode reveal.

## 1. The original idea (scene-setting)
- **Question:** What was different about Beck's 1933 diagram?
- **Output:** Link to the exact January 1933 original held/identified by London Transport Museum; accompanying one-paragraph gallery caption and direct museum URL.
- **Claim:** Routes straightened; interchange diamonds; central area enlarged; diagram prioritises transfers.
- **Status:** Source identified. **NO embedding** until exact image reuse rights are established. If denied, use an original contextual silhouette/icon and an external open-original link, clearly describing the difference.

## 2. When the map stops behaving geographically (tension)
- **Question:** Can rearranging the same network make an interchange easier to read?
- **Output:** Two matched panels:
  - left: selected portion of a *single verified period's* Tube network plotted at actual station coordinates (basemap-free geographical scatter + verified route edges);
  - right: an original compact *teaching diagram* of the **same nodes and edges**, with regularised angles and spacing.
- **Data needed:** official or independently verifiable station coordinates and stop order/adjacency for a small, legible subsection of the *current* network. Record snapshot date and source URLs in a dataset manifest. Do not copy Beck's historic layout or pretend a current network equals the 1933 system.
- **QA:** same identities; station and edge counts identical across panels; verified interchange identities; no implied distance or journey time on schematic. If reliable network data cannot be obtained, mark the graphic as a conceptual schematic with abstract nodes rather than fake real stations.
- **Story:** The stations remain connected even when their display positions move.

## 3. Decode the Icon (reveal)
A repeatable four-panel editorial explainer, in approved `#F3F4F6` / teal / muted red / charcoal house style:
1. **Connections:** which stops meet which (topology).
2. **Geometry:** horizontal, vertical, 45-degree constraints (orientation).
3. **Spacing:** central compression relieved by redistributing gaps (layout rather than distance).
4. **Symbols and colour:** interchange marker, line identity (visual grouping).
Panels show an openly labelled interpretative teaching schematic, not the historic original or another transit map's trademarked artwork. Historic diamond detail may be described with attribution, but avoid stylised copying of the full 1933 asset.

## QA / editorial gates
- The original source must be institutionally attributable; reuse rights explicitly checked.
- All generated charts deterministic vector/text rendered by code rather than image model; fonts/labels clear on phone, no clipping; template square 1920x1920 or repo-standard 1600x1600 as appropriate.
- Same time-scope, units and station ordering across any matched diagrams.
- Do not invent ridership, transfers, journey times, physical station spacing or UX statistics.
- Do not claim 'geographic maps are useless' — use the right map for the question (walking above ground versus navigating line changes).
- Source note distinguishes historical illustration and modern pedagogic experiment.
- Feature image specifically expresses **trade-off of geography for connectivity**; original symbolic artwork on light grey (not a copy of the Tube map or TfL branding).
- All finished images shown for Adam's visual approval before creating a Jekyll post, changing `site/resources/icons-of-data/`, or merging.
