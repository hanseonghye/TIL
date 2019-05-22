# Garbage Collection

## Root Set

> object의 사용 여부는 Root Set과의 관계로 판단하게 되는데, Root Set에서 어떤 식으로든 참조 관계까 있다면 **Reachable Object**라고 하며, 이를 현재 사용하고 있는 Object로 간주하게 된다.

### Reachable Object를 구별하는 방법

- Local variable Section, Operand Stack에 Object의 참조 정보가 있을 때.
- Method Area에 로딩된 클래스 중, constant pool에 있는 참조 정보를 토대로 스레드에서 직접 참조하진 않지만 constant pool을 통해 간점 link를 하고 있는 Object
  - Constant pool
    - 리터럴 상수값을 저장하는 곳. 
    - String 뿐만 아니라, 모든 종류의 숫자, 문자열, Class 및 Method 에 대한 참조와 같은 값이 포함된다.
    - 코드에 등장하는 리터럴들은 Class단위로 Constant Pool에서 관리가 이루어지고, 한 Class에 등장하는 동일한 리터럴값은 여러번 메모리에 Load되지 않는다.
- 아직 메모리에 남아 있으며 **native method area**로 넘겨진 Object의 참조가 **JNI** 형태로 참조 관계가 있는 Object는 Reachable Object이다. ??
  - JNI (Java Native Interface)
    - 자바와 다른 언어를 연동해주는 솔루션

위의 세 경우를 제외하면 모두 GC 대상이 된다.



### 경험적 지식 

> Weak Generational Hypothesis
>
> **Garbage Collection은 다음의 2가지 가설에 의해 만들어 졌다.**

1. Object는 생성된 후 금방 Garbage가 된다.

   이에 의해, 메모리 단편화가 많이 발생한다. 그래서 Compaction처럼 비싼 작업을 해야한다.

   때문에 Object할당만을 위한 전용 공간인 Eden Area를 만들고, GC 당시 Live한 Object들을 피신시키는 Survivor Area를 따로 구성한 것이다. --> Garbage가 될 확률이 적은 Object를 따로 관리 하는 것.

2. Old Object가 Younger Object를 참조할 일은 드물다.

   그렇다면 Old영역에 있는 객체가 Young 영역의 객체를 참조하는 경우가 있을 때는 어떻게 처리할까?

   --> Old 영역에는 512 바이티의 덩어리(chunk)로 되어있는 카드 테이블이 존재한다.



이 가설의 장점을 최대한 살리기 위해, **HotSpot ** jvm에서는 크게 2개의 물리적 공간을 나누었다. 

- Young 영역 

  새롭게 생성한 객체의 대부분이 여기에 위치한다. 대부분의 객체가 금방 접근 불가능 상태가 되기 때문에 많은 객체가 Young 영역에 생성됐다가 사라진다. 이 영역에서 객체가 사라질 때, Minor GC가 발생한다고 말한다.

- Old 영역

  접근 불가능 상태로 되지 않아 Young 영역에서 살아남은 객체가 여기로 이동 된다.

  대부분 Young영역보다 크게 할당되며 크기가 큰 만큼 GC가 적게 발생한다. 이 영역에서 객체가 사라질 때, Major GC( == Full GC)가 발생한다고 말한다.

  - 특정 회수 이상 참조되어 기준 을 초과하면 Old영역으로 이동된다.
  - Minor GC보다 Major GC는 더 많은 suspend 시간을 가진다.



### 카드 테이블

>  Old 영역의 메모리를 대표하는 별도 메모리이다. (Old 영역의 일부는 카드 테이블로 구성되어 있다.)

- 만약 Young 영역의 Object를 참조하는 Old 영역의 Object가 있다면, 카드 테이블에 Old Object를 알 수 있는 정보 (시작 주소?)를 표시한다.

- Old영역에 있는 객체가 Young 영역의 객체를 참조할 때마다 정보가 표시된다. Young 영역의 GC를 실행할 때에는 Old 영역에 있는 모든 객체의 참조를 확인하지 않고(Young 영역의 Object를 참조하는지), 이 카드 테이블만 뒤져서 GC대상인지 식별한다.

<https://hamait.tistory.com/196>

<https://d2.naver.com/helloworld/37111>



### TLAB

> Thread-Local Allocation Buffers
>
> GC가 발생하거나, 객체가 다른 영역으로 이동할 떄,  병목현상이 발생할 수 있다. 이를 해결하기 위한 솔루션.
>
> 각 스레드 별 메모리 버퍼를 사용하면, 다른 스레드에 영향을 주지 않는 메모리 할당 작업이 가능하게 된다.

### GC 대상 범위

GC대상 Area는 