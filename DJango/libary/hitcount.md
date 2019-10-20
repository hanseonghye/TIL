# hitcount

### install

`>> pip install django-hitcount `

```python
# settings.py
INSTALLED_APPS = (
    ...
    'hitcount'
)
```

### model

```python
from hitcount.models import HitCountMixin

class Post(models.Model, HitCountMixin):
```

migration을 해줘야 하는데 해당 app을 해주니까 안된다. 전체 프로젝트를 makemigrations 해줬다.

### view

DetailView를 사용하던 view 수정

count_hit = True를 선언해줌.

```python
from hitcount.views import HitCountDetailView

class PostDV(HitCountDetailView):
    ...
    count_hit = True
```

