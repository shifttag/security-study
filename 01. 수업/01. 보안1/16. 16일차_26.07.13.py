"""
OSPF

DR, BDR 선정 후에 

neighbor와 Adjacency를 정확히 구분할 줄 알아야 한다

HelloPacket Interval 을 보내는데 응답이 없으면 버린다 
그거를 dead Interval 라고 한다

OSPF - metric (host)
protocol  | metric기준
----------------------------
RIP       | hop count
OSPF      | bandwidth, delay등
EIGRP     | cost(대역폭)

OSPF에서 선택 경로
: 전체 경로의 cost의 합이 가장 낮은 경로를 선택

Interface Cost를 이용
cost = Reference Bandwidth (기본값: 100Mbps)/ Interface Bandwidth

라우터가 경로 cost를 계산

1. OSPF 라우팅 프로세스 활성화
2. Router ID
  - Router ID는 OSPF를 사용하는 Router를 식별하기 위한 식별정보이다.
  - 인터페이스 IP중 가장 높은 IP가 ID로 사용된다.
  - Router ID가 인터페이스의 상태에 따라 달라지는 것을 방지한다
    - router-id 명령으로 id를 지정한다
3. 각 인터페이스의 네트워크 등록
4. OSPF 작동 확인

인터페이스 등록
network [인터페이스 주소] 0.0.0.0 area [area #]


gdisk -> mkfs -> mount

gdisk : 파티션 만드는 역할
  gdisk /dev/sda

    b : 현재 GPT 파티션 정보를 파일로 백업합니다. 나중에 파티션 정보를 복구할 때 사용할 수 있습니다.
    c : 선택한 파티션의 이름(Partition Name)을 변경합니다.
    d : 선택한 파티션을 삭제합니다.

    i : 선택한 파티션의 상세 정보(시작/끝 섹터, 크기, 타입 등)를 출력합니다.
    l : 생성 가능한 GPT 파티션 타입 목록을 표시합니다.
    n : 새로운 파티션을 생성합니다.

    o : 기존 GPT 파티션 테이블을 삭제하고 새로운 빈 GPT 파티션 테이블을 생성합니다.
    p : 현재 디스크의 파티션 테이블 정보를 출력합니다.

    q : 변경 사항을 저장하지 않고 gdisk를 종료합니다.
    r : 파티션 복구 및 변환을 위한 고급 기능 메뉴로 이동합니다.
    s : 파티션 번호를 디스크상의 순서대로 다시 정렬합니다.
    t : 선택한 파티션의 타입 코드를 변경합니다.
    v : GPT 파티션 테이블의 무결성과 오류를 검사합니다.
    w : 변경한 파티션 정보를 디스크에 저장한 후 gdisk를 종료합니다.

    x : 전문가용(고급) 기능 메뉴로 이동합니다.
    ? : 사용할 수 있는 명령 목록(도움말)을 다시 출력합니다.

mkfs : 포맷 해주는 역할
  mkfs.xfs -f /dev/sda1 (강제로 xfs타입으로 포맷)

mount : 어떤 특정 디렉토리에 마운트
  mount /dev/sda1 /sda1
  mount /dev/sda2 /sda2

df : 어떠한 파티션에 디렉토리가 마운트 되어있는지 보는 명령어
umount : mount 해제
umount [디렉토리경로 | 파티션명]

"""