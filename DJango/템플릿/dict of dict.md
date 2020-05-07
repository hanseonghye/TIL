# dict of dict

dict의 value값으로 dict를 줬을 때, 다음과 같이 2중 for문으로 접근할 수 있다.

ps에는 쿼리셋의 결과가 들어간 경우이다.

```html
{% for category, ps in posts.items %}
    {% for p in ps %}
    	<p>{{ p.title }}</p>
    {% endfor %}
{% endfor %}
```

