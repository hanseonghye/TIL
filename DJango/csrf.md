# csrf

![img](./img/img4.png)



form을 사용하여 request를 할 때 다음과 같은 에러가 발생한다.

다음과 같이 {% csrf_token %}을 form 옆에 추가하면 된다.

```html
<form action="/emaillist/add" method="post">{% csrf_token %}
    ...
</form>
```

