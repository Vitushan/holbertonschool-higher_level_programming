-- lists all shows contained in database
-- the database name will be passed as an argument of the mysql command
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN INNER tv_show_genres = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id
