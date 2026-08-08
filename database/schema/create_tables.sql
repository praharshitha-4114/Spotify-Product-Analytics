-- ==========================================
-- Tables to be created
-- ==========================================

-- 1. users
-- 2. artists
-- 3. albums
-- 4. songs
-- 5. playlists
-- 6. playlist_songs
-- 7. subscriptions
-- 8. payments
-- 9. devices
-- 10. sessions
-- 11. listening_history


-- ==========================================
-- USERS TABLE
-- ==========================================

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    gender VARCHAR(10),
    date_of_birth DATE,
    country VARCHAR(50),
    city VARCHAR(50),
    signup_date DATE NOT NULL,
    subscription_plan VARCHAR(20)
);

Select * from "users";

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    gender VARCHAR(10),
    date_of_birth DATE,
    country VARCHAR(50),
    city VARCHAR(50),
    signup_date DATE NOT NULL,

    subscription_id INT
);
ALTER TABLE users
DROP COLUMN subscription_plan;

ALTER TABLE users
DROP COLUMN subscription_plan;

ALTER TABLE users
ADD COLUMN subscription_id INT;

-- ==========================================
-- SUBSCRIPTIONS TABLE
-- ==========================================

CREATE TABLE subscriptions (
    subscription_id SERIAL PRIMARY KEY,
    plan_name VARCHAR(30) NOT NULL,
    monthly_price DECIMAL(6,2) NOT NULL,
    max_devices INT NOT NULL,
    audio_quality VARCHAR(30),
    offline_download BOOLEAN,
    ad_free BOOLEAN
);

-- ==========================================
-- ARTISTS TABLE
-- ==========================================

CREATE TABLE artists (
    artist_id SERIAL PRIMARY KEY,
    artist_name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    debut_year INT,
    monthly_listeners BIGINT DEFAULT 0
);
-- ==========================================
-- ALBUMS TABLE
-- ==========================================

CREATE TABLE albums (
    album_id SERIAL PRIMARY KEY,
    artist_id INT NOT NULL,
    album_name VARCHAR(150) NOT NULL,
    release_date DATE,
    total_tracks INT
);
-- ==========================================
-- SONGS TABLE
-- ==========================================

CREATE TABLE songs (
    song_id SERIAL PRIMARY KEY,
    album_id INT NOT NULL,
    song_name VARCHAR(150) NOT NULL,
    genre VARCHAR(50),
    duration_seconds INT,
    language VARCHAR(50),
    explicit BOOLEAN DEFAULT FALSE
);

-- ==========================================
-- DEVICES TABLE
-- ==========================================

CREATE TABLE devices (
    device_id SERIAL PRIMARY KEY,
    device_name VARCHAR(50) NOT NULL,
    device_type VARCHAR(30),
    operating_system VARCHAR(30)
);

-- ==========================================
-- SESSIONS TABLE
-- ==========================================

CREATE TABLE sessions (
    session_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    device_id INT NOT NULL,
    login_time TIMESTAMP NOT NULL,
    logout_time TIMESTAMP,
    session_duration_minutes INT
);

ALTER TABLE sessions
ADD CONSTRAINT fk_session_user
FOREIGN KEY (user_id)
REFERENCES users(user_id);

ALTER TABLE sessions
ADD CONSTRAINT fk_session_device
FOREIGN KEY (device_id)
REFERENCES devices(device_id);

SELECT * FROM sessions;

-- ==========================================
-- LISTENING HISTORY TABLE
-- ==========================================

CREATE TABLE listening_history (
    history_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    song_id INT NOT NULL,
    session_id INT NOT NULL,
    played_at TIMESTAMP NOT NULL,
    listening_duration_seconds INT,
    completed BOOLEAN,
    skipped BOOLEAN
);
ALTER TABLE listening_history
ADD CONSTRAINT fk_history_user
FOREIGN KEY(user_id)
REFERENCES users(user_id);

ALTER TABLE listening_history
ADD CONSTRAINT fk_history_song
FOREIGN KEY(song_id)
REFERENCES songs(song_id);

ALTER TABLE listening_history
ADD CONSTRAINT fk_history_session
FOREIGN KEY(session_id)
REFERENCES sessions(session_id);
-- ==========================================
-- PAYMENTS TABLE
-- ==========================================

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    subscription_id INT NOT NULL,
    amount DECIMAL(8,2),
    payment_date DATE,
    payment_method VARCHAR(30),
    payment_status VARCHAR(20)
);
ALTER TABLE payments
ADD CONSTRAINT fk_payment_user
FOREIGN KEY(user_id)
REFERENCES users(user_id);

ALTER TABLE payments
ADD CONSTRAINT fk_payment_subscription
FOREIGN KEY(subscription_id)
REFERENCES subscriptions(subscription_id);

SELECT COUNT(*) FROM payments;

-- ==========================================
-- PLAYLISTS TABLE
-- ==========================================

CREATE TABLE playlists (
    playlist_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    playlist_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_public BOOLEAN DEFAULT TRUE
);
-- ==========================================
-- PLAYLIST SONGS TABLE
-- ==========================================

CREATE TABLE playlist_songs (
    playlist_song_id SERIAL PRIMARY KEY,
    playlist_id INT NOT NULL,
    song_id INT NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT table_name
FROM information_schema.tables
WHERE table_schema='public'
ORDER BY table_name;

SELECT COUNT(*)
FROM users;

SELECT
user_id,
first_name,
last_name,
email,
country,
subscription_id
FROM users
LIMIT 10;

SELECT *
FROM users
WHERE subscription_id = 2;

SELECT COUNT(*) FROM albums;
SELECT COUNT(*) FROM artists;

select * from songs;
-- final validation queries to check the number of records in each table
SELECT COUNT(*) FROM payments;
SELECT COUNT(*) FROM listening_history;
SELECT COUNT(*) FROM sessions;
SELECT COUNT(*) FROM devices;
SELECT COUNT(*) FROM songs;
SELECT COUNT(*) FROM albums;
SELECT COUNT(*) FROM artists;
SELECT COUNT(*) FROM users;

SELECT
    s.song_name,
    a.album_name,
    ar.artist_name
FROM songs s
JOIN albums a
    ON s.album_id = a.album_id
JOIN artists ar
    ON a.artist_id = ar.artist_id
LIMIT 20;