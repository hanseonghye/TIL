# Forever

서버에 접속하지 않을 때도 프로그램이 동작하게 해준다!



- 실행

    ```
    forever start file.js  --> 절대경로로 하면 어느 곳에서나 시행할 수 있다.
    forever start -l /파일 경로/logFile.log file.js --> 로그 파일 작성
    forever start -a -l /파일 경로/logFile.log file.js --> 로그파일 append
    ```
- 정지
    ```
    forever stop file.js
    ```

- 현재 실행중인 forever 목록

  ```
  forever list
  forever stopall
  forever stop 0  --> 0번 forever 모듈을 정지 시킴
  ```


