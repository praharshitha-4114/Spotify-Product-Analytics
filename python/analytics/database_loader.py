import pandas as pd
from sqlalchemy import create_engine

from python.config import (
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT
)


def get_engine():
    """
    Creates and returns a SQLAlchemy PostgreSQL engine.
    """

    database_url = (
        f"postgresql+psycopg2://"
        f"{DB_USER}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/"
        f"{DB_NAME}"
    )

    engine = create_engine(database_url)

    return engine


def load_table(table_name):
    """
    Loads a PostgreSQL table into a Pandas DataFrame.
    """

    engine = get_engine()

    try:
        query = f"SELECT * FROM {table_name}"

        dataframe = pd.read_sql_query(
            query,
            engine
        )

        return dataframe

    finally:
        engine.dispose()

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

    dataframes = {}

    for table in tables:

        print(f"\nLoading table: {table}")

        df = load_table(table)

        dataframes[table] = df

        print(f"✅ {table} loaded successfully")
        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}")