# HTTP

웹 서버와 웹 클라이언트 사이에서 데이터를 주고받기 위해 사용하는 통신 방식.

TCP/IP프로토콜 위에서 작동한다.



---

#### http 응답 코드

- 200 (OK) : 정상적인 요청에 정상적으로 응답함.

 - 206 (partial content) : 서버가 일부 콘테츠를 전송하였음.

- 301 (moved permanently) : 현재 요청한 페이지는 영구적으로 다른 주소로 이동됐음.

- 302 (moved temporarily) :현재 요청된 페이지는 임시로 다른 주소로 이동됐음.

- 304 (not modified) : 마지막 접속 요청 후 페이지가 변경되지 않았음.

- 403 (forbidden) : 요청된 주소는 접근이 막혀있음.

- 404 (not found) : 요청된 페이지를 찾을 수 없음.

- 500 (internal server error) : 서버에 오류가 생겨 해당 요청을 처리할 수 없음.



---

#### RPC vs REST

---

#### Web Server vs Web Application Server

##### Web Server

웹 클라이언트의 요청을 받아서 요청을 처리하고 그 결과를 웹 클라이언트에게 응답함.

정적인 페이지 (html, css, js , 이미지 만드로 이루어진 페이지) 파일을 웹 클라이언트에 제공할 때 사용.

ex) Apache httpd, Nginx 



##### Web Application Server (WAS)

웹 서버로부터 동적 페이지 요청을 받아서 요청을 처리함. ( web server ----- 정적페이지 전달 -----> WAS )

was는 실행결과를 웹 서버에 전달해 주며 웹 서버는 전달받은 응답 결과를 웹 클라이언트에 전송한다.

* 동적 페이지 

  동일한 요청에도 상황에( 누가, 언제 ... ) 따라 다른 내용이 반환되는 페이지.

  ex) jsp, asp

ex) Apache Tomcat, Jeus 



was가 정적, 동적 페이지 모두 처리하는 것 보다 정적은 was가 동적은 web server가 처리하는 것이 성능에 좋다. web server는 캐시, 프록시, 프로세스 관리 등 페이지를 처리하는 것 외에도 많은 기능을 한다.

---

