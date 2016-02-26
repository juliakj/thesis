use db;
#drop table locations;
create table locations (location_id INT NOT NULL AUTO_INCREMENT, npi INT, street VARCHAR(101), city VARCHAR(27), zip INT, the_state VARCHAR(2), FOREIGN KEY(npi) REFERENCES providers(npi), PRIMARY KEY(location_id));
select * from locations;
