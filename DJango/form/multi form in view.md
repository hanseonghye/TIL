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





## Form에서 ForeignKey 사용하기

두 model에서 foreignkey를 사용하여 save를 해보자!

```python
# view
def fun(request):
    formA = FormA(data = request.POST)
    
    if formA.is_valid():
        new_formA = formA.save(user = request.user)
        formB = FormB(data = request.POST)
        formB.save(a=new_formA)
        
        
# form
class FormA(forms.ModelForm):
    ...
    
    def __init__(self, *args, **kwargs):
        super(FormA, self).__init__(*args, **kwargs)
        
    def save(sefl, user):
        formA = super(FormA, self).save(commit = False)
        
        if user : 
            formA.user = user
            formA.save()
        return formA
    
    
class FormB(forms.ModelForm):
    a = forms.ModelChoiceField()
    ...
    
    def __init__(self, *args, **kwargs):
        super(FormB, self).__init__(*args, **kwargs)
        
        
    def save(self, a):
        formB = super(FormB, self).save(commit = False) # 실제 db에 insert하지 않는다.
        
        if a :
            formB.a = a
            formB.save()
            
        return formB
```

