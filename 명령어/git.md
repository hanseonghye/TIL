# Git 명령어


### remote
`$ git remote add origin [url]`



### git 최초 설정

`$ git config --global user.name "[name]"`

` $ git config --golbal user.email [email] `



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

