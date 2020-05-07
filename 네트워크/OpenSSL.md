# OpenSSL



# SSL (Secure Socket Layer) protocol

## SSL 인증서

> 클라이언트와 서버간의 통신을 공인된 제 3자(CA) 업체가 보증해주는 전자화된 문서

클라이언트가 서버에 접속하면 서버는 클라이언트에게 인증서를 보낸다. 클라이언트는 이 인증서에 비롯하여 해당 서버를 신뢰할 수 있다.

## CA(Certicicate Authority)

인증서를 만드는 기업



# OpenSSL

SSL( == TLS )의 오픈소스 구현판.

CA로 부터 인증서를 발급받을 때마다 비용이 드는데, 이 과정을 `OpenSSL`을 통해 직접 인증기관을 만들고 ssl 인증서를 발급 받을 수 있다.