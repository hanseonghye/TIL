# serializer

```python
from rest_framework import serializers, viewsets
from .models import CustomUser as User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

`Serializer` 는 api를 통한 요청에 대한 응답의 형태를 결정해주는 클래스.

`UserViewSet`은 요청을 처리하여 응답을 해주는 클래스이다. 추후에 이곳에 get,post,put,patch,delete에 대한 액션을 지정해 주는 것이 가능하다.

