import pandas as pd
from pathlib import Path

MATCHES_FILE = Path("data/arsenal_2025_26_matches.csv")
TABLE_FILE = Path("data/premier_league_final_table.csv")
OUTPUT_FILE = Path("data/arsenal_vs_top10.csv")

matches = pd.read_csv(MATCHES_FILE)
table = pd.read_csv(TABLE_FILE)

required_table_cols = ["Team", "P", "W", "D", "L", "GF", "GA", "GD", "Pts"]
required_match_cols = ["Opponent", "Result", "GF", "GA", "Points"]

missing_table = [c for c in required_table_cols if c not in table.columns]
missing_matches = [c for c in required_match_cols if c not in matches.columns]

if missing_table:
    raise ValueError(f"Missing columns in final table: {missing_table}")

if missing_matches:
    raise ValueError(f"Missing columns in Arsenal matches: {missing_matches}")

# Do not trust existing row order. Rebuild final league position from table rules.
table = table.sort_values(
    ["Pts", "GD", "GF"],
    ascending=[False, False, False]
).reset_index(drop=True)

table["FinalPosition"] = table.index + 1

# Top 10 finishers excluding Arsenal = 9 opponents.
top10 = table[(table["FinalPosition"] <= 10) & (table["Team"] != "Arsenal")].copy()

team_name_map = {
    "Man City": "Manchester City",
    "Man United": "Manchester United",
    "Bournemouth": "AFC Bournemouth",
    "Brighton": "Brighton & Hove Albion",
}

top10["Opponent"] = top10["Team"].replace(team_name_map)

summary = []

for _, team in top10.iterrows():
    opponent = team["Opponent"]
    subset = matches[matches["Opponent"] == opponent].copy()

    summary.append({
        "FinalPosition": int(team["FinalPosition"]),
        "Opponent": opponent,
        "TableName": team["Team"],
        "P": len(subset),
        "W": int((subset["Result"] == "W").sum()),
        "D": int((subset["Result"] == "D").sum()),
        "L": int((subset["Result"] == "L").sum()),
        "GF": int(subset["GF"].sum()),
        "GA": int(subset["GA"].sum()),
        "GD": int(subset["GF"].sum() - subset["GA"].sum()),
        "Points": int(subset["Points"].sum()),
    })

out = pd.DataFrame(summary).sort_values("FinalPosition", ascending=True)

expected = {
    "Manchester City",
    "Manchester United",
    "Aston Villa",
    "Liverpool",
    "AFC Bournemouth",
    "Sunderland",
    "Brighton & Hove Albion",
    "Brentford",
    "Chelsea",
}

actual = set(out["Opponent"])

if actual != expected:
    raise ValueError(
        "Top 10 opponent QA failed.\n"
        f"Missing: {sorted(expected - actual)}\n"
        f"Unexpected: {sorted(actual - expected)}\n"
        f"Actual: {sorted(actual)}"
    )

bad_p = out[out["P"] != 2]

if not bad_p.empty:
    raise ValueError(
        "Match count QA failed. Every opponent should have P = 2.\n"
        f"{bad_p[['Opponent', 'P']].to_string(index=False)}"
    )

out.to_csv(OUTPUT_FILE, index=False)

print("Created Arsenal vs top 10 dataset")
print(out.to_string(index=False))
print(f"\nSaved: {OUTPUT_FILE}")