-- lists all genres in the db by their rating
SELECT g.name, COALESCE(SUM(r.rating), 0) AS rating
FROM tv_genres g
LEFT JOIN tv_show_genres sg ON g.id = sg.genre_id
LEFT JOIN tv_show_ratings r ON sg.show_id = r.show_id
GROUP BY g.id, g.name
ORDER BY rating_sum DESC;
