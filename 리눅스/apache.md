# apache in linux (ubuntu)

#### 설치

> sudo apt-get install apache2

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

2. 실행 파일로 만들어준다.

   `chmod 775 tomcat`



`/etc/init.d/tomcat stop`

`/etc/init.d/tomcat start `:+1: