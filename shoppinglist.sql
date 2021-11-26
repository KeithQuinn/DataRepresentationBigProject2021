create database datarepresentation;
show databases;
use datarepresentation;
show tables;
create table shoppinglist (id int NOT NULL AUTO_INCREMENT, item varchar(250), brand varchar(250), quantity int, PRIMARY KEY(id));
describe shoppingList;
select * FROM shoppinglist;
INSERT into shoppinglist (item, brand, quantity) VALUES ('Chicken Fillets', 'Birdseye', 2);