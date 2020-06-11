e# trigger('click') vs click

jquery 에서 `click` 함수는 다음과 같다.

```js
jQuery.fn.click = function (data, fn) {
    if (fn == null) {
        fn = data;
        data = null;
    }

    return arguments.length > 0 ? this.on("click", null, data, fn) : this.trigger("click");
}
```

즉 `trigger("click")`를 실행한다. 

따라서 `trigger`를 사용하는게 한단계 덜 거치는 거며 좀 더 빠르다.



- <https://stackoverflow.com/questions/9666471/jquery-advantages-differences-in-trigger-vs-click>