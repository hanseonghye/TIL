# http header

### 네이버의 Response Headers를 공부해보자

![img](./img/img2.png)

- cache control

  - 캐시의 동작을 지시한다.

  - `no-cache, no-store, must-revalidate` 

    위의 헤더들을 통해 캐시를 막을 수 있다. 

- content-encoding

  - 컨텐츠의 압축된 방식을 명시.
  - 응답 컨텐츠를 `br`,`gzip`,`deflate`등의 알고리즘으로 압축해서 보내면, 브라우저가 알아서 해제해서 사용한다. 용량이 줄어들기 때문에 압추을 권장한다. --> 요청이나 응답 전송속도도 빨라지고 데이터 소모량도 줄어든다.

- content-type

  - 컨텐츠의 타입(MIME)과 문자열 인코딩 (utf-8 ...)을 명시한다.
  - `Content-Type: text/html; charset=utf-8`의 경우 현재 메시지 내용이 `text/html`타입이고 `utf-8`로 인코딩했음을 말한다.

- date

  - 응답 시간을 말함.

- p3p

  - Platform for Privacy Preferences
  - 개인정보 보호 관련 표준 기술
  - 해당 사이트에서 취급하는 개인 정보의 레벨이나 성격들을 브라우져에게 알려준다. 
  - 사용자가 인식하고 제어하는 것이 아닌, 기계 차원에서 접속한 사이트의 개인정보 보호 지침을 인식하고 현재 사용자가 설정해둔 허용값과 비교해본 후 허용, 제한, 강등, 금지 등의 처리를 자동으로 하게 하는 것.

- pargma

  - http/1.0에서 `cache-control`헤더가 생기기 전 동일한 역할을 하는 헤더로 사용됨.
  - `Cache-Control : no cache` == `pargma=no-cache`
  - http/1.0을 사용하는 경우에만 사용한다.

- referrer policy

- server

  - 서버 소프트웨어 정보

- status

  - 응답 상태

- strict-transport-security

  - 보안의 중요성에 따라 https 프로토콜만 사용하도록 강제하는 추세이다. --> ex) 구글
  - 클라이언트가 `http`를 요청할 때 `https`를 강제로 redirect하게 전환 하는 것.

  ![img](./img/img3.png)

  - 클라이언트는 서버로 부터 받은 `https` url을 다시 요청한다.
  - `max-age`는 해당 도메인이 앞으로 https만을 사용할 시간을 초단위로 말한것. 위의 63~ 는 2년을 말한다.

- x-frame-options

  - ClickJacking을 방지하는 옵션.
  - Deny 
    - 모든 표시를 거부한다.
  - SAMEORIGIN
    - 동일한 출처에 대한것만 표시한다.
  - ALLOW FROM http://google.com 
    - 해당 url에 대해서만 허용한다.

- x-xss-protection

  - xss 막기 위해 적용
  - xss (Cross-site Scription)
    - 공격자가 공격하려는 사이트에 스크립트를 넣는 기법
    - 공격을 성공하면, 사이트에 접속한 사용자는 삽입된 코드를 실행하게 되면, 의도치 않은 행동을 수행시키거나 쿠키나 세션 토큰등의 민감한 정보를 탈취당하게 된다. 
  - `X-XSS-Protection: 1`
    - 스크립트 공격을 차단하고 웹 페이지는 정상적으로 출력하라.
  - `X-XSS-Protection: 1; mode=block`
    - xss 공격을 탐지하면 웹 페이지를 사용자에게 보여주지 말라

<https://www.zerocho.com/category/HTTP/post/5b3ba2d0b3dabd001b53b9db>

<https://goodjoon.tistory.com/133>

<https://developer.mozilla.org/ko/docs/Web/HTTP/Headers>

<http://webhack.dynu.net/?idx=20161119.001>

