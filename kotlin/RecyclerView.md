# RecyclerView
#### recycle
```
1. (폐품을) 재활용하다
2. (같은 생각, 방법 등을) 다시 이용하다

인스타그램, 유튜브 피드와 같이 동일한 형태의 뷰에 데이터에 따라서 달라지는 형태의 뷰를 말한다.
```

`ListView`에서는 모든 데이터에 대한 view를 만들고, view가 사라졌다가 나타날 때마다 리소스를 불러와야 한다.
ex) 화면을 아래로 스크롤 했다가 다시 위로 올릴경우, 리소스를 불러오게 된다.
이 방법은 많은 메모리와 저장 공간을 사용하므로, 대용량의 데이터를 이용하면 앱이 느려 지게 된다.

- https://velog.io/@l2hyunwoo/Android-%EA%B8%B0%EB%8A%A5-%EA%B5%AC%ED%98%84-5
- https://blog.yena.io/studynote/2017/12/06/Android-Kotlin-RecyclerView1.html


## data
`recyclerView`에 들어가는 `data`들은 `data class`를 사용한다.
`data class`는 `equals`, 'toString'과 같은 함수들을 자동으로 생성해 준다.

```kotlin
data class LayoutData (
  var name : String,
  var age : Int
)
```

이 데이터가 반복적으로 들어가는 것이다.





## ViewHolder

위의 `data class`를 `view`와 연결해 주는 역할.

자바에서 `findViewById`로 했던 부분을 간단히 해준다.