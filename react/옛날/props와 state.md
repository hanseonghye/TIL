# props 와 state

## props

### defaultProps 

```react
import React, { Component } from 'react'

class MyName extends Component {
  static defaultProps = {
    name: '기본이름'
  }
  render() {
    return (
      <div>
        name --> <b>{this.props.name}</b>
      </div>
    )
  }
}


export default MyName
```





## state

### setState

> 객체로 전달되는 값만 업데이트 해준다.



```react
state = {
    number : 0,
    foo : 'bar'
}
```

`state`가 다음과 같을때 `this.setState({ number:1 });`을 하게 된다면 `foo`는 남고 `number`값만 업데이트 된다.

그런데 `setState`는 객체의 깊숙한 곳까지는 확인하지 않는다. 

```react
state = {
    number : 0,
    foo: {
        bar:0,
        foobar:1
    }
}
```

예를 들어 `state`가 다음과 같을때 

```react
this.setState({
    foo: {
        foobar : 2
    }
})
```

를 수행했을때는 `foobar`값만 업데이트 되는 것은 아니고 `foo` 객체 전체가 바뀌게 된다.

```react
{
    number : 0,
    foo : {
        foobar : 2
    }
}
```



`foobar`만 바꾸고 싶다면

```react
this.setState({
    number:0,
    foo: {
        ...this.state.foo,
        foobar: 2
    }
})
```

이렇게 수행해야 한다.

> `...`는 자바스크립트 연산자중 하나다. 기존의 객체 안에 있는 내용을 해당 위치에다가 풀어 준다는 의미.





 ### setState에 객체 대신 함수 전달하기

```react
this.setState({
    number: this.state.number + 1
})


this.setState(
	(state) => ({
        number : state.number
    })
)


this.setState(
	({number}) => ({
        number : number + 1
    })
)
```

같은 결과를 가져온다,

> `(stsate)` -->  `({ number })`   <==== 비구조화 할당





### 렌더링 될 필요 없는 값

> 렌더링 되는 것과 상관없는 값은 `state`에 넣어주지 않아도 된다. 

```react
class App extends Component {
    id = 0
    state = {
        ...
    }
}
```

