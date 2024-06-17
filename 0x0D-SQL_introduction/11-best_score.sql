-- lists all records with a score >= 10 in the table second_table
-- ordered by score(top firt)
SELECT t.score, t.name
FROM second_table t
WHERE t.score >= 10
ORDER BY t.score DESC;
