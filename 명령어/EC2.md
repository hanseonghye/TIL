# EC2


Local (window) 에서 EC2로 접근하기

- ssh로 접속
    ```
    ssh -i "pem 파일 경로" "전송파일경로" id@ec2~.amazonaws.com
    ```

- 로컬에서 파일 전송
    ```
    scp -i "pem 파일 경로" "전송파일경로" id@ec2~.amazonaws.com:"ec2저장경로"
    ```

