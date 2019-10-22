# ckeditor

## 설정하기

- install

  ` >> pip install django-ckeditor`

- install_apps 에 추가

```python
INSTALLED_APPS = [
    ...
    'ckeditor',
]
```

- media resource 가져오기

  ` >> python manage.py collectstatic `

  그전에 settings.py 파일에 **STATIC_ROOT** 를 설정해 줘야 한다.

- ckeditor 추가

```python
# in settings.py
CKEDITOR_BASEPATH = "/my_static/ckeditor/ckeditor/"
```



## 사용하기

```python
class post(models.Model) : 
    ...
    content = RichTextField()
```

++ 마이그레이션



### 어드민

```python
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from post.models import Post


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget = CKEditorWidget())

    class Meta:
        model = Post

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin )

```

