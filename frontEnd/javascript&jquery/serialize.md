# serialize()

`form`안의 데이터들을 쿼리스트링화 한다.

`name1=value1&name2=value2` 형식



이때 같은 name을 가진값이 있을 경우

`name=value1&name=value2` 로 전달되니 name값을 배열로 준다던지 `serializeArray`를 사용해야 한다.