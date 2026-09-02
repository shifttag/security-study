"""
접속 IP제한
  - 현재 배포되는 시스템에서는 지원되지 않는다
  
사용자 제한 설정(user_list)
  : userlist_file(/etc/vsftpd/user_list)에 등록된 계정에 대한
  접속 제어는 userlist_enable과 userlist_deny에 따라 결정된다.
  
ftp 교안 p.12

사용자 제한 설정(ftpusers)
: Pam

/etc/pam.d/vsftpd
: sense [deny | allow] 설정에 따라 /etc/vsftpd/ftpusers 설정이 바뀐다

auth  required pam_listfile.so item=user sense=deny
file=/etc/vsfptd/ftpusers oner=succees


HTTP(Hyper text transfer protocol)
  - Client : browser는 웹용 client app, 질의를 전달하고 요구한 
  web page를 보여주는 기능
을 담당
 - Server : Web server로 client의 질의에응답하고 여러 
 web object를 client에 전송한다.

사전과정
# dnf install -y gcc gcc-c++ cmake apr apr-util zlib-devel wget expat-devel

설치과정
1. httpd-2.2.34.tar.gz 버전을 /usr/local/ 에 다운 받는다.
  - wget https://archive.apache.org/dist/httpd/httpd-2.2.34.tar.gz
2. tar xvfz httpd-2.2.34.tar.gz
3. cd ./httpd-2.2.34
4. ./configure --prefix=/app/apache --enable-so
5. make
6. make install

apache reboot시 자동 실행
[root@Linux207 bin]#  cd /etc/rc.d
[root@Linux207 rc.d]# chmod u+x rc.local
[root@Linux207 rc.d]# ls
init.d  rc.local  rc0.d  rc1.d  rc2.d  rc3.d  rc4.d  rc5.d  rc6.d
[root@Linux207 rc.d]# vi rc.local
안에 내용에 /app/apache/bin/apachectl start  내용 추가
[root@Linux207 rc.d]# reboot






[root@Linux209 html]# ls
404.html  50x.html  index.html  nginx-logo.png  poweredby.png
[root@Linux209 html]# pwd
/usr/share/nginx/html

[root@Linux209 nginx]# ls
conf.d        fastcgi.conf.default    koi-utf     mime.types.default  scgi_params          uwsgi_params.default
default.d     fastcgi_params          koi-win     nginx.conf          scgi_params.default  win-utf
fastcgi.conf  fastcgi_params.default  mime.types  nginx.conf.default  uwsgi_params
[root@Linux209 nginx]# pwd
/etc/nginx





















"""