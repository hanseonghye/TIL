# filter

### AND

```python
filter(A='', B='')
```

### OR

```python
filter(Q(category=self.kwargs['pk'] )| Q( category__parent = self.kwargs['pk']), use_tf=True)
```



### NOT

```python
exclude(A='')
filter(A='').exclude(A='') #filter와 결합하여 filter뒤에서 사용할 수도 있다.
```