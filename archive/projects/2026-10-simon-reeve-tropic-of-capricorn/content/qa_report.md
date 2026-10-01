# QA report — Simon Reeve's Tropic of Capricorn

## Current status

**Pending official GitHub Actions renders.**

## Data checks completed

- Country route has exactly 10 rows and preserves the supplied travel order.
- Country sequence starts in Namibia and ends in Brazil.
- Longitude dataset contains only named stops from the supplied route notes.
- Coordinate sources are documented in the dataset/source notes.
- Transport dataset contains exactly eight named modes.
- Derived family counts reproduce Ground 4, Air 2, Water 1, Animal 1.

## Visual QA gate after render

Each official PNG must pass all of the following before Adam is asked to approve it:

- no title or subtitle clipping;
- no text outside safe margins;
- no overlapping country/place labels;
- readable at phone width;
- route order obvious without explanation;
- dashed Tropic reference line distinct from the route;
- start/end red highlight used consistently;
- continent/panel structure clear;
- footers do not collide;
- no unnecessary chart furniture;
- source/caveat language visible;
- output is 1600 × 1600 at 200 DPI.

## Publication status

No live Jekyll post or site assets have been staged yet. Site publication follows chart approval.
