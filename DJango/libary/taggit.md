# taggit

### install

`>> pip install django-taggit`

`>> pip install django-taggit-templatetags`



### 적용하기

- install apps에 추가

```python
INSTALLED_APPS = [
    ...
    'taggit',
]
```

- model에 적용

```python
from taggit.managers import TaggableManager

class Post(models.Model):
    ...
     tags = TaggableManager()
```

++ 마이그레이션

