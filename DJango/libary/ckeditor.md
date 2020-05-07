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

- static resource 가져오기

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

admin 처리를 안해줘도 자동으로 부여해 주는것 같다. 근데 확실히 하고 싶어서 추가해 줬다.





## 이미지 업로드



### 설정하기

#### settings.py

```python
INSTALLED_APPS = [
    ...
    'ckeditor',
    'ckeditor_uploader',
]

CKEDITOR_UPLOAD_PATH = 'uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```



#### urls.py

```python
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from myblog.views import HomeView

urlpatterns = [
    ...
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


```



이미지 업로드 기능을 사용할려면 model에서 부여한 Ckeditor 속성을 다른걸로 해줘야 한다.

```python
class post(models.Model) : 
    ...
    content = RichTextUploadingField()
```

그리고 어드민 부분도 그에 따라 바꿔줘야 한다. upload 부분에 따른 ckeditor 속성을 찾지 못해서 그에 따른 처리를 못해줬다. 하지만 따로 admin을 추가해 주지 않아도 model에 저렇게 선언해 주는것 만으로 업로드 기능을 제공해 주는 것같다.

따라서 변경된 admin은 다음과 같다.

```python
from django.contrib import admin
from post.models import Post


admin.site.register(Post) 
```





### Cannot set property 'dir' of undefined

그런데 저렇게 설정하고 admin 페이지로 가니 다음과 같은 에러가 났다. 구글링하니까 ckeditor관련 js파일이 있는 폴더를 못찾아서 그렇다고 한다. 즉 settings.py 에서 CKEDITOR_BASEPATH를 잘못했다는 말이다. 

```python
#CKEDITOR_BASEPATH = f'{STATIC_URL}/ckeditor/ckeditor/'
CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
```

나의 경우 이렇게 바꿔주니 작동했다!