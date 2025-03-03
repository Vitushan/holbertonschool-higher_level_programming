-- script tha lists the number of record with the same score
-- in the second_table of the database
SELECT score COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
