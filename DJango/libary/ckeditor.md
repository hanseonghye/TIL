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
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
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





### Cannot set property 'dir' of undefined

그런데 저렇게 설정하고 admin 페이지로 가니 다음과 같은 에러가 났다. 구글링하니까 ckeditor관련 js파일이 있는 폴더를 못찾아서 그렇다고 한다. 즉 settings.py 에서 CKEDITOR_BASEPATH를 잘못했다는 말이다. 

```python
#CKEDITOR_BASEPATH = f'{STATIC_URL}/ckeditor/ckeditor/'
CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
```

나의 경우 이렇게 바꿔주니 작동했다!