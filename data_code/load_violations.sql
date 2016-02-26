use db;

LOAD DATA LOCAL INFILE 'violations_full.csv' into table violations fields terminated by '\t' lines terminated by '\n' (npi, the_date, the_action, description, the_update);

