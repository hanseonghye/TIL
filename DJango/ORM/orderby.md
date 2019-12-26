# ORDER BY

```python
Model.objects.order_by('colunm')
```

- desc

```python
Model.objects.order_by('-colunm')
```



## model 에서 

```python
class Post(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    content = MarkdownxField()
    ins_dt = models.DateTimeField(auto_now_add=True)
    upd_dt = models.DateTimeField(auto_now=True)
    use_tf = models.BooleanField(default=True)

    class Meta:
        ordering = ['-ins_dt']
```

**ordering** 를 통해 filter 를 할 때마다 order by를 할 수 있다.