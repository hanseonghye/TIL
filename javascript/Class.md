# Class:fire:중요:fire:

를 하기 전에 prototype을 공부하자.

# :hotsprings: Prototype :hotsprings:

- JS는 프로토타입 기반 언어이다:heavy_exclamation_mark:

JS에서 원시타입을 제외한 모든 것들은 객체이다. JS의 모든 객체는 자신을 생성한 객체 원형에 대한 숨겨진 연결을 갖는다. 이때 자기 자신을 생성하기 위해 사용된 객체원형( == 부모객체 )을 프로토타입이라 한다. JAVA에서 Class와 동일한 의미를 가진다.



```javascript
let foo = {
    val1 : "val1",
    val2 : "val2"
};

console.log( foo.toString() );
console.log( foo );
```

foo 객체는 toString() 메서드가 없기 때문에 에러를 발생해야할 것 같지만 정상적으로 결과를 출력한다. 이는 foo 객체의 프로토타입에서 toString()이 정의되어있고 foo객체가 이 메서드를 상속받았기 때문이다.

![ex_screenshot](./img/class-tostring.png)

위와 같이 foo 객체의 `__proto_`프로퍼티에 toString() 메서드가 있음을 확인할 수 있다.

여기서 `__proto__` 프로퍼티는 foo객체의 부모인 프로토타입 객체를 가리킨다.

---

### 객체 비교

동등 연산자(==)를 사용하여 두 객체를 비교할 때, 객체의 프로퍼티값이 아닌 참조값을 비교한다.

```javascript
let a = 100;
let b = 100;

let objA = { value:100 };
let objB = { value:100 };
let objC = objB;

console.log( a == b ); // true
console.log( objA == objB ); //false
console.log( objC == objB ); //true
```

`a==b`의 경우 숫자 100을 저장하고 있는 기본 타입 변수다. 기본타입의 경우 동등연산자를 이용해서 비교할 때 값을 비교한다.

![ex_screenshot](./img/equal.png)

`objA == objB`와 `objC == objB`의 경우 객체의 비교에서는 참조값이 같아야 true가 되기 때문이다. 위의 그림과 같인 objB와 objC는 같은 객체를 참조하므로 true가 된다. objB나 objC중 하나의 값이 바뀌게 되면 같은 참조값이 변경되고 두개의 객체 모두에 영향을 끼친다.