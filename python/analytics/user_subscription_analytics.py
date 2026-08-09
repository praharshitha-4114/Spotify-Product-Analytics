import os
import pandas as pd

from python.analytics.database_loader import load_table

from python.analytics.data_cleaning import (
    clean_users,
    clean_payments,
    clean_sessions
)


# ============================================================
# LOAD ANALYTICS DATA
# ============================================================

def load_analytics_data():

    users_df = load_table("users")
    subscriptions_df = load_table("subscriptions")
    payments_df = load_table("payments")
    sessions_df = load_table("sessions")

    users_df = clean_users(users_df)
    payments_df = clean_payments(payments_df)
    sessions_df = clean_sessions(sessions_df)

    return (
        users_df,
        subscriptions_df,
        payments_df,
        sessions_df
    )


# ============================================================
# USER ANALYTICS
# ============================================================

def calculate_total_users(users_df):

    return users_df["user_id"].nunique()


def users_by_country(users_df):

    result = (
        users_df
        .groupby("country")["user_id"]
        .nunique()
        .sort_values(ascending=False)
    )

    return result


def users_by_gender(users_df):

    result = (
        users_df
        .groupby("gender")["user_id"]
        .nunique()
        .sort_values(ascending=False)
    )

    return result


# ============================================================
# SUBSCRIPTION ANALYTICS
# ============================================================

def users_by_subscription(
    users_df,
    subscriptions_df
):

    merged_df = users_df.merge(
        subscriptions_df,
        on="subscription_id",
        how="left"
    )

    result = (
        merged_df
        .groupby("plan_name")["user_id"]
        .nunique()
        .sort_values(ascending=False)
    )

    return result


