# alipsis

특정 문자열의 길이가 길때 `...`  처리를 하자

1. width및 height 처리를한다.
2. alipsis 처리를 해준다. --> 여기서 순서 중요하다.

```css
p.up {
	width: 80px;
	height: 20px;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
}
```

