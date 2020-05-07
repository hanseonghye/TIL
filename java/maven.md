# maven

> 자바에서 프로젝트를 빌드하고 관리하는 도구.

- 플러그인을 실행해주는 프레임워크. 여러개의 플러그인으로 구성되어 있다.
- 모든 작업은 프롤그인에서 수행한다.
  - 플러그인 == (Goal의 집합)
  - Goal == 특정 작업. 최소한의 실행 단위.

- 빌드 절차 간소화 & 동일한 빌드 시스템 제공
  - 이미 정해진 라이프 사이클에 의하여 작업을 수행하기 때문.

## 라이프 사이클

- 메이븐의 동장 방식은 일련의 단계에 연계된 Goal을 실행하는 것이며, 논리적인 작업 흐름인 단계의 집합을 라이프 사이클이라 한다.
- 사전 정의된 순서대로 빌드 단계를 수행하며, 모든 빌드 단계는 이전 단계가 성공적으로 실행됐을 때, 실행된다.
- 빌드 단계는 goal들로 구성된다.
- 메이븐은 3개의 표준 라이프 사이클을 제공한다
  - clean : 빌드 시 생성됐던 산출물을 지운다.
  - default : 일반적인 빌드 프로세스를 위한 모델. 프로젝트의 타입에 따라 다르게 정의됨
  - site : 프로젝트 문서와 사이트 작성을 수행.

## pom.xml

