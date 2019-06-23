# django 라이브러리



## http

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

### 파라미터 값 가져오기

```python
request.GET["para1"]
relquest.POST["para2"]

request.get("para3",0) # default 값 지정
```



### return json

```python
jsonresult = {
        "result": "success",
        "data": ['hello', 1, 2, 3, True, ('a', 'b')],
    }
return JsonResponse(jsonresult)
```



## model - db 관련

### 모두 가져오기

```python
# id 값을 역순으로 가져오기.
data = Model.objects.all().order_by('-id')
```



