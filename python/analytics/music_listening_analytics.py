import pandas as pd

from python.analytics.database_loader import load_table

from python.analytics.data_cleaning import (
    clean_listening_history
)


# ============================================================
# LOAD MUSIC & LISTENING DATA
# ============================================================

def load_music_analytics_data():

    songs_df = load_table("songs")
    artists_df = load_table("artists")
    albums_df = load_table("albums")
    listening_history_df = load_table(
        "listening_history"
    )

    listening_history_df = clean_listening_history(
        listening_history_df
    )

    return (
        songs_df,
        artists_df,
        albums_df,
        listening_history_df
    )


# ============================================================
# BASIC MUSIC OVERVIEW
# ============================================================

def calculate_total_songs(songs_df):

    return songs_df["song_id"].nunique()


def calculate_total_artists(artists_df):

    return artists_df["artist_id"].nunique()


def calculate_total_albums(albums_df):

    return albums_df["album_id"].nunique()


def calculate_total_listening_records(
    listening_history_df
):

    return len(listening_history_df)


# ============================================================
# TOP SONGS
# ============================================================

def top_songs(
    listening_history_df,
    songs_df
):

    merged_df = listening_history_df.merge(
        songs_df,
        on="song_id",
        how="left"
    )

    result = (
        merged_df
        .groupby("song_name")["history_id"]
        .count()
        .sort_values(ascending=False)
    )

    return result


# ============================================================
# TOP ARTISTS
# ============================================================

def top_artists(
    listening_history_df,
    songs_df,
    albums_df,
    artists_df
):

    merged_df = listening_history_df.merge(
        songs_df,
        on="song_id",
        how="left"
    )

    merged_df = merged_df.merge(
        albums_df,
        on="album_id",
        how="left"
    )

    merged_df = merged_df.merge(
        artists_df,
        on="artist_id",
        how="left"
    )

    result = (
        merged_df
        .groupby("artist_name")["history_id"]
        .count()
        .sort_values(ascending=False)
    )

    return result


# ============================================================
# TOP ALBUMS
# ============================================================

def top_albums(
    listening_history_df,
    songs_df,
    albums_df
):

    merged_df = listening_history_df.merge(
        songs_df,
        on="song_id",
        how="left"
    )

    merged_df = merged_df.merge(
        albums_df,
        on="album_id",
        how="left"
    )

    result = (
        merged_df
        .groupby("album_name")["history_id"]
        .count()
        .sort_values(ascending=False)
    )

    return result


# ============================================================
# LISTENING BEHAVIOR
# ============================================================

def calculate_average_listening_duration(
    listening_history_df
):

    return listening_history_df[
        "listening_duration_seconds"
    ].mean()


def calculate_total_listening_duration(
    listening_history_df
):

    return listening_history_df[
        "listening_duration_seconds"
    ].sum()


# ============================================================
# COMPLETION RATE
# ============================================================

def calculate_completion_rate(
    listening_history_df
):

    total_records = len(
        listening_history_df
    )

    if total_records == 0:
        return 0

    completed_records = (
        listening_history_df["completed"] == True
    ).sum()

    return (
        completed_records /
        total_records
    ) * 100


# ============================================================
# SKIP RATE
# ============================================================

def calculate_skip_rate(
    listening_history_df
):

    total_records = len(
        listening_history_df
    )

    if total_records == 0:
        return 0

    skipped_records = (
        listening_history_df["skipped"] == True
    ).sum()

    return (
        skipped_records /
        total_records
    ) * 100


# ============================================================
# COMPLETED VS SKIPPED
# ============================================================

def listening_status_distribution(
    listening_history_df
):

    completed_count = (
        listening_history_df["completed"] == True
    ).sum()

    skipped_count = (
        listening_history_df["skipped"] == True
    ).sum()

    result = pd.Series(
        {
            "Completed": completed_count,
            "Skipped": skipped_count
        }
    )

    return result


# ============================================================
# LISTENS BY GENRE
# ============================================================

def listens_by_genre(
    listening_history_df,
    songs_df
):

    merged_df = listening_history_df.merge(
        songs_df,
        on="song_id",
        how="left"
    )

    result = (
        merged_df
        .groupby("genre")["history_id"]
        .count()
        .sort_values(ascending=False)
    )

    return result


# ============================================================
# LISTENS BY LANGUAGE
# ============================================================

