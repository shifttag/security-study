"""
UDP (User Datagram Protocol)

putty로 계속 접속하고 있는거
connection oriented 지속적인 통신



흐름제어
: sender가 하는 역할
ex) 초당 100gb 이상 보내지 마 하고 제어
리시버 컴퓨터 성능에 따라 좌우된다

혼잡제어
: reciver가 하는 역할


udp는 
헤더 4byte의 2칸 8byte사용

검사합 (checksum) : 패킷이 깨졌는지 안깨졌는지 확인하기 위함
체크섬 사용 이유 : 가장 빠르다

checksum
Sender
➢ Segment의 content는 순서에 따라
16bit integers로 간주한다.
  : 메시지를 2진수로 보고 16bit씩 자른다
➢ 모든 16bit(word)의 합을 가지고 1
의 보수를 수행한다. (이때 오버플로우
는 버린다.)
  : 모든 블럭을 더해서 1의 보수를 취한다.
➢ 결과는 UDP segment checksum
field에 삽입한다.
➢ overflow bit를 wraparound로 이
용 하는 경우도 있음

receiver
➢ Segment를 수신후 checksum을 을
포함한 모든 16bit word를 더한다.
➢ 값이 모두 1이면 에러가 없지만 하나라
도 0이 나오면 오류가 있다.
➢ 참고 (checksum을 사용하는 방법과
bit sum에서 발생하는 overflow를
처리하는 방법이 다름. 과정은 다르지
만 판단 결과는 동일)


과정
메시지의 16bit로 잘라서
16bit당 한 블럭으로 지칭


TCP
: 신뢰적인 data 전송
p 153, 154 중요 사진 

TCP 입장
sender
  - event 발생
    : rdt_send() 함수 실행
    : application에서 메시지가 들어옴
  - action
    : message를 segment로 만듬
    : 그 후 udt_send() 함수 실행
    : IP한테 segment 전달

receiver
  - event 발생
    : rdt_rcv() 함수 실행
    : IP에서 segment가 들어옴
  - action
    : segment에서 message 추출
    : deliver_data() 함수 실행
    : application에게 message 전달

"""