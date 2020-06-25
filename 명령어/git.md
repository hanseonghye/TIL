# Git 명령어

### git 최초 설정

`$ git config --global user.name "[name]"`

` $ git config --golbal user.email [email] `





## remote 

### remote 등록

`$ git remote add origin [url]`

### remote 삭제

`$ git remote remove origin`

### remote 확인

`$  git remove -v`





### 삭제된 목록 update

`$ git add `를 할 때 삭제된 파일을 적용하고 싶은데 적용안될 때가 있다 (결국 git 에 삭제된 파일이 남아 있다는 말.)

삭제된 파일을 git에서도 제거하자.

`$ git rm -r --cached . `



### push 되돌리기 , 복구

`$ git reset --hard [push id]`

한 다음에 push 하기

`$ git push -f origin [branch]`

근데 이렇게 하면 이전 commit이 다 날아간다 :cry:

다른방법이 있는지는 모르겠담..



### 저장소에서 하위 dir만 clone하기

1. clone할 dir 만들고 이동. init도 해준다.

   `# git init`

2. sparse Checkout 이 가능하도록 설정

   `# git config core.sparseCheckout true`

3. remote 추가

   `# git remote add -f origin [url] `

4. 가져오고 싶은 파일이나 dir만 `.git/info/sparse-checkout` 파일에 기술한다.

   `# echo "python-crawler" >> .git/info/sparse-checkout`

   나의 경우는 해당 저장소중 `python-crawler` dir만 가져오고 싶었다. 

   sparse-checkout 파일이 없으면 생성해줘야 한다.

5. pull!

   `git pull origin master`

<https://www.lesstif.com/pages/viewpage.action?pageId=20776761>





## git ignore file 안 먹힐 때

` >> git rm -r --cached .`





## 변경된 파일 pull 한 시점으로 되돌리기

`# git checkout --파일명`





## add

### add 취소

`git reset`

`git reset 파일명`





## 한글 깨짐 해결

`git config --global core.quotepath false`



## show

### commit 내역 자세히 확인
`git show`



### 파일 확인

`git show --name-only`