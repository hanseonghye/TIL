# class

## 용어 정리

1. 클래스

   `class`문으로 정의하며, 멤버와 메소드를 가지는 객체

2. 클래스 인스턴스

   클래스를 호출하여 만들어지는 객체

3. 멤버

   클래스가 갖는 변수

4. 메소드

   클래스 내에 정의된 함수

5. 상위 클래스

   기반 클래스, 어떤 클래스의 상위에 있으며 여러 속성을 상속 해준다.

6. 하위 클래스

   파생 클래스, 상위 클래스로부터 여러 속성을 상속받는다.

   

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

객체를 없애는 소멸자. 호출 시, 메모리 공간에서 객체가 지워지게 된다.

프로그램이 종료되면 `__del__`함수가 호출된다.

`del [객체]` 이렇게 사용하면 소멸자가 호출된다.



```python
class Point:
    count_of_instance = 0

    def __init__(self, x, y):
        self.x, self.y = x, y
        Point.count_of_instance += 1

    def __del__(self):
        Point.count_of_instance -= 1
```



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

## `__str__`

print 로 객체를 출력할 때의 폼을 지정

### `__repr__`

`__str__`과 같은 목적. 그런데 '+ '를 통해 문자열을 합칠 수 없다.

```python
def __repr__(self): # 위처럼 + 를 사용하여 return 할 수 없다.
    return "Point ({0}, {1})".format(self.x, self.y)

def test_to_string():
    p = Point()
    print(repr(p)) # 이렇게 쓴다.
```

해보니까 repr도 str처럼 문자열을 합칠 수 있는데 알아보니 `__str__`은 비공식 적으로 개발자가 알아보기 쉽게 하기 위해 쓰는 것 같고 `__repr__`은 공식 적인 용도로 쓰는 것같다. 그래서 '+' 연산을 하지 말라는 거 인것 같다.

보통 `__str__`는 `__repr__` 값을 가져와서 쓴다.



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



## 클래스 네임스페이스

```python
class Stock :
    market = "kospi"
    
print (dir())
# ['Stock', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec_']
```

**dir** 내장함수의 결과값에 `Stock`클래스가 들어있기 때문에 프롬포트에 `Stock`를 입력해도 오류가 발생하지 않는다.

파이썬에서는 클래스가 정의되면, 하나의 독립적인 네임스페이스가 생성된다.( 함수와 마찬가지 ) 그리고 클래스 내에 정의된 변수나 메서드는 해당 네임스페이스에 등록된다.



## 메서드

- 인스턴스 메서드

  인스턴스 객체에 엑세스 할 수 있도록 메서드의 첫번째 파라미터에 항상 객체 자신을 의미하는 **self** 파라미터를 갖는다.

- 정적 메서드 : @classmethod와 @staticmethod

  - 클래스에서 직접 접근할 수 있는 메서드.

  - 인스턴스를 만들지 않아도 실행 가능하다.

  - 인스턴스에서도 접근이 가능하다.

    - classmethod
      - 첫번째 인자로 클래스를 입력한다.( 주로 cls )
    - staticmethod
      - 필수 인자없음.

    ```python
    >>> class calc:
    	@staticmethod
    	def add(n):
    		return n+10
    	@classmethod
    	def min(cls,n):
    		return n-10
    
    	
    >>> calc.add(10)
    20
    >>> calc.min(10)
    0
    ```

  - 클래스 변수에 접근할 때는 staticmethod보다는 classmethod가 좀 더 적절하다.

    ```python
    >>> class calc:
    	name ="계산을 하자"
    	
    	@staticmethod
    	def add(n):
    		print(calc.name)
    		return n+10
    	@classmethod
    	def min(cls,n):
    		print(cls.name)
    		return n-10
    
    	
    >>> calc.add(10)
    계산을 하자
    20
    >>> calc.min(10)
    계산을 하자
    0
    ```

    `cls.name`으로 클래스 변수에 접근하는 것이 좀더 좋아보인다.

### 클래스 멤버와 인스턴스 멤버

```python
class Point:
    count_of_instance = 0 # 클래스 멤버 정의
    
    def set_x(self,x):
        self.x = x # 인스턴스 멤버 정의
```

- 클래스 멤버는 모든 인스턴스 객체들에서 공유된다.
- 인스턴스 멤버는 각각의 인스턴스 객체에서만 참조된다.
- 클래스의 멤버에 접근할 때 먼저 인스턴스 멤버에서 찾으며, 없으면 클래스 멤버에서 찾게 된다.



<https://wikidocs.net/21054>

[http://pythonstudy.xyz/python/article/19-%ED%81%B4%EB%9E%98%EC%8A%A4](http://pythonstudy.xyz/python/article/19-클래스)





