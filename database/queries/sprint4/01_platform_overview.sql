-- Total Users
SELECT COUNT(*) AS total_users FROM users;

-- Total Artists
SELECT COUNT(*) AS total_artists FROM artists;

-- Total Albums
SELECT COUNT(*) AS total_albums FROM albums;

-- Total Songs
SELECT COUNT(*) AS total_songs FROM songs;

-- Total Sessions
SELECT COUNT(*) AS total_sessions FROM sessions;

-- Total Listening Records
SELECT COUNT(*) AS total_listening_records
FROM listening_history;

-- Total Payments
SELECT COUNT(*) AS total_payments
FROM payments;

-- Platform Overview
SELECT 'Users',COUNT(*) FROM users
UNION ALL
SELECT 'Artists',COUNT(*) FROM artists
UNION ALL
SELECT 'Albums',COUNT(*) FROM albums
UNION ALL
SELECT 'Songs',COUNT(*) FROM songs
UNION ALL
SELECT 'Sessions',COUNT(*) FROM sessions
UNION ALL
SELECT 'Listening History',COUNT(*) FROM listening_history
UNION ALL
SELECT 'Payments',COUNT(*) FROM payments;