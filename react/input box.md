# input box



## onChange

```react
class PhoneForm extends Component {
    state = {
        name: '',
        phone: ''
    }


	handleChange = (e) => {
        this.setState({
            [e.target.name] : e.targer.value
        })
    }
    
    
    render() {
        return (
         <form>
            <input value={this.state.name}
                onChange={this.handleChange}
                name="name"/>
            <input value={this.state.phone}
                onChange={this.handleChange}
                name="phone"/>

            <div>{this.state.name} / {this.state.phone}</div>
        </form>       
        )
    }
}

export default PhoneForm
```



`e.target.name`을 통해 `name`속성의 값을 가져올 수 있다.

> `[e.target.name]`  <-- Computed property names 라는 문법임, e.target.name 에 들어있는 값을 가져온다. ${val} 와 비슷한 느낌



- https://velopert.com/3634