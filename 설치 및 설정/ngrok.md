# ngrok

### 다운

` https://dashboard.ngrok.com/get-started`

### run

` .ngrok http [포트]`





### 장고에서 사용하기

장고에서 바로 위의 `run`을 하면 다음의 에러가 뜬다!


```
DisallowedHost at /
Invalid HTTP_HOST header: '~.ngrok.io'. You may need to add '~.ngrok.io' to ALLOWED_HOSTS.
```



**setting.py** 에서 allowed_hosts 를 열어 주자.

```python
ALLOWED_HOSTS = ['*']
```

