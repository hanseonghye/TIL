# 504 Gateway Timeout

프록시를 통한 응답이 늦거나, 제한 시간 보다 통신 연결이 길게 일어날 때 발생하는 에러

nignx의 경우 conf 파일에서 timeout 시간을 늘려주면 된다.



```xml
...
proxy_connect_timeout 300;
proxy_send_timeout 300;
proxy_read_timeout 300;
```





- https://pat.im/1195