#drop database sakila;
create database aju;

USE aju;

CREATE TABLE client(
client_id INT,
name VARCHAR(20),
project VARCHAR(20),
PRIMARY KEY(client_id)
);

DESCRIBE CLIENT;

ALTER TABLE CLIENT 
ADD BUDGET DECIMAL(4,2);

ALTER TABLE CLIENT 
DROP COLUMN BUDGET;

INSERT INTO client 
VALUES(1,'PUTHEN', 'website');

INSERT INTO client 
VALUES(4,'infosys');

INSERT INTO client(client_id, NAME)
VALUES(4, 'TCS');

insert into client(PROJECT)
values('app');


SELECT * FROM client;

delete from aju.client where client_id = 1;
update aju.client set client_id = 3 where(client_id = 4);
delete from aju.client where client_id = 4;
SELECT * FROM client;

SELECT name from client where project = 'website';
select name, project from client where project = 'website';
DROP TABLE client;
describe CLIENT;



#------------------------------------------
create table teacher(
teacher_id INT,
subject VARCHAR(20),
age int,
primary key (teacher_id)
);
describe teacher;








CREATE TABLE students (
student_id INT,
name varchar(20) NOT NULL,
subject varchar(20)UNIQUE,
PRIMARY KEY (student_id)
);
describe students;
INSERT INTO students values( 1, 'raj', 'computer');
INSERT INTO students VALUES(2, NULL, 'SCIENCE');
INSERT INTO students(student_id,name) value(3,'aju');
INSERT INTO students values( 4, 'boby', 'computer');


select* from students;
DROP table students;

create table students(
student_id INT auto_increment,
name VARCHAR(20),
subject varchar(20) default 'undecided',
primary key(student_id)
);

describe students;
alter table students drop column sbject;
alter table students add subject varchar(20) default 'undecided';

insert into students values(1, 'aju','ds');
insert into students values(2, 'umar','bcom');
select * from students;
insert into students(name, subject) values('nimya', 'ds');

set sql_safe_updates = 0;
update students 
set subject = 'data'
where subject ='ds';

delete from students where student_id= (1,2);
delete from students;
select* from students;

#delete database
drop database world

