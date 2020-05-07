# LifeCycle API

> 컴포넌트가 브라우저에 나타날때, 사라질때, 업데이트 될 때 호출되는 api



## 컴포넌트 초기 생성

> 컴포넌트가 브라우저에 나타나기 전, 후에 호출되는 api

### constructor

```react
constructor(props) {
    super(props) 
}
```

- 컴포넌트가 새로 만들어 질 때마다 생성자 함수가 호출된다.



### componentDidMount

```react
componentDidMount() {
}
```

화면에 컴포넌트가 나타나게 됐을때 호출. 주로 `dom`을 사용해야하는 외부 라이브러리 연동을 하거나, 해당 컴포넌트에서 필요로하는 데이터를 요청하기위해 `ajax`요청을 하거나, `dom`의 속성을 읽거나 직접 변경하는 작업을 한다.

- 외부 라이브러리 연동
  - ex) d3, ...
- 컴포넌트에서 필요한 데이터 요청
  - ex) ajax, ...
- dom에 관련된 작업
  - ex) 스크롤 설정, 크기 읽어오기, ...



## 컴포넌트 업데이트

> props, state의 변화에 따라 결정됨.
>
> 업데이트가 되기 전, 후에 호출되는 api가 있다

### ~~componentWillReceiveProps~~

```react
componentWillReceiveProps(nextProps) {
}
```

~~컴포넌트가 새로운 `props`를 받게 됐을 때 호출된다. 주로 `state`가 `props`에 따라 변해야 하는 로직을 작성. 새로 받게될 `props`는 `nextProps`로 조회 할 수 있으며, 이 때 `this.props`를 조회하면 업데이트 되기전의 값이다.~~

V16.3부터 안씀!  ➡ `getDerivedStateFromProps()` 로 대체



### static getDerivedStateFromProps

```react
state getDerivedStateFromProps(nextProps, prevState) {
}
```





너무 많아서 공부하면서 더 적겠음..



- https://velopert.com/3631