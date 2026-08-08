-- Songs per Genre
SELECT genre,
COUNT(*)
FROM songs
GROUP BY genre
ORDER BY COUNT(*) DESC;

-- Songs per Language
SELECT language,
COUNT(*)
FROM songs
GROUP BY language
ORDER BY COUNT(*) DESC;

-- Average Song Duration
SELECT
ROUND(AVG(duration_seconds),2)
FROM songs;

-- Explicit Songs
SELECT explicit,
COUNT(*)
FROM songs
GROUP BY explicit;

-- Songs Per Album
SELECT
a.album_name,
COUNT(s.song_id)
FROM albums a
LEFT JOIN songs s
ON a.album_id=s.album_id
GROUP BY a.album_name
ORDER BY COUNT(s.song_id) DESC;

-- Albums Per Artist
SELECT
ar.artist_name,
COUNT(a.album_id)
FROM artists ar
LEFT JOIN albums a
ON ar.artist_id=a.artist_id
GROUP BY ar.artist_name
ORDER BY COUNT(a.album_id) DESC;