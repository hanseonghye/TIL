# useEffect

`class 기반 컴포넌트`의 `componentDidUpdate`와 `componentDidMount`를 대신해 준다 !

```javascript
const UseEffectExample = () => {
    const [test, setTest ] = useState('init value')
    useEffect(() => {
        // 해당 컴포넌트가 렌더링 될 때마다 실행된다.
    })
    
    return (
        <div>
            <p>{test}</p> 
            <input onChange={(e) => {setTest(e.target.value)}} />
        </div>
    )
}
```


### state 특정 하기
`state`가 여러개 라면, 해당 `state`들이 변경 될 때마다 `useEffect`함수가 실행 될 것이다. 이것은 비효율적!
`useEffect`함수의 두번째 매개변수 인자를 통해 `state`를 특정 할 수 있다.
```javascript
    useEffect(() => {
    
    }, [test1])
    useEffect(() => {
    
    }, [test2])
```


### 첫번째 렌더링에만 호출 하기 == (첫 렌더링때에만 함수 생성)
```javascript
    useEffect(() => {
      console.log('첫 렌더링에만 호출')
    }, [])
```


## 컴포넌트가 unmount 될때 호출하기
```javascript
    useEffect(() => {
      console.log('state가 변경될 때 마다 호출!');
      return () => {
        console.log('언마운트 시 호출!')
      }
    })

```

- https://gist.github.com/ninanung/0ea87bc3d14ed8b1f9e7488561a4b910