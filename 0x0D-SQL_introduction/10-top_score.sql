-- lists all records of the table second_table (database: htn_0c_0)
-- ordered by score(top first)
SELECT t.score, t.name
FROM second_table t
ORDER BY t.score DESC;
