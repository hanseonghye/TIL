# django 라이브러리



## return

### HttpResponse

문자열을 화면에 출력시킬 수 있다.

```python
from django.http import HttpResponse

def fun(request):
    return HttpResponse("hello")
```

### render

```python
render(request, template_name, context = None)
```

### redirect

```python
return HttpResponseRedirect('/path')
```

<<<<<<< HEAD
=======
### 파라미터 값 가져오기

```python
request.GET["para1"]
relquest.POST["para2"]

request.get("para3",0) # default 값 지정
```



>>>>>>> 8c9eed990c6542cd6536dbcc1c52601fa758f718
### return json

```python
jsonresult = {
        "result": "success",
        "data": ['hello', 1, 2, 3, True, ('a', 'b')],
    }
return JsonResponse(jsonresult)
```




## 파라미터 가져오기

```python
request.POST['val']
```





## model - db 관련

### 모두 가져오기

```python
# id 값을 역순으로 가져오기.
data = Model.objects.all().order_by('-id')
```

### filter

```python
Model.objects.filter(col1=val1, col2=val2)
Model.objects.filter(col1=val1).filter(col2=val2)
```

### get

`Model.objects.get(col1=val1)`

get은 하나의 값을 가져오고 filter는 해당하는 모든 row를 가져온다.



### F()

`todo`