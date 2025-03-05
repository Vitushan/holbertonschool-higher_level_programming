-- import the database dump from hbtn_0d_tvshows
-- listes all shows contained in hbtn_0d_tvshows
CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows
FROM hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
JOIN tv_shows.title = tv_show_genres.genre_id
