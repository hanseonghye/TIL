# 간단한 ORM들



### 중복 제거

```python
Objects.objects.filter(...).distinct("pk")
```



## 중복 check

```python
if not MyObject.objects.filter(col = 'col').exists()
```



## count

```python
Model.objects.count()
Model.objects.filter(a='').count()
```

