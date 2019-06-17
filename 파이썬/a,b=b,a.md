# a,b = b,a

`a,b = b,a`는

```python
a = b
b = a
```

와 다른 수행이다.

`swap`과 같은 결과를 가져온다.

```python
a,b=b,a+b

temp = a+b
a = b
b = temp
```

위 또한 아래의 swap과 같은 결과를 가져온다.



