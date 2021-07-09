use join_us;

CREATE TABLE userss (
    users_salary int(11) ,
    id  int auto_increment not null primary key
);

INSERT INTO `userss` VALUES (11,12000);
select * from userss;
select max(users_salary) as Salary from userss where users_salary<(select max(users_salary) from userss);
select * from userss where id != id order by id desc limit 2;