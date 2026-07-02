"""
Cisco Packet Tracer

Switch> : User EXEC 모드
Switch# : Privileged EXEC 모드
Switch(config)# : Global Configuration 모드

# User EXEC 모드에서 Privileged EXEC 모드로 전환
Switch> enable (약자 : en)

# Privileged EXEC 모드에서 Global Configuration 모드로 전환
Switch# configure terminal (약자 : conf t)

# Global Configuration 모드에서 Privileged EXEC 모드로 전환
Switch(config)# exit (약자 : ex | ctrl + z)

# Privileged EXEC 모드에서 User EXEC 모드로 전환
Switch# disable (약자 : disa)

help : 명령어를 입력하면 명령어의 사용법을 확인할 수 있음
? : 각 모드에서 사용가능한 명령어
명령어 + ? : 명령어의 사용법을 확인할 수 있음
ex) show ? : show 명령어의 사용법을 확인할 수 있음

# Privileged EXEC 모드에서 CLI
show : 명령어를 입력하면 장치의 상태를 확인할 수 있음




# Global Configuration모드에서 CLI
hostname [장치명] : [장치명]으로 변경


cisco 명령어 특징
: 반대 명령어는 앞에 no를 붙이면 됨
ex) no shutdown : shutdown 명령어의 반대 명령어

# NVRAM에 설정 저장 명령
copy running-config startup-config (약자 : copy run start)

# NVRAM의 설정 삭제 명령
erase startup-config (약자 : erase start)

# 장비 재부팅
reload (약자 : relo)

# 장비 상태 확인
show ip interface brief : 장비의 인터페이스 상태 확인

# DNS lookup 기능 해제 (중요!)
no ip domain-lookup

# 시간 설정
show clock : 현재 시간 확인
clock set [시] [분] [초] [월] [일] [년도] : 시간 설정
- packet tracer에서는 시간 설정이 안됨 (외부와 통신 필요)

인터페이스 번호
: 0/0, 0/1, 
0 : slot 번호
1 : port 번호
0/1/2 - 0 : slot 번호, 1 : subslot 번호, 2 : port 번호

# ip 할당
ip address [ip주소] [서브넷마스크] : ip주소 할당
ex) (config-if)# ip address 192.168.10.1 255.255.255.0
- CIDR 불가능

netmask : 255.255.255.0
wildmask : 0.0.0.255

스위치는 vlan에 속한 포트에만 ip를 할당할 수 있음


리눅스 명령어
vi 편집기

명령모드
1. 검색
    # /문자열
n : 검색한 문자열의 다음 검색 결과로 이동
N : 검색한 문자열의 이전 검색 결과로 이동

2. 치환
    # %s/원단어/바꿀단어/[옵션]
        - 라인에 맨 앞에 단어만 치환한다
    옵션
    - g : 전역 치환
    - i : 대소문자 구분 없이 치환
    - c : 치환할 때마다 확인

3. 환경 설정
    # set [환경변수] [값]
    환경변수
    nu : 행번호 표시
    nonu : 행번호 표시 해제
    sm : 반대 괄호 표시


사용자 관리 (여기서부터 중요)

cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
계정:패스워드:UID:GID:설명:홈디렉토리:쉘

cat /etc/group
root:x:0:
그룹명:암호:GID:소속계정

ex) dba:x:1100:ora12c,ora11g,ora10g,root

해시코드에서 무작위 대입 공격은 생일 공격(Birthday Attack)이라 한다

groupadd
groupadd [-g [GID]] [그룹명] : 그룹 생성
ex) groupadd -g 2000 st

-g : 생성 그룹의 GID 번호를 지정한다
    - 할당하지 않으면 1000 이상 중복되지 않은 값으로 GID가 자동으로 할당된다
    - GID번호는 식별자일 뿐 값 자체에는 의미가 없다.
-r : 1000번 이하의 GID 번호를 자동으로 할당한다.
    - 1000번 이하의 GID는 시스템이 daemon이나 관리 목적으로 사용함으로 가능한 사용하지 않는것이 좋다
-o : 중복된 GID 번호 할당이 가능하다
    - GID가 같고 이름이 다른 그룹을 생성할 수 있다
    - 이름이 같고 GID가 다른 그룹은 생성할 수 없다

groupdel [그룹명] : 그룹 삭제

"""