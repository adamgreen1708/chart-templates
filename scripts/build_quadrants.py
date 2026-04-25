import pandas as pd
from pathlib import Path

input_path = Path("data/fuel_prices_trimmed_correct_pct_clean.csv")
output_path = Path("data/fuel_prices_low_low_quadrant.csv")

df = pd.read_csv(input_path)

gas_median = df["Gasoline_pct_change_y"].median()
diesel_median = df["Diesel_pct_change_y"].median()

filtered = df[
    (df["Gasoline_pct_change_y"] <= gas_median) &
    (df["Diesel_pct_change_y"] <= diesel_median)
]

filtered.to_csv(output_path, index=False)

print(f"Gasoline median: {gas_median}")
print(f"Diesel median: {diesel_median}")
print(f"Saved {len(filtered)} rows to {output_path}")