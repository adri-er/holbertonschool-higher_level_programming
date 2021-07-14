-- lists all genres of the show Dexter.
SELECT tg.name
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
INNER JOIN tv_genres AS tg
ON tsg.genre_id = tg.id
WHERE ts.name = 'Dexter'
ORDER BY tg.name ASC;
