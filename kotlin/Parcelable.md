# Parcelable

`activity`,`component`이동 시 `intent`를 사용한다.

이때 데이터 객체를 전달하기 위해 클래스를 직렬화 하는 부분이 필요하다. 이 역할을 해준다.



```kotlin
class User {
    val name: String? = null
    val email: String? = null
}
```



위 클래스를 parcelable로 구현하면 아래와 같다.



```kotlin
class User() : Parcelable {
    var name : String? = null
    var email : String? = null
    
    
    constructor(parcel: Parcel) : this() {
        parcel.run {
            name = readString()
            email = readString()
        }
    }
    
    override fun writeToParcel(Dest: Parcel?, flags: Int) {
        dest?run {
            writeString(this@User.name)
            writeString(this@User.email)
        }
    }

    override fun describeContents(): Int {
        return 0
    }

    companion object CREATOR : Parcelable.Creator<User> {
        override fun createFromParcel(parcel: Parcel): User {
            return User(parcel)
        }

        override fun newArray(size: Int): Array<User?> {
            return arrayOfNulls(size)
        }
    }
}
```

