# 특정 list의 원소가 다른 list에 모두 포함되는지 확인하자

`request`에 특정 키워드가 포함되어있는지 확인하기 위해 사용했다.

```python
if not all(x in ['sender_name', 'sender_email', 'sender_phone_number'] for x in request):
	raise serializers.ValidationError("null sender value")
```

`sender-#` 세개의 원소중 하나라도 `request`에 포함되지 않으면 raise를 일으킨다.