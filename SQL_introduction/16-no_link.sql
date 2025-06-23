--  script that lists all records of the second_table of the database


SELECT score, name FROM second_table WHERE name  IS NOT NULL AND name != ""
ORDER BY score DESC, name ASC;