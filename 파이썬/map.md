# map

map(f, iterable)은 함수(f)와 iterable을 입력으로 받는다. 

iterable의 각 요소가 함수 f를 수행한 결과를 묶어서 돌려준다.



```python
def two_times(unmberlist) :
    result = []
    for number in numberList:
        return.append(number*2)
    return result

result = two_times([1,2,3,4])

def map_two_times(x):
    return x*2

list(map(map_two_times, [1,2,3,4]))
```

