"""
chrome, winscp
이런 애들을 클라이언트 프로세스
클라이언트 프로세스 : end user가 직접 사용하는것'


스위치 허브는 콜리전이 발생하는거를 필터링으로 안보낸다
그거를 콜리전 도메인이라 한다

허브는 콜리전이 안생기지만 생긴다고 가정하면
그 콜리전 마저 전부 다른 포트로 전송한다.

=== Packet Tracer===
debug ip rip
rip 디버깅 명령어

auto summary
: 1.1.1.0의 ip는 a클래스라 자동으로 서브넷 마스크가 255.0.0.0으로 설정됨

RIP v2 설정
명령
passive-interface GigabitEthernet0/0
version 2 : RIP v2 모드 활성화
no auto-summary : Auto summary 비활성화

개인 인터넷 연결은 RIP으로 연결하면 라우터 상에 데이터가 넘쳐나니
정적 라우팅으로 연결한다. 정적 라우팅으로 ISP와 연결하고 그 하위에 있는
망은 다시 RIP으로 연결한다.
ISP로 가는 route를 default route 로 지정한다.
명령
default-interformation originate
  : RIP(OSPF)을 통해 default route 정보를 전달한다.
  : EIGRP는 static 재분배 명령을 이용한다
    - redistribute static

실습에서는 default route 설정은 정적 라우팅 설정과 동일하다
외부 네트워크로 local loopback 인터페이스를 이용한다

Loopback 인터페이스 활성화
interface loopback0
ip address 10.10.10.1 255.255.255.0

default route 설정
ip route 0.0.0.0 0.0.0.0 loopback0
router rip
default-information originate


# OSPF (Open Shortest Path First)
: 

Link의 cost를 기반으로 경로를 배정한다
  - Dijkstra SPF 알고리즘을 바탕으로 경로가 선택된다
  - link cost = 기준대역폭/실제대역폭
VLSM을 지원한다

neighbor relation
:
- 인접관계인 라우터만 리소스를 주고받음


윈도우는 master browser 선정 master 브라우저에 리소스를 던짐
(마스터 - 슬레이브 형태)


OSPF의 Neighbor와 인접 관계(Adjacency)는 동일한 의미가 아니다.
- neighbor 라우터 중에 인접관계인 라우터와 LSA를 교환한다
- adjancency는 DR(BDR)과 IR간에 이뤄진다

Point to Point : HDLC, PPP등의 Serial Link
- DR(Designated Router)/BDR(Backup Designated Router)를 선출하지 않는다.
- OSPF Hello 및 LSU 패킷은 Multicast 224.0.0.5를 이용한다
  - Hello Packet : 10s
  - Dead Interval : 40s

OSPF
1. OSPF 프로세스 활성화
명령
router ospf [process-id]

2. Router ID
명령
router-id [ip] : 자동 지정

3. 와일드마스크
  - 인터페이스 등록
  명령
  network [네트워크 주소] [와일드카드 마스크] area [area #]
  network [인터페이스 주소] 0.0.0.0 area [area #]

=== 리눅스 ===
파일시스템
: 파일을 저장하기 위한 운영체제의 논리적인 구조
- Linux : xfs, ext4, ext3, jfs, ...
- Windows : FAT, FAT32, NTFS 등
- Unix : UFS(UNIX File System), ZFS
- IOS : APFS(Apple File System), HFS+

파티션
: 물리적인 디스크를 논리적인 저장영역으로 구별한 것

1. Primary partition
: 물리적인 디스크에 독립적으로 존재하며 파일시스템을 생성,
운영체제가 직접 사용 가능하다. 각 물리적인 디스크마다 4개까지 생성할 수 있다.

2. Extended partition
: 디스크마다 1개 까지 생성 가능하며 직접 사용할 수 없고 logical partition으로 분할 사용한다.

3. Logical partition
: Extended partition내에 만들어지며 사용은 primary partition과 동일하다.

4. P+E는 최대 4개까지 생성 가능하다.






















"""