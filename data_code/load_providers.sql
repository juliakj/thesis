use db;
#drop table locations;
#drop table providers;

LOAD DATA LOCAL INFILE 'merged_personal.csv' into table providers fields terminated by '\t' lines terminated by '\r\n';
select * from providers; 
