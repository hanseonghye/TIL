# RAS (인프라) :briefcase:

> 시스템의 신뢰성을 종합적으로 고려한 지표

-  Reliability : 신뢰성
- Availability : 가용성
- Serviceability : 유지 보수성
- RASIS 는 RAS에서 **Integrity : 무결성 **, **Security : 안전성**이 추가된 것이다.



### 가동률 :fire:

> RSA를 검토할 때 사용하는 지표

- MTBF ( Mean Time Between Failures ) : 장애 발생 간격 = 누적사용시간 / 고장 횟수
- MTTR ( Mean Time To Repair ) : 평균 복구 기간 = 누적 수리 시간 / 고장 횟수
- 가동률 = MTBF / ( MTBF + MTTR )



### 가동률을 높이는 방법 :up:

1. 요소 각각의 가동률을 높인다.

   - 서버용 부품( CPU, 메모리, 하드디스크, SSD ...) 사용하기
   - 부품 이중화 하기 --> 하나가 고장나도 서비스가 중지 되지 않는다.

2. 요소를 조합해 전체의 가동률을 높인다.   ---> 이중화, 다중화

   - Active-Active ( 운영-운영 )

     - 서로 다른 업무에 대해 상호 대기 형태로 운영
     - 높은 처리률
     - 설정 및 구성이 복잡해진다.
     - 1대가 죽었을 경우, 2대의 처리량을 1대로 처리해야하기 때문에 그에 대한 대비책이 필요하다.

   - Active-Standby ( 운영-대기 )

     > - Active system이 죽을 경우를 대비하여 대기.
     > - Active system의 죽음을 감지하면 Standby system이 Active 상태로 변경된다. 이 변경되는 잠깐의 시간동안 서비스가 끊길 수 있다.

     1. Hot Standby :hotsprings: 

        - Standby 장비 기동후 즉시 사용가능. 
        - 소요시간 -> shortest

     2. Warm Standby :low_brightness: : Standby 쪽 장비에는 전원만 연결되어 있는 상태. Standby 측은 가동 후 이용가능하게 하기 위해서 나름대로의 준비가 필요한 구성

        - 데이터 파일은 동기화하고 있지만 이를 이용 가능하도록 하기 위해서는 데이터 복원에 대한 처리가 필요한 구성
        - 소요시간 -> middle

     3. Cold Standby :cold_sweat: : standby 측을 정지시켜 두는 구성. 

        - Active system에 장애가 발생했을떄, Cold Standby system에 전원을 넣고 시스템의 운용을 계속되도록 해야한다. 

        - 전원 조차 연결돼있지 않다!!!!
        - 소요시간 -> longest

     이러한 이중화를 적용함으로써, 1대의 장비가 죽을 경우 준비된 장비를 서비스에 투입하면서 짧은 시간내에 서비스의 복구가 가능해 진다.

     <https://ivyful.blog.me/221236799667>

3. 적절한 프로비저닝으로 부하 문제를 피한다.

   - 프로비저닝
     - 사용자 수 등을 예측하여 적절하게 리소스를 준비하는 것.
     - 웹을 사용하는 B2C 서비스는 부하를 예측하기어렵다. 예산 안에서의 최대한의 예측과 그에 따른 대응이 필요하다.
   - 스케일 업
     - 서버 등, 각 요소의 성능을 향상시키는 방법
     - 스케일 업 만으로 성능을 향상시키는 데는 한계가 있다.
   - 스케일 아웃
     - 서버 등 각 요소의 수를 늘리는 방법

:pushpin: MTBF를 길게하거나 MTTR을 짧게 한다.