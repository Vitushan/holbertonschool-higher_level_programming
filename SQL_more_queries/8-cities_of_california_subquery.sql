-- lists all cities of California
-- be found in the database
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = state.id AND state.name = 'California'
ORDER BY cities.id;
