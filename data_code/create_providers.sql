use db;
drop table locations;
drop table services;
drop table violations;
drop table providers;
create table providers (npi INT, lastname VARCHAR(25), firstname VARCHAR(20), middleinitial VARCHAR(3), cred VARCHAR(20), gender VARCHAR(1), specialty VARCHAR(43), medicare VARCHAR(1), school VARCHAR(94), grad_year INT, pac_id INT, PRIMARY KEY(npi));
select * from providers;
