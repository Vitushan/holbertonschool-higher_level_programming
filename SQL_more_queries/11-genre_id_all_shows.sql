-- script that lists all shows contained
-- in the database hbtn_0d_tvshows


SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
WHERE = tv_show_genres NOT NULL
INNER JOIN tv_shows ON tv_show_genres = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC;