-- Called first_table in the current database
-- first_table description : id: INT; name VARCHAR (256)
IF first_table EXISTS CREATE TABLE first_table(id INT, name VARCHAR(256))
