use db;

LOAD DATA LOCAL INFILE 'merged_locations.csv' into table locations fields terminated by ',' lines terminated by '\n' (npi, street, city, zip, the_state);
select * from locations; 
