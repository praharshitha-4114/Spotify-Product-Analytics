# Spotify Product Analytics Platform

## Database Overview

The database is designed using normalization principles to reduce redundancy and improve scalability.

## Tables

1. users
2. subscriptions
3. artists
4. albums
5. songs
6. devices
7. sessions
8. listening_history
9. payments
10. playlists
11. playlist_songs

## Relationships

- One Subscription → Many Users
- One Artist → Many Albums
- One Album → Many Songs
- One User → Many Sessions
- One User → Many Payments
- One User → Many Playlists
- One Playlist → Many Songs
- One Song → Many Playlist Entries