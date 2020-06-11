# 8 버전에서 extension 추가

9버전 이하의 postgresql 에서는 `CREATE EXTENSION XXX` 명령어가 먹히지 않는다. 

8버전의 경우 다음처럼 하니까 됐당



1. 먼저 해당 모듈이 설치되어 있어야 하고, 모듈.sql 파일을 가지고 있어야 한다.
2. 모듈.sql 파일이 있는 dir (보통 pgsql경로/share/contrib/)에서  db접속
3. `database=# \i XXX.sql`



- https://dba.stackexchange.com/questions/1883/how-do-i-install-pgcrypto-in-postgresql-8-4