"""
Redistribution
: 서로 다른 라우팅 프로토콜 간에 정보를 전달하기 위해서는
각 라우팅 프로토콜에 맞는 해석이 필요하다


nmtui
안에서 프로파일 이름, 장치명 수정 x
IPv4에서 
  주소
  게이트웨이
  DNS서버
수정가능

네트워크 시스템 재시작
: systemctl restart NetworkManager.service
  - 바뀐 IP가 추가
  - 기존 IP를 보존 : 기존 접속 유지를 위해

nmcli conn up [NIC]
nmcli dev disconnect [NIC] && nmcli dev connect [NIC]
  - IP가 바뀜
  - 터미널 접속이 끊긴다

인터페이스 활성화/비활성화
: ip link set [NIC] up/down
  - 지정한 인터페이스를 활성화 하거나 비활성화 한다.

ip 변경(추가)
: ip addr change [ip/mask] dev [NIC]
  - change는 add와 동일함으로 기존 IP는 del 해야 한다.

Gateway 변경
: ip route [add | del | change] default via [gateway ip] dev [NIC]
  ex) ip route change default via 192.168.11.245 dev ens224

Hostname 변경
: hostnamectl set-hostname [호스트명]
  - /etc/hostname 파일 편집과 동일
  - shell 재시작 필요
  

"""