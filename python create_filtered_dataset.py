import pandas as pd

# Load dataset
df = pd.read_csv("data/fuel_prices_trimmed_correct_pct_clean.csv")

# Define medians
gas_median = 16.5
diesel_median = 27.2

# Filter quadrant (bottom-left)
filtered = df[
    (df["Gasoline_pct_change_y"] <= gas_median) &
    (df["Diesel_pct_change_y"] <= diesel_median)
]

# Save new dataset
filtered.to_csv("data/fuel_prices_low_low_quadrant.csv", index=False)

print(f"Filtered rows: {len(filtered)}")