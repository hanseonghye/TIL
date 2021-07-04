# python-memcached for cache

## install

`$ pip install python-memcached`

## 설정

```python
# settings.py

CACHES = {
    'default':
        {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211'
        }
}
```

## 사용하기

```python

from django.core.cache import cache

# set
key = 'key'
value = 'value'
cache.set(key, value, 3600)


# get
cache.get(key)

```