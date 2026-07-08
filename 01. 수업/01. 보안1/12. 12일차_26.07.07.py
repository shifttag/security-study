"""
라우터는 서로 다른 네트워크를 연결하는 장치이다.

Routing Protocol
- static
- RIP
- OSPF
- EIGRP
- BGP


Distance Vector
: 최단거리
- Hop Count base
- RIP

Link-State
: 최단시간
- Cost base
- OSPF, IS-IS

Advanced Distance Vector
: Cisco사에서 만든 Link-State 방식
- EIGRP 

Classful
: IP Address를 입력하면 자동으로 서브넷마스크를 클래스에 맞게 지정
- subnet mask를 교환하지 않는다
- RIP, IGRP

정적 라우팅
: 모든 경로에 대한 정보를 직접 관리자가 입력해주는 방식이다
- 단순 경로 네트워크나 단일 외부 경로를 가진 최종 사용자 네트워크에 매우 유용하다
- 라우터 장치 이외에 리눅스나 유닉스 윈도우즈 등의 OS에서도 기본적인 기능으로 제공된다.

라우터를 hop이라 할수도 있다??

default 라우트 

=== 리눅스 명령어 ===

1. suid, sgid, sticky bit
: 추가된 퍼미션으로 실행 및 삭제 권한을 보완한다
suid, sgid
  : 실행 파일에만 적용된다. 파일이 실행된 프로세스는 실행한 사용자 소유로 실행 권한이 부여되지만 suid, 
sgid를 설정한 파일의 프로세스는 파일 소유자나 그룹 소유자의 ID로 실행된다.  실행 권한에 s로 명시
된다.
  - suid : 4000, u+s
  - sgid : 2000, g+s

  EX) passwd
    : Passwd 명령은 /etc/passwd, /etc/shadow 와 같은 root 소유자 파일을 변경함으로 실행 시에 파일 소
유자인 root 권한으로 실행된다.

2. sticky bit
: 파일에 대해서 퍼미션과 관계없이 소유자만 삭제 가능하게 할 때 디렉토리에 other 권한을 제한한다.
  - Other을 대상으로 설정한다.
  - 모든 권한 허가가 가능하지만 삭제는 소유자만 가능하다
  - 1000 : o+t

  suid(4), sgid(2), stick bit(1)
  suid와 sgid는 user와 group 퍼미션에 s로 표시되고
stichy bit는 other 퍼미션에 t로 표시된다.

7777  : rwsrwsrwt
4777  :  rwsrwxrwx  (u+s)
2777  :  rwxrwsrwx  (g+s)
1777  :  rwxrwxrwt  (o+t)

3. chown, chgrp
: 소유자 변경, 그룹 소유자 변경
chown [-R] [유저명] [대상]
chown [-R] [유저명].[그룹명] [대상] - 비표준명령
chgrp [-R] [그룹명] [대상]

"""