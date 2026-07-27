"""
## S-box

6bit를 4bit로 변환
p.36
ex) 101101
첫자리와 끝자리 bit 추출
11 : 3행, 0110 : 6열
S1 table에 3행 6열에 해당하는 1을 
4bit로 출력 : 0001

## 순열 p
p.33 사진 f함수, p37
: p.33 암호화 과정
  - 짝수번 반복하면 된다.
32bit인 함수를 한번 순열 돌린다.

DES 키가 만들어지는 과정 p.40
: 원키 64bit -> PC-1 (각 8번째 bit 삭제) -> 56bit
PC-1 table p.41  (보면 각 8번째 bit는 없음)
: 56bit -> left shift -> 순열/수축 (PC-2) -> 48bit
PC-2 table p.42 (48bit 추출)

16번 반복하면
k1~k16까지 각 DES 키가 나온다.

left shift 횟수 p.43

p.44 DES - 작동 원리 (참고만)

p.30 암호화 과정 (참고자료)

### DES 작동 모드
1. ECB (Electronic Codebook) 모드
  : 각 키를 가지고 암호화
2. CBC (Cipher Block Chaning)
  : P1 암호화 한 결과값 C1
  : 다음 암호화 할 때 P2와 C1 XOR 후에 암호화
  : 가장 기본적인 모드
3. CFB (Chipher Feedback) - (Chipher - 링크암호?)
  : NASA에서 개발
  : 64bit 레지스터 -> k 키값으로 DES 암호화 -> 선택 j비트
  : -> P1 XOR j비트 -> C1
  : -> C1이 16bit이면 다음 64비트에 오른쪽에 패딩
4. OFB (Output Feedback)
  : CFB와 거의 동일
  : 선택 j비트를 다음 레지스터에 보낸다.

AES (Advanced Encrytion Stardard)
: DES를 대체하기 위한 표준암호 알고리즘
  - 128, 192, 256 비트의 다양한 길이의 키를 사용
  - 알려진 모든 공격에 대응 가능
  - 스마트 카드상의 컴팩트한 보조 프로세서 등에 이용 가능

IDEA (International Data Encryption Algorithm)
: 국제 데이터 암호 알고리즘
  - 64bit 평문 블록에서 128비트 키를 이용 작동
  - 8라운드로 작동

RC5

SEED
: 한국 정보보호 센터에서 개발
  - G함수가 사용된다.


## 공개키 암호 시스템
: 두 개의 다른 키 사용
  - 공개키 : 모든 사람이 접근 가능한 키 (공개)
  - 개인키 : 각 사용자 자신만이 소유 (비밀)

특징
  - 암호 알고리즘과 암호키를 알아도 복호키 계산 불가능
  - 두 개의 키 중 하나는 암호에 다른 하나는 복호에 사용
  - 대칭키에 비해 속도가 느리다

1. 공개키와 개인키 생성
2. 공개키는 공개하고 개인키는 개인이 소유
3. A는 B의 공개키로 메시지를 암호화
4. B는 자신의 개인키로 메시지 복호화
  (B의 개인키를 모르는 제 3자는 메시지 복호 불가능)

공개키 사용법
p.59 : 기밀성을 이용한 방법
p.60 : 근원지 증명을 위한 서명문 작성법
p.61 : 근원지 증명 + 기밀성을 이용하는 방법 (통신속도 느림)

공개키 알고리즘의 조건 (diffie와 hellman)
  - 키 쌍(공개키 KU, 개인키 KR)의 생성이 쉽다.
  - 다음 식과 같은 암호문의 생성이 쉽다.
    C = Ekub(M)
  - 다음 식과 같은 암호문의 복구화가 쉽다
    M = Dkrb(C) = Dkrb[Ekub(M)]
  - 공개키 kub로부터 개인키 krb를 결정하는것은 어렵다.
  - 공개키 kub와 암호문 C로부터 메시지 M의 복구가 어렵다.
  - 암호와 복호 기능이 다음과 같이 적용 가능하다
    M = Ekub[Dkrb(M)]

=== 중요하다는데...? ===

비밀키 분배의 어려움
  - 물리적인 방법으로 전달
  - 이전의 키를 사용하여 암호화된 새로운 키를 전송
  - 제 3자를 통하여 키분배

해결
KDC를 이용한 키분배 (Kerboros)
p.71

3자를 통하여 키분배
(네트워크에 들어와있는 사람들 가입자
어떤 발신자 A와 응답자 B 이런애들이 엄청 많다
)
네트워크에 KDC (Key Distribution Center) 만든다
발신자, 응답자는 KDC와 마스터 키 교환을 한다
KDC와 발신자 A와 키교환을 할때는 KA 마스터키 교환을 한다
KB도 마찬가지

KDC는 가입자들의 비밀키를 다 가지고 있다.
발신자나 응답자는 KA, KB인 마스터키를 본인들만 가지고 있다.

(발신자는 B랑 통신할 세션키를 KDC에 만들어달라 요청
신원정보 : id - 구분
인증정보 : pw -      두개를 합쳐 I&A라고도 한다
ID(A)는 A의 신원정보 | 인증정보
A, B 는 발신자, 응답자
KDC에서 SK(session key)를 A와 B한테 분배해준다
T는 약속된 난수

받은 세션키와 난수 T를 이용해 A가 B한테 요청한다 (B는 난수 T로 A인것을 알 수 있다.)
B는 미리 약속된 연산 난수 T+1를 이용해 B가 A한테 인증한다.

통신이 끝나면 세션키와 난수 T는 폐기한다
)

(KDC는 1차 도메인 서버 )


=== 리눅스 ===
nmcli connection modify [CONN] \
      ipv4.method [option] \
      ipv4.address [ip/mask] \
      ipv4.gateway [gateway_ip]
      ipv4.dns [dns-server_ip]
      ipv4.dns-search [search_domain]

  ip 변경
    : nmcli connection mod [CONN] ipv4.address [ip/mask]
  gateway 변경
    : nmcli connection mod [CONN] ipv4.gateway [new gateway ip]
  Local DNS 변경
    : nmcli connection mod [CONN] ipv4.dns "[DNS IP]"
  설정 적용
    : nmcli connection up [CONN]

    option : auto(DHCP), manual, disable

"""