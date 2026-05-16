import pandas as pd

df = pd.read_csv("data/scotch_whisky_flavours_enriched.csv")

flavour_cols = [
    "Body", "Sweetness", "Smoky", "Medicinal", "Tobacco", "Honey",
    "Spicy", "Winey", "Nutty", "Malty", "Fruity", "Floral"
]

rows = []

for flavour in flavour_cols:
    counts = df[flavour].value_counts().sort_index()
    total = counts.sum()

    for score, count in counts.items():
        rows.append({
            "Flavour": flavour,
            "Score": int(score),
            "Whiskies": int(count),
            "Percent": round(count / total, 4)
        })

out = pd.DataFrame(rows)

out.to_csv("data/scotch_whisky_flavour_distribution.csv", index=False)

print("Saved data/scotch_whisky_flavour_distribution.csv")