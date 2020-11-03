# flow

## ~~connect???~~

### example

```react
class PaletteContainer extends Component {
  handleSelect = color => {
    const { changeColor } = this.props;
    changeColor(color);
  };

  render() {
    const { color } = this.props;
    return <Palette onSelect={this.handleSelect} selected={color} />;
  }
}


const mapStateToProps = state => ({
  color: state.Counter.color,
});

const mapDispatchToProps = dispatch => ({
  changeColor: color => dispatch(changeColor(color)),
});

export default connect(mapStateToProps, mapDispatchToProps)(PaletteContainer);
```



1. store가 가진 state를 어떻게 props에 엮을지 정한다 -> **mapStateToProps**
2. Reducer에 action을 알리는 함수인 `dispatch`를 어떻게 props에 엮을지 정한다. -> **mapDispatchToProps**
3. 위에 두가지가 적용된 `props`를 받을 component를 정한다.
4. Store와 Reducer를 연결시킬 수 있도록 만들어진 Component가 반환값이 된다. -> `connect(mapStateToProps, mapDispatchToProps)(Component)`





#### mapStateToProps

스토어 안에 들어있는 state를 props로 전달해준다

#### mapDispatchToProps

액션 생성함수들을 props로 전달하고 디스패치에 등록한다. 





## action creator

`액션을 만드는 함수`

단순히 파라미터를 받아와서 액션 객체 형태로 만들어 준다.

```react
function addTodo(data) {
    return {
        type: "ADD_TODO",
        data
    }
}


// arrow function
const addTodo = data => ({
    type: "ADD_TODO",
    data
})
```





## reducer

`변화를 일으키는 함수, state에 변화를 준다.`

현재 상태와 전달 받은 액션을 참고하여 새로운 상태를 만들어 반환한다.

```react
function reducer(state, action) {
    return alteredState
}
```





## store

일반적으로 한 앱 당 하나의 스토어를 만들게 된다.

스토어 내부엔 현재 앱 상태와 리듀서가 포함돼 있고 추가적으로 몇가지 내장 함수들이 있다.



### dispatch

스토어 내장 함수 중 하나. 액션이 일어나게 만들어 준다.

액션을 파라미터로 전달한다.

1. 디스패치가 호출됨
2. 스토어는 리듀서 함수를 실행
3. 해당 액션을 처리 -> 새로운 상태 만듬







## dir 구조

### components

하위 파일들은 렌더링될 컴포넌트 객체이다. `state`와 `action`을 주입받는다.



### containers

`connect함수`를 이용하여 스토어의 `state`와 `action`을 `props`로 전달하고 `components`에 상태를 주입. 특정 액션을 `dispatch`로 등록하여 사용자가 특정한 이벤트(onClick ...)를 수행하여 리듀서에 의해 `state`가 변경되고 재 렌덩리 되게 한다.