"""
방화벽 해제
: systemctl disabled firewalld.service

방화벽 확인
: systemctl status firewalld.service

selinux 해제
: vi /etc/selinux/config
: SELINUX=enforcing -> SELINUX=disabled 변경

selinux 상태 확인
: getenforce
: sestatus



dnf -y install ksh libaio-devel glibc-devel libstdc++-devel gcc-c++ libnsl wget
dnf install -y https://yum.oracle.com/repo/OracleLinux/OL7/latest/x86_64/getPackage/compat-libcap1-1.10-7.el7.x86_64.rpm
dnf install -y https://yum.oracle.com/repo/OracleLinux/OL7/latest/x86_64/getPackage/compat-libstdc++-33-3.2.3-72.el7.x86_64.rpm
dnf install -y https://yum.oracle.com/repo/OracleLinux/OL8/appstream/x86_64/getPackage/oracle-database-preinstall-19c-1.0-2.el8.x86_64.rpm

SQL 관리자 진입
: sqlplus / as sysdba

db 서버 상황 확인
: select status from v$instance;

db 서버 shutdown
: shutdown immediate

db 서버 켠다
: startup

db 연결
: conn / as sysdba

컴퓨터 끄는 순서
db shutdown -> exit -> poweroff










"""