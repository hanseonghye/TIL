# socket 프로그래밍

### 서버

1. TCP 소켓 객체를 생성

   ```java
   ServerSocket serverSocket = new ServerSocket();
   ```

2. 소켓을 호스트의 포트와 연결

   ```java
   serverSocket.bind( new InetSocketAddress ( "localhost", 7000));
   ```

3. 클라이언트로 부터 소켓 연결이 올 때까지 대기( == Accept )한다.

   ```java
   Socket socket = serverSocket.accept()
   ```

4. 연결이 되면 통신을 위한 stream 객체를 얻는다.

   ```java
   InputStream is = socket.getInputStream();
   OutputStream os = socket.getOutputStream();
   ```

5. 데이터 통신을 한다.

   ```java
   is.read( buffer );
   os.write( buffer );
   ```

6. 클라이언트와 연결을 종료

   ```java
   is.close();
   os.close();
   socket.close();
   ```

   

