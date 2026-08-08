import os
import pandas as pd

from python.analytics.database_loader import load_table


# ============================================================
# DATE CONVERSION
# ============================================================

def convert_date_columns(df, columns):
    """
    Converts specified columns into Pandas datetime format.
    """

    for column in columns:

        if column in df.columns:

            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    return df


# ============================================================
# DATE VALIDATION
# ============================================================

def validate_dates(df, columns):
    """
    Checks whether date conversion created
    invalid or missing dates.
    """

    for column in columns:

        if column in df.columns:

            invalid_dates = df[column].isna().sum()

            print(
                f"{column}: "
                f"{invalid_dates} invalid/missing dates"
            )


# ============================================================
# DUPLICATE REMOVAL
# ============================================================

def remove_duplicates(df):
    """
    Removes completely duplicated rows.
    """

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(
        f"Duplicates removed: {before - after}"
    )

    return df


# ============================================================
# USERS CLEANING
# ============================================================

def clean_users(df):

    date_columns = [
        "date_of_birth",
        "signup_date"
    ]

    df = convert_date_columns(
        df,
        date_columns
    )

    validate_dates(
        df,
        date_columns
    )

    df = remove_duplicates(df)

    return df


# ============================================================
# ALBUMS CLEANING
# ============================================================

def clean_albums(df):

    date_columns = [
        "release_date"
    ]

    df = convert_date_columns(
        df,
        date_columns
    )

    validate_dates(
        df,
        date_columns
    )

    df = remove_duplicates(df)

    return df


# ============================================================
# PAYMENTS CLEANING
# ============================================================

def clean_payments(df):

    date_columns = [
        "payment_date"
    ]

    df = convert_date_columns(
        df,
        date_columns
    )

    validate_dates(
        df,
        date_columns
    )

    df = remove_duplicates(df)

    return df


# ============================================================
# SESSIONS CLEANING
# ============================================================

def clean_sessions(df):

    date_columns = [
        "login_time",
        "logout_time"
    ]

    df = convert_date_columns(
        df,
        date_columns
    )

    validate_dates(
        df,
        date_columns
    )

    df = remove_duplicates(df)

    return df


# ============================================================
# LISTENING HISTORY CLEANING
# ============================================================

def clean_listening_history(df):

    date_columns = [
        "played_at"
    ]

    df = convert_date_columns(
        df,
        date_columns
    )

    validate_dates(
        df,
        date_columns
    )

    df = remove_duplicates(df)

    return df


# ============================================================
# USERS VALIDATION
# ============================================================

def validate_users(df):

    print("\n--- USERS VALIDATION ---")

    print(
        "Null user IDs:",
        df["user_id"].isna().sum()
    )

    print(
        "Duplicate user IDs:",
        df["user_id"].duplicated().sum()
    )

    print(
        "Invalid subscription IDs:",
        (df["subscription_id"] <= 0).sum()
    )


# ============================================================
# SONGS VALIDATION
# ============================================================

def validate_songs(df):

    print("\n--- SONGS VALIDATION ---")

    print(
        "Null song IDs:",
        df["song_id"].isna().sum()
    )

    print(
        "Duplicate song IDs:",
        df["song_id"].duplicated().sum()
    )

    print(
        "Invalid duration:",
        (df["duration_seconds"] <= 0).sum()
    )


# ============================================================
# SESSIONS VALIDATION
# ============================================================

def validate_sessions(df):

    print("\n--- SESSIONS VALIDATION ---")

    print(
        "Null session IDs:",
        df["session_id"].isna().sum()
    )

    print(
        "Duplicate session IDs:",
        df["session_id"].duplicated().sum()
    )

    print(
        "Invalid session duration:",
        (df["session_duration_minutes"] <= 0).sum()
    )


# ============================================================
# LISTENING HISTORY VALIDATION
# ============================================================

def validate_listening_history(df):

    print("\n--- LISTENING HISTORY VALIDATION ---")

    print(
        "Null history IDs:",
        df["history_id"].isna().sum()
    )

    print(
        "Duplicate history IDs:",
        df["history_id"].duplicated().sum()
    )

    print(
        "Invalid listening duration:",
        (df["listening_duration_seconds"] <= 0).sum()
    )


# ============================================================
# PAYMENTS VALIDATION
# ============================================================

def validate_payments(df):

    print("\n--- PAYMENTS VALIDATION ---")

    print(
        "Null payment IDs:",
        df["payment_id"].isna().sum()
    )

    print(
        "Duplicate payment IDs:",
        df["payment_id"].duplicated().sum()
    )

    print(
        "Negative amounts:",
        (df["amount"] < 0).sum()
    )


# ============================================================
# SAVE CLEANED DATA
# ============================================================

def save_cleaned_data(df, table_name):
    """
    Saves cleaned DataFrame as a CSV file.
    """

    output_directory = "data/cleaned"

    os.makedirs(
        output_directory,
        exist_ok=True
    )

    file_path = (
        f"{output_directory}/"
        f"{table_name}_cleaned.csv"
    )

    df.to_csv(
        file_path,
        index=False
    )

    print(
        f"✅ Saved: {file_path}"
    )


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print(
        "\n========== DATA CLEANING STARTED =========="
    )

    # --------------------------------------------------------
    # USERS
    # --------------------------------------------------------

    users_df = load_table("users")

    users_df = clean_users(
        users_df
    )

    validate_users(
        users_df
    )

    save_cleaned_data(
        users_df,
        "users"
    )

    # --------------------------------------------------------
    # ALBUMS
    # --------------------------------------------------------

    albums_df = load_table("albums")

    albums_df = clean_albums(
        albums_df
    )

    save_cleaned_data(
        albums_df,
        "albums"
    )

    # --------------------------------------------------------
    # SONGS
    # --------------------------------------------------------

    songs_df = load_table("songs")

    validate_songs(
        songs_df
    )

    save_cleaned_data(
        songs_df,
        "songs"
    )

    # --------------------------------------------------------
    # PAYMENTS
    # --------------------------------------------------------

    payments_df = load_table("payments")

    payments_df = clean_payments(
        payments_df
    )

    validate_payments(
        payments_df
    )

    save_cleaned_data(
        payments_df,
        "payments"
    )

    # --------------------------------------------------------
    # SESSIONS
    # --------------------------------------------------------

    sessions_df = load_table("sessions")

    sessions_df = clean_sessions(
        sessions_df
    )

    validate_sessions(
        sessions_df
    )

    save_cleaned_data(
        sessions_df,
        "sessions"
    )

    # --------------------------------------------------------
    # LISTENING HISTORY
    # --------------------------------------------------------

    listening_history_df = load_table(
        "listening_history"
    )

    listening_history_df = clean_listening_history(
        listening_history_df
    )

    validate_listening_history(
        listening_history_df
    )

    save_cleaned_data(
        listening_history_df,
        "listening_history"
    )

    print(
        "\n========== DATA CLEANING COMPLETED =========="
    )