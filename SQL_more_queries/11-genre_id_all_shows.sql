-- import the database dump of hbtn_0d_tvshows
-- lists all show contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
ORDER BY tv_shows.title AND tv_show_genres.genre_id;