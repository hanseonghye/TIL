# 동적 form 생성 및 submit

```js
var form = $('<form></form>');
form.attr('action', url);
form.attr('method', 'post');
form.appendTo('body');
var idx = $("<input type='hidden' value="+idx+" name='idx'>");
var pwd = $("<input type='hidden' value="+pw+" name='password'>");
var mode = $("<input type='hidden' value='educomPw' name='mode'>");
form.append(idx);
form.append(pwd);
form.append(mode);
form.submit();
```

- https://devgwangpal.tistory.com/55