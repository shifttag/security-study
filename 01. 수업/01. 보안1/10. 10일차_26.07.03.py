"""
VLAN
: 네트워크를 분할하기 위해 사용한다
- VLAN과의 연결은 라우터를 사용한다
- 각각의 VLAN은 마치 단독의 별도 장치처럼 패킷을 송수신한다.

VLAN 관련 명령
show vlan : VLAN 정보를 확인한다
show interface status : 각 인터페이스의 상태 확인
vlan ## : VLAN을 생성 또는 생성
  - name [vlan_name] : VLAN 이름 지정

switchport access vlan ## : 인터페이스를 VLAN에 할당
switchport mode [access | trunk | dynamic]
  - access : 단일 VLAN 모드
  - trunk : 여러 VLAN 트래픽 전달 모드
  - dynamic [auto | desirable] : 상대에 따라 달라짐. 가급적 사용 x

global mode에서
do show vlan : 각 인터페이스의 상태 확인
interface [port] : 인터페이스 진입

















"""