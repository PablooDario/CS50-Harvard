-- Insertions

-- Sample data for users
INSERT INTO users (id, username) VALUES
(1, 'Pablo'),
(2, 'Rodrigo'),
(3, 'Fernando'),
(4, 'Diego');

-- Sample data for artists
INSERT INTO artists (id, name) VALUES
(1, 'Kendrick Lamar'),
(2, 'Mac Miller'),
(3, 'Travis Scott');

-- Sample data for albums
INSERT INTO albums (id, name, released_date, artist_id) VALUES
(1, 'good kid, maad city', '2015-03-15', 1),
(2, 'DAMN.', '2017-04-14', 1),
(3, 'Circles', '2018-08-03', 2),
(4, 'Rodeo', '2018-08-03', 3);

-- Sample data for songs
INSERT INTO songs (id, name, duration, album_id) VALUES
(1, 'Money Trees', 3.39, 1),
(2, 'Real', 3.54, 1),
(3, 'Love', 2.57, 2),
(4, 'GOD.', 3.06, 2),
(5, 'I Can See', 5.45, 3),
(6, 'Thats On Me', 5.48, 3),
(7, 'Fight the Feeling', 5.01, 3),
(8, 'Apple Pie', 5.12, 4),
(9, '90210', 4.30, 4);

-- Sample data for playlists
INSERT INTO playlists (id, user_id, name) VALUES
(1, 1, 'Kendrick Vibes'),
(2, 1, 'Hits'),
(3, 2, 'I love u Mac'),
(4, 2, 'Late Night'),
(5, 3, 'Days Before Rodeo'),
(6, 4, ':)');

-- Sample data for artists_songs (relationships between artists and their songs)
INSERT INTO artists_songs (artist_id, song_id) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(2, 5),
(2, 6),
(1, 7),
(2, 7),
(3, 8),
(3, 9);

-- Sample data for playlists_songs (songs in playlists)
INSERT INTO playlists_songs (playlist_id, song_id) VALUES
(1, 1), -- Kendrick Vibes playlist
(1, 3), -- Kendrick Vibes playlist
(1, 4), -- Kendrick Vibes playlist
(2, 3), -- Hits playlist
(2, 5), -- Hits playlist
(2, 9), -- Hits playlist
(3, 5), -- I love you Mac Miller playlist
(3, 6), -- I love you Mac Miller playlist
(3, 7), -- I love you Mac Miller playlist
(4, 3), -- Late Night playlist
(4, 4), -- Late Night playlist
(4, 6), -- Late Night playlist
(5, 8), -- Days Before Rodeo playlist
(5, 9), -- Days Before Rodeo playlist
(6, 1), -- :) playlist
(6, 3), -- :) playlist
(6, 6), -- :) playlist
(6, 8); -- :) playlist

-- Update a username
UPDATE users
SET username = 'Pablooo'
WHERE id = 1;

-- Change the release date of the album 'Swimming' by Mac Miller 
UPDATE albums
SET released_date = '2018-08-10'
WHERE name = 'Swimming';

-- Rename the playlist for the user with id = 2.
UPDATE playlists
SET name = 'Happy Station'
WHERE name = 'Late Night' AND user_id = 2;


-- Delete a Song for innapropiate lyric
DELETE FROM songs
WHERE name = 'Fight the Feeling';

-- Query using the index on name in the albums table: Retrieve album details for an album with a specific name.
SELECT * 
FROM albums 
WHERE name = 'DAMN.';


-- Query using the index on artist_id in the artists_songs table: Retrieve all songs for a specific artist
SELECT s.name AS song_name
FROM songs s
JOIN artists_songs as ON s.id = as.song_id
WHERE as.artist_id = 1;


-- Query using the index on user_id in the playlists table: Retrieve all playlists created by a specific user
SELECT u.username, p.name AS playlist_name
FROM users u 
JOIN playlists p ON p.user_id=u.id
WHERE u.id = 1;

-- Query using the index on playlist_id in the playlists_songs table: Retrieve all songs in a specific playlist
SELECT s.name AS song_name
FROM songs s
JOIN playlists_songs ps ON s.id = ps.song_id
WHERE ps.playlist_id = 1;

-- Query using the view for the most popular songs of all time:
SELECT *
FROM most_popular_songs;