def listens_by_language(
    listening_history_df,
    songs_df
):

    merged_df = listening_history_df.merge(
        songs_df,
        on="song_id",
        how="left"
    )

    result = (
        merged_df
        .groupby("language")["history_id"]
        .count()
        .sort_values(ascending=False)
    )

    return result


# ============================================================
# TOP SONGS BY LISTENING DURATION
# ============================================================

def top_songs_by_listening_duration(
    listening_history_df,
    songs_df
):

    merged_df = listening_history_df.merge(
        songs_df,
        on="song_id",
        how="left"
    )

    result = (
        merged_df
        .groupby("song_name")[
            "listening_duration_seconds"
        ]
        .sum()
        .sort_values(ascending=False)
    )

    return result


# ============================================================
# TOP ARTISTS BY LISTENING DURATION
# ============================================================

def top_artists_by_listening_duration(
    listening_history_df,
    songs_df,
    albums_df,
    artists_df
):

    merged_df = listening_history_df.merge(
        songs_df,
        on="song_id",
        how="left"
    )

    merged_df = merged_df.merge(
        albums_df,
        on="album_id",
        how="left"
    )

    merged_df = merged_df.merge(
        artists_df,
        on="artist_id",
        how="left"
    )

    result = (
        merged_df
        .groupby("artist_name")[
            "listening_duration_seconds"
        ]
        .sum()
        .sort_values(ascending=False)
    )

    return result


# ============================================================
# LISTENING TREND BY DATE
# ============================================================

def listening_trend(
    listening_history_df
):

    result = (
        listening_history_df
        .groupby(
            listening_history_df["played_at"].dt.date
        )["history_id"]
        .count()
    )

    return result


# ============================================================
# LISTENING TREND BY MONTH
# ============================================================

def monthly_listening_trend(
    listening_history_df
):

    result = (
        listening_history_df
        .groupby(
            listening_history_df["played_at"].dt.to_period("M")
        )["history_id"]
        .count()
    )

    return result


# ============================================================
# MUSIC KPI SUMMARY
# ============================================================

