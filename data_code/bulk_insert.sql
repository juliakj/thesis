use test;
select * from authors; 
LOAD DATA LOCAL INFILE 'bookdata.csv' into table authors fields terminated by ',' lines terminated by '\r' ignore 1 lines;
select * from authors; 
