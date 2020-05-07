# Duck Typing

> 만약 어떤 사람이 오리처럼 걷고, 헤엄치고, 꽥꽥거리는 소리를 낸다면 나는 그 새를 오리라고 부를것이다.

- 사람이 오리처럼 행동하면 오리로 봐도 무방하다라는 것.
- 해당 함수를 통해 타입을 확인/정하는것.

그게 오리인지 검사하지 말고 당신이 오리의 무슨 행동이 필요한지에 따라서 오리처럼 우는지, 걷는지 등등의 적절한 방법으로 오리인지 검사하라!



```python
class Angel:
    def fly(self):
        print ('angel flying');
class Airplane:
    def fly(self):
        print ('airplan flying');
class Whale:
    def swim(self):
        print ('whale swimming');
        
def lift_off(entity):
    entity.fly();

angel = Angel();
airplane = Airplane();
whale = Whale();

lift_off(angel);
lift_off(airplane);
lift_off(whale); #threws error
```





#https://nesoy.github.io/articles/2018-02/Duck-Typing