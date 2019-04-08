# URLconf 코딩

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

#### path() 함수

`route`, `view` 2개의 필수 인자와 `kwargs`, `name`  2개의 선택 인자를 요구한다.

- route

  URL 패턴을 표현하는 문자열이다. URL 스트링이라고도 부른다.

- view

  URL 스트링이 매칭되면 호출되는 뷰 함수이다. HttpRequest 객체와 URL 스트링에서 추출된 항목이 뷰 함수의 인자로 전달된다.

- kwargs

  URL 스트링에서 추출된 항목외에 추가적인 인자를 뷰 함수에 전달할 때, 파이썬 사전 타입으로 인자를 정의한다.

- name

  각 URL 패턴별로 이름을 붙여준다. 템플릿 파일에서 많이 사용된다.



