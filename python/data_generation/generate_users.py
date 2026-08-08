import random
from faker import Faker

from python.data_generation.database_connection import get_connection

# ==========================================
# Configuration
# ==========================================

NUMBER_OF_USERS = 10

fake = Faker()

# ==========================================
# Main Program
# ==========================================

print("====================================")
print("Spotify User Data Generator Started")
print("====================================")
print()

connection = get_connection()
cursor = connection.cursor()

print(f"Generating {NUMBER_OF_USERS} users...")
print()

for _ in range(NUMBER_OF_USERS):

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.unique.email()
    gender = random.choice(["Male", "Female"])

    date_of_birth = fake.date_of_birth(
        minimum_age=18,
        maximum_age=60
    )

    country = fake.country()
    city = fake.city()

    signup_date = fake.date_between(
        start_date="-3y",
        end_date="today"
    )

    subscription_id = random.randint(1, 5)

    cursor.execute(
        """
        INSERT INTO users
        (
            first_name,
            last_name,
            email,
            gender,
            date_of_birth,
            country,
            city,
            signup_date,
            subscription_id
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            first_name,
            last_name,
            email,
            gender,
            date_of_birth,
            country,
            city,
            signup_date,
            subscription_id
        )
    )

print("Saving data to PostgreSQL...")
connection.commit()

cursor.close()
connection.close()

print()
print("====================================")
print(f"✅ {NUMBER_OF_USERS} Users Generated Successfully!")
print("====================================")