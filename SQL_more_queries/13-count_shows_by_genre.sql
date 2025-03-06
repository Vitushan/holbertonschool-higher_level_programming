-- lists all genres from hbtn_0d_tvshows
-- results must be sorted in descending order by the number of shows linked
SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS t ON g.id = t.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;
