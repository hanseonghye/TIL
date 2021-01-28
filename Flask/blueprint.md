# blueprint

`endpoint`를 Components 별로 구성하게 하는 역할!



```python
import requests

from flask import (
  request,
  Blueprint,
  jsonify
)


from service.user_service import UserService


class UserView:
    user_app = blueprint('user_app', __name__, url_prefix='/user')
    
    @user_app.route('/signin', methods=['POST'])
    def signin()
    	...
        return jsonify()
```



`user`과 관련된 component들을 endpoint `user/`로 부터 시작이 되게끔 하는 것

```python
# app.py

def create_app():
    app = Flask(__name__)
    app.register_blueprint(UserView.user_app)
    
    return app
```

