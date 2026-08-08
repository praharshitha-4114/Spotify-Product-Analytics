import random
from faker import Faker
from tqdm import tqdm

from python.data_generation.database_connection import get_connection

fake = Faker()

NUMBER_OF_ALBUMS = 600

connection = get_connection()

cursor = connection.cursor()

print("===================================")
print("Spotify Album Generator Started")
print("===================================")

for _ in tqdm(range(NUMBER_OF_ALBUMS)):

    artist_id = random.randint(1,200)

    album_name = fake.unique.catch_phrase()

    release_date = fake.date_between(
        start_date="-20y",
        end_date="today"
    )

    total_tracks = random.randint(6,20)

    cursor.execute(
        """
        INSERT INTO albums
        (
            artist_id,
            album_name,
            release_date,
            total_tracks
        )

        VALUES(%s,%s,%s,%s)
        """,
        (
            artist_id,
            album_name,
            release_date,
            total_tracks
        )
    )

connection.commit()

cursor.close()

connection.close()

print()
print("====================================")
print(f"✅ {NUMBER_OF_ALBUMS} Albums Generated Successfully!")
print("====================================")