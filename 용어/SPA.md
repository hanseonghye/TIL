# SPA

`Single Page Application`

- 프론트 엔드와 백엔드의 분리



## SSR

`Server Side Rendering`

- 페이지를 이동할 때마다(특정 url로 데이터를 요청) **서버에서** 새로운 페이지에 대한 응답을(ex) html) 하는 방식
- php, jsp는 대표적인 SSR 프레임워크이다.



## CSR

`Client Side Rendering`

- 최초 요청시에 html, css, js등 각종 리소스를 받아온다.
- 이후에 서버에는 데이터만 요청하고, js로 뷰를 컨트롤한다.
- 따라서 초기 렌더링 속도는 ssr이 빠르지만, 이후 다른 페이지로 이동 시에는 빠른 속도를 보여준다.
- 필요한 데이터만 백엔드에게 요청하기 때문에 서버 부하가 덜하다.





https://velog.io/@ru_bryunak/SPA-%EC%82%AC%EC%9A%A9%EC%97%90%EC%84%9C%EC%9D%98-SSR%EA%B3%BC-CSR



SPA 를 구현하기위해 SSR을 사용할 수도, CSR을 사용할 수도 있고, SSR을 사용한다고 SPA가 되는것도 아니다.