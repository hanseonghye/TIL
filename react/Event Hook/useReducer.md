# useReducer

```javascript
import React, {useReducer} from 'react'

const reducer = (state, action) => {
    switch(action.type) {
        case 'CHANGE':
            return action.value
        default:
            return state
    }
}

const UseReducer= () => {
    // state와 해당 state의 값을 변경할 dispatch를 선언
    // useReducer 함수의 첫번째 인자는 reducer함수, 두번째는 state의 최초값
    const [ state, dispatch ] = useReducer(reducer, 'init')
    
    return (
    	<div>
        	<h3>{state}</h3>
        	<input type='text' value={state} onChange={(e) => dispatch({value: e.target.value, type: 'CHANGE'})} />
        </div>
    )
}


export default UseReducer;
```



- https://gist.github.com/ninanung/cb199ad80ac29da4ca6111b970956d79