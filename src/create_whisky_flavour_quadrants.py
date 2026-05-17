import pandas as pd

df = pd.read_csv("data/scotch_whisky_flavours_enriched.csv")

df["Approachable_Index"] = (
    df["Sweetness"]
    + df["Fruity"]
    + df["Honey"]
)

df["Peat_Index"] = (
    df["Smoky"]
    + df["Medicinal"]
)

output = df[
    [
        "Distillery",
        "Region",
        "Approachable_Index",
        "Peat_Index",
        "Sweetness",
        "Fruity",
        "Honey",
        "Smoky",
        "Medicinal"
    ]
]

output.to_csv(
    "data/scotch_whisky_flavour_quadrants.csv",
    index=False
)

print(output.head())
print("Created: data/scotch_whisky_flavour_quadrants.csv")