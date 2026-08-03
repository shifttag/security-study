"""
=== 리눅스 ===

DNF (Dandified Yum)
: YUM의 기능을 개선한 명령으로 Linux 배포판 8버전 이상에서 사용되는
  패키지 매니저이다.
- python을 기반으로 제작되었다.
- 대부분의 사용법이 yum과 호환된다.
- 8 이전 버전은 지원되지 않는다. -yum을 이용한다.

1. dnf list
: 패키지를 확인하는 명령어
# dnf list [installed | updates | available | 패키지명]
  - 설치 가능한 모든 패키지 목록을 보여준다.
  - installed : 설치된 패키지 목록을 보여준다.
  - updates : 업데이트된(가능한) 패키지 목록을 보여준다.
  - available : 설치 가능한 패키지 목록을 보여준다.
  - 패키지명 : 패키지의 설치 여부와 update 정보를 보여준다.

검색 추가 옵션
: repolist, search, repoquery, provide

# dnf repolist
: 시스템에 등록된 repository list를 출력한다

# dnf search 문자열
: 패키지명이나 description에 문자열이 포함된 패키지들을 출력한다.

# dnf repoquery -l 패키지명
: 패키지에 포함된 파일의 목록을 출력한다

# dnf provides 파일
: 파일이 소속된 패키지들을 출력한다.

2. 설치 및 업데이트
# dnf install [-y] 패키지명
: 패키지를 repoisitory로 부터 설치한다.

# dnf update [-y] 패키지명
: 패키지를 repoisitory로 부터 업데이트한다.

# dnf remove [-y] 패키지명
: 지정한 패키지를 삭제한다.

# dnf upgrade [-y] [--security]
: upgrade와 동일함

# dnf clean all
# dnf makecache
: 초기화

3. Group package 확인과 설치
# dnf group [list | install "그룹" | remove "그룹" | info "그룹"]
  - list : 그룹 목록을 출력한다
  - install "그룹" : 그룹을 설치한다
  - remove "그룹" : 그룹을 삭제한다
  - info "그룹" : 그룹의 정보를 검색한다.

4. 저장소 관리
# dnf repolist [all]
: 저장소 목록을 검색한다

5. 저장소 활성화
# dnf config-manager --set-enabled [repo] || \*
: 저장소 활성화
# dnf config-manager --set-disabled [repo] || \*
저장소 비활성화

wget : 윈도우에서 다운받을 수 있는 명령어

Remi Repository
: PHP, MySQL, MariaDB, Redis, Memcached 등과 같은 최신 버전
dnf install https://rpms.remirepo.net/enterprise/remi-release-8.rpm


== 서비스와 데몬 ==

방식
1. stand alone
  - 스스로 listen하며 항상 메모리에 상주
  - 서비스 요청 즉시 대응 가능
2. Super daemon
  - Listen을 직접하지 않는다.
  - 메모리에 상주하지 않으며 서비스 요청이 있을 때 xinetd에 의해 호출된다.

서비스 조회
# systemctl list-unit-files

서비스 상태 확인
# systemctl [is-enabled | is-active] [서비스]
: is-enabled : 자동 실행 등록 여부
: is-active : 현재 실행 여부

서비스 등록
# systemctl [enable | disable] [서비스]

서비스 실행
# systemctl [start | stop | restart] [서비스]

systemctl 추가옵션
# systemctl [옵션] [서비스]
  옵션
  - try-restart : 실행, 재실행, 종료
  - Reload : 설정 재 구동
  - status : 상태 확인
  - disable --now : disable과 stop을 동시에 수행



ntsysv 명령
network system service
서비스 설정

레드햇 리눅스 런레벨
0 : shutdown
1 : single user mode
2 : multi user mode without NFS
3 : multi user mode with NFS (주로 사용 - CLI)
4 : unused
5 : Xwindows mode (주로 사용 - GUI)
6 : reboot

Target은 init의 run level과 동일한 개념
EX) multi-user.target : run level 3
    graphical.target : run level 5
    rescue.target : run level 1, single user mode
    emergency.target : run level 0, 응급 복구 모드

제공되는 target 확인
# systemctl list-unit-files --type target --all









"""