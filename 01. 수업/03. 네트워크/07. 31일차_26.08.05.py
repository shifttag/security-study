"""
리눅스 시스템 시관 관리

clock
: 리눅스 시스템에 탑재된 BIOS의 시간을 출력하거나 반영
# clock [옵션]
  -r : BIOS의 시간을 읽어 표준 출력
  -w : 시스템의 시간을 이용 시간을 변경
  -s : BIOS의 시간으로 시스템의 시간 변경

date
: 지정한 포맷으로 시스템의 날짜를 출력
# date [+포맷]
포맷
  - 시 : %H(00~23), %I(01~12), %k(0~23), %l(1~12), %p(am,pm)
  - 분 : %M(00~59)
  - 초 : %S(00~59)
  - 시간 : %r(hh12:mm:ss AM), %T(hh24:mm:ss)
  - 기타 : %s (1970년 1월 1일 이후 경과된 초)
  - 년 : %Y(YYYY), %y(yy)
  - 월 : %m(01~12), %B(January~December), %b(Jan~Dec)
  - 일 : %d(01~31)
  - 요일 : %A(Sunday~Saturday), %a(Sun~Sat), %w(0~6)

# timedatectl [set-timezone 타임존]
ex) timedatectl set-timezone Asia/Seoul

chrony
: 이전에는 rdate를 사용했으나 새로운 chrony는 더 적은 메모리와 CPU사용,
  갑작스러운 클럭 변화에도 빠르게 적응하는 장점이 있다

# dnf list chrony
: chrony 설치 확인

# dnf install -y chrony
: chrony 설치

# systemctl enable chronyd.service
# systemctl start chronyd.service
: chrony 실행 설정


nameserver
C:\Windows\System32\drivers\etc\hosts

FTP 서비스의 개요
vsftpd 서버 구성

소켓을 두개씩 연다 : Out of band
21 : control connection
20 : data connection

# dnf install -y vsftpd
: vsftpd 설치

# systemctl start vsftpd.service
# systemctl enable vsftpd.service
: vsftpd 서버 실행

관련 파일
  - 데몬 : /usr/sbin/vsftpd
  - 설정 파일 : /etc/vsftpd/vsftpd.conf
  - PAM 모듈 : /etc/pam.d/vsftpd
  - 접근 제한 파일 : /etc/vsftpd/ftpusers
                  : /etc/vsftpd/user_list

  f

"""