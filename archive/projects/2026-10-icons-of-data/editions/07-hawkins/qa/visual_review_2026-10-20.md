# Edition 07 — visual review handoff, 20 October 2026

**Approval stage:** Author approved editorial theme/headline/storyboard and expressly said to proceed to figures. **Not yet approved:** exact final figures, website rendition, merge or Pages publication.

## Completed for this visual-review pass

- Historical original identified: Ed Hawkins, *Climate Stripes: Warming Stripes, Global 2020*, University of Reading Art Collection, UAC/11018, digital artwork 2021, covering 1850–2020. Original source image exposed by the institution at https://collections.reading.ac.uk/art-collections/wp-content/uploads/sites/2/2021/10/UAC_11018-1200px-1024x576.jpg . See institutional collection/exhibition page https://collections.reading.ac.uk/art-collections/explore/online-exhibitions/climate-stripes/ . University explicitly describes share/copy/remix permission; formal artwork credit is still required.
- HadCRUT5 original-precision annual global series **1850–2026** committed for archive review at `data/HadCRUT.5.2.0.0.analysis.summary_series.global.annual.snapshot_2026-10-19.csv`, sourced from version-pinned `climate-resource/bookshelf-global-surface-temperature` snapshot taken **19 October 2026**. The snapshot's source manifest links to the UK Met Office official HadCRUT.5.2.0.0 producer file and states SHA256 `7f750b673bb34aad722736ee21f122b5ea692c99877fa0b1066df65e51f32c04`. **Producer download not independently repeated in this run**; source integrity against official producer remains a future publication gate.
- Latest `2026` annual row represents an incomplete year and **was excluded**. First/last year 1850–2025, exactly **176** complete-year anomalies, °C against native **1961–1990** HadCRUT5 reference.
- Two local chat-review PNGs rendered deterministically at **1920 × 1920** with #F3F4F6 background and one consistent, documented diverging blue/red scale fixed to -0.65..+1.3°C. They are *independent modern HadCRUT5 charts* — **not** claimed pixel-equal to the University of Reading's Global 2020 artwork or data source.
- `02_the_century_shifts_colour.png` observed local SHA256 `5d915709faeb9db69f7dd60ee840414141df32751d57e80b10496c58fea47ed4`: 176 equal-width annual bands and a sourced annual line with the native temperature anomaly scale. 2025 figure +1.07°C.
- `03_decode_the_icon.png` observed local SHA256 `64468017be2d3b969bf0204d6a05e9425c25abc6f5da8441a2969e033d0fcf0b`: adjacent four annual stripes (2022–2025), palette legend, real 95% interval values for 2022–2025, and an explicitly calculated 1961–2010 rebase of the 2025 anomaly (+0.89°C vs +1.07°C on 1961–1990 base). Mean source offset for 1961–2010 = 0.18100777836°C.
- PNGs were inspected visually at original size and downscaled 320px previews in this conversation. The tiny annotations are intended to be readable when enlarged, not necessarily at a 320px inline preview.

## What remains deliberately undone

- The original institutional JPEG **has not been locally copied or altered**. Show as an authenticated link to the preserved collection object until exact file is retrievable.
- The two PNGs are local conversation-review artefacts, **not yet committed** to the GitHub archive or website; no false claim of site asset existence. Store exact bytes later rather than silently rerendering after approval.
- A reproducible repo renderer still needs to be staged with binary assets before website QA.
- Final source checksum comparison directly against official Met Office download, artwork reproduction credit/rights at the object level, exact PNG visual approval, responsive Jekyll/site preview, asset checks, and explicit merge/page publishing gate remain pending.
- No `site/**` assets, `site/_posts/**`, resource catalogue, workflow, CSS or renderer touched for Edition 07.

## Review decision requested

Approve/revise two actual modern figures and the University of Reading Global 2020 historical artefact separately. Subsequent site staging requires a further user go-ahead.
