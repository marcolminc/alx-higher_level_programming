-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT * FROM cities c 
WHERE state_id = (
	SELECT id
	FROM states s
	WHERE s.name = 'California'
	)
ORDER BY c.id ASC;
