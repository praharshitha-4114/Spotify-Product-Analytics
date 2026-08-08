-- Average Session Duration
SELECT
ROUND(AVG(session_duration_minutes),2)
FROM sessions;

-- Longest Session
SELECT
MAX(session_duration_minutes)
FROM sessions;

-- Shortest Session
SELECT
MIN(session_duration_minutes)
FROM sessions;

-- Device Usage
SELECT
d.device_name,
COUNT(*)
FROM sessions s
JOIN devices d
ON s.device_id=d.device_id
GROUP BY d.device_name
ORDER BY COUNT(*) DESC;

-- Completed Songs
SELECT
completed,
COUNT(*)
FROM listening_history
GROUP BY completed;

-- Skipped Songs
SELECT
skipped,
COUNT(*)
FROM listening_history
GROUP BY skipped;

-- Average Listening Duration
SELECT
ROUND(AVG(listening_duration_seconds),2)
FROM listening_history;