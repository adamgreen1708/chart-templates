import pandas as pd

df = pd.read_csv("data/scotch_whisky_flavours_enriched.csv")

# Region mapping
region_map = {
    # Islay
    "Ardbeg": "Islay",
    "Bowmore": "Islay",
    "Bruichladdich": "Islay",
    "Bunnahabhain": "Islay",
    "Caol Ila": "Islay",
    "Lagavulin": "Islay",
    "Laphroig": "Islay",

    # Campbeltown
    "Glen Scotia": "Campbeltown",
    "Springbank": "Campbeltown",

    # Lowlands
    "Auchentoshan": "Lowlands",
    "Bladnoch": "Lowlands",
    "Glenkinchie": "Lowlands",

    # Islands
    "ArranIsleOf": "Islands",
    "Highland Park": "Islands",
    "Isle of Jura": "Islands",
    "OldPulteney": "Islands",
    "Scapa": "Islands",
    "Talisker": "Islands",
    "Tobermory": "Islands",

    # Speyside
    "Aberlour": "Speyside",
    "Balvenie": "Speyside",
    "Benriach": "Speyside",
    "Benrinnes": "Speyside",
    "Cardhu": "Speyside",
    "Craigallechie": "Speyside",
    "Craigganmore": "Speyside",
    "Dufftown": "Speyside",
    "GlenAllachie": "Speyside",
    "GlenElgin": "Speyside",
    "Glenfarclas": "Speyside",
    "Glenfiddich": "Speyside",
    "Glenlivet": "Speyside",
    "Glenlossie": "Speyside",
    "Glenrothes": "Speyside",
    "Linkwood": "Speyside",
    "Longmorn": "Speyside",
    "Macallan": "Speyside",
    "Mortlach": "Speyside",
    "Speyburn": "Speyside",
    "Strathisla": "Speyside",
    "Tamdhu": "Speyside",
    "Tomintoul": "Speyside",

    # Everything else defaults Highlands
}

df["Region"] = df["Distillery"].map(region_map)
df["Region"] = df["Region"].fillna("Highlands")

df.to_csv("data/scotch_whisky_flavours_with_regions.csv", index=False)

print(df[["Distillery", "Region"]].head(20))
print("Saved: data/scotch_whisky_flavours_with_regions.csv")