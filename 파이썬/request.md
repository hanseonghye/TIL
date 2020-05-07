# request

### 쿼리 스트링 데이터 만들어 요청

```python
import requests

url = "https://www.naver.com/"
res = requests.get(url, params = ["key1":"value1"])
```

:pushpin:query string은 `params`를 사용하지만 body 데이터에 추가할 때는 `data`를 사용한다.

```python
import requests
import json

url = "https://www.naver.com/"
res = requests.post(url, data = ["key1":"value1"])
res2 = reuqests.port(url, data = json.dumps({"key1":"value1","key2":"value2"}))  # 더 좋은 형태.

```

