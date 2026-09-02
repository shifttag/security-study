"""
create table board (
  no NUMBER,
  name VARCHAR2(50),
  sub VARCHAR2(100),
  content VARCHAR2(4000),
  hdate DATE DEFAULT SYSDATE
);

테이블 이름 확인
SELECT * FROM tab;

테이블 생성 확인
SELECT table_name FROM user_tables
WHERE table_name = 'BOARD';


"""