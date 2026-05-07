import pandas as pd

BASE_FILE = "data/snooker_world_championship_winners.csv"

df = pd.read_csv(BASE_FILE)

# -------------------------
# 1. Titles by player
# -------------------------
titles = (
    df.groupby("winner", as_index=False)
    .size()
    .rename(columns={"size": "titles"})
    .sort_values("titles", ascending=False)
)

titles.to_csv("data/snooker_world_titles_by_player.csv", index=False)

# -------------------------
# 2. UK vs International cumulative titles
# -------------------------
uk_codes = {"ENG", "SCO", "WAL", "NIR"}

df["group"] = df["winner_country"].apply(
    lambda x: "UK" if x in uk_codes else "International"
)

yearly = (
    df.groupby(["year", "group"], as_index=False)
    .size()
    .rename(columns={"size": "titles"})
)

all_years = pd.DataFrame({"year": sorted(df["year"].unique())})
groups = pd.DataFrame({"group": ["UK", "International"]})

grid = all_years.merge(groups, how="cross")

yearly_full = (
    grid.merge(yearly, on=["year", "group"], how="left")
    .fillna({"titles": 0})
    .sort_values(["group", "year"])
)

yearly_full["cumulative_titles"] = yearly_full.groupby("group")["titles"].cumsum()

yearly_full.to_csv("data/snooker_crucible_uk_vs_world.csv", index=False)

print("Created:")
print("data/snooker_world_titles_by_player.csv")
print("data/snooker_crucible_uk_vs_world.csv")