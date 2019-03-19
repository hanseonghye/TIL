# Class:fire:중요:fire:

를 하기 전에 prototype을 공부하자.

# Prototype

- JS는 프로토타입 기반 언어이다:heavy_exclamation_mark:

JS에서 원시타입을 제외한 모든 것들은 객체이다. JS의 모든 객체는 자신을 생성한 객체 원형에 대한 숨겨진 연결을 갖는다. 이때 자기 자신을 생성하기 위해 사용된 객체원형을 프로토타입이라 한다. JAVA에서 Class와 동일한 의미를 가진다.



### 프로퍼티

모든 함수 객체의 Constructor는 prototype이라는 __프로퍼티__를 가지고 있다. 이것은 객체가 생성될 당시 만들어지는 객체 자신의 원형이 될 prototype 객체를 가리킨다.

### 프로토타입과 프로퍼티

JS의 모든 객체는 생성과 동시에 자기자신이 생성될 당시의 정보를 취한 prototype Object 라는 새로운 객체를 Cloning 하여 만들어 낸다. 프로토타입이 객체를 만들어내기 위한 원형이라면 prototype Object는 자기 자신의 분신이며 자신을 원형으로 만들어진 다른 객체가 참조한 프로토타입이 된다.

http://insanehong.kr/post/javascript-prototype/