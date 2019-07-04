# 서블릿과 JSP

## JSP (Java Server Page)

- html 코드 내에 java 코드를 포함하는 형태.
- JSP 페이지가 처음 호출됐을 때, JSP 엔진은 JSP 코드를 서블릿으로 변환하고 컴파일 한다. 그리고 서블릿 엔진이 서블릿을 구동한다.

## 서블릿(Servlet)

- 서버에서 동작하는 Java 클래스
- HttpServlet 클래스를 상속한다.

### 서블릿 작성 방법

- HttpServlet 클래스를 상속받는다.
- HttpServlet 클래스의 doGet 메소드를 Overriding하고 GET 방식을 사용하는 요청을 처리한다. doPost 메소드 또한 동일한 방식을 적용한다.
- doGet과 doPost 메소드는 웹 서버가 전달한 두 개의 객체, HttpServletRequest, HttpServletResponse 객체를 인자로 받는다.

### 서블릿 라이프 사이클

- 서브는 init 메소드를 통해 서블릿을 구동하고 초기화 한다.
- service 메소드를 호출해서 서블릿이 브라우저의 요청을 처리하도록 한다.
- service 메소드는 특정 http요청(get,post 등)을 처리하는 다른 메소드(doGet,doPost 등)을 호출한다.
- 서버는 destroy메소드를 통해서 서블릿을 제거한다. 이러한 경우는 서버가 중단되거나 특정 시간동안 대기상태로 유지되는 경우에 발생한다.

### web.xml

- WEB-INF 디렉터리에 위치하고, 서블릿 엔진이 구동하면서 web.xml을 읽어 들인다.
- XML 태그를 사용하여 요소(element)를 정의한다.
- 파일을 수정하면 톰캣을 재 구동해야만 변경된 내용이 반영된다.

### xml 요소

```xml
<web-app>
    <context-param>
        <param-name>dbName</param-name>
        <param-value>stcdb</param-value>
    </context-param>

    <servlet>
        <servlet-name>Email6 list</servlet-name>
        <servlet-class>email6.EmailServlet</servlet-class>
        <init-param>
            <param-name>filename</param-name>
            <param-value>/UserEmail.txt</param-value>
        </init-param>
    </servlet>
</web-app>
```

- <web-app>
  - root-element이다. 모든 다른 요소들은 루트 요소에 포함되어야 한다.
- <context-param>
  - 모든 서블릿에서 사용가능한 파라미터를 정의한다.
- <servlet>
  - 어플리케이션의 특정 서블릿을 식별한다.
- <servlet-name>
  - web.xml파일에서 사용되는 서블릿의 이름을 정의한다.
- <servlet-class>
  - 서블릿 클래스의 실제 패키지와 클래스 명을 나타낸다.
- <init-param>
  - 서블릿 초기화 파라미터(ex encoding)의 이름/값 쌍을 정의한다.



## Forward vs Redirect

### forward

- 동일 서버의 다른 자원 (jsp, 서블릿 등)에게 제어를 넘긴다. 동일한 서버에서 요청이 처리되고, 지정된 자원에서 request 객체와 response 객체에 접근한다.
- servletContext 객체의 getReqestDispatcher 메소드를 사용해서 ReuqestDispatcher 객체를 얻는다.
- servletContext 객체를 얻기 위해서는 HttpServlet 클래스의 getReqestDispatcher 메소드를 사용한다.

### redirect

- 다른 서버의 자원에 제어를 넘길때 사용할 수 있다.
- 지정된 자원에서 request, response 객체에 접근할 수 없다.

#### 공통점

- 다른 페이지를 호출하는 방법으로 사용된다.

#### 차이점

- forward
  - 새로운 페이지는 이전 페이지에서 처리하던 것과 같은 요청을 처리하고 응답하여 브라우저는 하나 이상의 페이지가 연관된 것을 알 수 없다.
- redirect
  - 첫번째 페이지는 브라우저에게 새로운 페이지로 다시 요청해야 한다는 내용의 응답을 보낸다. 브라우저는 이 응답을 받으면 새로운 페이지로 다시 요청을 보낸다.

### 세션 처리

1. 최초 http 요청

   브라우저에서 JSP 또는 서블릿을 요청한다. 서블릿 엔진은 세션 객체를 생성하고 ID를 할당한다.

2. 최조 http 응답

   서버는 요청된 페이지와 세션에 할당된 id를 함께 보낸다.

3. 이후 http 요청

   브라우저에서 웹 페이지를 요청한다. 서블릿 엔진은 세션 ID를 이용해 브라우저에 할당된 세션 객체를 확인한다.