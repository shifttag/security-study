"""
Carrier Sense

네트워크상에 패킷이 있는지 없는지 확인하기 위함


헤더가 붙는 과정
Encapsulation : 상위 계층에서 하위 계층으로 내려가면서 헤더를 붙이는 과정
Decapsulation : 하위 계층에서 상위 계층으로 올라가면서 헤더를 제거하는 과정


사용자나 프로그램을 구별할 때 IP Address와 port Number를 사용한다.

클라이언트를 여러개 실행할때는 os에서 번호(포트 번호)를 하나씩 부여한다

arp 프로토콜
상대방 IP Address를 알고 있을때 상대방의 MAC Address를 알아내는 프로토콜
브로드캐스트로 multiple access를 사용하여 알아낸다

arp 스푸핑
: A가 C한테 프레임을 보내려는데 브로드캐스트 방식이다 보니 
B가 먼저 ip를 속여 A한테 그 IP의 MAC 주소가 나야 하면서 속여  
A는 B한테 프레임을 보내게 된다.

rarp
: 내 ip address를 뭐 쓰면 되냐고 상대방한테 물어보는
- 현재는 주로 사용하지 않음

리눅스
nmtui : 네트워크 설정을 GUI로 할 수 있는 명령어

변수
: 값을 저장할 수 있는 공간

"""