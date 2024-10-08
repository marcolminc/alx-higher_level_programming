-- lists all genres not linked to the show dexter
SELECT g.name
FROM tv_genres g
WHERE g.id NOT IN (
    SELECT sg.genre_id
    FROM tv_show_genres sg
    JOIN tv_shows ts ON sg.show_id = ts.id
    WHERE ts.title = 'Dexter'
)
ORDER BY g.name ASC;
