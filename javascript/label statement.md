# label statement

`break`나 `continue`구문과 함께 사용할 수 있다
```
label : // js 에서 허용하는 모든 시별자
    statement 
```


```javascript
my_label :
for () {
    break my_label
}
```


```javascript
foo: {
  console.log('face');
  break foo; // 반복문이 아닌 곳에서도 사용할 수 있다.
  console.log('this will not be executed');
}
```
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/label