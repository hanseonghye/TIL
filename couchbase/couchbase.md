# couchbase

`key-value`타입의 `NoSql`

`json`형식으로 저장된다.



https://soccerda.tistory.com/125?category=868378

https://bcho.tistory.com/934



## Bucket

`rdbms`에서의 `database` 같은 부분, `json`  데이터 들이 저장된다.

버킷 별로 고유 속성을 가지고 있으며, 버킷별로 사용할 수 있는 메모리양, 옵션으로 버킷별로 접근할 수 있는 포트를 , 접근 비밀번호를 지정할 수 있다. 

하나의 클러스트에 최대 128개의 버킷 생성이 가능하며 성능상 10개를 권장



## Node & Cluster

노드는 물리적인 서버에서 가동하는 하나의 인스턴스로, 카우치 베이스는 여러개의 노드로 이루어진 클러스터로 구성된다.



## View

`select 되는 부분들의 모음 같은건가???`

view를 이용해서 `rdbms`에서 제공되는, `indexing`, `grouping`, `sorting`등을 가능하게 한다









