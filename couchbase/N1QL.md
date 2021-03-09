# N1QL

`query language`

couchbase 에서 동적쿼리를 사용하기 위한 기술.

rdbms가 제공하는 sql문과 유사한 구조를 가지고 있다.





### keys

key값에 의한 문서를 가져올 수 있다.

```sql
SELECT name, type FROM beer-sample KEYS ['blabla01', 'blabla02']
```

value중 'blabla01', 'blabla02'가 잇으면 select된다.





## 비교 연산자

| 연산자         | 설명                                         | 리턴 값    |
| -------------- | -------------------------------------------- | ---------- |
| IS NOT NULL    | 필드 값이 NULL 값이 아니다.                  | TRUE/FALSE |
| IS MISSING     | 필드 값이 존재하지 않는다.                   | TRUE/FALSE |
| IS NOT MISSING | 필드 값이 존재하거나 NULL이다.               | TRUE/FALSE |
| IS VALUED      | 필드 값이 존재한다. 없거나 NULL 값이 아니다. | TRUE/FALSE |
| IS NOT VALUED  | 필드 값이 존재하지 않는다. NULL 이다         | TRUE/FALSE |

