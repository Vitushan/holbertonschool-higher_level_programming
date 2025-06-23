-- Lists all records with a score >= 10 in the second_table


SELECT score FROM second_table GROUP BY score >= 10;