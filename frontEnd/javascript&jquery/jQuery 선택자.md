# jQuery 선택자

```javascript
//1. 태그 선택자
var $li = $('li')
$li.css('color', '#000')

//2. id 선택자
$('#one').css('color', '#00f')
$('#two').css('color', '#0f0')

//3. class 선택자
$('.red').css('color', '#f00')
$('.blue').css('color', '#00f')
$('.a.b.c').css('color', '#00f') // class="a b c" 인 경우

//4. 자식
$('div > ul > li').css('font-weight', 'bold')

//5. 자손
$('ul strong').css('font-weight', 'normal')

//6. 전체
$('*').css('font-size', '1.1em')

//7. 그룹
$('#one, div> ul > *').css('text-decoration', 'underline')

//8. 인접
$('#one + li + li ').css('color','black') // <li class='red'>bbb</li> <-- 이걸 가리킴.

//9. 속성. id나 class와 같은 속성 외에도 직접 지정한 속성도 가능하다.
$('li[id]').css('text-decoration','line-through')//li중 id 속성을 가지고 있는 element들
$('li[class!="blue"]').css('font-style','italic')

//10. filter
$('li:first').css('background-color','#aaa') // 전체 li 중 첫번째 값.
$('ul li:first-child').css('background-color','#aaa')
```



- 그밖에 filter로 쓸 수 있는 것들
  - last
  - odd
  - even
  - contains(어떤것) // 부분
  - has(어떤것) //전체?