def revenue_by_subscription(
    users_df,
    subscriptions_df,
    payments_df
):

    users_subscription = users_df.merge(
        subscriptions_df,
        on="subscription_id",
        how="left"
    )

    payment_data = users_subscription.merge(
        payments_df,
        on="user_id",
        how="left"
    )

    result = (
        payment_data
        .groupby("plan_name")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    return result


# ============================================================
# PAYMENT ANALYTICS
# ============================================================

def calculate_total_revenue(payments_df):

    return payments_df["amount"].sum()


def calculate_average_payment(payments_df):

    return payments_df["amount"].mean()


def revenue_by_payment_method(payments_df):

    result = (
        payments_df
        .groupby("payment_method")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    return result


def payment_status_distribution(payments_df):

    result = (
        payments_df
        .groupby("payment_status")["payment_id"]
        .count()
        .sort_values(ascending=False)
    )

    return result


def successful_revenue(payments_df):

    successful_payments = payments_df[
        payments_df["payment_status"] == "Success"
    ]

    return successful_payments["amount"].sum()


def payment_success_rate(payments_df):

    total_payments = len(payments_df)

    successful_payments = (
        payments_df["payment_status"] == "Success"
    ).sum()

    if total_payments == 0:
        return 0

    return (
        successful_payments /
        total_payments
    ) * 100


def revenue_per_user(payments_df):

    result = (
        payments_df
        .groupby("user_id")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    return result


def calculate_average_revenue_per_user(
    payments_df
):

    revenue_by_user = (
        payments_df
        .groupby("user_id")["amount"]
        .sum()
    )

    return revenue_by_user.mean()


# ============================================================
# SESSION ANALYTICS
# ============================================================

def calculate_total_sessions(sessions_df):

    return sessions_df["session_id"].nunique()


def calculate_average_session_duration(
    sessions_df
):

    return sessions_df[
        "session_duration_minutes"
    ].mean()


def sessions_per_user(sessions_df):

    result = (
        sessions_df
        .groupby("user_id")["session_id"]
        .nunique()
        .sort_values(ascending=False)
    )

    return result


def calculate_average_sessions_per_user(
    sessions_df
):

    user_session_counts = (
        sessions_df
        .groupby("user_id")["session_id"]
        .nunique()
    )

    return user_session_counts.mean()


def calculate_active_users(sessions_df):

    return sessions_df["user_id"].nunique()


def calculate_user_activity_rate(
    users_df,
    sessions_df
):

    total_users = users_df["user_id"].nunique()

    active_users = sessions_df["user_id"].nunique()

    if total_users == 0:
        return 0

    return (
        active_users /
        total_users
    ) * 100


# ============================================================
# KPI SUMMARY
# ============================================================

def create_kpi_summary(
    users_df,
    payments_df,
    sessions_df
):

    total_users = users_df["user_id"].nunique()

    active_users = sessions_df["user_id"].nunique()

    total_revenue = payments_df["amount"].sum()

    average_payment = payments_df["amount"].mean()

    total_sessions = sessions_df["session_id"].nunique()

    average_session_duration = (
        sessions_df["session_duration_minutes"].mean()
    )

    success_rate = payment_success_rate(
        payments_df
    )

    if total_users == 0:
        activity_rate = 0
    else:
        activity_rate = (
            active_users / total_users
        ) * 100

    kpi_data = {
        "KPI": [
            "Total Users",
            "Active Users",
            "User Activity Rate",
            "Total Revenue",
            "Average Payment",
            "Total Sessions",
            "Average Session Duration",
            "Payment Success Rate"
        ],

        "Value": [
            total_users,
            active_users,
            round(activity_rate, 2),
            round(total_revenue, 2),
            round(average_payment, 2),
            total_sessions,
            round(average_session_duration, 2),
            round(success_rate, 2)
        ]
    }

    return pd.DataFrame(kpi_data)


# ============================================================
# SAVE KPI SUMMARY
# ============================================================

def save_kpi_summary(kpi_summary):

    output_directory = "data/analytics"

    os.makedirs(
        output_directory,
        exist_ok=True
    )

    file_path = (
        f"{output_directory}/"
        "user_subscription_kpis.csv"
    )

    kpi_summary.to_csv(
        file_path,
        index=False
    )

    print(
        f"\n✅ KPI summary saved to: {file_path}"
    )


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print(
        "\n========== "
        "USER & SUBSCRIPTION ANALYTICS "
        "=========="
    )

    # --------------------------------------------------------
    # LOAD DATA
    # --------------------------------------------------------

    (
        users_df,
        subscriptions_df,
        payments_df,
        sessions_df
    ) = load_analytics_data()

    # ========================================================
    # USER ANALYTICS
    # ========================================================

    total_users = calculate_total_users(
        users_df
    )

    print(
        f"\nTotal Users: {total_users}"
    )

    # Users by Country

    country_users = users_by_country(
        users_df
    )

    print("\n--- USERS BY COUNTRY ---")
    print(country_users)

    # Users by Gender

    gender_users = users_by_gender(
        users_df
    )

    print("\n--- USERS BY GENDER ---")
    print(gender_users)

    # ========================================================
    # SUBSCRIPTION ANALYTICS
    # ========================================================

    subscription_users = users_by_subscription(
        users_df,
        subscriptions_df
    )

    print(
        "\n--- USERS BY SUBSCRIPTION ---"
    )

    print(subscription_users)

    # Revenue by Subscription

    subscription_revenue = (
        revenue_by_subscription(
            users_df,
            subscriptions_df,
            payments_df
        )
    )

    print(
        "\n--- REVENUE BY SUBSCRIPTION ---"
    )

    print(subscription_revenue)

    # ========================================================
    # PAYMENT ANALYTICS
    # ========================================================

    total_revenue = calculate_total_revenue(
        payments_df
    )

    average_payment = calculate_average_payment(
        payments_df
    )

    print("\n--- PAYMENT ANALYTICS ---")

    print(
        f"Total Revenue: "
        f"{total_revenue:.2f}"
    )

    print(
        f"Average Payment: "
        f"{average_payment:.2f}"
    )

    # Revenue by Payment Method

    revenue_method = (
        revenue_by_payment_method(
            payments_df
        )
    )

    print(
        "\n--- REVENUE BY PAYMENT METHOD ---"
    )

    print(revenue_method)

    # Payment Status

    status_distribution = (
        payment_status_distribution(
            payments_df
        )
    )

    print(
        "\n--- PAYMENT STATUS DISTRIBUTION ---"
    )

    print(status_distribution)

    # Successful Revenue

    success_revenue = successful_revenue(
        payments_df
    )

    print(
        f"\nSuccessful Revenue: "
        f"{success_revenue:.2f}"
    )

    # Payment Success Rate

    success_rate = payment_success_rate(
        payments_df
    )

    print(
        f"Payment Success Rate: "
        f"{success_rate:.2f}%"
    )

    # ========================================================
    # SESSION ANALYTICS
    # ========================================================

    total_sessions = calculate_total_sessions(
        sessions_df
    )

    print(
        f"\nTotal Sessions: "
        f"{total_sessions}"
    )

    average_session_duration = (
        calculate_average_session_duration(
            sessions_df
        )
    )

    print(
        f"Average Session Duration: "
        f"{average_session_duration:.2f} minutes"
    )

    # Sessions per User

    user_sessions = sessions_per_user(
        sessions_df
    )

    print(
        "\n--- TOP 10 USERS BY SESSIONS ---"
    )

    print(
        user_sessions.head(10)
    )

    # Average Sessions per User

    average_sessions = (
        calculate_average_sessions_per_user(
            sessions_df
        )
    )

    print(
        f"\nAverage Sessions per User: "
        f"{average_sessions:.2f}"
    )

    # Active Users

    active_users = calculate_active_users(
        sessions_df
    )

    print(
        f"Active Users: "
        f"{active_users}"
    )

    # User Activity Rate

    activity_rate = (
        calculate_user_activity_rate(
            users_df,
            sessions_df
        )
    )

    print(
        f"User Activity Rate: "
        f"{activity_rate:.2f}%"
    )

    # ========================================================
    # USER REVENUE ANALYTICS
    # ========================================================

    user_revenue = revenue_per_user(
        payments_df
    )

    print(
        "\n--- TOP 10 USERS BY REVENUE ---"
    )

    print(
        user_revenue.head(10)
    )

    average_revenue_per_user = (
        calculate_average_revenue_per_user(
            payments_df
        )
    )

    print(
        f"\nAverage Revenue per Paying User: "
        f"{average_revenue_per_user:.2f}"
    )

    # ========================================================
    # KPI SUMMARY
    # ========================================================

    kpi_summary = create_kpi_summary(
        users_df,
        payments_df,
        sessions_df
    )

    print("\n--- KPI SUMMARY ---")

    print(
        kpi_summary.to_string(index=False)
    )

    # Save KPI Summary

    save_kpi_summary(
        kpi_summary
    )

    # ========================================================

    print(
        "\n========== "
        "ANALYTICS COMPLETED "
        "=========="
    )