# Garbage Collection

## Root Set

> object의 사용 여부는 Root Set과의 관계로 판단하게 되는데, Root Set에서 어떤 식으로든 참조 관계가 있다면 **Reachable Object**라고 하며, 이를 현재 사용하고 있는 Object로 간주하게 된다.

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

## Garbage Collection의 종류

### Old 영역에 대한 GC

> JDK7에서는 GC방식의 종류에 따른 다음의 5가지 GC를 가지고 있다.

- Serial Collection

  - PC의 CPU 코어가 하나만 있을 때, 사용하기 위해서 만든 방식.

  - Old영역의 GC는 `mark-sweep-compact`알고리즘을 사용한다.

    - mark-sweep-compact

      old영역에 살아 있는 객체를 식별(mark)하는 것.

  - 절대 사용해서는 안되는 GC. 사용할 경우 어플리케이션의 성능이 많이 떨어진다.

    

- Parallel Collection (Throughput Collector)

  - Serial Collection과 같은 알고리즘을 쓴다.
  - 단 처리하는 쓰레드가 여러개다.
  - 그래서 Serial 보다 빠르게 객체를 처리할 수 있다.
  - 코어의 개수가 많을 때 유리하다.

- CMS Collection ( == low latency collector )

  - 힙 메모리 영역의 크기가 클 때 적합.
  - suspend Time 을 분산하여 응답 시간을 개선한다.
  - Full GC때 어플리케이션이 막는 것을 방지하기 위해 고안됨.
  - 하나 이상의 백그라운드 쓰레드가 주기적으로 Old 영역을 스캔하고 사용되지 않는 객체를 제거한다.
  - 그렇기 때문에 CPU 소모량이 많고 단편화가 생기게 된다.

  #### 자세히 알아보자

  - 초기 **Initial Mark** 단계에서는 클래스 로더에서 가장 가까운 객체 중, 살아 있는 객체만 찾는 것으로 끝낸다. 싱글 스레드에서만 사용한다.

  - **Concurrent Mark**에서는 방금 살아있다고 확인한 객체에서 참조하고 있는 객체들을 따라가면서 확인한다. 싱글 스레드에서만 사용.

  - remark mark

    멀티 스레드가 사용되며 어플리케이션이 중지된다.

    이미 marking된 object를 다시 추적, live 여부 확정, 새로 추가된 객체 여부 확인.

     모든 자원을 투입한다.

  - Concurrent Sweep

    쓰레기를 정리함.  그런데 이 과정에서 죽은 객체를 지우기만 하기 때문에 단편화가 발생한다. 이것은 **Free List**를 사용하여 단편화를 지우고자 노력한다.

    #### Free List

    객체가 Young 영역에서 Old 영역으로 이동( ==승격 == promotion )할때 객체의 크기가 비산한 Old 영역에서의 Free Space를 찾아 그곳에 객체를 넣는것. 그리고 Free Space의 블록들을 붙이거나 쪼개는 것. (Compaction 작업) 그런데 이 과정 자체가 시간을 소모하고 객체가 Young 영역에서 오래 머무르는 결과를 가져 올 수 있다.  또한 compaction은 고비용의 작업이다. 그래서 승격이 일어나는 횟수 와 같은 요소를 고려하여 얼마나 Compaction을 할 것이지 등을 결정해야한다.

- Parallel Compaction Collector

  - Parallel Compaction 단계에서 old 알고리즘이 한단계 추가 된다. 다음의 3단계를 거친다.

    1. mark

       살아 있는 객체를 식별하여 표시

    2. sweep

       이전에 GC를 수행하여 컴팩션된 영역에 살아 있는 객체의 위치를 조사.

    3. compact 

       컴팩션을 수행. 수행 이후에는 컴팩션된 영역과 비어있는 영역으로 나뉜다. ???
- Garbage First Collector

  - cms의 단편화 문제를 해결하기 위해 디자인.
  - 힙을 여러개의 영역(region)으로 나눈다. 어떤 힙은 young를 위해 어떤 힙은 old에게 분배.
  - cms처럼 백그라운드 쓰레드로 old 영역에서의 객체를 정리한다. 이때 cms에서 쓸모없는 객체를 쏙쏙 빼버리는게 아니라 한 region을 통째로 정리해 버린다. 참조가 없는 객체는 버리고 사용 중인 남아있는 객체는 다른 region으로 복사시킨다. 이 때문에 단편화가 생기지 않게 된다.

:pushpin:GC도 특정 쓰레드에서 실행된다. GC 쓰레드가 동작할 떄는 모든 어플리케이션 쓰레드는 동작을 멈춘다. 때문에 FULL GC가 생기면 시스템이 멈추게 된다. 그렇기 때문에 GC가 동잘될 떄, 어플리케이션 쓰레드가 멈추는 시간을 최소화 하는 것이 GC 튜닝의 기본이라고 한다.

<https://free-strings.blogspot.com/2016/02/jvm-garbage-collector.html>