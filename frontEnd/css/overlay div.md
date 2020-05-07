# Overlay div

```html
<!DOCTYPE html>
<html>
<head>
	<style>

	.wrapper {
	  position: relative;
	}


	.navi {
	  background-color: black;
	  height: 100px;
	}


	#infoi {
	  position: absolute;
	  top: 0;

	  background-color: red;
	  height: 20px;
	  width:20px;
	  padding: 10px 10px;
	}
	</style>
	<title></title>
</head>
<body>

<div class="wrapper">
  <div class="navi"></div>
  <div id="infoi">
  </div>
</div>

</body>
</html>
```

https://stackoverflow.com/questions/2941189/how-to-overlay-one-div-over-another-div 참고

overlay 할 div에 top을 설정해 주는 것이 중요한 부분.