import pandas as pd
from pathlib import Path

DATA = Path("data")

ARSENAL_MATCHES = DATA / "arsenal_2025_26_matches.csv"
FINAL_TABLE = DATA / "premier_league_final_table.csv"

# Output files
RIVALS_OUT = DATA / "arsenal_vs_contenders.csv"
GA_OUT = DATA / "goals_against_by_team.csv"
MONTHLY_OUT = DATA / "arsenal_monthly_form.csv"

# -----------------------------
# Load data
# -----------------------------
ars = pd.read_csv(ARSENAL_MATCHES)
table = pd.read_csv(FINAL_TABLE)

# -----------------------------
# Dataset A: Arsenal vs contenders
# -----------------------------
contenders = [
    "Manchester City",
    "Manchester United",
    "Aston Villa",
    "Liverpool",
    "Chelsea",
    "Newcastle United",
]

rival_matches = ars[ars["Opponent"].isin(contenders)].copy()

summary = []

for team in contenders:
    subset = rival_matches[rival_matches["Opponent"] == team]

    summary.append({
        "Opponent": team,
        "P": len(subset),
        "W": (subset["Result"] == "W").sum(),
        "D": (subset["Result"] == "D").sum(),
        "L": (subset["Result"] == "L").sum(),
        "GF": subset["GF"].sum(),
        "GA": subset["GA"].sum(),
        "GD": subset["GF"].sum() - subset["GA"].sum(),
        "Points": subset["Points"].sum(),
    })

contenders_df = pd.DataFrame(summary).sort_values(
    ["Points", "GD", "GF"],
    ascending=False
)

contenders_df.to_csv(RIVALS_OUT, index=False)

# -----------------------------
# Dataset B: Goals against by team
# -----------------------------
ga_df = table[["Team", "P", "GA"]].copy()
ga_df["GA_per_game"] = (ga_df["GA"] / ga_df["P"]).round(2)
ga_df = ga_df.sort_values(["GA", "GA_per_game"], ascending=True)

ga_df.to_csv(GA_OUT, index=False)

# -----------------------------
# Dataset C: Arsenal monthly form
# -----------------------------
ars["Date"] = pd.to_datetime(ars["Date"])
ars["Month"] = ars["Date"].dt.strftime("%Y-%m")

monthly = ars.groupby("Month").agg(
    P=("Matchweek", "count"),
    W=("Result", lambda x: (x == "W").sum()),
    D=("Result", lambda x: (x == "D").sum()),
    L=("Result", lambda x: (x == "L").sum()),
    GF=("GF", "sum"),
    GA=("GA", "sum"),
    GD=("GoalDifference", "sum"),
    Points=("Points", "sum"),
    CleanSheets=("CleanSheet", "sum"),
).reset_index()

monthly["PPG"] = (monthly["Points"] / monthly["P"]).round(2)

monthly.to_csv(MONTHLY_OUT, index=False)

# -----------------------------
# QA output
# -----------------------------
print("\nCreated datasets:")
print(f"- {RIVALS_OUT}")
print(f"- {GA_OUT}")
print(f"- {MONTHLY_OUT}")

print("\nArsenal season QA:")
print("Matches:", len(ars))
print("Points:", ars["Points"].sum())
print("GF:", ars["GF"].sum())
print("GA:", ars["GA"].sum())
print("Clean sheets:", ars["CleanSheet"].sum())

print("\nContenders dataset:")
print(contenders_df)

print("\nGoals against dataset:")
print(ga_df.head(10))

print("\nMonthly form dataset:")
print(monthly)