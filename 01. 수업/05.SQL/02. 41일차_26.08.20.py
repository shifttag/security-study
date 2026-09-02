"""
DROP TABLE sales_detail CASCADE CONSTRAINTS;
DROP TABLE sales_slip CASCADE CONSTRAINTS;
DROP TABLE product CASCADE CONSTRAINTS;


CREATE TABLE product (
    제품번호 VARCHAR2(12),
    제품명   VARCHAR2(100),
    제품단가 NUMBER,

    CONSTRAINT product_제품번호_pk PRIMARY KEY (제품번호),
    CONSTRAINT product_제품명_uk UNIQUE (제품명),
    CONSTRAINT product_제품단가_ck CHECK (제품단가 > 0)
);

CREATE TABLE sales_slip (
    전표번호 VARCHAR2(12),
    판매일자 DATE NOT NULL,
    고객명   VARCHAR2(50) NOT NULL,
    총액     NUMBER,

    CONSTRAINT sales_slip_전표번호_pk PRIMARY KEY (전표번호),
    CONSTRAINT sales_slip_총액_ck CHECK (총액 > 0)
);

CREATE TABLE sales_detail (
    전표번호 VARCHAR2(12) NOT NULL,
    제품번호 VARCHAR2(12) NOT NULL,
    수량     NUMBER NOT NULL,
    단가     NUMBER NOT NULL,
    금액     NUMBER NOT NULL,

    CONSTRAINT 전표상세_pk
        PRIMARY KEY (전표번호, 제품번호),

    CONSTRAINT 전표상세_전표번호_fk
        FOREIGN KEY (전표번호)
        REFERENCES 판매전표(전표번호),

    CONSTRAINT 전표상세_제품번호_fk
        FOREIGN KEY (제품번호)
        REFERENCES 제품(제품번호),

    CONSTRAINT 전표상세_수량_ck
        CHECK (수량 > 0)
);
테스트(수강생평가)
1. 단말장치 네트워크 관리
1-1. Linux 네트워크 인터페이스(ens160) 설정 파일 내용 확인 명령
: cat /etc/sysconfig/network-scripts/ifcfg-ens160

1-2. nmcli 명령으로 ens160의 수정된 설정을 적용하는 명령
: nmcli conn up ens160

1-3. ip 명령으로 통해 현재 활성화된 인터페이스(ens160) 정보 확인
: ip a show dev ens160

2. 접근통제 관리
2-1. /home/data/ 소유자 및 소유그룹 확인
: ls -l /home

2-2. /home/data/  허가권을 절대모드를 이용해 변경
      (소유자와 그룹소유자 : 읽고쓰고실행 권한,  그외 : 권한 없음)
: chmod 770 /home/data

3. 소프트웨어 관리
3-1. dnf 명령을 이용해 bind 프로그램 설치
: dnf install -y bind

3-2. dnf 명령을 이용해 bind 프로그램 설치 여부 확인
: dnf list bind

4. 로그 파일 관리
4-1. /var/log/messages 파일의 최신(마지막) 내용 15줄만 출력하여 확인
: tail -15 /var/log/messages

5. 백업 및 복구 관리
   - rsync server의 IP : 192.168.10.11
   - rsync server의 서비스명 : backup
5-1. Client에서 rsync server의 backup을 /home/backup으로 동기화하기
: rsync -avuz 192.168.10.11::backup /home/backup

5-2. 5-1의 작업을 매일 23시 59분에 자동으로 작업하기위해서 crontab에 추가할 명령어
: 59 23 * * * rsync -avuz 192.168.10.11::backup /home/backup


SQL 테스트















"""