"""
Clinical CSV Cleaner (v1)
Reads a messy clinical CSV and prints a short data-quality report.
"""

import pandas as pd

CSV_PATH = "sample_data.csv"


def main():
    df = pd.read_csv(CSV_PATH)

    print("=" * 50)
    print("CLINICAL CSV QUALITY REPORT")
    print("=" * 50)
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print()

    print("-" * 50)
    print("MISSING VALUES PER COLUMN")
    print("-" * 50)
    print(df.isnull().sum())
    print()

    print("-" * 50)
    print("ROWS WITH MISSING bp_systolic")
    print("-" * 50)
    missing_bp = df[df["bp_systolic"].isnull()]
    if missing_bp.empty:
        print("(none)")
    else:
        print(missing_bp)
    print()

    sex_map = {
        "M": "M", "Male": "M", "male": "M",
        "F": "F", "Female": "F", "f": "F", "female": "F",
    }
    df["sex"] = df["sex"].map(sex_map).fillna(df["sex"])

    print("-" * 50)
    print("CLEANED SEX COLUMN")
    print("-" * 50)
    print(df["sex"])
    print("=" * 50)


if __name__ == "__main__":
    main()
