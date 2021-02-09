# firewall

### 실행 여부

`$ firewall-cmd --state`

이때 `is not running`이 뜬다면 firewall이 설치 되어있는지 확인하자.

### 설치 확인

`# yum list installed firewalld`

### 설치

`# yum install firewalld`

### 실행

`# systemctl start firewalld`



## 다시 로드

`$ firewall-cmd --reload`

### 사용중인 서비스/포트

`$ firewall-cmd --list-all`

### 포트 추가

`$ firewall-cmd --add-port=5432/tcp`

`$ firewall-cmd --add-port=5432/tcp  --permanent`

` --permanent` 안 붙이면, reload 할때 reset된다.

### 포트 삭제

`$ firewall-cmd --remove-port=5432/tcp`



- https://www.manualfactory.net/10153