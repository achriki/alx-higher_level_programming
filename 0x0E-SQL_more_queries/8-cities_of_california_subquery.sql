-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
select id as c_id, name from hbtn_0d_usa.cities 
where state_id in (select id from states)
order by c_id;