> 자바프로젝트의 빌드 툴을 **maven**으로 설정했다면 프로젝트 최상위 디렉토리에 생기는 파일. 
>
> 프로젝트 내 빌드 옵션을 설정한다.
- project 태그로 둘러싸여서 section 별로 여러 정보를 나타내거나 설정할 수 있다.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>com.cafe24</groupId>
	<artifactId>mysite2</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<packaging>war</packaging>

	<properties>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
		<org.springframework-version>4.3.1.RELEASE</org.springframework-version>
		<org.springframework-version>4.0.3.RELEASE</org.springframework-version>
		<jcloverslf4j.version>1.7.6</jcloverslf4j.version>
		<logback.version>1.1.1</logback.version>
	</properties>

	<dependencies>

		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>jcl-over-slf4j</artifactId>
			<version>${jcloverslf4j.version}</version>
		</dependency>
		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-classic</artifactId>
			<version>${logback.version}</version>
		</dependency>
		<!-- mariadb java client -->
		<dependency>
			<groupId>org.mariadb.jdbc</groupId>
			<artifactId>mariadb-java-client</artifactId>
			<version>2.4.0</version>
		</dependency>

		<!-- jstl -->
		<dependency>
			<groupId>javax.servlet</groupId>
			<artifactId>jstl</artifactId>
			<version>1.2</version>
		</dependency>

		<!-- Spring core -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-context</artifactId>
			<version>${org.springframework-version}</version>

			<!-- JCL 제외 -->
			<exclusions>
				<exclusion>
					<groupId>commons-logging</groupId>
					<artifactId>commons-logging</artifactId>
				</exclusion>
			</exclusions>
		</dependency>

		<!-- Spring Web ( Servlet / Anotation ) -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-web</artifactId>
			<version>${org.springframework-version}</version>
		</dependency>

		<!-- Spring MVC -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-webmvc</artifactId>
			<version>${org.springframework-version}</version>
		</dependency>

		<!-- spring aspect -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-aspects</artifactId>
			<version>${org.springframework-version}</version>
		</dependency>

		<!-- spring jdbc -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-jdbc</artifactId>
			<version>${org.springframework-version}</version>
		</dependency>

		<!-- Common DBCP -->
		<dependency>
			<groupId>commons-dbcp</groupId>
			<artifactId>commons-dbcp</artifactId>
			<version>1.4</version>
		</dependency>

		<!-- MyBatis -->
		<dependency>
			<groupId>org.mybatis</groupId>
			<artifactId>mybatis</artifactId>
			<version>3.2.2</version>
		</dependency>

		<dependency>
			<groupId>org.mybatis</groupId>
			<artifactId>mybatis-spring</artifactId>
			<version>1.2.0</version>
		</dependency>

		<!-- jackson -->
		<dependency>
			<groupId>com.fasterxml.jackson.core</groupId>
			<artifactId>jackson-databind</artifactId>
			<version>2.4.4</version>
			<exclusions>
				<exclusion>
					<groupId>com.fasterxml.jackson.core</groupId>
					<artifactId>jackson-core</artifactId>
				</exclusion>
				<exclusion>
					<groupId>com.fasterxml.jackson.core</groupId>
					<artifactId>jackson-annotations</artifactId>
				</exclusion>
			</exclusions>
		</dependency>
		<dependency>
			<groupId>com.fasterxml.jackson.core</groupId>
			<artifactId>jackson-core</artifactId>
			<version>2.4.4</version>
		</dependency>

		<dependency>
			<groupId>com.fasterxml.jackson.core</groupId>
			<artifactId>jackson-annotations</artifactId>
			<version>2.7.4</version>
		</dependency>


		<!-- validation -->
		<dependency>
			<groupId>javax.validation</groupId>
			<artifactId>validation-api</artifactId>
			<version>1.0.0.GA</version>
		</dependency>

		<dependency>
			<groupId>org.hibernate</groupId>
			<artifactId>hibernate-validator</artifactId>
			<version>4.2.0.Final</version>
		</dependency>

	</dependencies>



	<profiles>
		<profile>
			<id>production</id>
			<build>
				<resources>
					<resource>
						<directory>${project.basedir}/src/main/resources</directory>
						<excludes>
							<exclude>**/*.java</exclude>
						</excludes>
					</resource>
					<resource>
						<directory>${project.basedir}/src/main/production/resources</directory>
						<excludes>
							<exclude>**/*.java</exclude>
						</excludes>
					</resource>
				</resources>
				<plugins>
					<plugin>
						<groupId>org.apache.maven.plugins</groupId>
						<artifactId>maven-resources-plugin</artifactId>
						<configuration>
							<encoding>UTF-8</encoding>
						</configuration>
					</plugin>
				</plugins>
			</build>
			<dependencies>
				<!-- Servlet -->
				<dependency>
					<groupId>javax.servlet</groupId>
					<artifactId>javax.servlet-api</artifactId>
					<version>3.0.1</version>
					<scope>provided</scope>
				</dependency>
				<dependency>
					<groupId>javax.servlet.jsp</groupId>
					<artifactId>jsp-api</artifactId>
					<version>2.0</version>
					<scope>provided</scope>
				</dependency>
			</dependencies>
		</profile>
	</profiles>

	<build>
		<sourceDirectory>src/main/java</sourceDirectory>
		
		<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-compiler-plugin</artifactId>
				<version>3.8.0</version>
				<configuration>
					<source>1.8</source>
					<target>1.8</target>
				</configuration>
			</plugin>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-war-plugin</artifactId>
				<version>3.2.1</version>
				<configuration>
					<warSourceDirectory>src/main/webapp</warSourceDirectory>
				</configuration>
			</plugin>
				
			<plugin>
				<groupId>org.codehaus.mojo</groupId>
				<artifactId>tomcat-maven-plugin</artifactId>
				<configuration>
					<url>http://127.0.0.1:8080/manager/text</url>
					<path>/mysite2</path>
					<username>admin</username>
					<password>manager</password>
				</configuration>
			</plugin>
			
		</plugins>
	</build>
</project>
```



### properties tag

- 자바, 스프링 등의 버전 관리를 해주는곳.

- pom.xml에서 중복해서 사용되는 상수 값(ex 버전)들을 지정해 놓는 부분.



### dependency tag

- 라이브러리 설정
- 개발자는 프로젝트에 사용할 라이브러리 이 태그에 정의하면, 메이븐이 repository에서 검색해서 자동으로 추가해 준다.

### profiles

- dev, prod 등으로 개발할때, 릴리즈할 때를 나눠야 할 필요가 있는 경우 profiles태그에서 설정할 수 있다.
- 다른 환경에서 달라지는 설정을 각각 관리할 수 있다.

### build

- 빌드 관련된 정보를 설정하는 곳.
- 빌드에 사용할 플러그인 목록을 나열.

https://sjh836.tistory.com/131

