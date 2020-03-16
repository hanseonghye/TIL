# WebJar

> Jquert나 부트스트랩같은 클라이언트 라이브러리를 jar 파일로 만들어, 다른 java 라이브러리처럼 Mave이나 Gradle에서 사용할 수 있도록 한 서비스



## gradle

```xml
// https://mvnrepository.com/artifact/org.webjars.bower/jquery
compile group: 'org.webjars.bower', name: 'jquery', version: '3.4.1'
```



```html
<script src="/webjars/jquery/3.4.1/dist/jquery.min.js"></script>
```

이때 `</script>`로 닫아줘야 한다. `<script src=""/>` 안먹힘!



```xml
compile group: 'org.webjars', name: 'webjars-locator-core', version: '0.43'
```

`webjars-locator-core` 라이브러리를 추가해주면 script를 추가할때 버전을 명시 안해줘도 된다!



- <https://araikuma.tistory.com/28>