# ElasticSearch

>  Java로 만들어진 분산 검색 엔진
>
> 방대한 양의 데이터를 신속하게, 거의 실시간으로 저장, 검색 할 수 있다.

검색을 위해 단독으로 사용되기도 하며, ELK(ElasticSearch / Logstatsh / Kibana ) 스택으로 사용되기도 한다.



###  ELK 스택

- Logstash
  - 다양한 파일 (DB, csv, ..)의 로그 또는 데이터를 수집, 집계, 파싱하여 ElasticSearch로 전달.
- ElasticSearch
  - Logstash로부터 받은 데이터를 검색 및 집계하여 필요한 관심 있는 정보를 획득
- Kibana 
  - ElasticSearch의 빠른 검색을 통해 데이터를 시각화 및 모니터링



## ElasticSearch와 RDB의 용어 비교

| RDB      | ElasticSearch |
| -------- | ------------- |
| Database | Index         |
| Table    | Type          |
| Row      | Document      |
| Column   | Field         |
| Index    | Analyze       |
| PK       | _id           |
| Schema   | Mapping       |



### ElasticSearch 아키텍쳐

![img](./img/img18.png)



1. 클러스터

   ElasticSearch에서 가장 큰 시스템 단위를 의미하며, 최소 하나 이상의 노드로 이루어진 노드들의 집합이다.

   서로 다른 클러스터는 데이터의 접근, 교환을 할 수 없는 독립적인 시스템으로 유지되며, 여러 대의 서버가 하나의 클러스터를 구성할 수 있고, 한 서버에 여러 개의 클러스터가 존재할 수도 있다.

2. 노드

   ElasticSearch를 구성하는 하나의 단위 프로세스를 의미한다.

   그 역할에 따라 Master-dligible, Data, Ingest, Tribe 노드로 구분할 수 있다.

   - master-eligible node
  - 클러스터를 제어하는 마스터로 선택할 수 있는 노드를 말함.
     - 여기서 master 노드가 하는 역할은 다음과 같다.
       1. 인덱스 생성, 삭제
       2. 클러스터 노드들의 추적 및 관리
       3. 데이터 입력 시 어느 샤드에 할당할 것인지.

3. 샤딩 (Sharding)

   데이터를 분산해서 저장하는 방법을 의미함.

   즉 ElasticSearch에서 스케일 아웃을 위한 index를 여러 shard로 쪼갠것.
   
   - 스케일 아웃
     - 서버 등 각 요소의 수를 늘리는 방법
   
4. replica

   또 다른 형태의 shard.

   노드를 손실했을 경우, 데이터의 신뢰성을 위해 shard를 복제하는 것.

   따라서 replica는 서로 다른 노드에 존재할 것을 권장한다.



## 역색인

Elasticsearch가 빠른 이유와도 같다.

"Lorem Ipsum is simply dummy text of the printing and typesetting industry"

예를 들어 이 문장을 모두 파싱해서 각 단어들을 저장하고 대문자는 소문자 처리, 유사어 체크 등의 작업을 통해 텍스트를 저장한다. 따라서 RDBMS보다 Full Text Search에 빠른 성능을 보인다.



<https://victorydntmd.tistory.com/308>