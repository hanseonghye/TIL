# Class:fire:중요:fire:

를 하기 전에 prototype을 공부하자.

# Prototype

js에서 원시 타입을 제외한 모든 것들은 객체이다. 이 객체 들은 함수를 통해서 생성된다.

```javascript
console.log(typeof(Object));
console.log(typeof(Array)); // function
```

```javascript
let arr = [1,2,3];//js 는 이것을 다음과 같이 해석한다.
let arr2 = new Array(1,2,3);
```



### 함수 생성시 발생하는 일

1. 함수를 정의하면 함수가 생성되고 prototype object가 같이 생성된다.
2. prototype object는 constructor와 `__proto__`를 갖고 있다. constructor는 생성된 함수를 가리킨다. `__proto__`는 prototype link로, 객체가 생성될 때 사용된 함수(생성자)의 prototype object를 가리킴.



---

Class는 prototype을 기반으로 상속을 보다 명료하게 사용할 수 있도록 문법을 제공한다.

https://jongmin92.github.io/2017/06/18/JavaScript/class/