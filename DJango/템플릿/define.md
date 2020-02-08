# define

```html
{% load custom_tags %}

{% define 'helloooooo' as hello %}
<p>
    {{ hello }}
</p>
```



custom tag 를 load해주는것 잊지 말자~

참고로 custom_tags 라는 명은 아래의 커스텀 태그 파일의 파일명과 같다.



custom_tag

```python
@register.simple_tag(name='define')
def define(value=None):
    return value
```

