# CURD

## Insert

### save()

```python
obj = MyModel(name='hanseonghye') # instance 생성
obj.save() # db에 insert
```

### obejcts.create()

```python
obj = MyModel.objects.create(name='hanseonghye') # db에 insert
```



## Delete

```python
MyModel.object.get(no=1).delete() #단일행 삭제

MyModels.objects.filter(name='hanseonghye').delete() #다중행 삭제
```



-  https://brownbears.tistory.com/63 