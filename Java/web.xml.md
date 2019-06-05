# web.xml

- display-name

  - url로 들어갈 최상위 path를 설정

- welcome-file-list

  - 서버로 요청이 들어왔을 때, 표시할 파일을 표시. 차례대로 우선순위를 가진다.

- context-param

  - Servlet context의 파라미터를 선언해주는 부분. 전역변수를 설정하는 느낌.
  - param-name : 파라미터의 이름
  - param-value : 파라미터를 호출했을 때의 값

  

  - contextConfigLocation
    - dao, vo 등과 같은 부분이 여기 등록돼 있다.
    - dispatcherServlet 보다 먼저 호출된다.

- listener

  - application listener bean을 가리키기 위한 부분. 해당 bean은 어플리케이션에 등록돼 있어야한다.

- filter

  - 웹 어플리케이션에서 사용하는 filter를 선언하는 부분.
  - 어떤 필터를 사용할것인지 설정한다. 대표적으로 encodingFilter가 있다.
  - filter-name : filter-mapping Element와 매핑하기 위한 변수
  - filter-class : 사용할 클래스의 정규화 된 이름을 나타내는 변수
  - init-param : filter 에서 사용할 name-value 쌍을 선언하는 부분

- filter-mapping 

  - filter tag로 설정한 filter를 url이나 servlet를 통해 어디에 적용할 것인지를 선언. --> filter에서 설정한 속성을 어느 클래스, url에 설정할 것인가.
  - filter-name : filter element와 매핑하기 위한 변수.
  - url-pattern : filter를 적용할 url을 선언하는 부분
  - servlet-name : filter를 적용할 servlet를 선언하는 부분.

- servlet

  - servlet를 선언할 때 사용하는 태그 ( == 서블릿 추가)

  - 흔히 spring에서 dispatcherServlet을 선언할 때 사용한다.

  - servlet-name : 사용할 servlet의 이름을 지정.

  - servlet-class : 사용할 클래스의 정규화 된 이름을 나타내는 변수

  - init-param : servlet에서 사용할 name-value 쌍을 선언하는 부분.

    ```xml
    <servlet>
    		<servlet-name>spring</servlet-name>
    		<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    	</servlet>
    ```

    이렇게 설정하면 `WEB-INF/spring-servlet.xml` 파일을 servlet-class의 속성으로 서블릿에 추가한다는 의미이다.

    만약 [servlet-name]-servlet.xml 파일이 web.xml 파일과 같은 경로에 있다면 따로 설정을 하지 않아도 자동으로 로드된다. 같은 경로에 없다면 init-param으로 설정을 해줘야 한다. 

- servlet-mapping

  - servlet과 url사이의 매핑을 정의하는 부분.

  - 아래의 경우 `.html`로 들어오는 모든 요청은 dispatcherServlet으로 들어오게 된다.

    ```xml
    // .viii로 끝나는 모든 URL에 dispatcherServlet을 매핑
    <servlet-mapping>
        <servlet-name>dispatcherServlet</servlet-name>
        <url-pattern>*.html</url-pattern>
    </servlet-mapping>
    
    ```

    

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns="http://java.sun.com/xml/ns/javaee"
	xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd"
	version="2.5">
	<display-name>mysite2</display-name>
	<welcome-file-list>
		<welcome-file>index.html</welcome-file>
		<welcome-file>index.htm</welcome-file>
		<welcome-file>index.jsp</welcome-file>
		<welcome-file>default.html</welcome-file>
		<welcome-file>default.htm</welcome-file>
		<welcome-file>default.jsp</welcome-file>
	</welcome-file-list>


	<!-- Dispatcher server (front controller) -->
	<servlet>
		<servlet-name>spring</servlet-name>
		<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
	</servlet>

	<servlet-mapping>
		<servlet-name>spring</servlet-name>
		<url-pattern>/</url-pattern>
	</servlet-mapping>

	<listener>
		<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
	</listener>

	<context-param>
		<param-name>contextConfigLocation</param-name>
		<param-value>classpath:applicationContext.xml</param-value>
		<!--  <param-value>/WEB-INF/applicationContext.xml</param-value>-->
	</context-param>

	<filter>
		<filter-name>encodingFilter</filter-name>
		<filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
		<init-param>
			<param-name>encoding</param-name>
			<param-value>UTF-8</param-value>
		</init-param>

		<init-param>
			<param-name>forceEncoding</param-name>
			<param-value>true</param-value>
		</init-param>
	</filter>

	<filter-mapping>
		<filter-name>encodingFilter</filter-name>
		<url-pattern>/*</url-pattern>
	</filter-mapping>


	<!-- 공통 에러 페이지 -->
	<error-page>
		<error-code>404</error-code>
		<location>/WEB-INF/views/error/404.jsp</location>
	</error-page>

	<error-page>
		<error-code>500</error-code>
		<location>/WEB-INF/views/error/500.jsp</location>
	</error-page>

</web-app>
```

<https://jayviii.tistory.com/7>