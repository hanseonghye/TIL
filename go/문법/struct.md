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





## method

```go
type rect struct {
    width, height int
}


func (r *rect) area() int {
    return r.width * r.height
}
```



## interface

`명명된 메서드 들의 모음`

인터페이스에 있는 모든 메서드를 구현해야 한다 !



```go
type geometry interface {
    area() float64
    perim() float64
}


type rect struct {
    width, height float64
}


type circle struct {
    radius float64
}


func (r rect) area() float64 {
    return r.width * r.height
}

func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}

func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

func measure(g geometry) { // interface를 인자로 갖는 함수
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}


func main() {
    r := rect{width: 3, height: 4}
    c := circle{radius : 5}
    
    
    measure(r)
    measure(c)
}
```

`circle`과 `rect` 구조체는 모두 `geometry` 인터페이스의 메소드를 구현했기 때문에 함수 `measure`의 인자로 사용 될 수 있다.



- https://mingrammer.com/gobyexample/methods/