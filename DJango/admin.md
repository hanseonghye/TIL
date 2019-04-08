# admin

### 관리자 생성

> python3 manage.py createsuperuser

### admin 페이지

![img](./img/django1.png)

기본으로 장고에서 제공하는 `Groups`와 `Users`테이블을 포함하여 앞으로 만들 db 테이블에 대한 데이터의 입력, 변경, 삭제 등이 가능한 페이지이다.



### admin 사이트에 테이블 반영

```python
# admin.py

from django.contrib import admin
from polls.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
```

`models.py` 모듈에서 정의한 클래스를 `admin.site.register()` 함수를 사용하여 등록해 준다.

이와 같이 테이블을 새로 만들떄는 model을 정의한 파일과 admin파일을 함께 수정 해야 한다.