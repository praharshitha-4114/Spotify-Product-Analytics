import random
from datetime import timedelta

from faker import Faker
from tqdm import tqdm

from python.data_generation.database_connection import get_connection
from python.Utils.database_helper import fetch_ids

fake = Faker()

NUMBER_OF_SESSIONS = 50000

print("=" * 45)
print("Spotify Session Generator Started")
print("=" * 45)

connection = get_connection()
cursor = connection.cursor()

user_ids = fetch_ids("users", "user_id")
device_ids = fetch_ids("devices", "device_id")

for _ in tqdm(range(NUMBER_OF_SESSIONS)):

    user_id = random.choice(user_ids)

    device_id = random.choice(device_ids)

    login_time = fake.date_time_between(
        start_date="-2y",
        end_date="now"
    )

    duration = random.randint(5, 240)

    logout_time = login_time + timedelta(minutes=duration)

    cursor.execute(
        """
        INSERT INTO sessions
        (
            user_id,
            device_id,
            login_time,
            logout_time,
            session_duration_minutes
        )

        VALUES (%s,%s,%s,%s,%s)
        """,
        (
            user_id,
            device_id,
            login_time,
            logout_time,
            duration
        )
    )

connection.commit()

cursor.close()
connection.close()

print()
print(f"✅ {NUMBER_OF_SESSIONS} Sessions Generated Successfully!")