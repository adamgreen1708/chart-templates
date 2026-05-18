import pandas as pd
from pathlib import Path

input_file = "data/scotch_whisky_flavour_quadrants.csv"
output_dir = Path("data/region_quadrants")
output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_file)

regions = sorted(df["Region"].dropna().unique())

for region in regions:
    safe_region = (
        region.lower()
        .replace(" ", "_")
        .replace("/", "_")
    )

    out = df[df["Region"] == region].copy()

    output_file = output_dir / f"scotch_whisky_quadrants_{safe_region}.csv"
    out.to_csv(output_file, index=False)

    print(f"Saved {output_file} ({len(out)} rows)")