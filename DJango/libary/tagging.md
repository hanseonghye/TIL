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

- model에 적용

```python
from tagging.fields import TagField

class Post(models.Model):
    ...
    tag = TagField()
```

 ++ 마이그레이션 해주기

