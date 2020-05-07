# Model에서 FK 사용하기

```python
user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
```

부모 테이블, 부모 테이블에서 FK를 가져올 컬럼, on_delete를 명시해 준다.