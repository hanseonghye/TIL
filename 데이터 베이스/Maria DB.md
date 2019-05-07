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



### sql 파일 mysql에 넣기

1. backup

2. restore dump

   `$ mysql -u root -p < [somthing.sql]`



### 계정 생성

- 로컬 접근 계정 생성

  `> create user '[계정 이름]'@'localhost' identified by '[password]';`

  `> grant all privileges on [table]  to '[계정이름]@'localhost';` --> 권한 부여

  `> flush privileges;`

- '192.168.1.*'에서 접근하는 계정 생성

  `> create user '[계정 이름]'@'192.168.1.%' identified by '[password]';`

  or

  `> grant all privileges on [table] to '[계정이름]'@'192.168.1.%' identified by '[password]';`





### Group 함수 사용 오류

