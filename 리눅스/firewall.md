# firewall

### 실행 여부

`$ firewall-cmd --state`

## 다시 로드

`$ firewall-cmd --reload`

### 사용중인 서비스/포트

`$ firewall-cmd --list-all`

### 포트 추가

`$ firewall-cmd --add-port=5432/tcp`

### 포트 삭제

`$ firewall-cmd --remove-port=5432/tcp`



- https://www.manualfactory.net/10153