# useState
`ReactConf 2018`에서 `Event Hook`의 일원으로 등장했다.
기존의 `함수 방식의 컴포넌트`에서 `state`의 사용이 불가능하다는 단점을 보완하고, `class 기반 컴포넌트`를 대체할 목적으로 만들어짐.

### 기존의 class 기반의 컴포넌트
```javascript
import React from 'react'

class Example extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            test: 'initial value',
        }
    }

    changeText = (e) => {
        this.setState({
            test: e.target.value,
        })
    }

    render() {
        return (
            <div>
                <p>{this.state.test}
                <input onChange={this.changeText} />
            </div>
    }
}

export default Example
```


### useState를 통한 함수형 컴포넌트
```javascript
import React, {useState} from 'react';

const UseStateExample = () => {
    const [test, setTest] = useState('initial value')
    
    return (
        <div>
            <p>{test}</p> 
            <input onChange={(e) => {setTest(e.target.value)}} />
        </div>
    )
}


export default UseStateExample
```


**useState**는 `class 컴포넌트`의 `this.state`와 `this.setState`를 합친 것과 비슷하다.
함수 컴포넌트에서 `state`를 사용할 수 있게 해주며, 초기값 설정,  선언시 두번째 인자를 통해 `state의 변경`도 구현하라 수 있다.


- https://gist.github.com/ninanung/25bdbf78a720846e4dc4c30ac1c9ec9b