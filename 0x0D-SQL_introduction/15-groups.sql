-- lists teh number of records with the same score in the second_table
-- the resulting number of scores ins in col labelled number
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score;
