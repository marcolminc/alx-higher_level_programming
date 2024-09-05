-- lists all shows without the genre Comedy
SELECT ts.title
FROM tv_shows ts
WHERE ts.id NOT IN (
    SELECT sg.show_id
    FROM tv_show_genres sg
    JOIN tv_genres g ON sg.genre_id = g.id
    WHERE g.name = 'Comedy'
)
ORDER BY ts.title ASC;
