--lists all record of the second_table
--display the score and the name  by descending order
SELECT score, name
FROM second_table
WHERE  name != '' AND name IS NOT NULL
ORDER BY score DESC;
