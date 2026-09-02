"""

window : rtt내에 보낼수 있는 pkt의 양 (window size)

Go-Back-N
1. sender
- timer
  : sendbase에 단일 timer

- 상위 layer에서 Data가 수신되면
  : pkt의 다음 seq#를 검사 window내에 있으면 pkt를 전송한다.

- timeout(n)
  : sendbase에서부터 윈도우 내에 모든 패킷을 재전송한다.

- ACK(n) 이 수신
  : n < sendbase : 무시.
  : n >= sendbase :
    • sendbase를 윈도우내에 미확인 패킷중 가장 오래된 패킷으로 이동
    • 윈도내에 미발송 패킷 전송

2. receiver
- pkt n [n in rcvbase, rcvbase+N-1]
  : 누적 ACK을 송신
  : out-order인 경우 : 버림.
  : in-order인 경우 : 정상 처리

- 이외의 경우
  : 무시한다.

Selective Repeat
1. sender
- 상위 layer에서 Data가 수신되면
  : pkt의 다음 seq#를 검사 window내에 있으면 pkt를 전송한다.

- timeout(n)
  : pkt n을 재전송하고 timer를 restart한다.

- ACK(n) 이 수신
  : n이 윈도우에 있다면 pkt가 수신된 것을 확인한다.
  : n이 send_base와 같다면 send_base는 가장 작은 seq#를 갖는 미확인 pkt
  로 이동하고 window내에 이 전송 pkt가 있으면 전송한다.

2. receiver
- pkt n [n in rcvbase, rcvbase+N-1]
  : ACK(n)을 송신
  : out-order인경우 buffering한다.
  : in-order인 경우 필요하다면 buffer에 저장된 번호가 연속적인 pkt와 함께 상위
  layer에 전달하고 rcv_base를 가장 낮은 seq#를 가진 미전송 pkt로 옮긴다.

- pkt n [n in rcvbase-N, rcvbase-1]
  : ACK(n)

- 이외의 경우
  : 무시한다.

TCP: overview
  - point-to-point
    : 단일 송/수신자 간에 통신
  - 신뢰적인 in-order byte stream
    : Message에 구분이 없다
  - piplined
    : 혼잡제어나 흐름제어를 통해 window size를 제어한다
  - full duplex
    : 동일 connection에 양단이 동시에 data를 전송할 수 있다.
    : MSS : maximum segment size
      (segment에서 app layer data의 최대 크기)
  - connection oriented
    : handshake를 먼저 수행한다
  - flow control
    : sender가 receiver를 압박하지 못하도록 receiver가 전송량을 통제한다.

    
TCP segment의 구조
최초 전송 - syn 1번 날라감
: 클라이언트가 서버한테 먼저 보냄 3번정도 왔다갔다 하는데 그걸 3way-handshake라함

RST - seq# 잃어버림 - 리셋보냄 - seq# 초기화하자는 의미
FIN - 접속 끝난다는 의미

TCP의 seq#
  - Segment의 첫번째 byte의 stream에서의 byte 순서 번호
ACKs 
  : 다음에 받을 첫번째 byte의 순서 번호
  : Cumulative ACK가 가능하다                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            


TCP - RTT & Timeout
1. EstimatedRTT
  sampleRTT
    : segment가 송신된 시간으로부터 ACK가 도착한 시간간격
  EstimatedRTT는 부드럽게 변경된다

EstimatedRTT = (1 - a) * EstimatedRTT + a * sampleRTT
(typical value : a = 0.125)

2. DevRTT
  : SampleRTT가 EstimatedRTT로 부터 얼마나 벗어나는지에 대한 예측

DevRTT = (1 - b) * DevRTT + b * abs(SampleRTT - EstimatedRTT)
(b는 베타 b의 권장값 : 0.25)

실제 timeout 설정
TimeoutInterval = EstimatedRTT + 4 * DevRTT

=== 실제 TCP 전송 ===
- Pipelined segment
- 누적 ACK
- 단일 Timer 사용


TCP의 connection 관리


1. Three way handshake
step 1 : client가 server에게 TCP SYN segment를 전송
  - 초기 seq# 설정
  - data는 없다
  (SYN : p.189에 S부분)
step 2 : server는 SYN를 수신하고 SYNACK를 전송
  - server : 변수 및 buffer 할당
  - server의 초기 seq# 설정
step 3 : client는 SYNACK 수신 ACK 전송 (데이터 추가 가능)
  - client : 변수 및 buffer 할당

-- 취약점
step 2가 취약성이 있다
ip를 바꿔서 계속 보냄 - 여러개의 클라이언트가 접속 요청
그러다 보니 서버쪽에는 변수와 buffer를 계속 할당
서비스 거부 공격 (DoS) -> SYN Flooding


2. closing a connection
step 1 : client는 connection을 종료하기 위해 FIN bit가 1로 설정된
        TCP segment를 server에게 전달
step 2 : server는 FIN을 수신하면 ACK를 응답하고 connection을 종료한다는
        FIN을 client에게 전송한다.
step 3 : client는 FIN을 수신하면 ACK를 응답하고 일정시간을 기다린 후
        connection을 종료한다.
step 4 : server는 ACK를 수신하면 connection을 종료한다.

조기 종료 프로세스 - 고스트 커널 - 폴링(프로세스 점검)
















"""