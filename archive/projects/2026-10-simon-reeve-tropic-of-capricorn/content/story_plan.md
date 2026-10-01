# Story plan — Simon Reeve's Tropic of Capricorn

## Recommended editorial route

**One invisible line creates a very crooked journey.**

The project should not use a world map as the main explanatory device. At square/mobile size, the globe compresses the route until the African and South American stops become unreadable. Instead, the chart sequence uses the Tropic of Capricorn itself as the visual spine.

## 3-chart sequence

### Chart 1 — Simon Reeve's Tropic of Capricorn
**Role:** Set the scene.

**Question:** What was the travel order?

**Visual:** Ten evenly spaced country nodes zig-zagging above and below a dashed Tropic of Capricorn line.

**Why it works:** It explains the route in seconds on a phone and preserves the Claude prototype's strongest idea: the invisible latitude line is the organising device.

**Caveat:** Deliberately schematic. Stops are evenly spaced and do not encode distance or longitude.

### Chart 2 — Ten countries, west to east, placed by longitude
**Role:** Build the tension.

**Question:** How closely did the named stops actually hug 23.4° south?

**Visual:** Broken longitude panels for Africa, Australia and South America. Named stops are placed by approximate longitude and latitude, with latitude visually exaggerated 3×.

**Why it works:** It turns the phrase 'following the Tropic' into something analytical: the expedition repeatedly wanders north and south of the line.

**Caveat:** Place positions are approximate and use representative named stops from the supplied route notes. The chart is not a GPS trace.

### Chart 3 — A straight line still took eight ways to travel
**Role:** Land the lighter aha moment.

**Question:** How many different forms of transport did the journey require?

**Visual:** Four grouped clusters linked by a journey thread: Ground 4, Air 2, Water 1, Animal 1.

**Why it works:** It avoids a dull four-bar ending and turns a small categorical count into a memorable visual.

## Design decision

Use the locked coffeetableviz light-grey background, teal primary and muted-red accent. Typography is intentionally larger than the historical 538 default because the charts are designed to be read on mobile.

## Publication gate

The deterministic GitHub Actions renders must be visually reviewed before the site post and site assets are staged.
