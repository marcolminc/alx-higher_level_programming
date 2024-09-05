-- write a script that lists all shows and all genres linked to the show
SELECT ts.title, g.name
FROM tv_shows ts
LEFT JOIN tv_show_genres sg ON ts.id = sg.show_id
LEFT JOIN tv_genres g ON sg.genre_id = g.id
ORDER BY ts.title ASC, g.name ASC;
