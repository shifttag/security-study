"""
dal : 192.168.10.11
  DNS, FTP

윈도우 계정을 공유 걸어두고 다른컴퓨터에서 접근하면 하드를 공유해서 사용할 수 있다.

samba : 
  리눅스에서 윈도우 공유폴더를 접근할 수 있게 해주는 프로그램
  설치 : sudo apt install samba
  설정 : /etc/samba/smb.conf
  공유폴더 설정 : [공유폴더명]
                path = /home/사용자명/공유폴더명
                read only = no
                guest ok = yes
  사용자 추가 : sudo smbpasswd -a 사용자명
  서비스 재시작 : sudo systemctl restart smbd

파일탐색기(네트워크) 주소창에 \\192.168.10.11
하면 dalserver 접근 가능
파일 직접 열지는 말고, 내 폴더에서 복사하여 사용해야 함. 직접 열면 권한 문제로 안됨.

패킷의 종류
- unicast : 1:1 통신
- broadcast : 1:다수 통신
  : FF:FF:FF:FF:FF:FF MAC 주소를 가진 패킷은 같은 네트워크에 있는 모든 컴퓨터가 수신 가능
- multicast : 1:다수 통신, 특정 그룹만 통신 가능
  
CSMA/CA, CSMA/CD
옛날에 CSMA/CA를 사용했다
CSMA/CA(Carrier Sensing Multiple Access with Collision Avoidance) : 충돌을 피하기위함이 있어 느리다
CSMA/CD(Carrier Sensing Multiple Access with Collision Detection) : 현재 사용중인 방식, Bus 형태 사용중

MAC Address : 48bit, 16진수, 6byte, 12자리
: NIC에 할당된다.

브릿지는 라우터와 다르게 라우팅 테이블이 없어 모든 포트에 패킷을 전달한다.

브로드 캐스트 일때는 테이블에 저장이 안된다 
그래서 브릿지에 연결된 모든 포트로 패킷을 전달한다.

콜리전 도메인은 나눠지지만 브로드캐스트 도메인은 나눠지지 않는다.

Bridge 기능
  #1  #2
  A   D
  B   E
  C   F
- Learning : 브릿지에 연결된 포트의 MAC 주소를 학습하여 테이블에 저장
- Filtering : A에서 B로 패킷을 보내면 브릿지는 패킷을 버린다
- Forwarding : A에서 D로 패킷을 보내면 브릿지는 2번 테이블로 전달한다.
- Flooding : A가 X 포트에 패킷을 보내면 1번을 제외한 나머지 테이블로 패킷을 전달한다.
- Aging : 주된 기능이 아니지만, 1번 테이블에 계속 추가되면 메모리 부족 포트가 삭제된다.

Bridge aging attack : 브릿지에 연결된 포트에 계속 패킷을 보내서 테이블을 가득 채워서 브로드캐스트 도메인으로 만들어버리는 공격

라우터 (Router)
: 브로드캐스트 도메인을 나누는 장비

Linux 명령어
ls : 디렉토리 목록 확인
ls -l : 디렉토리 목록 확인(자세히)
ls -a : 숨김파일까지 확인

man : 명령어 도움말 확인
ex) man ls

디렉토리 구조 : 트리 구조

절대 경로 표현 방법
  : / 디렉토리를 기준으로 표현하는 방법
상대 경로 표현 방법
  : 현재 위치(./)를 기준으로 표현하는 방법

ls > crt : ls 명령어의 결과를 crt 파일에 저장
ls > a.txt : ls 명령어의 결과를 a.txt 파일에 저장

ls < crt : crt 파일을 ls 명령어의 입력으로 사용
ls < a.txt : a.txt 파일을 ls 명령어의 입력으로 사용

ls >> crt : ls 명령어의 결과를 crt 파일에 이어서 저장
ls >> a.txt : ls 명령어의 결과를 a.txt 파일에 이어서 저장

ls << crt : crt 파일의 내용을 ls 명령어의 입력으로 사용
ls << a.txt : a.txt 파일의 내용을 ls 명령어의 입력으로 사용
"""