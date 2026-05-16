import pandas as pd

df = pd.read_csv("data/scotch_whisky_flavours_enriched.csv")

out = (
    df["Smoky"]
    .value_counts()
    .sort_index()
    .reset_index()
)

out.columns = ["Smoky_Score", "Whiskies"]

out["Percent"] = (
    out["Whiskies"] / out["Whiskies"].sum() * 100
).round(1)

out.to_csv("data/scotch_whisky_smoky_distribution.csv", index=False)

print(out)
print("Saved: data/scotch_whisky_smoky_distribution.csv")