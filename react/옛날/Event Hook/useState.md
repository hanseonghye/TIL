# useState
컴포넌트의 상태값을 설정할 수 있다.

- 매개변수는 상태값의 초기값을 의미한다.

- 배열을 반환한다.
  - 배열의 첫 아이템은 상태값
  - 두번째 아이템은 상태값 변경 함수

```react
const [state, setState] = useState([]);
# state를 []로 초기화
```

