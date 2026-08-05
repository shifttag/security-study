"""
1. CRON & RSYNC

CRON
: 주기적으로 작업되는 작업 일정을 저장해서 자동으로 실행
  /usr/lib/systmd/system/crond.service
    - 데몬 프로세스
    - /etc/rc.d/init.d/crond
      : 데몬 실행 스크립트
  /etc/crontab
    - 기본 스케줄 일정
  /usr/bin/crontab
    - 스케줄 설정 프로그램 파일
  /etc/cron.allow, /etc/cron.deny
    - crontab 사용 권한 관리 파일

# crontab -u [유저] [옵션]
  옵션
    -e : 스케줄 등록
        : vi 환경으로 스케줄 등록
    -l : 스케줄 확인  
    -r : 스케줄 삭제
  명령어 형식
    : [분] [시] [일] [월] [요일] [작업 내용]
      - 분 : 0~59
      - 시 : 0~23
      - 일 : 1~31
      - 월 : 1~12
      - 요일 : 0~6 (0 : 일요일, 6 : 토요일)
      앞에 / 붙으면 n마다 실행
      ex) /5 : 5분마다 실행

  /var/log/cron : crontab 로그 확인


RSYNC
: 어떤 디렉토리와 다른 디렉토리의 파일을 동기화하는 명령어
  - 같은 컴퓨터도 되고 다른 컴퓨터도 된다.
    "약간 깃허브에 commit push와 비슷한 느낌"
  교안 p.8 사진

  관련 파일
  - 데몬 : /usr/bin/rsync
  - 관리 스크립트 : /usr/lib/systemd/system/rsyncd.service
  - 설정 파일 : /etc/rsyncd.conf

    [서비스 명] : 리소스 식별자, client에서 이용한다.
    path : 백업 경로
    comment : 주석
    uid : 전송자 UID
    gid : 전송자 GID
    use chroot : rsync 경로를 외부에서 / 로 인식한다.
    read only : 읽기 전용으로 접근한다.
    hosts allow : 접속 허용할 호스트 (클라이언트만 지정)
    max connections : 동시 접속자 수
    timeout : 접속 제한 시간

  rsync client 명령어
  : server의 디렉토리와 client의 디렉토리를 동기화
    rsync -avuz [--delete] source destination
    rsync -avuz [--delete] IP::[서비스명] [백업 디렉토리] : 주로 사용
    rsync -avuz [--delete] [백업 디렉토리] IP::[서비스명] 

  # rsync [옵션] [원본 경로] [대상 경로]
    옵션
      -a : archive mode 작업, 심볼릭 링크, 권한 등 모든 내용을 보존한다.
      -v : 작업내용 출력
      -z : 파일을 압축 전송한다
      -u : 최신 파일은 복사하지 않는다
      --delete : source에서 지워진 파일을 destination에서도 지운다


rsync install -y rsync* 양쪽 다 
서버에서 vi /etc/rsyncd.conf
위의 양식대로 설정 후
systemctl restart rsyncd.service


ntsysv
systemctl enable --now rsyncd.service
systemctl status firewalld.service
sestatus
echo 11 > /backup/test.txt


rsync -avuz 192.168.10.206::backup /backup
rsync -avuz --delete 192.168.10.206::backup /backup (완전 동기화)



== 프로세스 ==
프로세스
: 실행중인 프로그램
: 프로그램을 실행시켜 메모리에 적재한 상태
적재된 메모리 영역을 프로텍션 도메인이라 한다.

프로세스는 pid에 의해 구분된다.
포트넘버 : 네트워크 프로세스가 할당받는 번호

fork
: 서버에서 보면 포트넘버는 같은데 PID가 다른 프로세스가 여러개 존재한다.
  - 서버에서 fork를 통해서 프로세스를 복제한다.
  - 클라이언트에서 요청이 들어오면 fork를 통해서 프로세스를 복제한다.

process idle time
: 프로세스가 아무것도 하지 않고 대기하는 시간
- 네트워크 교안 p.145 -> idle time이 99%정도 된다
해결하기위해 p.146 그림처럼 소켓을 여러개로 해서 multi Thread로 만들었다. 

JOB
: job은 터미널에서 실행한 프로세스로 shell에 의해서 job번호가 부여된다




Foreground, Background
1. Foreground
: 현재 터미널에서 제어되는 프로세스이다.
: 터미널 입출력은 foreground 프로세스를 위해서 대기한다.
2. Background
: 터미널과 무관하게 메모리에서 실행되는 프로그램이다.
: 터미널 입출력에 대해서 투명하다.
: 보통 daemon(service) 프로세스들이 background로 실행된다.

ps
: 프로세스를 확인한다.
  옵션
  -a(x) : 현재 터미널에서 실행중인 프로세스
  -e : 모든 프로세스
  -f : 자세한 내용
  -p : 특정 PID의 프로세스를 지정한다.

kill
: 사용자나 프로그램이 프로세스를 제어하기 위해 시그널(Signal)을 발생시키는데
  이런 시그널을 직접 보내는 명령어이다
# kill [-signal] [PID]
  옵션
  -l : signal 목록 (9: 프로세스 강제 종료) p.11 시그널 목록



SQL
날짜 형식 변경과 확인

ALTER SESSION SET NLS_DATE_FORMAT ='YYYY/MM/DD';

SELECT *
FROM NLS_SESSION_PARAMETERS
WHERE PARAMETER = 'NLS_DATE_FORMAT';


1.
select *
from student
where major = '화학';

2. 
select *
from student
where avr < 2.0;

3. 
select sno 학번, sname 이름, avr 평점
from student
where sname = '권현';

4. 
select *
from professor
where orders = '정교수';

5.
select *
from professor
where section = '화학';

6.
select *
from professor
where pname = '송강';

7.
select *
from student
where major = '화학'
order by avr desc;

8.
SELECT *
FROM professor
WHERE hiredate < '2000-01-01'
ORDER BY hiredate;


1.
select *
from professor
where hiredate between '1999-01-01' and '2001-12-31';

2. 
select *
from professor
where orders in('정교수', '조교수');

3.
select *
from course
where st_num in(1, 2);

4.
select *
from student
where syear in(1, 2) and avr between 2.0 and 3.0;

5.
select *
from student
where major in('물리', '화학') and ((avr/4.0) * 4.5) between 3.5 and 4.0;

6.
select *
from student
where major in('물리', '화학')
order by syear desc, avr desc;

7.
select *
from professor
where section in('물리', '화학') and hiredate between '1999-01-01' and '2000-12-31'
order by orders desc;

8.
select *
from course
where pno is null and st_num = 3;

9.
select *
from course
where cname like '%화학%' and st_num <= 2;

10.
select *
from student
where sname like '권%' and major = '화학';


emp table
"""