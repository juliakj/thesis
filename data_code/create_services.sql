use db;
#drop table services;
create table services (npi INT, code INT, descrip VARCHAR(256), cnt INT, beneficiaries INT, medicare_allowed_amnt FLOAT, submitted_charge FLOAT, medicare_payment_amnt FLOAT, FOREIGN KEY(npi) REFERENCES providers(npi));
select COUNT(*) from services;
