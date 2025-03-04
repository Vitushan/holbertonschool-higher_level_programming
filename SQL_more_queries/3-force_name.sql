-- Create a new table:
--@:force_name"
IF force_name EXISTS
CREATE TABLE (id INT, NAME VARCHAR(256)) VALUES(1, 'force_name');
