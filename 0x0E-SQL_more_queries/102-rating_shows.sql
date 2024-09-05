-- lists all shows from the db by their rating
SELECT ts.title, COALESCE(SUM(r.rating), 0) AS rating_sum
FROM tv_shows ts
LEFT JOIN tv_show_ratings r ON ts.id = r.show_id
GROUP BY ts.id, ts.title
ORDER BY rating_sum DESC;
