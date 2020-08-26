# 504 Gateway Timeout

프록시를 통한 응답이 늦거나, 제한 시간 보다 통신 연결이 길게 일어날 때 발생하는 에러

nignx의 경우 conf 파일에서 timeout 시간을 늘려주면 된다.



```xml
...
proxy_connect_timeout 300;
proxy_send_timeout 300;
proxy_read_timeout 300;
```



### proxy_connect_timeout

백엔드 서버 접속 제한 시간

http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_connect_timeout



### proxy_read_timeout

백엔드 서버로부터 데이터를 읽을 때의 제한 시간.

이 시간은 전체 응답 지연시간에 적용되지 않는다.

http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_read_timeout



### proxy_send_timeout

백엔드 서버로 데이터를 전송할 때의 제한시간

http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_send_timeout



- https://pat.im/1195