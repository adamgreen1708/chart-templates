import pandas as pd

df = pd.read_csv("data/fuel_prices_trimmed_correct_pct_clean.csv")

df["Diesel_pct_change_minus_gasoline_pct_change"] = (
    df["Diesel_pct_change_y"] - df["Gasoline_pct_change_y"]
)

df.to_csv("data/fuel_prices_trimmed_correct_pct_clean.csv", index=False)

print("Column added successfully")