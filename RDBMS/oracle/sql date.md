# 날짜형 DATA Type

**date --> DATE**

기원전 4712년 부터 9999년까지의 연,월,일,시,분,초의 자료를 저장.


**예시**
```
insert into dateTable(d1) values(to_date('20180105','YYMMDD));

select to_char(d1,'YY/MM/DD') from dateTable;
```

**date type 변경**
```
alter session set nls_Date_format='YYYY.MM.DD HH24:MI:SS';
```

**date type 확인**
```
select sysdate from dual;
 ```
