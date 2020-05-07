# apache in linux (ubuntu)

#### 설치

> sudo apt-get install apache2

> yum install httpd

#### 특정 port 열기

`ports.conf`파일에서 **Listen `port`**를 입력한다.

> cd /etc/apache2
>
> sudo vim ports.conf

![img](./img/img1.png)

### 아파치 설정 파일 수정

`vi /etc/apache2/site-available/000-default.conf` 파일을 수정한다. 실행한 프로그램의 위치를 입력해서 이 프로그램을 아파치를 통해 실행할 것이라는 것을 알려준다.

![img](./img/img2.png)

[예시]

## for Python

#### 아파치 mod-wsgi 설치

> sudo apt-get install libapache2-mod-wsgi-py3



# tomcat

### 실행 및 중지

/.../tomcat8/bin/catalina start

/.../tomcat8/bin/catalina stop

### 쉘로 실행 시키기

1. `/etc/init.d` 에 tomcat으로 shell 파일을 만든담.

    ```shell
    #!/bin/sh 
    # 
    # Startup script for Tomcat for HMO
    # 
    # chkconfig: 35 85 35 
    # description: Start Tomcat 
    # 
    # processname: tomcat 
    # 
    # Source function library. 

    . /etc/rc.d/init.d/functions 

    export JAVA_HOME=/자신의 경로/jdk
    export CLASSPATH=.:$JAVA_HOME/lib/tools.jar
    export CATALINA_HOME=/자신의 경로/tomcat
    export PATH=$PATH:$JAVA_HOME/bin

    case "$1" in 

        start) 

            echo -n "Starting tomcat: " 
            daemon $CATALINA_HOME/bin/startup.sh 
            touch /var/lock/subsys/tomcat
            echo
            ;; 
        stop) 
            echo -n "Shutting down tomcat: " 
            daemon $CATALINA_HOME/bin/shutdown.sh 
            rm -f /var/lock/subsys/tomcat
            echo 
            ;; 
        restart) 
            $0 stop
            sleep 2 
            $0 start 
            ;; 
        *) 
            echo "Usage: $0 {start|stop|restart}" 
            exit 1 
    esac 
    exit 0
    ```

2. 해당 파일의 권한을 풀어준다. --> 실행권한을 준다. 

   `chmod 775 tomcat`



`/etc/init.d/tomcat stop`

`/etc/init.d/tomcat start `:+1:



### mod_jk 모듈

아파치와 톰캣을 연동하기 위해서 필요한 모듈

*AJP 프로토콜*을 사용해서 아파치와 톰캣을 연동해준다. 

- AJP 프로토콜
  - 웹 서버 뒤에 있는 어플리케이션 서버로부터 웹 서버로 들어오는 요청을 위임할 수 있는 바이너리 프로토콜 이며 , 주로 로드밸런싱에 사용됨



### 가상 호스트

웹 서버에 기본적으로 존재하는 호스트인 `main host`를 제외한 나머지 `host`



## httpd.conf 파일 분석

### `<Directory>`

`<Directory> ~ </Directory>` 는 지정한 디렉터리 이하의 모든 웹문서들에 대하여 어떤 서비스와 기능을 허용/거부 할 것인지를 설정한다.





<https://victorydntmd.tistory.com/226?category=706521>