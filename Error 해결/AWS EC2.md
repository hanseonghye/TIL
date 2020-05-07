

# AWS EC2



- ssh 연결 permission denied(publickey)

  ```tcl
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  Permissions for '.ssh/my_private_key.pem' are too open.
  It is required that your private key files are NOT accessible by others.
  This private key will be ignored.
  bad permissions: ignore key: .ssh/my_private_key.pem
  Permission denied (publickey)
  ```

  pem 파일을 admin 폴더 (C:\Users\Administrator)로 옮긴후 admin만 접근 가능하게 한다.
