# next.js 란

React JS를 이용한 서버 사이드 렌더링 프레임워크



## 시작하기

```shell
$ yarn init -y
$ yarn add next react react-dom
$ mkdir pages
$ npm run dev
```

각 route에 해당된 파일은 반드시 `pages`라는 디렉토리 안에 들어가야 하기 때문에 `pages` dir 을 반드시 생성.





## 기능

- 서버 사이드 렌더링
- 코드 스필릿
- 페이지를 기반으로 간단한 클라이언트 사이드 라우팅
  - next는 기본적으로 SSR을 제공하는데, 추가적으로 간단하게 CSR을 적용할 수도 있다.
  - 첫 페이지는 백엔드 서버에서 렌더링한다. 그 다음 부턴 csr을 적용하여 필요한 데이터 부분만 갱신한다.
- Hot Module Replacement



## SSR

모든 요청에 대해 서버에서 렌더링을 진행하지 않는다. 

초기 렌더링만 서버가 담당하고, 그 이후에는 `next/router`을 이용하여 클라이언트에서(xxx.js 파일을 통해) 렌더링을 진행한다.

예시는 다음과 같다.

1. 유저가 브라우저에접속 (ex. /index)
2. 미리 실행되고 있는 node 서버가 요청을 받고 서버 렌더링을 한다.
3. 만들어진 html을 브라우저에게 보낸다.
4. 브라우저는 받은 html을 그린다.
5. html에 기능을 부여할 `index.js`파일을 다운받고 이를 브라우저에 반영한다.
6. 추가적으로 다른 `xxx.js`파일이 다운받아지면 해당 사항을 반영한다.



https://jcon.tistory.com/124

https://blueshw.github.io/2018/04/15/why-nextjs/

https://www.sarah-note.com/%ED%81%B4%EB%A1%A0%EC%BD%94%EB%94%A9/posting2/

