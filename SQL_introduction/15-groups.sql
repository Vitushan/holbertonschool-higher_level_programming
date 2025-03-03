-- script tha lists the number of record with the same score
-- in the second_table of the database hbtn_0c_0
SELECT score, COUNT(score) AS COUNT
FROM second_table GROUP BY number
ORDER BY count DESC;
