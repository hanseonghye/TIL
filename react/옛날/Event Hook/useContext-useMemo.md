# useContext & useMemo


## useContext
```javascript
import React, {useContext, createContext} from 'react'


const TestContext = createContext()
const TestContext2 = createContext()


const UseContextExample = () => {
    const hello = useContext(TestContext)
    const world = useContext(TestContext2)
    
    return (
        <div>
            {hello + ' ' + world }
        </div>
    )   
}


function App() {
    return (
        <div>
            <TextContext.Provider value='hello'> 
                <TextContext2.Provider value='world'>
                    <UserContextExample />
                </TextContext2.Provider>
            </TextContext.Provider>
        </div>
    )
}


export default App
```

값으로 `hello`, `world` 문자열을 준다.
`UserContextExample` 컴포넌트에서는 해당 값을 `useContext(TestContext) 를 통해 가져온다.


## useMemo
```javascript
const UseMemoExample = () => {
    const [str,  setStr] = useState('')
    const [strList, setStrList] = useState([])
    
    const insert = () => {
        const newList = strList.slice()
        newList.push(str)
        setStrList(newList)
    }
    
    const sum = (list) => {
        let strSum = ''
        for (let v of list)  {
            strSum += v + ''
        }
        return strSum
    }
    
    const result = useMemo(() => sum(strList), [strList])


    return (
        <div> 
            <input type='text' onchange={(e) => {setStr(e.target.value)}} />
            <button onClick={insert}>문자열 추가</button>
            {result}
        </div>
    )
}
```

`useMemo`의 두번째 인자가 변경될 때만 함수가 실행된다.


- https://gist.github.com/ninanung/6a2d37bebe1358591b48ac364261e744