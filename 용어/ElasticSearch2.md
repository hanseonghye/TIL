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

