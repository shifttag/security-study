"""
교안 Linux Server_02 DNS.pdf

nameserver
역할 : 클라이언트가 도메인을 질의를 하면 그 도메인에 해당하는 IP를 알려주는 역할

- IP와 이름간 mapping


1. Client가 Local DNS 서버에게 www.naver.com의 IP 주소를 질의
2. Local DNS 서버가 Root DNS 서버에게 www.naver.com의 IP 주소를 질의
3. Root DNS 서버가 Local DNS 서버에게 .com DNS 서버의 주소를 응답
4. Local DNS 서버가 .com DNS 서버에게 www.naver.com의 IP 주소를 질의
5. .com DNS 서버가 Local DNS 서버에게 naver.com DNS 서버의 주소를 응답
6. Local DNS 서버가 naver.com DNS 서버에게 www.naver.com의 IP 주소를 질의
7. naver.com DNS 서버가 Local DNS 서버에게 www.naver.com의 IP 주소를 응답
8. Local DNS 서버가 Client에게 www.naver.com의 IP 주소를 응답

1. client가 local DNS 서버에게 www.naver.com IP를 질의
2. local DNS 서버가 root DNS 서버에게 ns.com의 IP를 질의
3. root DNS 서버가 local DNS 서버에게 ns.com의 IP를 응답
4. local DNS 서버가 ns.com에게 ns.naver.com의 IP를 질의
5. ns.com이 local DNS 서버에게 ns.naver.com의 IP를 응답
6. local DNS 서버가 ns.naver.com에게 www.naver.com의 IP를 질의
7. ns.naver.com이 local DNS 서버에게 www.naver.com의 IP를 응답
8. local DNS 서버가 client에게 www.naver.com의 IP를 응답

=== 리눅스 ===
1. DNS 서버 설치 및 설치 확인
# dnf list bind bind-utils
# dnf install -y bind bind-utils

2. /etc/named.conf 파일 설정
  - 데몬 : /usr/sbin/named
  - 관리 스크립트 : /usr/lib/systemd/system/named.service
  - 환경 설정 파일 : /etc/named.conf
  - 설정 파일 경로 : /var/named/
    - named.ca와 여러 zone 파일들
  - 이외 관련 파일 : /etc/resolv.conf, /etc/host.conf
  - 실행을 위한 최소 권한
    - /etc/named.conf, /var/named, /var/named/*
    - 그룹 소유자는 반드시 named로 정의한다.

3. Cache 파일 확인
- named.ca 파일
- 도메인을 관리할 필요가 없다.
4. name 서버 시작
# systemctl [start | stop | status] named.service


=== SQL ===
자기 참조 조인

SQL> select d.dno 부서번호, dname 부서명, ename 사원명
  2  from dept d, emp e
  3  where d.dno = e.dno(+)
  4  order by 1;

  (+) 해주면 빈 값으로 한 행을 만들어 준다.

  
1.
select DISTINCT *
from student s, student t
where s.sname = t.sname AND s.sno < t.sno;

2.
select s.eno 사번, s.ename 이름, s.mgr 사수사번, e.ename 사수이름
from emp e, emp s
where e.eno = s.mgr;

3.
select e.eno 사번, e.ename 이름,e.sal 급여, e.mgr 사수사번, s.ename 사수이름, s.sal 사수급여
from emp e, emp s
where s.eno = e.mgr AND s.sal < e.sal
order by e.sal-s.sal desc;

4.
select p.pno 교수번호, p.pname 교수이름, p.section 학과, c.cname 과목
from professor p, course c
where p.pno = c.pno(+)
order by p.section;

"""