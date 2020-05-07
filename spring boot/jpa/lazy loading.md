# lazy loading

자신과 연관된 엔티티를 실제로 사용할 때 연관된 엔티티를 SELECT하는것.

예를 들어 `Category` 엔티티와 `Book`엔티티가 관계를 맺고 있을때, 카테고리의 이름이 필요한 시점에서야 `book.getCategory().getName()`을 통해 가져 오는 것.



### n + 1 select

여러가지의 book을 select한다고 생각해 보자.

전체 `book`를 select할때 `1`번, 각 book마다 `category.name`을 1번씩 select한다. 따라서 총 `n+1` 번 select하게 된다.

 

## Eager Fetch (즉시 로딩)

반대로 즉시 로딩이란 엔티티를 조회할 때 자신과 연관되는 엔티티를 JOIN을 통해 함께 조회하는 방식





- https://victorydntmd.tistory.com/210