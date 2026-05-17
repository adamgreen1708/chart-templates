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

grouped = (
    df.groupby("Region")[flavour_cols]
    .mean()
    .round(2)
    .reset_index()
)

out = grouped.melt(
    id_vars="Region",
    var_name="Flavour",
    value_name="Average_Score"
)

out.to_csv("data/scotch_whisky_region_profiles.csv", index=False)

print(out.head(20))
print("Saved: data/scotch_whisky_region_profiles.csv")