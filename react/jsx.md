# jsx

jsx문법의 코드가 번들링되면서, `babel-loader`를 사용하여 자바스크립트로 변환된다.



```jsx
let a = (
	<div>
    	<h1>hello</h1>
    </div>
)
```

이코드는 아래로 변환됨.



```javascript
let a = React.createElement(
	"div",
    null,
    React.createElement(
    	"hi",
        null,
        "hello",
    )
)
```



jsz에 오류가 있다면, 바벨이 코드를 변환하는 과정에서 이를 감지하고 올려준다.

(ex, 태그를 닫지 않았을 때)