from python.data_generation.database_connection import get_connection


def fetch_ids(table_name, column_name):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f"SELECT {column_name} FROM {table_name}")

    ids = [row[0] for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return ids