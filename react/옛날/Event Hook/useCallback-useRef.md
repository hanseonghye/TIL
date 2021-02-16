# useCallback & useRef


## useCallback
리액트에서 컴포넌트가 다시 렌더링 될때 컴포넌트 안에 선언된 함수들을 새로 생성한다. 계속 같은 함수를 생성하는 것이다.
이 부분을 개선하기위해 나옴!


```javascript
const UseCallbackExample = () => {
    const [str, setStr] = useState('')
    const [strList, setStrList] = useState([])
    
    const change = useCallback((e) => {
        setStr(e.target.value)
    }, [])


    const insert = useCallback(() => {
        const newList = strList.slice()
        newList.push(str)
        setStrList(newList)
    }, [str, strList])

    const sum = useCallback((list) => {
        let stringSum = '';
        for(let value of list) {
          stringSum += value + ' ';
        }
        return stringSum;
    }, [])

    const result = useMemo(() => sum(stringList), [stringList, sum]);

    return (
        <div>
            <input type='text' onChange={change}/>
            <button onClick={insert}>문자열 추가</button>
            {result}
        </div>
    )
}
```


`change`,`sum` 함수의 경우, 두번째 인자로 빈 배열을 줬기 때문에 최초 렌더링 시에만 함수가 생성된다.
`insert` 함수의 경우 두번째 인자인 `str`과 `strList`가 변경될 때에 함수가 재생성 된다.
이 차이는 `change`,`sum`함수의 경우 `state`값을 사용하지 않으며, `insert`함수의 경우 `state`값을 사용하기  때문이다 (해당 값에 의존)


## useRef

`todo`