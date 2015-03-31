drop database if exists test;
create database test;
use test;

grant select,update,insert,delete on test.* to 'root'@'localhost' identified by '123456';

create table users(
	id varchar(50) primary key not null,
	name varchar(50) not null,
	email varchar(50) not null,
	password varchar(50) not null,
	admin bool not null,
	create_at real not null
) engine=innodb default charset=utf8;

insert into users (id,name,email,password,admin,create_at) values 
	('1432523','qinlei','qinlei@qinlei.com','123456',1,234234);

select * from users;
