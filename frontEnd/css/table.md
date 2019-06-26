# table

```html
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>테이블</title>
<style type="text/css" media="screen">
* {
	margin: 0;
	padding: 0
}

body {
	font-family: '맑은 고딕', 돋움, 굴림;
	font-size: 0.75em;
	color: #333
}

.tbl-ex {
	margin: 20px auto;
	border: 1px solid #000;
	border-collapse: collapse;
	border-left-width: 0;
	border-right-width: 0;
}

.tbl-ex th, .tbl-ex td {
	border: 1px solid #000;
	padding:8px;
	border-left-width: 0;
	border-right-width: 0;
}

.tbl-ex th{
	background-color: #999;
	color: #fff;
	font-size: 1.1em;/* 1.1 X 16 */
	border-top-width: 2px;
	border-bottom-width: 2px;
}

.tbl-ex td{
	border-style: dotted;
}

.tbl-ex tr.even td{
	background-color: #e8ecf6;
}

.tbl-ex tr:hover td{
	background-color: #fc6;
	cursor: pointer;
}

</style>
</head>
<body>
	<table  class="tbl-ex">
		<tr>
			<th>형식</th>
			<th>선택자 이름</th>
			<th>스타일 적용 요소</th>
			<th>호환성</th>
		</tr>
		<tr>
			<td>a</td>
			<td>HTML</td>
			<td>모든 HTML에 적용</td>
			<td>IE4, FF1,Safari 1, 크롬 1,오페라 3.5, CSS1</td>
		</tr>
		<tr class="even">
			<td>.classname</td>
			<td>클래스</td>
			<td>클래스로 정의해 준 HTML 태그</td>
			<td>IE4, FF1,Safari 1, 크롬 1,오페라 3.5, CSS1</td>
		</tr>
		<tr>
			<td>a.classname</td>
			<td>종속 클래스</td>
			<td>특정 HTML 태그에 종속된 클래스</td>
			<td>IE4, FF1,Safari 1, 크롬 1,오페라 3.5, CSS1</td>
		</tr>
		<tr class="even">
			<td>#idname</td>
			<td>아이디</td>
			<td>아이디로 정의해준 HTML 태그</td>
			<td>IE4, FF1,Safari 1, 크롬 1,오페라 3.5, CSS1</td>
		</tr>
		<tr>
			<td>a#idname</td>
			<td>종속아이디</td>
			<td>특정 HTML 태그에 종속된 아이디</td>
			<td>IE4, FF1,Safari 1, 크롬 1,오페라 3.5, CSS1</td>
		</tr>
		<tr class="even">
			<td>*</td>
			<td>전체 선택</td>
			<td>모든 HTML 태그에 적용</td>
			<td>IE4, FF1,Safari 1, 크롬 1,오페라 3.5, CSS2</td>
		</tr>
	</table>
</body>
</html>

```

![img](./img/img2.png)