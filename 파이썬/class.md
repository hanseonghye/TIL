# class

## self

메소드를 호출할 때 어느 객체가 호출한 것인지 알려주는 키워드.

이 키워드가 없다면 생성된 객체가 메소드 및 속성을 사용할 때 누가 호출한 것인지 알 수 없기 때문에 정상적으로 작동하지 않는다.

클래스에 메소드를 만들 때, 첫 번째 인자는 `self`를 받아 줘야 한다. 메소드는 `self`를 첫 번째 인자로 받게 되며, 해당 메소드를 호출한 객체를 의미한다.



:pushpin:객체가 메소드를 호출할 떄는, 직접 호출하기 때문에 `self`를 사용할 필요가 없다. 하지만 메소드를 호출하고 그 메소드가 다른 메소드를 호출할 때는 `self`를 명시해 줘야 해당 객체의 속성을 이용할 수 있다.



## `__init__`,` __del__`활용

특점 시점에 호출되는 메소드. 

:pushpin:메소드 이름 앞의 `__`의 의미는 이 메소드를 호출 하지 말라는 뜻이다. 파이썬에서는 모든 것이 `public이기 때문에 메소드 이름앞에 `__`를 붙임으로써, 암묵적으로 말하는 것이다.

### `__init__`

생성자

### `__del__`

객체를 없애는 소면자. 호출 시, 메모리 공간에서 객체가 지워지게 된다.

프로그램이 종료되면 `__del__`함수가 호출된다.

### `__caㅣl__`

init, del과 같은 특수 메소드. 객체를 호출할 때 실행된다.

### `__new__`

클래스 자체를 받으며 할당하게 되고,  `__init__`가 self를 받으며 객체의 내부에서 사용할 속성을 초기화 한다.

```python
class Flight:
    
    def __init__(self):
        print('init')
        super().__init__()
        
    def __new__(cls):
        print('new')
        return super().__new__(cls)
    
    def number(self):
        return 'number'
    
f = Flight() #new init
```





## 상속

```python
class unit :
    unit_count = 0
    
    def __init__(self):
        print('unit 생성')
        unit.unit_count += 1
    def move(self):
        print('unit move')
        
class bird(unit):
    def __init__(self):
        print('bird 생성')
        super(bird, self).__init__()
        
class ground(unit):
    def __init__(self):
        print('ground 생성')
        super(ground, self).__init__()
        
b1 = bird();
b2 = bird()
b3 = bird()

b1.move()
print(unit.unit_cout)
```

:pushpin:상속을 받을 때는, 클래스 명 옆 괄호에 부모 클래스를 넣어주면 된다.

:pushpin:`super(해당 클래스명, self).__init__()`을 자식 생성자에 넣어주면 자식 생성자가 호출될 때마다, 부모 생성자를 호출한다.

### 다중 상속

```python
class A :
    #something
class B :
    #something
class C (A,B):
    #subclass
```

### .mro() 메소드

해당 클래스의 상속관계를 확인할 수 있다.



### 정적 메소드 : @classmethod와 @staticmethod

- 클래스에서 직접 접근할 수 있는 메소드
- 다른 언어들과 다르게 정적메소드 임에도, 인스턴스에서도 접근이 가능하다.

`todo`