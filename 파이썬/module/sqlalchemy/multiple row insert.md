# multiple row insert

### bulk_insert_mappings 함수를 사용하자!



```python
for r in restaurants:
    menus = []
    for m in menu_arr:
        menus.append({
            'name' : m['name'],
            'price' : m['price'],
            'restaurant_id' : r.id
        })
        
    session.bulk_insert_mappings(Menu, menus)
```



- https://stackoverflow.com/questions/3659142/bulk-insert-with-sqlalchemy-orm