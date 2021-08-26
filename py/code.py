# < ----- 1등급 ----- >
# no.1 SQL 삽입 pg.148
# PreparedStatement 객체 사용(데이터 직접 입력 방지)
# ex) https://earthconquest.tistory.com/m/172?category=888280
# MyBatis : $ 기호말고 #기호 사용 ex) '%${keyword}%' -> '%'||#{keyword}||'%' 
# Hibernate : 파라미터 바인딩     ex) "from Student where studentName = ? " or "from Student where studentName = :name

# no.2 크로스사이트 스크립트
# https://www.kisa.or.kr/uploadfile/201312/201312161355109566.pdf
# 외부 입력값 또는 출력값에 스크립트가 삽입되지 못하도록 문자열 치환 함수를 사용
# ex) description = description.replace('<','&lt;') -> https://roadofdevelopment.tistory.com/38
# 잘 만들어진 외부 라이브러리를 활용(AntiXSS, OWASP ESAPI)

# no.3 경로 조작 및 자원 삽입 pg.154
# 외부의 입력이 파일명인 경우 경로순회 공격의 위험이 있는 문자자( “ / ￦ .. 등 )을 제거할 수 있는 필터 이용
# filename=filename.replace('a','').replace('i','').replace('o',''),replace('u','').replace('e','')
# 외부에서 입력되는 값에 대해 null 여부 체크
# ex) if string_variable : (null일 때)

# no.4 운영체제 명령어 삽입
# 외부 입력에 따라 명령어를 생성하거나 선택이 필요한 경우에는 명령어 생성에 필요한 값 들을 미리 지정해 놓고 외부 입력에 따라 선택하여 사용
# 파라미터의 배열에 실행할 수 있는 프로그램 저장하여 제한
# 우회문자 필터링 필요
# 외부 입력값 정규식이나 white list 등을 이용하여 검증 필요

# no.5 메모리 버퍼 오버플로우
# 파이썬, 자바는 취약하지 않음. 주로 C에서
# strncpy대신 strlcpy 함수 사용
# memcpy(cv_struct.x, SRC_STR, sizeof(cv_struct)); -> memcpy(cv_struct.x, SRC_STR, sizeof(cv_struct.x));
# 널(Null) 문자를 버퍼 범위 내에 삽입하여 널(Null)문자로 종료
# cv_struct.x[(sizeof(cv_struct.x)/sizeof(char))-1] = '￦0';


# < ----- 2등급 ----- >
# < ----- 3등급 ----- > (17 ~ 27)

# no.17 XQuery 삽입 pg.178
# XQuery에 사용되는 외부 입력데이터에 대하여 특수문자 및 쿼리 예약어를 필터링하고, XQuery를
# 사용한 쿼리문은 문자열을 연결하는 형태로 구성하지 않고 파라미터(Parameter)화된 쿼리문을 사용
# 한다.

# no.18 XPath 삽입 pg.182
# XPath 쿼리에 사용되는 외부 입력데이터에 대하여 특수문자(", [, ], /, =, @ 등) 및 쿼리 예약어
# 필터링을 수행하고 파라미터화된 쿼리문을 지원하는 XQuery를 사용한다.

# no.19 신뢰되지 않는 URL주소로 자동접속 연결 pg.174
# 자동 연결할 외부 사이트의 URL과 도메인은 화이트 리스트로 관리하고, 사용자 입력값을 자동
# 연결할 사이트 주소로 사용하는 경우에는 입력된 값이 화이트 리스트에 존재하는지 확인해야 한다.
# - 이동할 수 있는 URL범위를 제한하여 피싱 사이트 등으로 이동 못하도록 한다. ( 허용 URL 리스트 만들기 )

# no.20 중요한 자원에 대한 잘못된 권한 설정 pg.222
# 파일에 대해서는 최소권한을 할당하기!! 해당 파일의 소유자에게만 읽기 권한을 부여한다.
# os.chmod ( "v.txt", 400) # 권한 변경 => 소유자만 읽기 가능

# no.21 무결성 검사 없는 코드 다운로드 pg.272
# DNS 스푸핑(Spoofing)을 방어할 수 있는 DNS lookup을 수행하고 코드 전송 시 신뢰할 수 있는
# 암호 기법을 이용하여 코드를 암호화한다. 또한 다운로드한 코드는 작업 수행을 위해 필요한 최소한
# 의 권한으로 실행하도록 한다.
# https://my-devblog.tistory.com/19
# DNS lookup in python 찾기

# no.22 초기화되지 않은 변수 사용 pg.314
# //변수의 초기값을 지정하지 않을 경우 공격에 사용 될 수 있어 안전하지 않다.
# int x, y;
# //변수의 초기값은 항상 지정하여야 한다.
# int x=1, y=1;

