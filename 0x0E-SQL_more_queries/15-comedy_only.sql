-- lists all Comdey shows in the db
SELECT ts.title
FROM tv_shows ts
JOIN tv_show_genres sg ON ts.id = sg.show_id
JOIN tv_genres g ON sg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY ts.title ASC;
