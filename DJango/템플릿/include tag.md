# include tag

`include tag를 통해 html 페이지를 재 사용하자!`

**include** 태그를 사용하면 html 페이지에서 다른 html 페이지를 불러 올 수 있다.

이렇게 되면 반복적으로 for문을 수행하는 부분이 있을 경우 include tag 한 줄로 끝낼 수 있다.

```html
<select name='select'>
    {% for o in objects %}
    	<option value='{{ o.id }}'>{{ o.name }}</option>
    {% ndfor %}
</select>
```

이걸 include 태그를 통해 한 줄로 바꿔 보자!



```html
{% include "select_box.html" with objects=objects name="select" %}
```

이때 띄어쓰기를 조심해야 한다. `=`사이를 띄어 주면 안된다.

그리고 호출할 `select_box.html`파일을 만들어야 한다.

```html
<select name={{ name }}>
    {% for o in objects %}
    	<option value='{{ o.id }}'>{{ o.name }}</option>
    {% endfor %}
</select>
```

