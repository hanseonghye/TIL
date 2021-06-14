# http-proxy-middleware

react에서 B도메인의 api를 호출할때 `proxy`를 적용해 보자!



`src/setupProxy.js` 파일 작성.

반드시 이 이름이여야하는거 같다.

```javascript
const {createProxyMiddleware} = require('http-proxy-middleware');

module.exports = function (app) {
    app.use('/api',
        createProxyMiddleware({
            target : 'http://localhost:3002',
            changeOrigin : true,
        }))
}
```

이러면 프록시가 등록되고,

`http://localhost:3002/api/~~~`형식의 api를 호출하고자 하면, 

`/api/~~~`형식으로만 call 하면 해당 프록시를 타고 호출한다.