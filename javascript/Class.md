# Class:fire:중요:fire:

를 하기 전에 prototype을 공부하자.

# Prototype

JS는 프로토타입 기반 언어이다!!

js에서 원시 타입을 제외한 모든 것들은 객체이다. 모든 객체는 프로토타입을 기반으로 하며, 프로토타입은 객체에 기본적인 프로퍼티 집합을 부여한다.

```javascript
console.log(typeof(Object));
console.log(typeof(Array)); // function
```

```javascript
let arr = [1,2,3];//js 는 이것을 다음과 같이 해석한다.
let arr2 = new Array(1,2,3);
```

### new

``` javascript
function newRabbit(adj){
	this.adj = adj;
    this.speak = function(line){
        console.log( this.adj, " 토끼가 말합니다. ", line);
    };
};

let rabbit1 = new newRabbit("킬러");
rabbit1.speak("hihi");
```

```javascript
function Rabbit(adj){
    return {
        adj : adj,
        speak : function(line){
            console.log( this.adj, " 토끼가 말합니다. ", line);
        }
    }
};

let rabbit2 = Rabbit("킬러");
rabbit2.speak("하이루");
```

두 코드의 차이는 뭘까 :face_with_head_bandage:

:arrow_forward:__new를 사용했을때__

1. 생성자라는 프로퍼티가 있다. 이것은 newRabbit을 생성한 rabbit1 함수를 가리킨다. 
   Rabbit에도 그런 프로퍼티가 있지만, Rabbitsms Object함수를 카리킨다.

### 함수 생성시 발생하는 일

1. 함수를 정의하면 함수가 생성되고 prototype object가 같이 생성된다.
2. prototype object는 constructor와 `__proto__`를 갖고 있다. constructor는 생성된 함수를 가리킨다. `__proto__`는 prototype link로, 객체가 생성될 때 사용된 함수(생성자)의 prototype object를 가리킴.



---

Class는 prototype을 기반으로 상속을 보다 명료하게 사용할 수 있도록 문법을 제공한다.

https://jongmin92.github.io/2017/06/18/JavaScript/class/