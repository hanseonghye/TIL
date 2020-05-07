# 절대경로 import



## 방법 1. cross-env 모듈

### install cross-env

`$ yarn add cross-env`



### path 설정

> package.json 파일 수정

```json
"start": "cross-env NODE_PATH=src/ react-scripts start",
"build": "cross-env NODE_PATH=src/ react-scripts build",
```



## 방법 2. jsconfig.json 파일 생성

```json
{
  "compilerOptions": {
    "baseUrl": "src"
  },
  "include": ["src"]
}
```





두 방법 모두다 

`components/~~~~` 로 import 할 수 있다.



