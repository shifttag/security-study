"""
Switch = Bridge

Switch는 segment 연결 장치인 Bridge가 확장된 장비이다.
  - Switch와 Bridge의 작동 방식, 알고리즘은 동일하다

Switch 설정
  -STP : Spanning Tree Protocol
  -VLAN : Virtual LAN

show interface [status | if_명 | vlan #]
- show interface status

BID (Bridge ID)
: Bridge 고유 식별번호
- 8byte로 구성된다
  - Bridge Priority(2byte) + MAC Address(6byte)
  - Bridge Priority default 32768 (0~65535)
    : 32786 + VLAN # (VLAN 1의 경우 32769)

Path Cost
: 데이터 전송비용
  - 1000Mbps를 링크 대역폭으로 나눈 값 : IEEE 802.1D
  - Fast Ethernet : 1000 / 100 = 10
  - Gigabit Ethernet : 1000 / 1000 = 1

STP
: looping을 제어하는 프로토콜이다
  - 자동화된 기능이다
  - 다중 경로를 하나의 경로로 구성하고 네트워크 상황에 따라 동적으로 경로를 수정한다

  구현
    1. 네트워크에 Root Bridge를 선정한다
      - 나머지 모든 스위치는 non root bridge가 된다
    2. 모든 non root bridge는 하나의 root port를 갖는다
    3. 연결마다 하나씩 데지그네이티드 포트(Designated Port) 선정한다
    4. Non designated port를 선정한다

    step 1. Root Bridge 설정
      - 각 스위치는 BID(Bridge ID)를 갖는다
      - 스위치는 부팅이후 매 2초마다 BPDU(Bridge Protocol Data Unit)를 송신한다
      - BID = priority + MAC
      - BID가 가장 작은 SW가 root bridge가 된다
    step 2. Root Port를 결정한다
      - Non Root bridge에서 Root bridge까지 가장 빠른 경로에 연결된 port를 찾는다
      - 경로의 cost가 동일한 경우 BID가 낮은 switch를 통과하는 경로의 port가 root port가 된다
    step 3. Designated Port(지정 포트)를 결정한다
      - 각 segment에서 root bridge 까지 가는 가장 cost가 낮은 port를 designated port라고 한다
      - cost가 동일한 경우 BID가 낮은 switch를 통과하는 port가 designated port가 된다
    step 4. Port Block과 STP 완성
      - 연결된 링크 중에 root port나 designated port가 아닌 포트는 block한다

  sw3, sw4를 root bridge로 지정하는 방법
  - sw3(config)# spanning-tree vlan 1 priority 4096
  - sw3(config)# do show spanning-tree

  - sw4(config)# spanning-tree vlan 1 root primary
  - sw4(config)# do show spanning-tree


=== 리눅스 명령어 ===

useradd [옵션] [계정명]
  - 계정 생성 명령어

옵션
-u : 계정의 UID를 지정한다
-g : 계정의 GID를 지정한다
-d : 홈 디렉토리 지정
-G : 보조 그룹 지정
-D : 기본 설정 확인 및 변경
-s : 쉘 지정

ex) useradd -g st -u 2001 st01

userdel [옵션] [계정명]
  - 계정 삭제 명령어

옵션
-r : (필수)계정에 귀속된 홈디렉토리와 mailbox등을 모두 삭제한다 

원래 전자우편은 유닉스 계정이 있는사람이 유닉스 계정이 있는사람한테 보낸다

> 특별한 사용자 생성 옵션
옵션
  - M : 메일 전용 계정 생성
  - r : 999번 이하의 UID 자동 할당  

passwd [옵션] [계정명]
  - 계정의 패스워드를 변경하는 명령어

옵션
  - d : 계정의 패스워드를 삭제한다
  - e : 계정의 패스워드를 만료시킨다
  - i : 계정의 패스워드가 만료된 후 비활성화되는 기간을 지정한다
  - l : 계정의 패스워드를 잠근다
  - S : 계정의 패스워드 상태를 확인한다
  - u : 계정의 패스워드를 잠금 해제한다

useradd -D [옵션]
  -b : 홈디렉토리 수정
  -g : 기본 그룹 수정
  -s : 기본 쉘 변경
  -m : skel 디렉토리 변경
  -e : 패스워드 만료일 변경
  -f : grace 기간 변경

 /etc/login.defs
• MAIL_DIR  : 메일이 저장되는 디렉토리 설정
• PASS_MAX_DAYS : 패스워드 유효기간 (99999 :  무한대)
• PASS_MIN_DAYS : 지정 기간내에는 패스워드 변경불허
• PASS_MIN_LEN : 패스워드 최소길이
• PASS_WARN_AGE : 패스워드 grace time
• UID_MIN : 생성 UID 의 최소 숫자
• UID_MAX : UID 의 최대 가능 숫자
• GID_MIN : 생성 GID 의 최소 숫자
• GID_MAX : GID 의 최대 가능 숫자
• CREATE_HOME : 홈디렉토리 생성 여부

usermode [옵션] [사용자명]

옵션
  -g : 그룹 변경
  -G : 보조 그룹 변경
    -a와 함께 쓰면 보조그룹이 추가된다
  -s : 쉘 변경
  -u : UID 변경
  -l : 계정 변경 (--login)
    -d, -m도 같이 사용된다
  - d : 홈디렉토리 변경 (--home)
    -m : 지정한 홈디렉토리 생성 및 파일 이전, -d와 함께 쓰인다. (--move-home)

# usermode [-L | -U] [사용자명]
  -L : lock(--lock), -U : unlock(--unlock)
# usermode [-l | -u | -S] [사용자명]
  -l : lock, -u : unlock, -S : 잠금 확인

"""