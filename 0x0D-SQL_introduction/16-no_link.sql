-- lists all records of the table second_table
-- excludes rows with empty name value
SELECT score, name
FROM second_table
WHERE name <> ''
ORDER BY score DESC;
