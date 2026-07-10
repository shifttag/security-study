"""
!중요 (패킷 분석 때 사용 예정)

TCP
: 서로 다른 application 간에 논리적인 통신을 제공한다

event와 action
Send Tcp
message가 오는것을 event라 한다 rdt.send()
action으로 하는거는 segment를 만들어서 보낸다 udt.send()

Recive Tcp
segment가 들어오는것을 evnet rdt.rev()
segment를 받아 message로 만들어 보낸다 deliver_data()

rdt(Reliable Data Transfer)
udt(Unreliable Data Transfer)

conjection control(혼잡 제어)
: 네트워크가 처리할 수 있는 양보다 너무 많은 데이터가 한꺼번에 전송되어 
성능이 저하되는 것을 방지
혼잡하면 네트워크에서 패킷을 보내는 양을 줄임

network layer
:  host 간에 logical communication을 제공
transport layer
: process간에 logical communication을 제공
  - Network layer가 제공하지 못하는 신뢰적인 전송을 제공 할 수 있다.
  - 그러나 network layer의 제약을 받는 경우도 있다.
    : 지연이나 대역폭에 대한 보장은 불가능하다.


link layer : node끼리 통신하는 장치





"""