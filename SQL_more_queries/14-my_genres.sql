-- import the database dump from hbtn_0d_tvshows
-- result must be sorted in ascending order by the genre
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
