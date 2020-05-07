# dict

### keys()

```python
>>> d = {'basketball': 5, 'baseball': 9}
>>> d.keys()
dict_keys(['basketball', 'baseball'])
```

### values()

keys() 함수와 비슷한 역할. values를 가져옴

### items()

```python
>>> d.items()
dict_items([('basketball', 5), ('baseball', 9)])
```

### get()

```python
>>> phone = {
    '둘리': '010-1111-1111',
    '또치': '010-2222-2222',
}
>>> phone.get('도우너')
>>> phone.setdefault('둘리', '010-000')
'010-1111-1111'
>>> phone.setdefault('도우너', '010-6666-6666')
'010-6666-6666'
>>> phone
{'둘리': '010-1111-1111', '또치': '010-2222-2222', '도우너': '010-6666-6666'}


```



### 대입

- `d1 = d2`

  d1이 바뀌면 d2도 바뀐다.

- `d1 = d2.copy()`

  d1의 변경이 d2에 영향을 끼치지 않는다.



### 업데이트

```python
phone.update({
    '고길동': '010-7777-7777',
    '또치': '010-8888-8888'
})
```

