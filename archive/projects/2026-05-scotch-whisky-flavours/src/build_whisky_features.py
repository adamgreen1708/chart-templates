import pandas as pd
import numpy as np

df = pd.read_csv("data/scotch_whisky_flavours.csv")
df.columns = [c.strip() for c in df.columns]

flavour_cols = [
    "Body",
    "Sweetness",
    "Smoky",
    "Medicinal",
    "Tobacco",
    "Honey",
    "Spicy",
    "Winey",
    "Nutty",
    "Malty",
    "Fruity",
    "Floral"
]

for col in flavour_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Derived metrics
df["Peat_Index"] = (
    df["Smoky"]
    + df["Medicinal"]
    + df["Tobacco"]
)

df["Dessert_Index"] = (
    df["Sweetness"]
    + df["Honey"]
    + df["Fruity"]
)

df["Total_Intensity"] = df[flavour_cols].sum(axis=1)

df["Complexity"] = df[flavour_cols].std(axis=1)

# Islay highlighting
islay_distilleries = [
    "Ardbeg",
    "Bowmore",
    "Bruichladdich",
    "Bunnahabhain",
    "Caol Ila",
    "Lagavulin",
    "Laphroig"
]

df["Islay_Flag"] = df["Distillery"].isin(islay_distilleries)

# Region mapping
region_map = {
    # Islay
    "Ardbeg": "Islay",
    "Bowmore": "Islay",
    "Bruichladdich": "Islay",
    "Bunnahabhain": "Islay",
    "Caol Ila": "Islay",
    "Lagavulin": "Islay",
    "Laphroig": "Islay",

    # Campbeltown
    "GlenScotia": "Campbeltown",
    "Springbank": "Campbeltown",

    # Lowlands
    "Auchentoshan": "Lowlands",
    "Bladnoch": "Lowlands",
    "Glenkinchie": "Lowlands",

    # Islands
    "ArranIsleOf": "Islands",
    "Highland Park": "Islands",
    "Isle of Jura": "Islands",
    "OldPulteney": "Islands",
    "Scapa": "Islands",
    "Talisker": "Islands",
    "Tobermory": "Islands",

    # Speyside
    "Aberlour": "Speyside",
    "Balvenie": "Speyside",
    "Benriach": "Speyside",
    "Benrinnes": "Speyside",
    "Cardhu": "Speyside",
    "Craigallechie": "Speyside",
    "Craigganmore": "Speyside",
    "Dufftown": "Speyside",
    "GlenElgin": "Speyside",
    "Glenfarclas": "Speyside",
    "Glenfiddich": "Speyside",
    "Glenlivet": "Speyside",
    "Glenlossie": "Speyside",
    "Glenrothes": "Speyside",
    "Linkwood": "Speyside",
    "Longmorn": "Speyside",
    "Macallan": "Speyside",
    "Mortlach": "Speyside",
    "Speyburn": "Speyside",
    "Strathisla": "Speyside",
    "Tamdhu": "Speyside",
    "Tomintoul": "Speyside"
}

df["Region"] = df["Distillery"].map(region_map)
df["Region"] = df["Region"].fillna("Highlands")

# Jitter for scatterplots
rng = np.random.default_rng(42)

df["Sweetness_Jitter"] = (
    df["Sweetness"]
    + rng.uniform(-0.13, 0.13, len(df))
)

df["Smoky_Jitter"] = (
    df["Smoky"]
    + rng.uniform(-0.13, 0.13, len(df))
)

# Export enriched dataset
output_file = "data/scotch_whisky_flavours_enriched.csv"

df.to_csv(output_file, index=False)

print(df.head())
print(f"Saved: {output_file}")