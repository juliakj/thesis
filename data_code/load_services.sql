use db;

LOAD DATA LOCAL INFILE 'service_util.csv' into table services fields terminated by '\t' lines terminated by '\n' IGNORE 1 LINES;
select COUNT(*) from services; 
