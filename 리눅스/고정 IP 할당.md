# 고정 IP 할당

`$ vi / etc/sysconfig/network-scripts/ifcfg-잡혀있는 네트워크`

```shell
BOOTPROTO= "static"
IPADDR= 게이트웨이에 맞는 IP #192.168.1.~
NETMASK= #255.255.255.0
GATEWAY= 게이트웨이 #192.168.1.1 
DNS1=DNS #168.126.36.1
```



나는 안된다.