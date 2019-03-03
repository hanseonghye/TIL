# HTTP 모듈



#### res.write VS res.end

write는 write할때 마다 데이터( 묶음이라 하자 )를 전송하는 것이 아닌 일정 묶음 이상의 데이터( --> 패킷 )가 모였을 때 전송한다. ( 전송상의 효율을 위해 )

반면 end로 데이터를 보내면 데이터를 바로 보내고 접속을 종료 한다.

---

#### http.get

```javascript
const http = require('http');

http.get('http://google.co.kr', (res) => {
    res.on('data', (data) => {
       // data 이벤트를 처리하는 부분
       // 네크워크의 상태가 좋지 않을 경우 나눠서 받게 됨.
    });
    
    res.on('end', () => {
    	// 'end' 이벤트는 모든 데이터를 다 받았음을 의미한다.
    })
}).on('error', (err) => {
    
})
```



#### http.post

헤더를 이용.

```javascript
const post_data = {
    'key1':'val1',
    'key2':'val2'
};

const post_options = {
    host:'postserver.com',
    port:'80',
    path:'/path',
    headers:{
        'Content-Type':'application/json'
    }
};

const post_req = http.request(post_options, (res) => {
    res.on('data', (d) => {
        
    });
});

post_req.write(post_data);
post_req.end();
```



