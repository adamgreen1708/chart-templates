# Beck #02 — sourced Tube subnetwork (2013)

This is a **derived subset** of the London multiplex network collated from Transport for London information in **2013**, published for the research paper:

> M. De Domenico, A. Solé-Ribalta, S. Gómez and A. Arenas (2014), "Navigability of interconnected networks under random failures", PNAS 111 (23), 8351–8356.

Original data repository: https://github.com/CoMuNeLab/London-Multiplex-Transport-Network

Source tables at the time of extraction:
- `Dataset/london_transport_nodes.txt`, Git blob `b5b1cdf10db74cce4ac44cb0b8c978f864d33018` (station IDs, station labels, latitude, longitude; 369 source rows).
- `Dataset/london_transport_raw.edges`, Git blob `958e0a39ead38cea8d1d38ac50840a8c4b40770e` (line-specific edges; 503 source rows).

## Extraction
- Keep precisely these 10 station IDs: `bondstreet`, `regentspark`, `greenpark`, `oxfordcircus`, `charingcross`, `coventgarden`, `holborn`, `tottenhamcourtroad`, `piccadillycircus`, `leicestersquare`.
- Keep a link only when it connects two selected stations and its line is `central`, `bakerloo` or `piccadilly`.
- Result: **10 stations**, **10 separate line-specific links** (Central 3, Bakerloo 3, Piccadilly 4).
- Station coordinates copied from the source strings without statistical inference. Exact source names normalized to display text in the third column (source `station_id` retained).
- The two figures compare **exactly the same nodes and labelled line edges**. The geographic version joins station centres with *straight segments*; these are not physical tunnel/route shapes.
- Teaching version uses manually chosen abstract x/y positions. The geometry is original illustrative artwork, **not** Beck's 1933 diagram or an official modern TfL map. No journey duration or distance is claimed from segment lengths.
- The research source dates to 2013 and **must not be passed off as the network in 1933 or October 2026**.

## Open-data licence and attribution
The original data is licensed **Open Database Licence (ODbL) 1.0**, with individual contents under **Database Contents Licence (DbCL) 1.0**. This derived data subset is shared on the same ODbL 1.0 terms. Keep this notice and accompanying source link with any public reuse of the data, and link to the original licences:

- https://opendatacommons.org/licenses/odbl/1-0/
- https://opendatacommons.org/licenses/dbcl/1-0/
- Full licence text in the source repository: https://github.com/CoMuNeLab/London-Multiplex-Transport-Network/blob/master/LICENSE_odbl-10.txt and `LICENSE_dbcl-10.txt`.

**Credit on chart**: De Domenico et al. / TfL (network captured 2013). House palette differs intentionally from TfL official line branding. Typography/layout: original Coffeetableviz interpretation.

## QA
- Station IDs: all unique; coordinates numerical and non-null; no invented stations.
- Edges: no duplicates; all endpoints in selected stations; one line per source edge.
- Diagram's node/edge identities match the geographic panel 1:1.
- Labels are shown only for selected key stations to preserve safe margins. All selected station nodes remain drawn.
