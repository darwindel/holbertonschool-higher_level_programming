-- list all records with >= 10 score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY DESC
