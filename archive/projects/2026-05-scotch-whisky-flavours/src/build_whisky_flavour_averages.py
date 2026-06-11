import pandas as pd

df = pd.read_csv("data/scotch_whisky_flavours_enriched.csv")

flavour_cols = [
    "Body", "Sweetness", "Smoky", "Medicinal", "Tobacco", "Honey",
    "Spicy", "Winey", "Nutty", "Malty", "Fruity", "Floral"
]

out = (
    df[flavour_cols]
    .mean()
    .reset_index()
    .rename(columns={"index": "Flavour", 0: "Average_Score"})
)

out["Average_Score"] = out["Average_Score"].round(2)

out.to_csv("data/scotch_whisky_flavour_averages.csv", index=False)

print("Saved data/scotch_whisky_flavour_averages.csv")