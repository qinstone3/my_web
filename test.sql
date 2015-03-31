 drop database if exists test;
 create database test;
 use test;
-- grant select,insert,update,delete on test.* to 'rednumber'@'localhost' identified by '123456';

create table users(
	id varchar(50) not null,
	name varchar(50) not null,
	password varchar(50) not null,
	email varchar(50) not null,
	admin bool not null,
	create_at real not null,
	primary key(id)
) engine=innodb default charset=utf8;