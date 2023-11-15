-- create he database hbtn_0d_usa and the table cities
create database if not exists hbtn_0d_usa;
create table if not exists hbtn_0d_usa.cities(
	id int UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id int NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id),
	name varchar(256) NOT NULL);
