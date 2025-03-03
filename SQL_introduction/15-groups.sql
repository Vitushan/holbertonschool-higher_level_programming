-- script tha lists the number of record with the same score
-- in the second_table of the database
UPDATE score SET name = 'number' WHERE second_table 
SELECT score COUNT(*) AS count
FROM second_table
GROUP BY score
ORDER BY count DESC;
