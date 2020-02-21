# JSX

```react
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
```

여기서 `html` 같이 생긴 부분을 `JSX`라 한다.

jsx를 작성하면 이를 자바스크립트 형태로 변환해 준다. 





## JSX 규칙

### 두 개 이상의 엘리먼트는 하나의 엘리먼트로 감싸져야 한다.

```react
class App extends Component {
    render() {
        return (
        	<div>
            	hello
            </div>
            <div>
            	world
            </div>
        )
    }
}
```

🔽 두개의 `div`를 `Fragment`로 감싸줬다. `div`로 감싸줄 수도 있다.

```react
class App extends Component {
    render() {
        return (
            <Fragment>
                <div>
                    hello
                </div>
                <div>
                    world
                </div>
            </Fragment>
        )
    }
}
```



## style과 className

```react
import './App.css'

class App extends Component {
    render() {
        const style = {
            color: 'white'
        }
        
        return (
        	<div style={style} className="bbb">
            </div>
        )
    }
}
```



```css
# App.css

.bbb {
    color: red;
}
```





- https://velopert.com/3626