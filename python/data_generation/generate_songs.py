import random

from tqdm import tqdm

from python.data_generation.database_connection import get_connection
from python.Utils.database_helper import fetch_ids
from python.Utils.random_generator import (
    random_genre,
    random_language,
    random_song
)

NUMBER_OF_SONGS = 8000

print("====================================")
print("Spotify Song Generator Started")
print("====================================")

connection = get_connection()
cursor = connection.cursor()

# Fetch all valid album IDs
album_ids = fetch_ids("albums", "album_id")

for _ in tqdm(range(NUMBER_OF_SONGS)):

    album_id = random.choice(album_ids)

    song_name = random_song()

    genre = random_genre()

    language = random_language()

    duration_seconds = random.randint(120, 360)

    explicit = random.choice([True, False])

    cursor.execute(
        """
        INSERT INTO songs
        (
            album_id,
            song_name,
            genre,
            duration_seconds,
            language,
            explicit
        )

        VALUES (%s,%s,%s,%s,%s,%s)
        """,
        (
            album_id,
            song_name,
            genre,
            duration_seconds,
            language,
            explicit
        )
    )

print()
print("Saving songs...")

connection.commit()

cursor.close()
connection.close()

print()
print(f"✅ {NUMBER_OF_SONGS} Songs Generated Successfully!")