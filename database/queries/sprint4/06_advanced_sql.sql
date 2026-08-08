-- Top 10 Spending Users
SELECT
user_id,
SUM(amount) total_spent
FROM payments
GROUP BY user_id
ORDER BY total_spent DESC
LIMIT 10;

-- Top 10 Longest Sessions
SELECT *
FROM sessions
ORDER BY session_duration_minutes DESC
LIMIT 10;

-- Top Genres
SELECT
genre,
COUNT(*) total
FROM songs
GROUP BY genre
ORDER BY total DESC
LIMIT 10;

-- Songs With Album
SELECT
s.song_name,
a.album_name
FROM songs s
JOIN albums a
ON s.album_id=a.album_id;

-- Artist Album Song Count
SELECT
ar.artist_name,
COUNT(DISTINCT a.album_id) albums,
COUNT(s.song_id) songs
FROM artists ar
JOIN albums a
ON ar.artist_id=a.artist_id
JOIN songs s
ON a.album_id=s.album_id
GROUP BY ar.artist_name
ORDER BY songs DESC;

-- Revenue Rank
SELECT
user_id,
SUM(amount) total_spent,
RANK() OVER(
ORDER BY SUM(amount) DESC
) rank
FROM payments
GROUP BY user_id;

-- Session Rank
SELECT
user_id,
session_duration_minutes,
ROW_NUMBER() OVER(
ORDER BY session_duration_minutes DESC
)
FROM sessions;

-- Running Revenue
SELECT
payment_date,
SUM(amount)
OVER(
ORDER BY payment_date
)
FROM payments;