use db;

LOAD DATA LOCAL INFILE 'groups_extracted.csv' into table groups fields terminated by '\t' lines terminated by '\n';
select COUNT(*) from groups;

