-- script that lists all shows contained in
-- hbtn_0d_tvshows that have at least one genre linked.


SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows
INNER JOIN tv_shows ON tv_shows.title = tv_shows_genres_id.genre_id