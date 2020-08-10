# Browser timeout

대부분은 브라우저는 각자의 `timeout`을 가진다.

A로 요청을 한 뒤, 응답을 기다릴때 까지의 시간을 말한다.



브라우저에 따라 이 시간을 변경할 수도 있으며, 크롬의 경우 변경 불가능 하다.

크롬의 경우 5분의 `timeout`을 가진다.

```js
int64_t g_used_idle_socket_timeout_s = 300 // 5 minutes
```





- https://stackoverflow.com/questions/5798707/browser-timeouts