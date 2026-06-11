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

def flavour_lane(score):
    if score >= 10:
        return "Sweet / fruity"
    elif score >= 8:
        return "Malty / honeyed"
    elif score >= 6:
        return "Balanced / approachable"
    else:
        return "Smoky / peaty"

df["Flavour_Profile"] = df["Peat_Avoider_Score"].apply(flavour_lane)

output = df[
    [
        "Distillery",
        "Region",
        "Peat_Avoider_Score",
        "Flavour_Profile",
        "Sweetness",
        "Fruity",
        "Malty",
        "Honey",
        "Smoky",
        "Medicinal",
    ]
].sort_values("Peat_Avoider_Score", ascending=False)

output.to_csv("data/scotch_whisky_flavour_menu.csv", index=False)

print(output.head(20))
print("Created: data/scotch_whisky_flavour_menu.csv")