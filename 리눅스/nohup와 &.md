# nohup 와 &

## &

`CLI`를 통해 백그라운드에서 프로그램을 실행시킬 때 사용.

터미널이 꺼지면 해당 프로그램도 꺼질 수 있다. 그래서 나온게 `nohub`

( 그런데 `&`도 많은 옵션이 생기면서 `nohub`와 같은 기능을 할 수 있다고 한다.)



## nohup 

**장고 백그라운드에서 실행 시키기**

`# nohup python manage.py runserver &`

**종료시키기**

`#ps -ef | grep python`

`#kill -9 PID번호`