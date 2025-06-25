-- script that lists all cities contained in the database hbtn_0d_usa


SELECT cities_id, cities_name, states_name
FROM cities
INNER JOIN states ON cities.states_id = state.id
ORDER BY cities.id ASC
