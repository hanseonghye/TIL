# load

## DOMContentLoaded

html이 모두 로드되고, DOM트리가 완성되었지만 외부 리소스(img, script, ...) 가 아직 로드되지 않았을때

```js
$(document).ready(function() {
    // ready 는 ComContentLoaded의 jquery 버전
})


window.addEventListener('DOMContentLoaded', function(){ 
    //실행될 코드 
})
```



## load ( == onload )

브라우저의 모든 리소스가 로드되었을때





즉 `DomContentLoaded`가 `load`보다 먼저 발생한다.







- https://mygumi.tistory.com/281
- https://webdir.tistory.com/515