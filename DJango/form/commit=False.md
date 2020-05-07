# commit = False

form을 통해 save()를 할때 따로 설정하지 않으면 `commit = True`가 되고, db에 insert하는 쿼리가 동작한다. 이 값을 인위적으로 `False`로 넣고, 실제 insert하고 싶을때 이 인자값을 True로 넣으면 그때서야 insert하도록 할수 있다. 예를 들어 외래키를 가지는 intance가 외래키를 제외한 값들을 미리 셋팅해놓고  외래키를 다른곳에서 가져왔을때 추가로 값을 넣고 `commit = True`를 적용해 insert하는 것이다.

- Form

```python
class MyForm(forms.ModelForm):
    ...
    
    def save(self, pk = None) :
        mymodel = super(MyForm, self).save(commit = False) #pk가 없어도 값을 미리 셋팅한다.
        if pk :
            mymodel.pk = pk
            mymodel.save() # pk가 있다면 save
        return mymodel
```

- View

```python
class MyView(CreateView):
    def post(self, request):
        mymodel = MyForm(data=request.POST) # 이때 form에서 save 함수를 실행한다. 하지만 commit하지는 않는다.
        mymodel2 = MyForm2(data=request.POST) # 추가작업
        mymodel.save(pk = mymodel2.pk) #실제 insert를 수행
```

