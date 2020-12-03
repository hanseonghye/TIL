# AJAX (Asynchronous JavaSript And XML)

JS 라이브러리 중 하나. JS의 비동기 통신을 사용하여 구현됨.

브라우저가 가지고 있는 XMLHttpRequest 객체를 이용하여 전체 페이지를 새로 고치지 않고도 페이지의 일부만을 위한 데이터를 로드하는 기법.

- 비동기 통신

  웹페이지를 리로드하지 않고 데이터를 불러오는 방식. 이 방식을 통해 스크립트, 이미지 등을 재요청하는 등의 리소스 낭비가 발생하지 않는다.







### processData

default값은 `true`

`ajax`를 사용하여 데이터를 전송할때, 기본적으로 key와 value값을 `query string`으로 변환해서 보낸다.

이때 `processData`가 `false`로 되어있으면 `query String`으로 설정하지 않는다.