# apache

1. `$ yum install httpd`

2. `$ yum install mod_wsgi`

3. .conf 파일 생성

   /etc/httpd/conf.d 디렉토리 아래에 .conf 파일을 만든다.

   etc/httpd/httpd.conf에 추가해도 상관없지만 관리가 쉽도록 새로운 파일을 만든다.

   ```xml
   <VirtualHost *:80>
           WSGIScriptAlias / /myJango/myJango/mysite/wsgi.py
           <Directory /myJango/myJango/mysite>
           <Files wsgi.py>
                   Order deny,allow
                   Allow from all
           </Files>
           </Directory>
   </VirtualHost>
   ```

   ![img](./img/img2.png)

   - 80 port로 들어오는 url의 /아래 모든 요청은 /myJango/myJango/mysite/wsgi.py를 호출하게 된다.
   - wsgi.py파일은 모든 접근을 allow한다.

4.  wsgi.py 파일 수정

   ```python
   import os, sys
   
   from django.core.wsgi import get_wsgi_application
   
   path = os.path.abspath(__file__+'/../..')
   if path not in sys.path:
   	sys.path.append(path)
   
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
   
   ```

   

