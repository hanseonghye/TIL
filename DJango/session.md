# session

- `installed_apps`에 `django.contrib.sessions`를 추가한다.

### view에서 세션 사용하기

`session middleware`가 실행되면 모든 장고 view함수에서 첫번째 인자값으로 전달되는 HttpRequest들은 모두 dict 타입인 session 속성을 가지게 된다.

view의 어느 부분에서라도 `request.session`을 통해 수정하고 읽을 수 있다.

`request.session['세션 명']`으로 접근할 수 있다.



### SESSION_EXPIRE_AT_BROWSER_CLOSE

`settings.py`파일에 `SESSION_EXPIRE_AT_BROWSER_CLOSE =True`로 설정한다. 사용자가 브라우저를 닫으면 바로 세션 값을 지운다.

`False`인 경우는 설정된 기간만큼 세션이 남아있게 된다.



<http://egloos.zum.com/blackyyy/v/5314617>

