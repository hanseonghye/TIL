## install nginx in Centos

- 설치
  - `$ sudo yum install nginx`
- nginx  시작
  - `$ sudo systemctl start nginx`
- 상태 확인
  - `$ sudo systemctl status nginx`
  - ` Started nginx - high performance web server.` 가 뜨면 잘 실행 된것.



그밖에 80 port 방화벽을 확인해주자 ~



### nginx 가동을 위한 문법 체크

`# nginx -t`



### 로그

`/var/log/nginx/` 하위에 있다.





### 특정 도메인만 접근 허용하기

```nginx
add_header 'Access-Control-Allow-Origin' "${scheme}://example.com"
```

${scheme}를 통해 `http`와 `https` 모두 받을 수 있다.

