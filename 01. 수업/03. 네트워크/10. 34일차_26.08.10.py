"""
DNS 서버
  - Cache DNS
    /etc/named.conf
    /var/named/named.ca

  - 책임 DNS
    :ast##.sec
    /etc/named.conf
    /var/named/.named.ca
    /var/named/ast##.zone
    : 호스트 관련 내용 zone 파일에 있음

Cache DNS는 root DNS 서버만 보고 찾고
책임 DNS 서버는 ast##.zone 파일에서 찾고 없으면 root DNS 서버에서 찾는다

책임 DNS (Authoritative DNS)

리눅스 nameserver 만들때는 root domain인 "." 생략 불가능

$TTL 1D
@ IN SOA ns.te.sec. root.ns.te.sec. (
                                      0 ; Serial
                                      1D ; Refresh
                                      1H ; Retry
                                      1W ; Expire
                                      3H ) ; Minimum
; Name Server
  IN NS ns.te.sec.
; Host address
    IN A 192.168.10.31
  ns IN A 192.168.10.31
  mail IN A 192.168.10.32
;
  www IN CNAME mail

0 ; Serial : 파일 수정 시 시리얼 넘버 증가해야함

Host address
A 타입 : IP 형식
CNAME 타입 : 한 IP에 여러 name 등록할 때

ns는 1, 6 ftp, www 는 2, 7

복사된 zone 파일은 바이너리 파일이라 내용을 확인할 수 없다.














"""