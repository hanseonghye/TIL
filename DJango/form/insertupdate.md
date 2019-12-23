# insert / update

## insert

```python
chainfc = forms.MyModelForm(data=request.POST)
if chainfc.is_valid() :
    chainfc.save()
```



## update

```python
pre_mymodel = MyModel.objects.get(id=request.POST['id'])
# instance 값을 주면 request.POST에 존재하는 값만 update한다.
mymodel = forms.MyModelForm(data= request.POST, instance = pre_mymodel)

if mymodel.is_valid() :
    mymodel.save()
```

