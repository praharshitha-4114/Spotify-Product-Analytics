import random
from faker import Faker
from tqdm import tqdm

from python.data_generation.database_connection import get_connection

fake = Faker()

NUMBER_OF_ARTISTS = 200

connection = get_connection()
cursor = connection.cursor()

print("===================================")
print("Spotify Artist Generator Started")
print("===================================")

for _ in tqdm(range(NUMBER_OF_ARTISTS)):

    artist_name = fake.unique.name()

    country = random.choice([
        "India",
        "USA",
        "United Kingdom",
        "Canada",
        "Australia",
        "Germany",
        "France",
        "Japan",
        "South Korea"
    ])

    debut_year = random.randint(1985,2025)

    monthly_listeners = random.randint(
        500000,
        120000000
    )

    cursor.execute(
        """
        INSERT INTO artists
        (
            artist_name,
            country,
            debut_year,
            monthly_listeners
        )

        VALUES(%s,%s,%s,%s)
        """,
        (
            artist_name,
            country,
            debut_year,
            monthly_listeners
        )
    )

connection.commit()

cursor.close()
connection.close()

print("====================================")
print(f"✅ {NUMBER_OF_ARTISTS} Artists Generated Successfully!")
print("====================================")