-- lists all Comdedy shows
SELECT title FROM tv_shows
where title NOT IN(
SELECT tv_shows.title from tv_shows
JOIN tv_show_genres on tv_shows.id = tv_show_genres.show_id
JOIN tv_genres on tv_show_genres.genre_id = tv_genres.id
where tv_genres.name = "Comedy"
)
ORDER BY title ASC;
