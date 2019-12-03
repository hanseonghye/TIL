# PostgreSql 띄우기



## 실행 명령어 

```shell
> docker run -p 5432:5432 -e POSTGRES_PASSWORD=비밀번호 -e POSTGRES_USER=사용자이름 -e POSTGRES_DB=디비명 --name 컨테이너이름 -d postgres
```





## 로컬에서 확인하기

### 커널에서 확인하기

- 도커 서버에 접속하기 ?

    ```shell
    > docker exec -i -t 컨테이너이름 bash
    ```

- psql 접속

  ```
  > su - postgres
  > psql --username 사용자이름 --dbname db이름
  ```

  

### 데이터 베이스 툴로 확인하기

postgresql 데이터 베이스 툴을 통해 연결이 됐는지 확인해 보자.

