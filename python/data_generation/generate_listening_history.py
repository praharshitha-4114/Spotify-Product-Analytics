import random

from faker import Faker
from tqdm import tqdm

from python.data_generation.database_connection import get_connection
from python.Utils.database_helper import fetch_ids

fake = Faker()

NUMBER_OF_RECORDS = 300000
BATCH_SIZE = 5000

print("=" * 50)
print("Spotify Listening History Generator")
print("=" * 50)

connection = get_connection()
cursor = connection.cursor()

user_ids = fetch_ids("users", "user_id")
song_ids = fetch_ids("songs", "song_id")
session_ids = fetch_ids("sessions", "session_id")

records = []

for _ in tqdm(range(NUMBER_OF_RECORDS)):

    user_id = random.choice(user_ids)

    song_id = random.choice(song_ids)

    session_id = random.choice(session_ids)

    played_at = fake.date_time_between(
        start_date="-2y",
        end_date="now"
    )

    listening_duration = random.randint(20, 300)

    completed = random.random() < 0.75

    skipped = not completed

    records.append(
        (
            user_id,
            song_id,
            session_id,
            played_at,
            listening_duration,
            completed,
            skipped
        )
    )

    if len(records) == BATCH_SIZE:

        cursor.executemany(
            """
            INSERT INTO listening_history
            (
                user_id,
                song_id,
                session_id,
                played_at,
                listening_duration_seconds,
                completed,
                skipped
            )

            VALUES (%s,%s,%s,%s,%s,%s,%s)
            """,
            records
        )

        connection.commit()
        records.clear()

if records:

    cursor.executemany(
        """
        INSERT INTO listening_history
        (
            user_id,
            song_id,
            session_id,
            played_at,
            listening_duration_seconds,
            completed,
            skipped
        )

        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """,
        records
    )

    connection.commit()

cursor.close()
connection.close()

print()
print(f"✅ {NUMBER_OF_RECORDS} Listening Records Generated Successfully!")