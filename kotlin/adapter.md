# adapter 패턴

`사용자는 어댑터 패턴의 인터페이스를 사용함으로써 각각 구현체의 세부 로직과 변경에 관계없이 일관성 있는 사용이 가능하다.`





### 로그인 어댑터를 추상화

```kotlin
interface LoginAdapter {
    fun goLoginPage() : LoginAdapter
    fun requestLogin(id:String, pw:String) : LoginAdapter
    fun redirect(url: String) : String
}


class GoogleLoginAdapterImpl : LoginAdapter {
    
    override fun goLoginPage() : LoginAdapter {
        
    }
    ...
}



class FaceBookLoginAdapterImpl : LoginAdapter {
    
    override fun goLoginPage() : LoginAdapter {
        
    }
    ...
}

```



### 추상화된 로그인 어댑터를 사용하는 클라이언트

``구글, 페이스북 인증을 추상화한 인터페이스를 클라이언트에게 제공하고, 개별 세부 구현체를 생성한다.`

```kotlin
class LoginService(private val loginAdapter: LoginAdapter) {
    fun login(id: String, pw: String, redirectUrl: String) = loginAdapter
            .goLoginPage()
            .requestLogin(id, pw)
            .redirect(redirectUrl)
}


val clientService = LoginService(FaceBookLoginAdapterImpl())
val clientService2 = LoginService(GoogleLoginAdapterImpl())
```





- https://kimchanjung.github.io/design-pattern/2020/05/15/adapter-pattern/