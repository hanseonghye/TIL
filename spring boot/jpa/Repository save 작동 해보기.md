# Repository save 작동 해보기

> spring boot Test를 사용해서 간단한 save를 구현해보자



### 1. test class 생성

`src/test/java/com/project/` 하위 경로에 test class 파일을 생성하자

```java
@RunWith(SpringRunner.class)
@SpringBootTest
public class UserRepositoryTest {
    
    @Autowired
    UserRepository userRepository;
    
    @Test
    public void insertTest() {
        String id = "id".concat(String.valueOf(i));
        String name = "test".concat(String.valueOf(i));
        UserEntiry userEntity = new UserEntiry(id);
        userEntity.setName(name)
        userRepository.save(userEntity);
    }
}
```



### 2. Entity 생성

```java
@Entity
@Table(name="user")
public class UserEntity {
    @Id
    String id;
    String name;
    
    public UserEntity() {
       
    }
    
    @Builder
    public UserEntity(String id) {
        this.id = id;
    }
    
    public void setName(String name) {
        this.name = name
    }
}
```



### Repository 생성

```java

public interface UserRepository extends JpaRepository<UserEntity, String> {

}
```





## 만날수 있는 에러들

### "userentity" 이름의 릴레이션(relation)이 없습니다

entity 에서 테이블과 매칭은 클래스 명과 연결된다. 클래스명에 해당하는 테이블이 디비에 없을 경우 발생한다. 실제 매칭하고 싶은 테이블 명을 명시하자.

```java
@Entity
@Table(name="user")  // user 테이블과 매칭
public class UserEntity {
```



### save 할때 NullPointerException

test class에`RunWith(SpringRunner.class)`,  `SpringBootTest` 어노테이션을 명시해 주자.

- https://n1tjrgns.tistory.com/224

