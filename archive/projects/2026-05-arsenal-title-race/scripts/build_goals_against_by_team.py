import pandas as pd
from pathlib import Path

INPUT_FILE = Path("data/premier_league_final_table.csv")
OUTPUT_FILE = Path("data/goals_against_by_team.csv")

df = pd.read_csv(INPUT_FILE)

required_cols = ["Team", "P", "GA"]
missing_cols = [col for col in required_cols if col not in df.columns]

if missing_cols:
    raise ValueError(f"Missing required columns: {missing_cols}")

out = df[["Team", "P", "GA"]].copy()

out["GA_per_game"] = (out["GA"] / out["P"]).round(2)

out = out.sort_values(
    ["GA", "GA_per_game"],
    ascending=True
)

out.to_csv(OUTPUT_FILE, index=False)

print(out)
print(f"\nSaved: {OUTPUT_FILE}")