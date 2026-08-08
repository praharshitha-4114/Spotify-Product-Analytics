from python.analytics.database_loader import load_table
import pandas as pd

def explore_table(table_name):

    print("\n" + "=" * 60)
    print(f"DATA EXPLORATION: {table_name.upper()}")
    print("=" * 60)

    df = load_table(table_name)

    print("\n--- First 5 Records ---")
    print(df.head().to_string(index=False))

    print("\n--- Shape ---")
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\n--- Column Names ---")
    print(df.columns.tolist())

    print("\n--- Data Types ---")
    print(df.dtypes)

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    print("\n--- Duplicate Rows ---")
    print(df.duplicated().sum())

    print("\n--- Unique Values ---")
    print(df.nunique())

    return df

def generate_profile(df, table_name):

    profile = pd.DataFrame({
        "column": df.columns,
        "data_type": df.dtypes.astype(str).values,
        "missing_values": df.isnull().sum().values,
        "unique_values": df.nunique().values
    })

    profile["missing_percentage"] = (
        profile["missing_values"] / len(df) * 100
    ).round(2)

    print(f"\n===== PROFILE SUMMARY: {table_name.upper()} =====")
    print(profile.to_string(index=False))

    return profile

if __name__ == "__main__":

    tables = [
        "users",
        "artists",
        "albums",
        "songs",
        "subscriptions",
        "devices",
        "sessions",
        "listening_history",
        "payments"
    ]

    for table in tables:
        df = explore_table(table)
        generate_profile(df, table)