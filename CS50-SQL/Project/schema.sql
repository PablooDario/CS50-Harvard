-- Create Princiapl Tables
CREATE TABLE IF NOT EXISTS users(
    id NUMERIC NOT NULL,
    username TEXT NOT NULL UNIQUE,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS artists(
    id NUMERIC NOT NULL, 
    name TEXT NOT NULL UNIQUE,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS albums(
    id NUMERIC NOT NULL, 
    name TEXT NOT NULL UNIQUE, 
    released_date TEXT NOT NULL,
    artist_id NUMERIC NOT NULL, 
    PRIMARY KEY(id),
    FOREIGN KEY(artist_id) REFERENCES artists(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS songs(
    id NUMERIC NOT NULL, 
    name TEXT NOT NULL UNIQUE,
    duration NUMERIC NOT NULL,
    album_id NUMERIC NOT NULL, 
    PRIMARY KEY(id),
    FOREIGN KEY (album_id) REFERENCES albums(id) ON DELETE CASCADE ON UPDATE CASCADE 
);

CREATE TABLE IF NOT EXISTS playlists(
    id NUMERIC NOT NULL, 
    user_id NUMERIC NOT NULL,
    name TEXT NOT NULL, 
    -- Enforcing unique playlist name per user
    UNIQUE (user_id, name),
    PRIMARY KEY(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create Relational Tables

-- Relationships between artists and their songs
CREATE TABLE IF NOT EXISTS artists_songs(
    artist_id NUMERIC NOT NULL, 
    song_id NUMERIC NOT NULL, 
    PRIMARY KEY(artist_id, song_id),
    FOREIGN KEY(song_id) REFERENCES songs(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(artist_id) REFERENCES artists(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Relationships between playlists and the songs contained
CREATE TABLE IF NOT EXISTS playlists_songs(
    playlist_id NUMERIC NOT NULL, 
    song_id NUMERIC NOT NULL, 
    PRIMARY KEY(playlist_id, song_id),
    FOREIGN KEY(playlist_id) REFERENCES playlists(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(song_id) REFERENCES songs(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create Indexes
CREATE INDEX "album_name_index" ON albums ("name");
CREATE INDEX "artist_id_index" ON songs ("artist_id");
CREATE INDEX "user_id_index" ON playlists ("user_id");
CREATE INDEX "playlist_id" ON playlists_songs ("playlist_id");

-- Create a View for the Most Popular Songs
-- A popular song is when a sog is added to 3 or more playlists

CREATE VIEW "popular_songs" AS
SELECT "name" 
FROM songs 
WHERE "id" IN (
    SELECT "song_id" FROM playlists_songs
    GROUP BY "song_id"
    HAVING COUNT(*) > 3
);