use db;
#drop table violations;
create table violations (npi INT, the_date VARCHAR(10), the_action VARCHAR(702), description VARCHAR(865), the_update VARCHAR(10));
select * from violations;
