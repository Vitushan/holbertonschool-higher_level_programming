-- script that lists the number of records with the same score in the second table


SELECT score FROM second_table GROUP BY score DESC;
