-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
select tv_shows.title, tv_show_genres.genre_id from tv_shows
LEFT JOIN tv_show_genres on tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
order by tv_shows.title, tv_show_genres.genre_id;
