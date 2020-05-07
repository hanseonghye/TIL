## install nginx in Centos

- 설치
  - `$ sudo yum install nginx`
- nginx  시작
  - `$ sudo sysctmctl start nginx`
- 상태 확인
  - `$ sudo sysctmctl status nginx`
  - ` Started nginx - high performance web server.` 가 뜨면 잘 실행 된것.



그밖에 80 port 방화벽을 확인해주자 ~



### nginx 가동을 위한 문법 체크

`# nginx -t`



### 로그

`/var/log/nginx/` 하위에 있다.