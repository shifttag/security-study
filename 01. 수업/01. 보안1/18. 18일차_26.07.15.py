"""
1. EIGRP

rip
class

rip2
class less
1.1.1.11/24 인경우 
1.1.1.0이 네트워크 주소가 되야하는데
1.0.0.0이 된다

EIGRP도 마찬가지로 class less


EIGRP 전용 기능
경로 값이 같은거를 load balancing

두개 다 쓸 데도 있다

Local 뜻 : 내가 사용하는 - Local Router : 내가 사용하는 라우터
---------------------------------------------------------
EIGRP - DUAL (Diffusing Update Algorithm)
metric이 작은 경우를 찾는다
p.16 
dst Network으로 가기 위한 경로
Local Router에서 Dst Network까지 m = 2500 (A를 통과할 때)
m = 4000 (B를 통과할때), m = 3000 (C를 통과할 때)

A를 통과할 때 metric이 가장 낮으니까 A Router를 successor라 한다
그 경로를 Feasible Dist라 한다


A경로는 A만 보고 B경로는 B만보고 그러는 자기 일만 하는것을 투명성
= 각자 맡은 역할만 한다
- 책임과 권한이 확실해야한다

A나 B나 C한테 Dst까지 비용이 있는데 
그 다음 metric값이 낮은 경로를 feasible successor라고 한다 (C를 통과하는 곳 = 백업경로)
라우터를 거쳐 Dst까지 경로 중 가장 cost가 낮은 경로를 Reported Dist라 한다

Local Router 기준 A, B, C metric이 같으면 2개 이상 Successor라 표현 가능

drtisl interface 확인 및 조절

show interface [interface명] : 특정 인터페이스 확인
bandwidth [##]
delay [##]


==========================================
리눅스

ip 명령
ip [옵션] <object> <command> [arguments]
  - object : 하위 명령 : link, adress, route, neighbor
  - command : 작업 : show, set, add, del

교안 6-1 p.3 표 캡쳐

네트워크 설정 파일
NetworkManager가 활성화 된 경우 직접 편집하지 않는다. (nmcli, nmtui)

1. 네트워크 설정 : IP, subnetmask, gateway
/etc/sysconfig/network-scripts/ifcfg-NIC                  : RockyLinux8
/etc/NetworkManager/system-connections/NIC.nmconnection   : RockyLinux9

2. DNS Server
/etc/resolv.conf

3. 호스트명
/etc/hostname

DNS
8.8.8.8
cat /etc/resolv.conf에 있는 파일 확인하여 찾아감

cat /etc/sysconfig/network-scripts/ifcfg-ens160
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=none
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
......
......
UUID=2e57c2df-b5bf-4d38-8ac4-a69f7c7112bd
DEVICE=ens160
ONBOOT=yes
IPADDR=192.168.10.31
PREFIX=24
GATEWAY=192.168.10.1
DNS1=192.168.10.11
IPV6_PRIVACY=no

















"""