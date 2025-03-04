-- create the unique_id table
-- description: id INT with default value 1 and unique
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT VALUE 1,
    name VARCHAR(256)
);
