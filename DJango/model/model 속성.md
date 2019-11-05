# models 속성

## 속성

### unique

```python
models.CharField(unique = True)
```

### null 허용

```python
models.CharField(null=True)
```

### default

```python
models.BooleanField(default=True);
```



### related_name

ForeignKey를 사용할때 해당 column을 다른 Model, 혹은 같은 Model에서 같은 table을 참조하는 column을 구분하기 위해 사용한다. 특수한 이름을 붙이면 되지만, 매번하기 까다롭다! 이렇게 설정하잠.

```python
col = models.ForeignKey(MyModels,related_name="%(app_label)s_%(class)s_related_col", db_column='col')
```

