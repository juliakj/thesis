use test;
#create table authors2 (id INT, title VARCHAR(45), author VARCHAR(40), price INT, PRIMARY KEY (id));
insert into authors2 (id, title, author, price) VALUES (1, 'Book', 'Author', 6);
select * from authors2; 