def create_music_kpi_summary(
    songs_df,
    artists_df,
    albums_df,
    listening_history_df
):

    total_songs = calculate_total_songs(
        songs_df
    )

    total_artists = calculate_total_artists(
        artists_df
    )

    total_albums = calculate_total_albums(
        albums_df
    )

    total_listening_records = (
        calculate_total_listening_records(
            listening_history_df
        )
    )

    average_duration = (
        calculate_average_listening_duration(
            listening_history_df
        )
    )

    total_duration = (
        calculate_total_listening_duration(
            listening_history_df
        )
    )

    completion_rate = (
        calculate_completion_rate(
            listening_history_df
        )
    )

    skip_rate = (
        calculate_skip_rate(
            listening_history_df
        )
    )

    kpi_data = {

        "KPI": [
            "Total Songs",
            "Total Artists",
            "Total Albums",
            "Total Listening Records",
            "Average Listening Duration (sec)",
            "Total Listening Duration (sec)",
            "Completion Rate (%)",
            "Skip Rate (%)"
        ],

        "Value": [
            total_songs,
            total_artists,
            total_albums,
            total_listening_records,
            round(average_duration, 2),
            round(total_duration, 2),
            round(completion_rate, 2),
            round(skip_rate, 2)
        ]
    }

    return pd.DataFrame(kpi_data)


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print(
        "\n========== "
        "MUSIC & LISTENING ANALYTICS "
        "=========="
    )

    # --------------------------------------------------------
    # LOAD DATA
    # --------------------------------------------------------

    (
        songs_df,
        artists_df,
        albums_df,
        listening_history_df
    ) = load_music_analytics_data()

    # ========================================================
    # BASIC MUSIC OVERVIEW
    # ========================================================

    total_songs = calculate_total_songs(
        songs_df
    )

    total_artists = calculate_total_artists(
        artists_df
    )

    total_albums = calculate_total_albums(
        albums_df
    )

    total_listening_records = (
        calculate_total_listening_records(
            listening_history_df
        )
    )

    print(
        f"\nTotal Songs: {total_songs}"
    )

    print(
        f"Total Artists: {total_artists}"
    )

    print(
        f"Total Albums: {total_albums}"
    )

    print(
        f"Total Listening Records: "
        f"{total_listening_records}"
    )

    # ========================================================
    # TOP SONGS
    # ========================================================

    top_song_data = top_songs(
        listening_history_df,
        songs_df
    )

    print(
        "\n--- TOP 10 MOST PLAYED SONGS ---"
    )

    print(
        top_song_data.head(10)
    )

    # ========================================================
    # TOP ARTISTS
    # ========================================================

    top_artist_data = top_artists(
        listening_history_df,
        songs_df,
        albums_df,
        artists_df
    )

    print(
        "\n--- TOP 10 MOST PLAYED ARTISTS ---"
    )

    print(
        top_artist_data.head(10)
    )

    # ========================================================
    # TOP ALBUMS
    # ========================================================

    top_album_data = top_albums(
        listening_history_df,
        songs_df,
        albums_df
    )

    print(
        "\n--- TOP 10 MOST PLAYED ALBUMS ---"
    )

    print(
        top_album_data.head(10)
    )

    # ========================================================
    # LISTENING BEHAVIOR
    # ========================================================

    average_duration = (
        calculate_average_listening_duration(
            listening_history_df
        )
    )

    total_duration = (
        calculate_total_listening_duration(
            listening_history_df
        )
    )

    print(
        "\n--- LISTENING BEHAVIOR ---"
    )

    print(
        f"Average Listening Duration: "
        f"{average_duration:.2f} seconds"
    )

    print(
        f"Total Listening Duration: "
        f"{total_duration:.2f} seconds"
    )

    # ========================================================
    # COMPLETION & SKIP ANALYSIS
    # ========================================================

    completion_rate = (
        calculate_completion_rate(
            listening_history_df
        )
    )

    skip_rate = (
        calculate_skip_rate(
            listening_history_df
        )
    )

    print(
        "\n--- LISTENING ENGAGEMENT ---"
    )

    print(
        f"Completion Rate: "
        f"{completion_rate:.2f}%"
    )

    print(
        f"Skip Rate: "
        f"{skip_rate:.2f}%"
    )

    # Completed vs Skipped

    status_distribution = (
        listening_status_distribution(
            listening_history_df
        )
    )

    print(
        "\n--- COMPLETED VS SKIPPED ---"
    )

    print(
        status_distribution
    )

    # ========================================================
    # GENRE ANALYTICS
    # ========================================================

    genre_data = listens_by_genre(
        listening_history_df,
        songs_df
    )

    print(
        "\n--- TOP 10 GENRES BY LISTENS ---"
    )

    print(
        genre_data.head(10)
    )

    # ========================================================
    # LANGUAGE ANALYTICS
    # ========================================================

    language_data = listens_by_language(
        listening_history_df,
        songs_df
    )

    print(
        "\n--- LISTENS BY LANGUAGE ---"
    )

    print(
        language_data
    )

    # ========================================================
    # TOP SONGS BY LISTENING DURATION
    # ========================================================

    duration_song_data = (
        top_songs_by_listening_duration(
            listening_history_df,
            songs_df
        )
    )

    print(
        "\n--- TOP 10 SONGS BY LISTENING DURATION ---"
    )

    print(
        duration_song_data.head(10)
    )

    # ========================================================
    # TOP ARTISTS BY LISTENING DURATION
    # ========================================================

    duration_artist_data = (
        top_artists_by_listening_duration(
            listening_history_df,
            songs_df,
            albums_df,
            artists_df
        )
    )

    print(
        "\n--- TOP 10 ARTISTS BY LISTENING DURATION ---"
    )

    print(
        duration_artist_data.head(10)
    )

    # ========================================================
    # DAILY LISTENING TREND
    # ========================================================

    daily_trend = listening_trend(
        listening_history_df
    )

    print(
        "\n--- DAILY LISTENING TREND ---"
    )

    print(
        daily_trend.head(10)
    )

    # ========================================================
    # MONTHLY LISTENING TREND
    # ========================================================

    monthly_trend = monthly_listening_trend(
        listening_history_df
    )

    print(
        "\n--- MONTHLY LISTENING TREND ---"
    )

    print(
        monthly_trend
    )

    # ========================================================
    # MUSIC KPI SUMMARY
    # ========================================================

    music_kpi_summary = create_music_kpi_summary(
        songs_df,
        artists_df,
        albums_df,
        listening_history_df
    )

    print(
        "\n--- MUSIC KPI SUMMARY ---"
    )

    print(
        music_kpi_summary.to_string(
            index=False
        )
    )

    # ========================================================

    print(
        "\n========== "
        "MUSIC ANALYTICS COMPLETED "
        "=========="
    )