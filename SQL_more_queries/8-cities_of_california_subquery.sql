-- lists all the cities of California
-- be found in the database
SELECT cities.id, cities.name;
FROM cities, states WHERE cities.id, cities = states.id AND state.name = 'California';
ORDER BY cities.id ASC;
