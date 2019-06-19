# :smiling_imp:CSRF 공격 :smiling_imp:

> Cross Site Request Forgery : 사이트 간 요청 위조

사용자(==희생자)가 현재 로그인돼 있는 취약한 사이트에 자신도 모르게 악의적인 요청을 전송하도록 만드는 공격.

희생자는 의도치 않게 웹서버(ex. 페이스북, 네이버 등 )에 악의적인 내용이 담긴 코드를 전송(요청)하게 되며, 웹 서버는 그 요청을 받아 들인다.

2008년 1080만 명의 개인정보가 유출된 옥션 해킹사건에 사용된 공격 기법이다.



## 공격법

![img](./img/img14.png)

1. 공격자는 게시판에 사용자(== 희생자)가 관심을 가진 만한 게시글에 CSRF 공격 스크립트를 포함하여 등록한다.

2. 사용자는 해당 게시글을 클릭하게 되고 자신도 모르게 서버에 악영향을 끼치는 요청을 하게 된다.

   

## 공격 예제 :memo:

![img](./img/img7.png)

이 사이트를 보던 해커는 게시판 페이지에서 번호가 게시글 테이블의 번호와 같다는 점을 발견했고 이것을 이용하여 CSRF 공격을 하기로 했다.



해커는 회원가입을 한뒤 직접 게시글을 작성하고 수정하면서 게시글 수정 request에는 다음과 같은 값들이 필요한것을 확인했다.

![img](./img/img9.png)

이러한 점을 확인한 뒤 관리자의 게시글을 수정하기로 마음먹었다.

이 공격의 타겟은 해당 게시글(84번 게시글)의 글쓴이인 관리자 이다.

csrf 공격은 이 사이트에 이미 피해자가 될 유저의 세션이 저장돼 있다는 점을 이용하여 해당 요청과 같은 요청을 할 수 있다.



공격을 하기 위한 조건은 

1. 관리자가 로그인한 상태여야 한다.

   그래야 세션에 관리자가 저장돼 있고 관리자의 글을 수정할 수 있다.

2. 관리자가 글을 수정하는 request를 실행하게 해야 한다.

   이것을 하기 위해 관리자가 알지 못하는 곳에 request form을 넣어야 한다.

   다음과 같이 구현할 수 있다.

   ![img](./img/img10.png)

   

![img](./img/img11.png)

수정을 완료한 뒤 관리자가 해당글을 보고 버튼을 클릭하면 post 요청이 가고 다음과 같이 글이 수정된다.

![img](./img/img12.png)



get 요청의 경우 post 요청 보다 더욱 쉽게 공격 가능하다. 또한 html에서 img 태그의 src 값으로 get 요청의 url을 넣음으로써 공격하는 방법도 있다. 대부분의 페이지가 이미지의 값을 필터링하지 않는 다는 점을 이용했다.

## 대응 방안 :+1:

### CSRF 토큰 사용

요청을 할때 파라미터 값으로 서버와 약속된 정해진 무작위 값을 전달함으로써 믿을 수 있는 요청이라는 것을 인증하는 것이다.

1. 클라이언트가 폼이 존재하는 html 페이지를 요청한다.

2. 서버는 응답에 두 가지 토큰을 포함시켜 반환한다. 이 두 값은 해커가 추측할 수 없도록 무작위로 생성된다.
   1. 쿠키에 저장되는 값.
   
      타 도메인에서 쿠키의 값을 조회 못한다는 점을 이용
   
   2. form 필드에 해당하는 값.

    ```java
    // 토큰 값 생성 및 전달
    String csrfToken = UUID.randomUUID().toString();
    session.setAttribute(Session.CSRF_TOKEN, csrfToken);
    ```
   
   ```html
   <form action='', method='post'>
       <input type="hidden" name="csrfToken" value="${sessionScope._CSRF_TOKEN_}" />
           ...
   </form>
   ```
   
3. 클라이언트가 폼을 제출할 때, 두개의 토큰이 모두 서버로 재 전송돼야 한다. 만약 두 토큰 중 하나라도 일치하지 않으면 서버는 해당 요청을 허용하지 않는다.
   ```java
   // 토큰 값 비교
   String storedCsrfToken = (String) session.getAttribute(Session.CSRF_TOKEN);
   String requestedCsrfToken = request.getParameter("csrfToken");
   
   if( storedCsrfToken == null || !storedCsrfToken.equals(requestedCsrfToken)){
       return "/board";
   }
   ```


###  Referer 체크

Referer는 http 헤더에 있는 정보로, 해당 요청이 요청된 페이지의 정보를 가지고 있다. 

네이버에서 > 네이버 웹툰 버튼을 클릭하면 다음과 같은 Referer 값을 가진다.

![img](./img/img13.png)

하지만 최근은 Referer 값을 쉽게 변조할 수 있어서 이 기술만으로 공격을 막을 수는 없다.



### 사용자와 상호 처리 기능 적용

CAPTCHA(사용자가 실제 사람인지 컴퓨터 프로그램 인지를 구별하는 기술)와 같은 사용자 상호 처리 가능한 기법을 적용한다. 뚫기 매우 쉬워 보이지만 정교한 CAPTCHA는 [바둑을 인공지능으로 풀어내는 것](https://namu.wiki/w/알파고) 이상으로 어렵다고 한다.

![img](./img/img6.png)

### 재인증 요구

재인증을 통해 안전하게 실제 요청 여부를 확인 하도록 설계한다.

예를 들어서 비밀번호 변경의 경우 변경할 비밀번호만 적는 것이 아니라 현재 비밀번호를 먼저 적는 절차를 넣는 것이다.



<https://best421.tistory.com/64>

<http://www.egocube.pe.kr/Translation/Content/asp-net-web-api/201402030001>