# null 처리

### ?.

`?.`연산자를 사용하면, 앞의 변수가 `null`이 아닐 때만, 오른쪽 함수가 수행된다.

null이면 null을 반환한다.

```
a != null ? somethig... : null
와 같은 수행을 하는것!
```





### ?:

null 인 경우, default 값을 주는것.

```kotlin
val name = str ?: "unknown"
```



### !!

`not null 처리`

변수를 `nullable`로 설정하였으나, 로직상 `null`이 들어가지 않는 경우가 있다.  이럴때 사용

```kotlin
fun ignoreNulls(s: String?) {
    val sNotNull: String = s!!
}
```



- https://tourspace.tistory.com/114