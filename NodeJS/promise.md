# Promise

## 3가지 상태 (states)

> **new Promise()**로 생성하고 종료될 때까지 3가지 상태를 갖는다.

### Pending (대기)

- 비동기 처리 로직이 아직 완료 되지 않은 상태

```javascript
new Promise()
```

`new Promise()`메서드를 호출하면 대기 상태가 된다.

이때 콜백 함수의 인자로 `resolve`, `reject`에 접근 할 수 있다.

```javascript
new Promise(function (resolve, reject) {
    ...
})
```



### Fulfilled (이행) --> 완료를 말함

- 비동기 처리가 완료되어 프로미스가 결과 값을 반환해준 상태

```javascript
new Promise(function (resolve, reject) {
    resolve()
})
```

여기서 콜백 함수의 인자 `resolve`를 아래와 같이 실행하면 이행 상태가 된다.

이때, `then()`을 이용하여 처리 결과 값을 받을 수 있다.

```javascript
function getData() {
    return new Promise(function (resolve, reject) {
        let data = 100
        resolve(data)
    })
}

getData().then(function (resolvedData) {
    console.log(resolveData)
})
```



### Rejected (실패)

- 비동기 처리가 실패하거나 오류가 발생한 상태

`new Promise()`에서 콜백 함수 인자로 `resolve`와 `reject`를 사용할 수 있다.

여기서 `reject`인자로 `reject()`메서드를 사용하면 실패 상태가 된다.

```javascript
new Promise(function(resolve, reject) {
    reject();
})
```



- 실패 상태가 되면, 실패한 이유를 `catch()`로 받을 수 있다.

```javascript
function getData() {
    return new Promise(function (resolve, reject) {
        reject(new Error("Request is failed"))
    })
}

getData().then().catch(function (err) {
    console.log(err)
})
```



### 예제

```javascript
function getData() {
    return new Promise(function (resolve, reject) {
        $.get('url', function (res) {
            if (res) {
                resolve(res)
            }
            
            reject(new Error("err"))
        })
    })
}

getData().then(function (data) {
    console.log(data)
}).catch(function (err) {
    console.err(err)
}})
```

- 서버에서 제대로 응답을 받아오면 `resolve()`메서드를 호출하고, 응답이 없으면 `reject()`메서드를 호출한다. 
- 호출된 메서드에 따라 `then()`이나 `catch()`로 분기하여 데이터 또는 에러를 출력한다.





- https://joshua1988.github.io/web-development/javascript/promise-for-beginners/

