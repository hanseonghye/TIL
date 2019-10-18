# tagging

###  install

` >> pip install django-tagging`

### 적용하기

- install_app 에 추가

```python
INSTALLED_APPS = [
    ...
    'tagging.apps.TaggingConfig',
]
```



```python
from tagging.fields import TagField

class Post(models.Model):
    ...
    tag = TagField()
```

 ++ 마이그레이션 해주기





django-tagging은 업데이트가 끊겼다고 한다.

django-taggit을 사용하겠다~