# Model 코딩

> 모델 작업은 데이터 베이스에 테이블을 생성하도록 해주는 작업이다.

### 테이블 정의

장고에서는 테이블을 하나의 클래스로 정의하고 테이블의 컬럼은 클래스의 변수로 매핑한다. 

테이블 클래스는 `django.db.models.Model`클래스를 상속 받아 정의하고, 각 클래스 변수의 타입도 장고에서 미리 정의된 필드 클래스를 사용한다.

- 필드 클래스

  - ` models.CharField(maxlength = 200)`, `models.DateTimeField('date published')`...

  - PK(Primary Key)는 클래스에 지정해 주지 않아도, 항상 PK에 대한 속성을 `not null` 및 `Autoincrement`로, 이름은 `id`로 해서 자동으로 만들어 준다.
  - `__str__` 메소드는 객체를 문자열로 표현할 때 사용하는 함수이다. Admin사이트나 장고 쉘 등에서 테이블 명을 보여줘야 할 때가 있는데 이때 사용한다.



### 데이터 베이스 변경사항 반영

테이블의 신규 생성, 정의 변경 등 디비에변경이 필요한 사항이 있으면, 이를 디비에 실제로 변경해 주는 작업을 해야한다. 

> python manage.py makemirations
>
> python manage.py migrate

- 마이그레이션 (migrations)

  테이블 및 필드의 생성, 삭제, 변경 등과 같이 디비에 대한 변경사항을 알려주는 정보. 장고에서는 `makemigrations`명령에 의해 마이그레이션 파일들이 생성되고 이 파일들을 이용해 `migrate`명령으로 디비에 테이블을 만들어 준다.

### Admin 사이트에 테이블 반영

```python
#bookmark/admin.py

from django.contrib import admin
from bookmark.models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title','url')

admin.site.register(Bookmark,BookmarkAdmin)
```

`BookmarkAdmin` class는 `Bookmark`class가 Admin사이트에서 어떤 모습으로 보여줄지를 정의하는 클래스 이다. Bookmark 내용을 보여줄 때, title과 url을 화면에 출력하라고 지정한다 그리고 `admin.site.register()`함수를 사용해 `Bookmark`와 `BookmarkAdmin`클래스를 등록한다.