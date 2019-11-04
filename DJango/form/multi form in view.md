# multi form in view

단순히 html로 렌더링 할때 data부분에 form을 여러개 주면 된다.

```python
class MultiForm(CreateView):
    form_classes = [Form1, Form2]
    
    def get(self, request):
        form = {
            'form1' : self.form_classes[0](request.POST),
            'form2' : self.form_classes[1](request.POST),
        }
        
        return render(request, self.template_name, {"form":form}) # 나는 이렇게 넘겨줌!
```



템플릿 코드에서는 `form.form1.abc` 이렇게 접근할 수 있다.

