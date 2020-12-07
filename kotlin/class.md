# class

## class

```kotlin
class WhoAmI(private val name:String) {
    fun myNameIs() = "나의 이름은 ${name}입니다"
}


class WhoAmI2{
    private val name: String
    constructor(name:String) {
        this.name = name
    }
    
    
    fun myNameIs() = "나의 이름은 ${name}입니다"
}



fun main(args: Array<String>) {
    val m1 = WhoAmI("영수")
    println(m1.myNameIs())
}
```

- https://www.bsidesoft.com/8187



## data class

- 소괄호 2쌍으로`(())` 열고 닫는다.
- 변수나 상수만 선언할 수 있다.
- 초기화는 해도되고 안해도 된다
- 생성과 동시에 생성자가 만들어 진다.
- getter(), setter(), toString() 등의 메서드가 자동으로 생성된다.


```kotlin
data class Student (
  val name : String,
  var age : Int
)


fun main() {
    val student01 = Student('hanseonghye',20)
}
```





## object

- class 가 아닌 object라는 키워드로 선언

- 생성자가 없다.
- 어느 클래스, 함수에서든 별도의 객체화 과정 없이 접근 가능하다.
- 프로그램이 실행되는 동안 저장된 데이터는 손실되지 않는다. 단 프로그램이 종료되면 소멸
- 위 특징 덕분에 안드에서는 액티비티, 프래그먼트를 구분하지 않고 데이터 전달이 가능하다.
- 코틀린에는 `static`가 없는데, `object`가 이런 느낌이당



```kotlin
object Student {
    var name : String = ""
    var age : Int = 0
    
    fun myFun() {
    }
}


fun main() {
    var name = "hans"
    var age = "30"
    
    Student.name = name
    Student.age = age
}

# 일반 class 처럼 객체화하는 것이 아니라, object의 요소에 직접 접근하여 데이터를 조작하고 데이터 및 함 수 호출을 한다.
```



### companion object

클래스 내부에 객체를 선언할때 사용



- https://medium.com/@sket8993/kotlin-%EB%8B%A4%EC%96%91%ED%95%9C-%ED%81%B4%EB%9E%98%EC%8A%A4-%EC%B4%88%EA%B0%84%EB%8B%A8-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-38416cd8d63d

