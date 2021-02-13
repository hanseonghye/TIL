# npm

Node Package Manager



#### npm update

```
npm install npm@latest -g
```



#### 버전별 install

```
npm install 모듈@버전
npm install 모듈@latest
npm install 모듈 --> 가장 최신 버전
```



#### 모듈 삭제

```
npm uninstall 모듈
```



#### ~~save 자동으로 되는듯~~

````
npm install --save 모듈  --> package.json 파일에 추가 // 
npm uninstall --save 모듈
````



### degit

git 프로젝트를 클론

다른 remote 저장소의 정보는 가져오지 않는다.

`npm degit [클론받을 url] [다운받을 dir]`

https://stove99.github.io/etc/2019/08/20/degit-project-template/