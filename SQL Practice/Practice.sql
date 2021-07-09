create database Queries;
use Queries;
create table employees
(
  Eid int not null,
  E_name_ varchar(255),
  Dept varchar(20),
  Salary int(11),
  primary key (Eid)
);

insert into employees(Eid,E_name_,Dept,Salary)
values
(1,'RAM','HR',10000),
(2,'AMRIT','MRKT',20000),
(3,'RAVI','HR',30000),
(4,'NITIN','MRKT',40000),
(5,'VARUN','IT',50000);

select *from employees;
-- Query 1
select max(Salary) from employees;

-- Query 2
select E_name_ from employees where Salary =(select max(Salary) from employees);

-- Query 3
select E_name_ from employees where 
Salary = (select max(salary) from employees where 
Salary!=(select max(Salary) from employees));

-- Query 4
select Dept,count(*) from employees group by Dept;

-- Query 5
select Dept from employees group by Dept having count(*)<2;

-- Query 6
select Eid,E_name_,Dept from employees where Dept in (select Dept from employees group by Dept having count(*)<2); 

-- Query 7
select E_name_,Dept,Salary from employees where Salary in (select max(Salary) from employees group by Dept);





