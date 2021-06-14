# json-server👏

## install

`$ npm i -g json-server`


## run

`$ json-server --watch file.json --port 포트`





## route 추가

```json
{
        "/api/*" : "/$1"
}
```

`$ json-server db.json --routes 해당파일`

이렇게 실행하면 기존 url에 `api/기존url`형식으로 api를 호출할 수 있다.

