# ComtextLoaderListener의 역할

계층 별로 나눈 xml 설정 파일이 있다고 가정할 때, web.xml에서 모두 load되도록 등록할 때 사용.

**contextConfigLocation**라는 파라미터를 쓰면 Context Loader가 load할 수 있는 설정 파일을 여러개 쓸 수 있다.

web.xml에 contextConfigLocation이 따로 없으면 /WEB-INF/applicationContext.xml을 쓰게 된다.

