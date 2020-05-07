# ping 막기

`$ vi /etc/sysctl.conf` 에 추가

```shell
net.ipv4.icmp_echo_ignore_all = 1
```

`$ sysctl -p`로 동기화

![img](./img/img8.PNG)

