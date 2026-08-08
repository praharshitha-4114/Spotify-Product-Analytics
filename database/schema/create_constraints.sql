ALTER TABLE users
ADD CONSTRAINT fk_users_subscription
FOREIGN KEY (subscription_id)
REFERENCES subscriptions(subscription_id);

SELECT *
FROM information_schema.table_constraints
WHERE table_name = 'users';

ALTER TABLE albums
ADD CONSTRAINT fk_albums_artist
FOREIGN KEY (artist_id)
REFERENCES artists(artist_id);

ALTER TABLE songs
ADD CONSTRAINT fk_songs_album
FOREIGN KEY (album_id)
REFERENCES albums(album_id);

-- Sessions
ALTER TABLE sessions
ADD CONSTRAINT fk_sessions_user
FOREIGN KEY (user_id)
REFERENCES users(user_id);

ALTER TABLE sessions
ADD CONSTRAINT fk_sessions_device
FOREIGN KEY (device_id)
REFERENCES devices(device_id);

-- Listening History
ALTER TABLE listening_history
ADD CONSTRAINT fk_history_user
FOREIGN KEY (user_id)
REFERENCES users(user_id);

ALTER TABLE listening_history
ADD CONSTRAINT fk_history_song
FOREIGN KEY (song_id)
REFERENCES songs(song_id);

ALTER TABLE listening_history
ADD CONSTRAINT fk_history_session
FOREIGN KEY (session_id)
REFERENCES sessions(session_id);

-- Payments
ALTER TABLE payments
ADD CONSTRAINT fk_payments_user
FOREIGN KEY (user_id)
REFERENCES users(user_id);

ALTER TABLE payments
ADD CONSTRAINT fk_payments_subscription
FOREIGN KEY (subscription_id)
REFERENCES subscriptions(subscription_id);

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;


-- Playlists

ALTER TABLE playlists
ADD CONSTRAINT fk_playlist_user
FOREIGN KEY (user_id)
REFERENCES users(user_id);

-- Playlist Songs

ALTER TABLE playlist_songs
ADD CONSTRAINT fk_playlist_song_playlist
FOREIGN KEY (playlist_id)
REFERENCES playlists(playlist_id);

ALTER TABLE playlist_songs
ADD CONSTRAINT fk_playlist_song_song
FOREIGN KEY (song_id)
REFERENCES songs(song_id);