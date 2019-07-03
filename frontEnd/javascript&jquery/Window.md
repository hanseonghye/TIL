# Window 객체

클라이언트 측의 전역 객체. 객체의 계층 구조에서 최상위에 존재한다.

창열기, 창 크기 조절 등 을 제어하는 작업을 할 수 있다.

- window.parseInt() 와 parseInt()는 같은 실행을 한다. window는 최상위 객체이기 때문 :exclamation:

- 전역에 생성한 변수또한 window 객체안에 등록된다.

  ```javascript
  let val = "window";
  console.log(window.val);
  ```


### Document 객체

웹 페이지를 담당하는 window 객체중 일부. 해당 window에 나타난 문서를 나타내는 객체가 담겨있다.

image, link form(text, button 등을 포함) 등의 객체를 가지고 있음.

##### document.createElement(tag)

새로운 태그를 만들 때 사용. 바로 생기는 것이 아니라 메모리에 저장된다. 이것을 생성하는 작업이 추가적으로 필요하다.



### navigator

브라우저에 특화된 기능을 두기 위해 도입됨.

브라우저나 운영체제에 대한 정보를 가지고 있다.

모바일 환경에서는 GPS나 배터리를 체크하는 기능도 있다고 한다.

```javascript
console.log(window.navigator.userAgent);
console.log(navigator.language);
```



https://www.zerocho.com/category/JavaScript/post/573b321aa54b5e8427432946



### 버블링

이벤트가 감지됐을떄, 해당 노드를 포함하고 있는 부모 노드를 통해서 최상위 까지 이벤트가 전달되는 현상

```html
<form onclick="alert('form')">
    <div onclick="alert('div')">
        <p onclick="alert('p')">
        </p>
    </div>
</form>
```

p tag를 클릭시 p - div -> form 팝업 창이 뜨게된다.

### 캡쳐링

버블링과 반대 방향으로 이벤트가 진행

evt.stopPropagation();을 넣어주면 버블링이나 캡쳐링같이 이벤트가 전파되지 않는다.

https://medium.com/@shlee1353/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%B2%84%EB%B8%94%EB%A7%81-bubbling-%EC%BA%A1%EC%B2%98%EB%A7%81-capturing-%EC%A0%95%EB%A6%AC-f63e0cda620b





---

# 함수

### open

``` javascript
let newWindow = window.open("www.naver.com");
```

웹페이지에서 스크립트에 의해 새로운 페이지를 여는 것은 적절하지 않다. --> 브라우저가 이 기능을 차단한다.

But 같은 도메인에서는 가능하다.

열린 윈도우는 close 메소드로 닫을 수 있다.

``` javascript
newWindow.close();
```

