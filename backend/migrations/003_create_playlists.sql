CREATE TABLE playlists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,

    user_id INTEGER NOT NULL REFERENCES users(id),

    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);