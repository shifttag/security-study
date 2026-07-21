"""
static =====
R1 -----
enable
conf t
  ip route 0.0.0.0 0.0.0.0 g1/0
R2 -----
enable
conf t
  ip route 1.1.1.0 255.255.255.0 g2/0
  ip route 2.2.2.0 255.255.255.0 g1/0
R3 -----
enable
conf t
  ip route 0.0.0.0 0.0.0.0 g2/0

RIP =====
R1 -----
enable
conf t
  router rip
  version 2
  no auto-summary
  passive-interface g0/0
  network 1.1.1.0
  network 12.1.1.0
R2 -----
enable
conf t
  router rip
  version 2
  no auto-summary
  network 12.1.1.0
  network 23.1.1.0
  network 10.10.10.0
R3 -----
enable
conf t
  router rip
  version 2
  no auto-summary
  passive-interface g0/0
  network 23.1.1.0
  network 2.2.2.0

OSPF =====
R1 -----
enable
conf t
  router ospf 1
  router-id 1.1.1.1
  network 1.1.1.1 0.0.0.0 area 0
  network 12.1.1.1 0.0.0.0 area 0
R2 -----
enable
conf t
  router ospf 1
  router-id 10.10.10.1
  network 10.10.10.1 0.0.0.0 area 0
  network 12.1.1.2 0.0.0.0 area 0
  network 23.1.1.2 0.0.0.0 area 0
R3 -----
enable
conf t
  router ospf 1
  router-id 2.2.2.1
  network 2.2.2.1 0.0.0.0 area 0
  network 23.1.1.3 0.0.0.0 area 0


### 리눅스 ###

ip neighbor show | ip n 
  : 전체 ARP 테이블 확인
ip n show dev [NIC]
  : 특정 인터페이스의 ARP 테이블 확인
ip n show [IP]
  : 특정 IP의 ARP 정보 확인
ip n add [IP] lladdr [MAC] dev [NIC]
  : ARP 엔트리 수동 추가
ip n del [IP] dev [NIC]
  : 특정 ARP 엔트리 삭제
ip n flush all
  : ARP 테이블 초기화
ip n flush dev [NIC]
  : 특정 인터페이스의 ARP 테이블 초기화

ip route show
  : Routing table 확인


# ip route add/del [target ip/mask] via [new gateway ip] dev [NIC]
• 명령은 일시적이다.
# ip route add default via 192.168.1.1 dev ens160
# ip route add 192.168.12.0/24 via 192.168.11.254 dev ens224
# ip route add 192.168.2.50 via 192.168.1.1 dev ens160
# ip route add default nexthop via 192.168.1.1 dev ens160 \
nexthop via 192.168.1.2 dev ens160
# ip route del default via 192.168.1.1
# ip route del 10.0.0.0/24 via 192.168.1.254


## 윈도우 ##
ARP
  옵션
  - a : ARP 목록 확인
  - s : 정적 등록
  - d : ARP 삭제, 추가 항목이 없으면 ARP cache 초기화
"""