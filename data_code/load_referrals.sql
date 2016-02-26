use db;

LOAD DATA LOCAL INFILE 'referrals.csv' into table referrals fields terminated by ',' lines terminated by '\n';
select COUNT(*) from referrals; 
