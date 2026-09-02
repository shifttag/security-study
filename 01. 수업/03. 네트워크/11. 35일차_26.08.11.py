"""
DNS - 구조
p.4 - dns 교안

Client가 www.amazon.com의 IP를 원하는 경우 local DNS 서버의 동작
  1. Root DNS서버에 접속 com DNS server의 IP를 질의한다.
  2. 응답 받은 com DNS서버의 IP로 amazon.com을 관리하는 DNS server의 IP를 질의한다.
  3. 응답 받은 amazon.com 관리 DNS server에게 www.amazon.com의 IP를 질의한다.
  4. 획득한 www.amazon.com의 IP를 Client에 제공한다.

도메인 위임
















"""