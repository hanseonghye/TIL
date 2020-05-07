# migration



## 마이그레이션 파일 지우기

기존의 디비는 유지하면서 마이그레이션 파일을 지우고 싶을 때라던지 기타 등등의 상황에서

1. 마이그레이션 파일을 지운다.
2. `$ python manage.py makemigrations`
3. `$python manage.py migrate --fake-initial`

makemigrations한 뒤에, `--fake`로 마치 `migrate`를 한 것 처럼 해준다.





## 마이그레이션 이력

`>> python manage.py showmigrations app_name`

반영된 마이그레이션 영역을 볼 수 있다. 아직 반영전이라면 해당 마이그레이션 파일을 삭제해도 영향끼치지 않는다.