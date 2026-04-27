from pathlib import Path
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = REPO_ROOT / "data" / "uk-mean-temperature.csv"
OUTPUT_FILE = REPO_ROOT / "data" / "uk_mean_temperature_top20.csv"

TEMP_COL = "Annual mean temperature (°C)"
YEAR_COL = "Year"

def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)

    print("Loaded file:", INPUT_FILE)
    print("Columns found:", list(df.columns))

    required = [YEAR_COL, TEMP_COL]
    missing = [c for c in required if c not in df.columns]

    if missing:
        raise ValueError(
            f"Missing column(s): {missing}\n"
            f"Available columns: {list(df.columns)}"
        )

    df[TEMP_COL] = pd.to_numeric(df[TEMP_COL], errors="coerce")

    top20 = (
        df.dropna(subset=[TEMP_COL])
          .sort_values(TEMP_COL, ascending=False)
          .head(20)
          .copy()
    )

    top20.insert(0, "Rank", range(1, len(top20) + 1))

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    top20.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved: {OUTPUT_FILE}")
    print(top20.to_csv(index=False))


if __name__ == "__main__":
    main()