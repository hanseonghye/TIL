# http 모듈

### ListenAndServe

```go
http.ListenAndServe(":8080", nil)
```

웹서버가 구동되고 request를 기다리는 상태가 되도록 해줌.



### HandleFunc

어떤 request가 들어왔을 때, 어떤 일을 할 것인지 핸들러를 등록하는 함수

```go
http.HandleFunc("/amin", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprint(w, "hello bar")
	})
```

- http.ResponseWriter
  - response를 write하기 위한 인자

- http.Request
  - 사용자가 요청한 reuqest 정보를 가져오 있는 인자



- https://velog.io/@soosungp33/Golang%EC%9C%BC%EB%A1%9C-%EC%9B%B9%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0