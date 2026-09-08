CREATE TABLE playlist_songs (
    playlist_id INTEGER NOT NULL REFERENCES playlists(id),
    song_id INTEGER NOT NULL REFERENCES songs(id),

    added_at TIMESTAMP NOT NULL DEFAULT NOW(),

    PRIMARY KEY (playlist_id, song_id)
);