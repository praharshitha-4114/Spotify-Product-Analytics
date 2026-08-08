import random

from faker import Faker
from tqdm import tqdm

from python.data_generation.database_connection import get_connection
from python.Utils.database_helper import fetch_ids

fake = Faker()

NUMBER_OF_PAYMENTS = 5000
BATCH_SIZE = 1000

PAYMENT_METHODS = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "PayPal",
    "Net Banking"
]

PAYMENT_STATUS = [
    "SUCCESS",
    "FAILED",
    "PENDING"
]

# Subscription Prices
PLAN_PRICES = {
    1: 0.00,     # Free
    2: 9.99,     # Individual
    3: 14.99,    # Duo
    4: 16.99,    # Family
    5: 5.99      # Student
}

print("=" * 50)
print("Spotify Payment Generator Started")
print("=" * 50)

connection = get_connection()
cursor = connection.cursor()

user_ids = fetch_ids("users", "user_id")
subscription_ids = fetch_ids("subscriptions", "subscription_id")

records = []

for _ in tqdm(range(NUMBER_OF_PAYMENTS)):

    subscription_id = random.choice(subscription_ids)

    user_id = random.choice(user_ids)

    amount = PLAN_PRICES[subscription_id]

    payment_date = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    payment_method = random.choice(PAYMENT_METHODS)

    payment_status = random.choices(
        PAYMENT_STATUS,
        weights=[90, 5, 5]
    )[0]

    records.append(
        (
            user_id,
            subscription_id,
            amount,
            payment_date,
            payment_method,
            payment_status
        )
    )

    if len(records) == BATCH_SIZE:

        cursor.executemany(
            """
            INSERT INTO payments
            (
                user_id,
                subscription_id,
                amount,
                payment_date,
                payment_method,
                payment_status
            )

            VALUES(%s,%s,%s,%s,%s,%s)
            """,
            records
        )

        connection.commit()

        records.clear()

if records:

    cursor.executemany(
        """
        INSERT INTO payments
        (
            user_id,
            subscription_id,
            amount,
            payment_date,
            payment_method,
            payment_status
        )

        VALUES(%s,%s,%s,%s,%s,%s)
        """,
        records
    )

    connection.commit()

cursor.close()
connection.close()

print()
print(f"✅ {NUMBER_OF_PAYMENTS} Payments Generated Successfully!")