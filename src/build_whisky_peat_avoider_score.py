import pandas as pd

df = pd.read_csv("data/scotch_whisky_flavours_enriched.csv")

df["Peat_Avoider_Score"] = (
    df["Sweetness"]
    + df["Fruity"]
    + df["Malty"]
    + df["Honey"]
    - df["Smoky"]
    - df["Medicinal"]
)

out = df[
    [
        "Distillery",
        "Sweetness",
        "Fruity",
        "Malty",
        "Honey",
        "Smoky",
        "Medicinal",
        "Peat_Avoider_Score",
    ]
].copy()

out = out.sort_values("Peat_Avoider_Score", ascending=False)

out.to_csv("data/scotch_whisky_peat_avoider_score.csv", index=False)

print(out.head(20))
print("Saved: data/scotch_whisky_peat_avoider_score.csv")