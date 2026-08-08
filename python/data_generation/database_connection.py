import psycopg2

from python.config import (
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT
)


def get_connection():
    """
    Creates and returns a PostgreSQL database connection.
    """

    connection = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    return connection


if __name__ == "__main__":

    try:
        connection = get_connection()

        print("✅ Connected to PostgreSQL Successfully!")

        connection.close()

        print("🔒 Connection Closed.")

    except Exception as e:

        print("❌ Database Connection Failed!")
        print("Error:", e)