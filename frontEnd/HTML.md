# HTML

### 문서형 정의 - Doctype

HTML5, XHTML, HTML의 세가지 문서 유형이 존재. 유형에 따라 마크업 문서의 요소와 속성등을 처리하는 기준이 된다.

문서형 정의를 생략하는 경우 웹브라우저가 비표준 모드로 렌더링 되어 크로스 브라우징에 어려움을 겪는다. 문서형 정의는 html문서의 최상위에 위치해야한다.

- 크로스 브라우징

  웹 표준 기술을 적용하여 서로 다른 OS, 플랫폼에서도 구현되는 기술을 말한다. html5를 사용한다는 것을 알려주자!

- html5를 사용한다는 것을 알려주자

  ```html
  <!doctype html>
  ```


### 공간

세가지 종류의 공간이 있다! 

1. Block 

   한 줄을 통째로 차지

   - div --> but 설정(css)을 통해 Inline-block처럼 구현할 수 있다.

     ```html
     <div style="display:inline-block; width:50%; height:auto">
     </div>
     ```

2. Inline

   내용물의 길이만큼 공간을 차지

   - span

3. Inline-block

   Inline + 각자의 높이와 너비를 가지고 있다. --> 설정을 통해

대부분 설정이 가능한 inline-block를 사용한다.



### 시맨틱 태그

div가 너무 많아져서 무슨 역할을 하는지 알아보기 힘들다. 그래서 명확한 역할을 하는 div를 따로 분류했다. :+1:

- header

  페이지 소개나 제목을 담당

- footer

  저작권 정보나 사이트 제공자 정보를 넣는 공간

- main

  몽통 부분. 한 페이지 당 하나만 사용해야 한다. 

- nav

  네비게이션 바

- section

  기능에 따른 구분. ex) 내용 부분, 댓글 부분

- article

- aside

https://www.zerocho.com/category/HTML&DOM/post/5821b15f577d375e5c73bbc5



### Entity

- `&lt;`  '&lt;'를 html에서 표현하는 방법
- `&nbsp` '&nbsp;' 띄어쓰기
- 등등~