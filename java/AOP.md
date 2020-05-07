# AOP 

> Aspect Oriented Programming : 관점 지향 프로그래밍

- 기능을 **핵심 비지니스 로직**과  **공통 모듈**로 구분하고, 핵심 로직에 영향을 미치지 않고 사이사이에 공통 모듈을 효과적으로 끼워넣도록 하는 개발 방법.
- 즉! 공통 모듈을 만든 후에 코드 밖에서 이 모듈을 비즈니스 로직에 삽입하는 것.
- 코드 밖에서 공통 모듈들이 설정 된다는 것이 핵심이다.
- 공통 모듈
  - 보안 인증
  - 로깅 같은 요소들

### AOP가 사용되는 경우

1. 간단한 메소드 성능 검사

   개발 도중 다량의 db를 넣고 읽는 등의 작업에 대하여 시간을 측정하고 개선해 나가는 작업의 경우 매번 해당 메소드에 시간을 재는 함수 (System.currentTimeMills() )함수를 넣는 것은 매우 번거롭다. 이런 경우 aop를 적용하자.

2. 트랜잭션 처리.

3. 예외 변환

   예외가 발생했을 때, 그걸 잘잡아서 컨트롤 하자.

4. 로깅

5. 보안 (ex  session)



### method 를 기준으로 소요 시간을 측정하는 aop

```java
@Aspect
@Component
public class MeasureExecutionTimeAspect { // 실행시간 측정 aspect

	@Around( "execution(* *..repository.*.*(..)) || execution(* *..controller.*.*(..)) || execution(* *..service.*.*(..))" ) //repository 패키지에 있는 모든 class의 모든 method
	public Object aroundAdvice(ProceedingJoinPoint pjp) throws Throwable {
		// before
		StopWatch sw = new StopWatch();
		sw.start();
		// method 실행
		Object result = pjp.proceed();
		// after
		sw.stop();
		System.out.println("[ " + sw.getTotalTimeMillis() + "ms; in " + pjp.getTarget().getClass() + " ; "
				+ pjp.getSignature().getName()+" ]");
				// time;classname;methodname
		return result;
	}
}
```

