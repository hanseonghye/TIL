# 2.4 개발 코딩하기-URLConf

```python
# myjango/mysite/urls.py

from django.contrib import admin
from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    path('admin/', admin.site.urls),

   path('bookmark/', BookmarkLV.as_view(), name='index'),
   path(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]
```



# 2.5 개발 코딩하기 - 뷰

URLconf에서 지정한 클래스형 뷰를 개발하자.

```python
# myjango/bookmark/views.py

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
	model = Bookmark

class BookmarkDV(DetailView):
	model = Bookmark
```

- BookmarkLV
  - Bookmark 테이블의 레코드 리스트를 보여주기 위한 뷰로서 ListView 제너릭 뷰를 상속 받는다.
  - 다음 두가지는 명시적으로 지정하지 않아도 장고에서 디폴트로 알아서 지정해 주는 속성이다.
    1. 컨텍스트 변수로 object_list를 디폴트 값으로 html 페이지에 전달한다.
    2. 모델명_list.html [ 여기서는 bookmall_list.html ] 형식의 템플릿 파일을 리턴한다. 따라서 bookmall_list.html 파일이 템플릿 폴더에 있어야 한다.
- BookmarkDV
  - Bookmark 테이블의 특정 레코드에 대한 상세 정보를 보여주기 위한 뷰로서, DetailView 제너릭 뷰를 상속받는다.
  - 다음 두가지는 명시적으로 지정하지 않아도 장고에서 디폴트로 알아서 지정해 주는 속성이다.
    1. 컨텍스트 변수로 object를 사용한다.
    2. 템플릿 파일을 모델명_detail..html 을 사용한다.

