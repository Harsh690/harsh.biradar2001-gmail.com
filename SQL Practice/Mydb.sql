create database shirts_db;
SET SQL_SAFE_UPDATES = 0;
use shirts_db;
create table shirts
(id int not null auto_increment  ,
article varchar(255), 
color varchar(255),
shirt_size varchar(255),
last_worn int,
primary key (id)
);
insert into shirts(article, color, shirt_size, last_worn)
values
('t-shirt', 'white', 'S', 10),
('t-shirt', 'green', 'S', 200),
('polo shirt', 'black', 'M', 10),
('tank top', 'blue', 'S', 50),
('t-shirt', 'pink', 'S', 0),
('polo shirt', 'red', 'M', 5),
('tank top', 'white', 'S', 200),
('tank top', 'blue', 'M', 15);

insert into shirts(article, color, shirt_size, last_worn)
values ("polo shirt","Purple","M",50);

 Update shirts set shirt_size ="L" where article = "polo shirt";
 Update shirts set last_worn = 0  where last_worn = 15;
 update shirts set shirt_size = "XS"  where color = "white" ;
 update shirts set color = "Off white"  where color = "white" ;
select * from shirts;

delete from shirts where last_worn = 200;
delete from shirts where article = "tank Top";
drop table shirts;
delete from shirts;

