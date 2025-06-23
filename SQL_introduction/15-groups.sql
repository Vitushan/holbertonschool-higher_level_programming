-- script that lists the number of records with the same score in the second table


SELECT COUNT(*), score as number FROM second_table GROUP BY score ORDER BY number DESC;
