# Index



**non Unique Index**

```sql
create table tab01
(
	c1 number
);

create index my_index on tab01(c1);
```



**Unique Index**

```sql
create table tab02
(
	c1 number unique
);
```



**Primary Key**

```sql
create table tab03
(
	c1 number primary key
);


create table tab04
(
	c1 number constraint tab04_pk primary key
);

```





index가 있는 경우 없는 경우보다 insert 처리 시간이 느려진다. index에 따른 처리를 해야하기 때문. index의 구조가 table 보다 복잡할 수 있다.