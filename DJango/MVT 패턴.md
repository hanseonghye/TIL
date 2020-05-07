# MVT 패턴 ( Model-View-Template )

mvc패턴에서 view->template, controller->view된 것.

- Model

  데이터베이스에 저장되는 데이터를 의미

- View

  실질적으로 프로그램 로직이 동장하여 데이터를 가져오고 적절하게 처리한 결과를 템플릿에 전달하는 역할

- Template

  사용자에게 보여지는 UI부분

라고 책에 나오는데 인터넷에 찾아보니 `Mode`에서 디비 역할뿐만 아니라 복잡한 로직까지 처리해 주는 것 같다. View는 사용자의 request를 받고 적절한 Model을 호출하며 Model이 주는 response를 알맞은 Template에 전달해 주는 역할을 하는듯 하당.



### MVT패턴에 따른 처리 과정

- 클라이언트로부터 요청을 받으면 URLconf를 이용하여 URL을 분석한다.
- URL 분석 결과를 통해 해당 URL에 대한 처리를 담당한 뷰를 결정한다.
- 뷰는 자신의 로직을 실행하면서 데이퍼베이스 처리가 필요하면 모델을 통해 처리하고 그 결과를 반환받는다.
- 뷰는 자신의 로직 처리가 끝나면 템플릿을 사용하여 클라이언트에 전송한 html 파일을 생성한다.
- 뷰는 최종 결과로 html파일을 클라이언트에게 보내 응답한다.



##### URLconf - URL 정의

urls.py파일에 정의된 url패턴과 매칭되는지 분석한다.



### Model - 데이터베이스 정의

사용될 데이터에 대한 정의를 담고 있는 장고의 클래스.

하나의 모델 클래스는 하나의 테이블에 매핑된다. --> `ORM`기법을 사용하여 가능해짐.

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

이 Person 모델은 장고 내부적으로 SQL명령을 사용하여 다음과 같은 테이블을 생성한다.

```sql
CREATE TABLE myapp_person (
	"id" serial NOT NULL PRIMARY KEY,
	"first_name" varchar(30) NOT NULL,
	"last_name" varchar(30) NOT NULL
);
```



### View - 로직 정의

웹 요청을 받아서 db접속 등 해당 어플리케이션의 로직에 맞는 처리를 하고 그 결과 데이터를 html로 변환하기 위하여 템플릿 처리를 한 후에 최종 html로 된 응답 데이터를 웹 클라리언트로 반환한다.

응답은 html페이지 일수도, 리다이렉션명령일수도, 404 에러 메시지 일 수도 있다.