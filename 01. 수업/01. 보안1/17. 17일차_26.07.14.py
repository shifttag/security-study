"""
OSPF 확인 명령
  : show ip ospf neighbor
    - OSPF 네이버를 확인한다.
  : show ip ospf
    - OSPF 프로세서에 대한 정보를 확인한다.
  : show ip ospf interface
    - OSPF에 참여하는 인터페이스의 자세한 상태정보를 확인한다.
  : show ip ospf database
    - OSPF 링크 상태 데이터베이스를 열람한다.
    - LSA의 요약정보를 보여주지만 실제 링크 상태는 알 수 없다.
  : show ip ospf database [추가]
    - router, network, summary ......


EIGRP (Enhanced Interior Gateway Protocol)


Metric factor : 

- Bandwidth, Delay를 이용해 계산
- 원래는 5가지 Reliability(신뢰도), Load(부하), MTU(Maximum Transmission Unit)

neighbor 끼리만 라우팅 정보 주고받는다
DR, BDR 개념이 없다

K 상수 값이 일치해야 라우팅 정보를 교환한다.

-------------------------------------------------
k상수  | Metric factor  | 설명
k1    | Bandwidth       | Dst를 가는 대역폭 중에 가장 낮은 대역폭으로 10^7을 나눈 값
k2    | Load            | 인터페이스의 부하
k3    | delay           | Dst까지의 모든 지연의 합의 1/10
k4    | Reliability     | 인터페이스의 에러 발생률
k5    | MTU             | 최대 패킷의 크기

(K1 * BW + (K2 * BW) / ( 256 - load ) + K3 * delay) * 256 * (K5 / (Reli + K4))

Default : K2=K4=K5=0
EIGRP Metric = (K1 * BW + K3 * delay) * 256

기본적인 Metric 계산
  • BW는 목적지 까지 경로 중 가장 낮은 대역을 사용한다.
    - bandwidth : kbps
  BW = (10^7/banwidth) * 256
  • Delay는 경로 까지의 모든 지연을 합한 값이다.
    - delay : μs(micro-second), usec로 표기, 1/1,000,000(백만분의1초)
    - 모든 지연의 합을 10으로 나누고 256을 곱한 값
  Delay = (sum(delay) / 10) * 256

  
# show interface g|s */*/*
BW : Bandwidth, DLY : delay


=== 리눅스 ===

포맷 : 파티션을 생성한다라는 표현이 적절

# mount [-a] [-t [FStype]] [장치명] [디렉토리]

옵션
  -a : /etc/fstab의 내용을 읽어 모두 mount 한다.
  -B(--bind) : 장치가 아니라 디렉토리를 디렉토리에 mount한다.
  -t : 파일 시스템 양식을 정한다.
  -o : 마운트 옵션을 추가로 지정한다.
    . noatime : atime을 갱신하지 않는다. .
    . remount : 옵션을 변경을 위해 재마운트한다.
    . ro : Read Only로 정의한다

ex) mount -B /home/data /home2/ast**/data



/etc/rc.d/rc.local : 부팅 시 자동으로 실행


blkid : 각 장치의 UUID 정보 확인 가능

xfs_admin : 파티션에 다양한 파라미터를 변경하거나 확인 한다
xfs_admin -L [라벨명] [장치명]     : 라벨명 변경
xfs_admin -L "--" [장치명]        : 라벨명 삭제
xfs_admin -l [장치명]             : 라벨명 확인

findfs : UUID나 라벨명으로 장치명을 확인한다.
findfs LABEL=[라벨명]
findfs UUID=[uuid]

자동 마운트
/etc/fstab 파일은 시작 시 자동으로 마운트 할 파일 시스템의 목록이나 옵션을 저장한다
"""