"""

컴퓨터는 패킷망 방식으로 사용된다

회선망
: 송수신자간의 경로에 있는 스위치들이 연결상태를 유지하는 연결

회선 교환
- FDM (frequency division multiplexing)
- TDM (time division multiplexing)
    : 특정 시간대에 전체 대역폭을 사용 한 타임을 쉘이라 지칭

통계적 다중화
    : A와 B 패킷의 순서가 일정하지 않다. 즉 보내지는 순서에 일정한 패턴이 없다.
    -> TCP : 패킷의 순서를 정렬시킨다

    
    - 가정 접속 (residential access)
    - 기관 접속 (institutional access)


    ADSL (asymmetric digital subscriber line)
      : 

    local ISP
        : 내가 사용하고 있는 ISP

TCP / IP Layer 와 OSI 7 Layer는 약간 다르다

TCP / IP Layer
01. application
02. transport
03. network
04. link
05. physical

투명성 : 볼 필요가 없는 것
  - 정보, 의사결정 과정, 규칙 등이 숨김없이 명확하게 공개되어 누구나 접근하고 이해할 수 있는 상태


01. application
  ex) 네이버에 접속한다 가정해보자
  크롬 프로그램을 실행시키는 것이 application 역할이다. 
  크롬 프로그램을 실행시키는 것은 네이버는 web server이며 HTTP, nginx를 실행한 것이다.

### Layer 흐름 과정 ###
1. Application 은 메시지를 보낸다
2. TCP는 메시지를 받아 포트를 붙여서 세그먼트를 만들어 보낸다
3. IP는 세그먼트를 받아 주소를 붙여 데이타그램을 보낸다
4. Ethernet은 MAC Address를 붙여 프레임을 보낸다 (물리 계층)
5. 프레임을 받아서 MAC Address를 확인하고 맞으면 Datagrame을 IP로 보낸다
6. IP에서 Datagram이 맞으면 Segment를 TCP로 보낸다
7. TCP에서 Segment 포트가 맞으면 FTP로 메시지를 보낸다

## tier

1-tier
: 1대의 Host에 다량의 terminal이 serial을 통해 연결된 환경
- Host : 컴퓨터, terminal : 모니터, 키보드

2-tier
: 
- 클라이언트-서버 아키텍처





"""