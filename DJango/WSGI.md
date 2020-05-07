# WSGI( Web Server Gateway Interface)

CGI방식은 요청이 들어올 때마다 처리를 위한 프로세스가 생성되는 방식이다. 그래서 짧은 시간에 다량의 요청을 받으면 서버의 부하가 높아져서 프로세스가 멈추거나 다운될 수도 있다. 이러한 단점을 해결하고 파이썬 언어로 어플리케이션을 좀 더 쉽게 작성할 수 있도록 웹 서버와 웹 어플리케이션간에 연동 규격을 정의한 것이 WSGI이다.

:arrow_forward: [CGI 포스팅](https://github.com/hanseonghye/TIL/blob/master/%EC%9A%A9%EC%96%B4/web.md#cgi--common-gateway-interface-)

그래서! 파이썬에서는 wsgi규격만 맞추면 어떤 웹 서버에서도 파이썬을 실행할 수 있다. 예를 들어 장고로 웹 어플리케이션을 작성하면 아파치나 nginx에서도 실핼할 수 있다. 그런데 이 웹서버에는 wsgi처리 기능이 없다. 그래서 이 웹서버와 파이썬 웹 어플리케이션 중간에서 wsgi통신 규격을 처리해 주는 mod_wsgi와 같은 것을 WSGI 서버라 한다.

