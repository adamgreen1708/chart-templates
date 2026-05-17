import pandas as pd

df = pd.read_csv("data/scotch_whisky_flavours_enriched.csv")

flavour_cols = [
    "Sweetness",
    "Fruity",
    "Malty",
    "Honey",
    "Smoky",
    "Medicinal",
    "Floral",
    "Spicy"
]

out = (
    df.groupby("Region")[flavour_cols]
    .mean()
    .round(2)
    .reset_index()
)

out.to_csv("data/scotch_whisky_region_profiles.csv", index=False)

print(out)
print("Saved: data/scotch_whisky_region_profiles.csv")