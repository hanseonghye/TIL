# form

## onSubmit



### PhoneForm.js

```react
class PhoneForm extends Component {
    state = {
        name: '',
        phone: ''
    }


	handleSubmit = (e) => {
        e.preventDefault()
        this.props.onCreate(this.state)
        
        this.setState({
            name: '',
            phone: ''
        })
    }
    
    render() {
        return (
        	<form onSubmit={this.handleSubmit}>
            	<input name="name" />
                <input name="phone" />
                <button type="submit">등록</button>
            </form>
        )
    }
}
```



- `e.preventDefault()` 를 쓰는 이유
  - 기존의 `form`의 `submit`이 발생해서 페이지를 다시 불러오게 되는 상황을 막고 우리가 만든 함수만 실행되고 끝나게 하기 위해서.



### App.js

```react
import PhoneForm from './components/PhoneForm'

class App extends Component {
    handleCreate = (data) => {
        // todo
    }
    
    render() {
        return (
        	<div>
            	<PhoneForm onCreate={this.handleCreate} />
            </div>
        )
    }
}
```



- https://velopert.com/3634