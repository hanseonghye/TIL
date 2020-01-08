# update

`update`를 할 수 있는 많은 방법이 있는것 같다.



1. save() 를 통한 update

```java
int id = 1;
String name = "새로운이름"
Optional<MyEntity> oldEntity =  chaInfCRepository.findById(id);
MyEntity newEntity = oldEntity.get();
newEntity.setName(name);
myRepository.save(newEntity);
```

