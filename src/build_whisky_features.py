import pandas as pd

# Load raw dataset
df = pd.read_csv("data/scotch_whisky_flavours.csv")

# Clean column names
df.columns = [c.strip() for c in df.columns]

# Flavour columns
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

# Convert flavour columns to numeric
for col in flavour_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Derived metrics
df["Peat_Index"] = (
    df["Smoky"] +
    df["Medicinal"] +
    df["Tobacco"]
)

df["Dessert_Index"] = (
    df["Sweetness"] +
    df["Honey"] +
    df["Fruity"]
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

# Export enriched dataset
output_file = "data/scotch_whisky_flavours_enriched.csv"

df.to_csv(output_file, index=False)

print(f"Saved enriched dataset to: {output_file}")
print(df.head())