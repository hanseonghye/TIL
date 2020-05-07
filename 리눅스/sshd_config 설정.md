# sshd_config 설정



특정 사용자만 패스워드 방식으로 서버에 들어가게 하고 싶은 경우.

`/etc/ssh/sshd_config` 파일을 수정하자.

파일의 제일 아래에 다음을 넣어주자.

```txt

Match User 유저명
        PasswordAuthentication yes

```



저장한뒤 sshd 재시작

`# systemctl restart sshd`

