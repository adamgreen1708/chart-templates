import pandas as pd
from pathlib import Path

INPUT_FILE = Path("data/arsenal_2025_26_matches.csv")
OUTPUT_FILE = Path("data/arsenal_rivals_results.csv")

RIVALS = [
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Chelsea",
    "Newcastle United",
    "Tottenham Hotspur",
]

df = pd.read_csv(INPUT_FILE)

required_cols = ["Opponent", "GF", "GA", "Result", "Points"]
missing_cols = [col for col in required_cols if col not in df.columns]

if missing_cols:
    raise ValueError(f"Missing required columns: {missing_cols}")

rival_matches = df[df["Opponent"].isin(RIVALS)].copy()

summary = []

for rival in RIVALS:
    subset = rival_matches[rival_matches["Opponent"] == rival]

    summary.append({
        "Opponent": rival,
        "P": len(subset),
        "W": (subset["Result"] == "W").sum(),
        "D": (subset["Result"] == "D").sum(),
        "L": (subset["Result"] == "L").sum(),
        "GF": subset["GF"].sum(),
        "GA": subset["GA"].sum(),
        "GD": subset["GF"].sum() - subset["GA"].sum(),
        "Points": subset["Points"].sum(),
    })

out = pd.DataFrame(summary)

out = out.sort_values(
    ["Points", "GD", "GF"],
    ascending=False
)

out.to_csv(OUTPUT_FILE, index=False)

print(out)
print(f"\nSaved: {OUTPUT_FILE}")