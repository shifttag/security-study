"""
#max_clients=30 - 최대 접속자 수 
#max_per_ip=3 (0은 무제한) - 한 ip에서 클라이언트 최대 접속 수 
#ls_recurse_enable=YES (ls -R 명령은 부하가 크다)

➢ 익명 사용자 관련 설정
anonymous_enable=YES ← NO - 익명 사용자 접속 가능 여부
#anon_upload_enable=YES (d:NO)
#anon_mkdir_write_enable=YES (d:NO)
#deny_email_enable=YES (d:NO banned_email_file )
- banned_email_file 파일에 지정된 메일 계정은 접속이 불허된다.
#non_anon_password=NO
#anon_root=/var/ftp (d:/var/ftp)
#ftp_username=ftp (d:ftp)


chroot 설정
#chroot_list_enable=YES
  - chroot_local_user가 NO일 때 chroot_list_file에 지정된
    사용자만 chroot를 적용한다.
  - chroot_local_user가 YES일 때 chroot_list_file에 지정된
    사용자만 chroot를 적용하지 않는다.
#chroot_local_user=YES (d:No)

#chroot_list_file=/etc/vsftpd/chroot_list - 사람 계정 목록
- Default 값 : /etc/vsftpd/chroot_list
#allow_writeable_chroot=YES ← chroot 적용시 반드시 추가필요, 접속이 불가하다.
• chroot 설정은 외부 디렉토리로 연결된 link 디렉토리에 접근도 금지된다. 이때는 mount 명령을 이
용한다.
mount --bind [원본 디렉토리] [연결할 디렉토리]


rdt 3.0 : sender

채널에 error나 loss가 가능

sender가 패킷을 보내면 timer 실행
일정시간이 지나면 timeout event 발생

전송한 PK에 대한 ACK를 수신햇을 때 timer가 stop

timeout = RTT + @

timer : 
  start : PK을 전송한 다음 바로
  stop : 전송한 PK에 대한 ACK를 받았을 때만

  timeout : PK 재전송

  
Pipelining 
: sender에게 ACK를 기다리지 않고 여러 개의 pkt를 전송하도록 사용하는것
  - sequence number의 범위는 증가되어야 한다.
  - sender와 receiver는 하나이상의 pkt를 buffering 해야한다.

piplining protocol : go-Back-N, selective repeat

p.174 한꺼번에 보내는 패킷의 양을 window size라 한다

window 사이즈가 너무 커지면
sender가 보내는 패킷의 양이 기하급수적으로 커진다 (재전송 포함)
네트워크가 느려지는 현상이 생긴다
그거 해결하기 위해 혼잡제어와 흐름제어가 있는거다.


"""