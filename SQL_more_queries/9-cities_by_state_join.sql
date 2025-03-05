-- lists all cities contained in the hbtn_0d_usa database
-- results must be sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id;
