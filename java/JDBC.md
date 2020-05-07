### JDBC

> Java Database Connectivity

- 자바를 이용한 데이터 베이스 **접속**과 **SQl문장의 실행**. 
- 실행 결과로 얻어진 데이터의 핸들링을 제공하는 방법과 절차에 관한 규약.
- 자바 프로그램 내에서 **SQL문**을 실행하기 위한 **자바 API**
- SQL과 프로그래밍 언어의 통합 접근 중 한 형태.



### 사용 방법

> JDBC를 사용하는 방법은 어떤 데이터베이스를 사용하던지 같다.

1. `Class.forName()`을 이용해서 드라이버 로드
2. DriverManager.getConnection()으로 연결 얻기
3. `Connection` 인스턴스를 이용해서 `Statement` 객체 생성
4. Statement 객체의 `결과`를 ResultSet이나 int에 받기

```java
public class ConnectionTest {

	public static void main(String[] args) {
	
		Connection conn = null;
		try {
			//1. JDBC Driver(MariaDB) 로딩
			Class.forName("org.mariadb.jdbc.Driver");
			
			//2.연결하기
			String url = "jdbc:mariadb://ip:3307/db";
			conn = DriverManager.getConnection(url,id,pw);

			System.out.println("연결 성공");
		} catch (ClassNotFoundException e) {
			System.out.println("드라이버 로딩 실패 : "+e);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			System.out.println("error "+e);
		}finally {
				try {
					if(conn!=null) {
						conn.close();
					}
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
	}
}
```

