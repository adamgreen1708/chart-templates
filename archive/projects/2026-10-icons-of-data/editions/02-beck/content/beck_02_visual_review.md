# Visual review #01 — 9 October 2026

**Status: two finished contemporary explanatory graphics prepared for author visual approval, NOT published or committed as PNG assets.**

## Delivered for editorial review
- **Visual 1 — museum original:** external authoritative record for Harry Beck's 1933 pocket diagram. Source: [London Transport Museum catalogue](https://library.ltmuseum.co.uk/portal/Default/en-GB/RecordView/Index/106). The historical picture itself has **not** been copied or embedded because exact reproduction rights remain unclear.
- **Visual 2 — Same network. Different priorities.** `02_geography_vs_connections.png` — 1920 x 1920 PNG; SHA-256 `c3437080ab4f0309a43f05312063a45d3649ab280407ea863c99a018e55a277d`.
- **Visual 3 — One diagram. Four design decisions.** `03_decode_the_icon.png` — 1920 x 1920 PNG; SHA-256 `cd65ae43cd4c7fa9aa9f635f5a729c5e6a6157760cf32c9b1e3e2dd3e7ea36e1`.

Images and deterministic renderer were included in the `icons_of_data_02_beck_visual_review.zip` review file delivered in the ChatGPT conversation. **Assets are intentionally not staged to Jekyll**, preserving image-approval-first.

## Data and analysis
Both comparative maps use the exact same **10 station identities** and **10 source-verified line edges** from the research network captured in **2013**. Source licence: ODbL 1.0, DBCL 1.0, De Domenico et al. (PNAS, 2014), as documented in `data/README.md`.

- `data/stations_2013.csv` — 10 coordinates with source station IDs.
- `data/connections_2013.csv` — 10 direct line connections: Central 3 / Bakerloo 3 / Piccadilly 4.
- Geographic panel uses station coordinates; connecting segments are drawn **straight between station centres**, NOT as tunnel routes.
- Right-hand panel is a **new original teaching diagram** whose spacing conveys readability, not geography, physical distances or journey durations. Its 0/45/90 degree geometry was tested against its own points.
- Three salient interchange points (Oxford Circus, Piccadilly Circus, Holborn) and two terminals selectively labelled on both panels for clarity; every input station and connection remains drawn.
- The house colour palette is **not** the official Tube-line palette. Markers are original design, not a reconstruction of specific 1933 symbols.

## Visual QA
- Both exported at **1920 x 1920** pixels, 1:1.
- Adjusted label positions after first render detected crowding; kept adequate margin at edge and for footer.
- Four-panel figure revised to remove colliding bottom right caption and increase clearance between panels/footer.
- Checked full-sized outputs and 600 x 600 reductions for label hierarchy.
- Code asserts station uniqueness, source endpoint containment, graph edge counts per line, constant identity of both layout inputs and octilinear diagram constraints.
- No bar-truncation or fictitious comparison metric.

## After approval
1. Commit exact approved original PNGs and renderer, verify SHA-256 via GitHub Actions.
2. Complete article/Jekyll publication package on a review branch, no merge without explicit permission.
3. Update Resources item 02 from 'In research' to article link after final visual and editorial approval.
4. Build site and check mobile/desktop clipping, card aspect and alt text.
5. Historical map remains a museum link unless exact reproduction reuse rights are cleared. Do not imply visual 2/3 show the 1933 network.

## Approval and exact-asset delivery — 9 October 2026
Both modern charts were explicitly approved by the author. The exact images were reproduced on the GitHub runner using pinned `numpy==2.3.5`, `pandas==2.2.3`, `matplotlib==3.10.8` and `pillow==12.3.0`; the workflow failed closed on SHA mismatch. **Both checks succeeded**, and the PNGs were committed to `site/assets/icons-of-data/beck/`. Successful run: https://github.com/adamgreen1708/chart-templates/actions/runs/37969690244. The temporary rendering workflow was deleted. The approved reproducible source is `render_beck.py`.

The Jekyll article at `site/_posts/2026-10-09-the-map-that-put-connections-first.md` and Resources entry are staged on draft PR #109, not merged. Original 1933 map is still a museum link only. Final site preview, responsive QA and author publishing approval remain required.
