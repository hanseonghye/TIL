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
# 수정 대상이 되는 model instance 값을 instance 값으로 준다.
mymodel = forms.MyModelForm(data= request.POST, instance = pre_mymodel)

if mymodel.is_valid() :
    mymodel.save()
```

