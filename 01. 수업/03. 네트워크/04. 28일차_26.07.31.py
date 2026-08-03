"""

rdt 2.0 : 비트 오류가 있는 채널

-> 패킷이 가다가 깨질 수 있다는 가정

acknowledgement (ACKs)
  : receiver 가 sender에게 pkt를 잘 받았다는 응답
negative acknowledgement (NAKs)
  : receiver 가 sender에게 pkt에 error또는 장애가 있다는 응답

TCP에 buffer가 필요하게 됨 (sender)
: packet을 저장하게 될 공간

Net01 교안 p.158 그림 확인


패킷 보내는 간격을 
RTT라 하고 그 간격이 생각보다 길다 p.169 (b)확인하면 알게됨

rdt 2.0 : 치명적인 결함
ACK 신호도 깨질 수 있다
그걸 해결하기 위해 ACK신호가 깨진것은 NAK로 판단한다
sender는 pkt에 sequence number를 추가해서
신뢰적인 데이터를 확보한다.

그것을 rdt 2.1

p.162
wait for call 0 from above
: 0번 패킷을 보내기 위해서 app에서 데이터 주기를 기다리는중

rdt 2.1 결함
: 응답 패키지 ACK, NAK 두개가 불편함
-> NAK가 필요 없다 생각

rdt 2.2
: NAK를 없애고 정확히 수신된 pkt에 대한 ACK를 전달한다.
(내가 몇번 pkt까지 잘 받았다는 신호 - ACK의 누적)
응답 패킷을 보관할 buffer가 필요하게 됨 (recieve)


== SQL ==
널이 포함된 연산

NVL(컬럼, 치환값)
: 컬럼의 값이 NULL이면 치환값으로 바꾼다.








"""