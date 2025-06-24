-- script that lists all cities contained in the database hbtn_0d_usa



SELECT name FROM cities WHERE = state_id = SELECT (id, cities, state_id FROM states) ORDER BY state_id;
