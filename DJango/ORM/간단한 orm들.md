# 간단한 ORM들



## 중복 check

```python
if not MyObject.objects.filter(col = 'col').exists()
```

