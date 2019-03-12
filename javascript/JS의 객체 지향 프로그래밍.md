# JS와 객체 지향 프로그래밍



프로젝트의 대형화로 인해 비슷한 함수나 객체를 묶어서 개발할 필요가 생김.

### Apply 와 Call

``` javascript
let myMethods = {
    getName : function(){
        return this.name;
    },
    getAge : function(){
        return this.age;
    }
};

let myData = {
    name : 'seonghye',
    age : 20
};

let myCar = {
    name : 'mini',
    age : 2019,
    color : 'blue'
};

console.log (myMethods.getName.apply(myData));
console.log (myMethods.getAge.call(myCar));
```

call은 인자 하나하나(1,2,3,4,5)를 apply는 리스트([1,2,3,4,5])를 전달한다.



### bind

- 문제

  콜백 함수 안에서의 this는 window를 가르킨다. 그럼 어떻게 콜백에서 객체에 접근할 수 있을까 ?

  ``` javascript
  let obj = {
      data : 'dummy',
      time : function(){
          setTimeout(function(){
              console.log(this); // --> window
              console.log(this.data); // undefined
          },1000)
      }
  }
  
  obj.time();
  ```

1. scope 를 활용

   ``` javascript
   let obj = {
       data : 'dummy',
       time : function(){
           let that = this;
           window.setTimeout(function(){
               console.log(that.data); 
           },1000)
       }
   }
   
   obj.time();
   ```

2. bind()

   ``` javascript
   let obj = {
       data : 'dummy',
       time : function(){
           window.setTimeout( function(){
               console.log(this.data);
           }.bind(this),1000)
       }
   }
   
   obj.time()P;
   ```




https://wayhome25.github.io/javascript/2017/02/18/js-oop-1/