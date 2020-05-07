# State와 Props

> state는 나의 데이터, props는 다른 누구로부터 받는 데이터.
>
> 여기서 누구는 보통 부모 component 또는 상태머신(vuex)이다.





## State

```vue
<template>
	<div v-bind:style="{ width: width + 'px', height: height + 'px'}" class="box">
    </div>
</template>


<script>
export default {
    data() {
        return {
            width: 40,
            height: 80
        };
    }
};
</script>
```

`state`는 **data()** 라는 함수를 이용하여 구성 할 수 있다.





## Props

```vue
// App.vue

<template>
	<div>
        <Box color="blue"/>
        <Box color="pink"/>
        <Box/>
    </div>
</template>


<script>
import Box from "./components/Box";
    
export default {
    name: "app",
    components: {
        Box
    }
};
</script>


<style>
    .blue {
        background : blue;
    }
    
    .pink {
        background : pink;
    }
</style>
```

부모 컴포넌트에 해당한다. Box 컴포넌트를 호출 한다.



```vue
// Box.vue

<template>
	<div v-bind:style="{ width: width + 'px', height: height + 'px'}" v-bind:class="['box', color]"></div> 
</template>


<script>
export default {
    data() {
        return {
            width: 40,
            height: 80
        };
    },
    props: {
        color: { type : String, default: ""}   // 값을 받아옴
    },
};
</script>


<style scoped>
.box {
    border:1px solid #000;
}
</style>
```



- `props`를 통해 `color`값을 받아온다.
- 이 값을 `template`에 적용하면 된다. 
  - `v-bind:class` , `:class`를 통해서 `class` 값을 넣어 줄 수 있다. 배열형태로 들어간다.