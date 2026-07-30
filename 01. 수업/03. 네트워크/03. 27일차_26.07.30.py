"""
echo 1 > /proc/sys/net/ipv4/ip_forward
이거는 임시적인 방법이다.
재부팅 시 사라짐

vi /etc/sysctl.conf 파일에
net.ipv4.ip_forward = 1 
추가하면 재부팅 시 사라지지 않는다.

프로그램 설치
1. 관련 패키지 설치.
# dnf install -y gcc gcc-c++ cmake apr apr-util zlib-devel wget
net-tools expat-devel perl wget

2. Apache 2.2.34 소스파일 /usr/local/에 다운
# cd /usr/local/
# wget https://archive.apache.org/dist/httpd/httpd-2.2.34.tar.gz

3. 소스파일 압축을 해제
# tar xvfz httpd-2.2.34.tar.gz
4. 아파치 설치&실행
# cd httpd-2.2.34
# ./configure --prefix=/app/apache --enable-rewrite --enable-so
 (https://httpd.apache.org/docs/2.2/programs/configure.html)
# make -j$(nproc)
# make install

# /app/apache/bin/apachectl start



make -j$(nproc) : CPU 전부를 사용하겠다는 것
/app/apache/bin/apachectl : apache 실행하는 스크립트 파일




RPM과 DNF

RPM 패키지의 구조
패키지명-버전-릴리즈.아키텍처.rpm

rpm -qa : 시스템에 설치된 모든 패키지명
rpm -qi [패키지명] : 패키지의 상세한 정보
rpm -ql [패키지명] : 패키지의 파일 리스트
rpm -qf [파일명] : 지정한 파일이 포함된 패키지


설치 및 업그레이드

rpm [-ivh | Uvh | -Fvh] 패키지명

옵션
  -i : 설치
  -U : 업그레이드 (이전 버전 미설치시 -i와 동일)
  -F : 업그레이드만
  -v : 설치과정 출력
  -h : 설치정도 출력 (#)
  -e : 패키지 삭제

sqlplus ast22/ast@dal

dal : TNS명

tnsnames.ora
TNS_ADMIN
ORACLE_HOME/network

%ORACLE_HOME%
%ORACLE_BASE% : C:\app\ora19c

기존에는
sqlplus ast##/ast##@192.168.10.11:1521/DB19


테이블명이 너무 길 때
col 컬럼 format a##
ex) col tname format a20


set line 100
set pages 100
"""