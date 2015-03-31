drop database if exists test;
create database test;
use test;

create table user(
	id varchar(50) primary key not null,
	name varchar(50) not null,
	email varchar(50) not null,
	password varchar(50) not null,
	admin bool not null,
	create_at real not null
) engine=innodb default charset=utf8;
