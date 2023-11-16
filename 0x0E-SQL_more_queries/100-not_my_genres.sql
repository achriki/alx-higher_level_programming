-- lists all Comdedy shows
SELECT name FROM tv_genres
where name NOT IN(
SELECT tv_genres.name from tv_genres
JOIN tv_show_genres on tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows on tv_show_genres.show_id = tv_shows.id
where tv_shows.title = "Dexter"
)
ORDER BY name ASC;
