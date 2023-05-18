-- script that delete all records with a score <= 5


SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
