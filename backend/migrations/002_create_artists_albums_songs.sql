CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    spotify_id VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    spotify_id VARCHAR(100) NOT NULL UNIQUE,
    cover_url TEXT
);

CREATE TABLE songs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    spotify_id VARCHAR(100) NOT NULL UNIQUE,
    duration_ms INTEGER,
    preview_url TEXT,

    artist_id INTEGER NOT NULL REFERENCES artists(id),
    album_id INTEGER REFERENCES albums(id)
);