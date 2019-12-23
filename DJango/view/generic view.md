# generic view



## DetailView

```python
class MyDetailView(DetailView):
    model = MyModel
    template_name = 'template.html'
    lookup_field = 'pk'
    context_object_name = 'mymodel' # html에서 MyModel 객체에 접근하는 변수 명
    
    # 위에서 지정한 model외에 다른 데이터를 가져오고 싶을때 사용하는 함수
    def get_context_data(self, **kwargs):
        id = self.kwargs['pk']
        data = super(MyDetailView, self).get_context_data(**kwargs)
        data['mymodel2'] = MyModel2.objects.get(id=id) # html에서 mymodel2로 접근할 수 있다.
        return data
```