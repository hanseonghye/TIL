# mysql

> mysql 실행

mysql -u root -p

> database 모두 보기

show database;

> table 보기

desc table_name;  





## make dump file

`mysql -u USERNAME --password=PASSWORD --database=DATABASE --execute='SELECT FIELD, FIELD FROM TABLE LIMIT 0, 10000 ’ -X > file.xml`



https://stackoverflow.com/questions/11631128/how-to-export-a-specific-column-data-in-mysql