# nginx 띄우기

## install

`$ yum install nginx uwsgi uwsgi-plugin-python`



## uWsgi 설정

```ini
# 프로젝트 경로에 저장, venv 하고 같은 위치에
# /home/프로젝트경로~~/uwsgi.ini

[uwsgi]
master = true
virtualenv = /home/프로젝트경로~~/venv
chdir = /home/프로젝트경로~~
http-socket = :포트
chmod-socket = 666
vacuum = true
die-on-term = true
callable = app # 실행파일명
module = app # application 명
buffer-size=32768
logto = /var/log/uwsgi/%n.log # 로그 위치
```





## nginx 설정

`$ yum install nginx`

```conf
# vim /etc/nginx/conf.d/default.conf

upstream test01 {
        server 127.0.0.1:5000;
}


server {
	...
	
    location / {
        include uwsgi_params;
        uwsgi_pass test01;
    }
    ...
```





- ` $ nginx -t`
- `$ systemctl start nginx`
- 프로젝트 경로에서 위에서 작성한 ini 파일을 기반으로 uwsgi 실행
- `$ uwsgi  uwsgi.ini`  