# no.24 중요정보 평문저장 pg.231
# 중요정보를 저장할 때는 반드시 암호화하여 저장해야 하며, 중요정보를 읽거나 쓸 경우에 권한인증 등을 통해
# 적합한 사용자가 중요정보에 접근하도록 해야 한다.
# https://scribblinganything.tistory.com/197 (DB에 비밀번호 암호화 hash해서 저장하는 코드)

# no.25 제거되지 않고 남은 디버그 코드 pg.321
# 디버그 코드 확인 및 삭제하기

# no.26 HTTP 응답 분할 pg.196
# 요청 파라미터의 값을 HTTP응답헤더(예를 들어, Set-Cookie 등)에 포함시킬 경우 CR, LF와 같은
# 개행문자를 제거한다.
# text.replace(",","") 
# https://jangjy.tistory.com/228 (strip())

# no.27 위험한 형식 파일 업로드 pg.170
# 화이트 리스트 방식으로 허용된 확장자만 업로드를 허용한다. 업로드 되는 파일을 저장할 때에는
# 파일명과 확장자를 외부사용자가 추측할 수 없는 문자열로 변경하여 저장하며, 저장 경로는 ‘web
# document root’ 밖에 위치시켜서 공격자의 웹을 통한 직접 접근을 차단한다. 또한 파일 실행여부를
# 설정할 수 있는 경우, 실행 속성을 제거한다.
# https://takeardor.tistory.com/16 (파일의 확장자명 불러오기)



# < ----- 5등급 ----- >
# no. 38 Null Pointer 역참조
# 일반적으로 그 객체가 널(Null)이 될 수 없다'라고 하는 가정을 위반했을 때 발생
# 널이 될 수 있는 레퍼런스(Reference)는 참조하기 전에 널 값인지를 검사 (검사 후 참조)
# obj.equals(elt) -> (null != obj and obj.equals(elt)
# if ( url.equals("") ) -> if ( url != null or url.equals("") )

# no. 39 종료되지 않는 반복문 또는 재귀 함수
# 재귀 호출 횟수를 제한하거나, 초기값을 설정(상수)하여 재귀 호출을 제한
# 탈출 조건, 즉 귀납조건을 반드시 구현할 것 (if 문)

# no. 40 오류 메시지를 통한 정보 노출
# 소스코드에서 예외 상황은 내부적으로 처리, 사용자에게 민감한 정보를 포함하는 오류를 출력하지 않도록 미리 정의된 메시지를 제공하도록 설정
# traceback.print_exc() -> logger.error("ERROR-01: 파일 열기 에러");

# no. 41 잘못된 세션에 의한 데이터 정보 노출
# 다중 스레드 환경에서 정보를 저장하는 멤버변수가 포함되지 않도록 하여, 서로 다른 세션에서 데이터를 공유하지 않도록
# 자바에서는 jsp 선언부 (<%! 소스코드 %>)에 선언한 변수는 모든 사용자에게 공유
# 서블릿(<% 소스코드 %>)에 정의한 변수는 공유 발생 x
# **-> 파이썬에서는? 

# no. 42 주석문 안에 포함된 시스템 주요정보
# 주석에는 ID, 패스워드 등 보안과 관련된 내용을 기입하지 x

# no. 43 부적절한 예외 처리
# 값을 반환하는 모든 함수의 결과값을 검사하여, 그 값이 의도했던 값인지 검사. 광범위한 예외처리가 아닌 구체적인 예외 처리 수행
# Exception e 말고 세분화하여 예외 처리 할 것 (NameError, ValueError, ZeroDivisionError, IndexError, TypeError)

# no. 44 사용자 하드디스크에 저장되는 쿠키를 통한 정보 노출
# 쿠키의 만료시간은 세션이 지속되는 시간을 고려하여 최소한으로 설정하고 영속적인 쿠키에는 사용자 권한 등급, 세션ID 등 중요정보가 포함되지 않도록
# cookie=driver.get_cookies() / cookie.setMaxAge(60*60*24) / driver.add_cookie(cookie)
# **-> 코드 맞는지 모르겠음.. 뇌피셜

# no. 45 시스템데이터 정보노출
# 예외상황이 발생할 때 시스템의 내부 정보가 화면에 출력되지 않도록
# logger.error(""IOException Occured");

# no. 46 Public 메소드부터 반환된 Private 배열
# public : num, private : __num, protected: _num
# private로 선언된 배열을 public으로 선언된 메소드를 통해 반환하지 않도록
# Private 배열의 복사본을 만들기 -> copy 함수
# **-> ??

# no. 47 Private 배열에 Public 데이터 할당
# public으로 선언된 메서드의 인자를 private선언된 배열로 저장되지 않도
# 인자로 들어온 배열의 복사본을 생성하고 clone() 메소드를 통해 복사된 원소를 저장
# --> ??

class Color():
    __colors ={}

def getColors(Color):
    return colors

# 하 모르겠다..

