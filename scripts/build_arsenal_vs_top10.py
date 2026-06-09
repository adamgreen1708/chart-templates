import pandas as pd
from pathlib import Path

MATCHES_FILE = Path("data/arsenal_2025_26_matches.csv")
TABLE_FILE = Path("data/premier_league_final_table.csv")
OUTPUT_FILE = Path("data/arsenal_vs_top10.csv")

matches = pd.read_csv(MATCHES_FILE)
table = pd.read_csv(TABLE_FILE)

table = table.copy()
table["FinalPosition"] = range(1, len(table) + 1)

top10 = table[table["FinalPosition"] <= 10].copy()
top10 = top10[top10["Team"] != "Arsenal"].copy()

team_name_map = {
    "Man City": "Manchester City",
    "Man United": "Manchester United",
    "Bournemouth": "AFC Bournemouth",
    "Brighton": "Brighton & Hove Albion",
}

top10["OpponentName"] = top10["Team"].replace(team_name_map)

summary = []

for _, team in top10.iterrows():
    opponent = team["OpponentName"]
    subset = matches[matches["Opponent"] == opponent].copy()

    summary.append({
        "FinalPosition": team["FinalPosition"],
        "Opponent": opponent,
        "TableName": team["Team"],
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

out = out.sort_values("FinalPosition", ascending=True)

out.to_csv(OUTPUT_FILE, index=False)

print(out)
print(f"\nSaved: {OUTPUT_FILE}")