# django debug toolbar

### install

`> pip install django-debug-toolbar`



### setting.py

- INSTALLED_APPS

```python
INSTALLED_APPS = [
    ...
    'debug_toolbar',
]
```

- MIDDLEWARE 

```python
MIDDLEWARE = [
    ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
```

- INTERNAL_IPS 추가

```python
INTERNAL_IPS = ('127.0.0.1')
```



### urls.py

프로젝트의 `urls.py`파일에 debug-toolbar를 적용하자.

```python
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
```

