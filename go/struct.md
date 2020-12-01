# struct

go에서는 oop를 지원하는데 `class`가 아닌, `struct`로 지원한다. 메소더는 별도로 분리하여 정의한다.

```go
type person struct {
    name string
    age int
}


func main() {
    p := person{}
    p.name = "seonghye"
    p.age = 10
    
    
    var p1 person
    p1 = person{"seonghye",10}
   
    p2 := person{name:"seonghye", age:10}
}
```

