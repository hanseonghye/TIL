# Maria DB

### 계정 생성

`$ groupadd [group name]`

`$ useradd -M -g  계정명 그룹명 ` ?? 미확실 `todo`



- create database [db]
- use [db]



### table

- show tables
- describe [table]
- desc [table]
- drop table [table]
- load data local infile '경로'  into table [table]



### select 

- select * from [table] where [col] like '[]'
- select concat(first_name , ' ', last_name ) as '이름' from ~
- HAVING
  - Group을 거친 값에대한 조건을 기술

### delete

- delete from [table]

### alter

- alter table user add column role enum('ADMIN','USER') default 'USER' NOT NULL after gender;



### sql 파일 mysql에 넣기

1. backup

2. restore dump

   `$ mysql -u root -p < [somthing.sql]`
   
   `$ cat *.sql | mysql -u root -p [database]



### 계정 생성

- 로컬 접근 계정 생성

  `> create user '[계정 이름]'@'localhost' identified by '[password]';`

  `> grant all privileges on [table]  to '[계정이름]@'localhost';` --> 권한 부여

  `> flush privileges;`

- '192.168.1.*'에서 접근하는 계정 생성

  `> create user '[계정 이름]'@'192.168.1.%' identified by '[password]';`

  or

  `> grant all privileges on [table] to '[계정이름]'@'192.168.1.%' identified by '[password]';`





## join

### inner join

`join`이라하면 보통 `inner join`을 뜻함

- equi join == join on

  - 컬럼에 있는 값들이 정확하게 일치하는 경우에 **=** 연산자를 사용하여 조인
  - 일반적으로 `PK-FK`관계에 의하여 `join`이 성립
  - `where`절 혹은 `on`절을 이용
  - 같은 이름의 칼럼이 조인대상 테이블에 존재하면 반드시 컬럼 이름 앞에 테이블 이름을 밝혀 주어야 한다.
  - `join`을 위한 테이블이 **n**개라고 하면 `join`을 위한 최소한의 조건은 `n-1`이다.

  ```sql
  select a.first_name, b.title
  	from employees a
      join titles b on a.emp_no = b.emp_no
  		and a.gender = 'F';
  ```

  

- natural join  --> 쓰면 안됨

  동일한 타입과 이름을 가진 컬럼을 조인 조건으로 ~

  조인에 이용되는 컬럼은 명시하지 않아도 자동으로 조인에 사용된다.
  
  ```sql
  select a.first_name, b.title
  	from employees a
      join titles b
  	where gender = 'F';
  ```
  
  
  
- join ~using

  natural join에서 특정 칼럽을 명시하는 경우
  
  ```sql
  select a.first_name, b.title
  	from employees a
      join titles b
  	using  (emp_no)
  	where a.gender = 'F';
  ```
  

### outer join

- left
- outer
- both



### subquery

> 하나의 SELECT 문 안에 포함되어 있는 SELECT 문장
>
> 여러 절에서 사용할 수 있으나 SELECT문안에 포함되어 있는 것이 일반적





---

---

```sql
-- DDL

use employees; 

drop table member;
create table member(
	no int not null primary key auto_increment,
	email varchar(50) not null default '',
    passwd varchar(64) not null,
    name varchar(25),
    dept_name varchar(25)
);


alter table member add juminbunho char (13) not null after email ;
alter table member drop juminbunho; 

alter table member add join_date datetime not null;
alter table member change no no int unsigned not null auto_increment;

alter table member change dept_name department_name varchar(25);
alter table member change name name varchar(10);

-- alter table member rename user;
-- drop table member;



--------------------- insert

insert
	into member (passwd, name, department_name)
	values(password('1234'),'한성혜','시스템개발팀');
    
insert
	into member(join_date, name, passwd, department_name)
	values(now(), '한성혜2', password('1234'),'시스템개발팀');

update member 
	set join_date = (select now())
	where no = 1;
    
update member
	set join_date = now(),
		name = 'han seonghye hye'
	where no =1;

delete from member where no =1;

select * from member;
```

