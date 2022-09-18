create database details;
USE details;
show tables;

create table accounts(name varchar(20),roll_no varchar(20),email varchar(30),password varchar(10));
ALTER TABLE s_detail ADD `ip` int(20);
describe s_detail;
INSERT INTO accounts (`name`,`roll_no`, `email`,`password`) VALUES ('neha','20csu149', 'neha20csu149@ncuindia.edu','NCU149');
INSERT INTO accounts (`name`,`roll_no`, `email`,`password`) VALUES ('neha','20csu149', 'neha20csu149','NCU149');

select * from accounts;

create database detail;
USE detail;
show tables;

create table HTM(Name varchar(20) not null,Roll_no varchar(20) not null Primary Key,Email varchar(30) not null ,Password varchar(20) not null,Department varchar(20) not null,Stream varchar(20) not null,Specialisation varchar(20) not null, Device_name varchar(20) not null,Device_serial varchar(50) not null ,MAC varchar(20) not null , Hash varchar(50) not null, ip float(20));
select * from HTM;


