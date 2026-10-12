# Icons of Data #06 — John Snow visual storyboard
**Subject:** John Snow's Broad Street cholera map, **1855 second edition**, representing fatal attacks during **1854**.
**Editorial theme:** Putting a pattern on a map changes what you notice. It does not automatically determine why the pattern arose.

## 01 — The historical original: where the marks came from
Use the **authentic 1855 book map**, not a model-generated imitation: *Map showing deaths from Cholera in Broad Street, Golden Square and the neighbourhood, from 19 August to 30 September 1854*. The specific **Wellcome L0063431** digital reproduction is at:
https://commons.wikimedia.org/wiki/File:Map_showing_deaths_from_Cholera_in_Broad_Street..._Wellcome_L0063431.jpg

Specific **image scan** is CC BY 4.0; credit *John Snow, 1855; digital image Wellcome Collection, L0063431, CC BY 4.0* plus changes/resizing. Original 1855 second-edition book at https://wellcomecollection.org/works/uqa27qrt is marked Public Domain Mark, which is **not** the same licence statement as the photographic digital reproduction on Wikimedia. Distinguish it from the separately published **July 1855 St James parish inquiry map**, such as Wellcome L0072142 / L0072917.

- Keep recognizable source orientation, legible bars and pump symbols. Do not crop the source so tight that legend and scale vanish.
- The source depicts fatal attacks identifiable at specific **houses**, not geocoded home address 'points' in a GPS system, dates of all infections, or infection rates.

## 02 — The pattern, redrawn (data-faithful modern map)
Question: **Where were the recorded fatal attacks, and where were the pumps?**
- Data: public `HistData` Snow datasets, archived unchanged at `data/Snow.deaths.csv`, `data/Snow.pumps.csv`, `data/Snow.streets.csv`.
- Exact source tables contain **578 reconstructed death-mark positions**, **13 water pumps**, **1,241 polyline coordinate rows describing 528 street segments**. These are **map-specific x/y coordinates** copied from the historical/cartographic digitisation, **not latitude/longitude**. Never reproject as geographic coordinates without defensible transformation.
- Plot streets as context grey `#D9D9D9`, fatal-attack marks dark `#111111` or restrained house primary for visibility, pump positions with legible symbol/label, and Broad Street pump in accent `#C44E52`. Explain that **red is a modern annotation**, not a historical source colour.
- Use the locked square 538 visual grammar (light-grey `#F3F4F6`, black message-led title, conversational subtitle, safe margins, small bottom source), but do not pretend a map is a `bar` or `scatter` with normal numerical axis interpretation; a dedicated **deterministic cartographic renderer** using verifiable coordinate positions may be appropriate with no change to shared `src/render_538.py`.
- Keep equal x/y aspect on map, no fictional figures and **no random jitter**. The `Snow.deaths` table includes intentional outward *stacking* at shared addresses, so those x/y positions are display marks rather than exact house centroids.
- Do not show *total outbreak deaths = 578*. The source is a digitisation of selected mapped marks; it is not a complete disease surveillance dataset. The data lack individual onset dates and street-address exposure denominators.
- If comparing proximity to pump, never infer source use from straight-line distance or put false 'catchment' rings around the pump.
- Accessible alt text should express clustering and pump locations while warning against rate/causal inference.

## 03 — Decode the Icon: geography is useful, but incomplete
Four distinct editorial panels in the established Icons of Data style, not a decorative repeat of Chart 2:
1. **One mark is one death** — several small bars stacked at an address, not an average or mortality rate; schematic bars explicitly flagged.
2. **Pumps give context** — one coloured pump annotation among neighbours; streets and walking access matter, not simply Euclidean circles.
3. **Counts are not rates** — no number of residents/people drinking from each pump in the historical drawing; do not create fabricated denominators.
4. **A sequence cannot be read from a snapshot** — the map does not encode individual dates; the Sep 8 handle removal followed decline already in progress. If using any miniature timeline, it must use source-verified fatal-attack-by-day counts, or simply a clear textual note without invented curves.
- One palette: archive monochrome source, house grey canvas, teal and red accents; no arbitrary new colours or cluttered modern banners. Keep visual identity consistent with approved #04/#05 editions.

**QA:** real source rows only; clear historical 1854 event vs **1855 print**, exact original image licence, value-type integrity, no fake GPS; chart labels and safe margins tested at 1920×1920 and 390/320px.
**Review stages:** approve manuscript + this storyboard; build/show original and two modern diagrams for image approval; assemble site/Resources and desktop/mobile QA; obtain **separate explicit approval before merge/Pages publication**.
