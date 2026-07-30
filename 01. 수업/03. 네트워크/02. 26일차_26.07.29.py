"""
리눅스 설치 후 
Linux Basic_00_00 Rocky Linux8_9_install
교안 p.21 ~

시험 진행 후 

리눅스를 라우트로 설정은 영상자료 참고

결국
방화벽 disable
Selinux disable
패킷 포워딩 기능 활성화

sysctl -a | grep ipv4.ip_forward
echo 1 > /proc/sys/net/ipv4/ip_forward

하면 라우터로 사용 가능
정적 라우팅

네트워크 설정에서 고급설정에서
여러개 IP로 설정해서 라우트 설정 없이도
11.0/24, 12.0/24 로 접속 가능하다.



























"""