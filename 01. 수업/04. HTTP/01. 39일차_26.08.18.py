"""
각각의 페이지에 ip할당하면 현실적 한계점
: IP의 한계

Web 서버
192.168.10.33
- www.ast.sec
- www.ast.itc

DNS 서버
www.ast.sec : 192.168.10.33
www.ast.itc : 192.168.10.33

26.08.18자 영상 참조






INSERT INTO emp (eno, ename, sex, job, mgr, hdate, sal, comm, dno)
VALUES ('1001', '문시현', '남', '모델링', NULL, '1991/02/01', 4500, 520, '10');
INSERT INTO emp (eno, ename, sex, job, mgr, hdate, sal, comm, dno)
VALUES ('1002', '김주란', '여', '모델링', NULL, '1992/03/03', 4100, 330, '20');
INSERT INTO emp (eno, ename, sex, job, mgr, hdate, sal, comm, dno)
VALUES ('1003', '양선호', '남', '모델링', NULL, '1995/02/21', 4300, NULL, '30');

ALTER SESSION SET nls_date_format='YYYY/MM/DD:HH24:MI:SS';
INSERT INTO emp (eno, ename, hdate)
VALUES ('0001', '안영희', '2021/09/25:03:07:15');
INSERT INTO emp (eno, ename, hdate)
VALUES ('0202', '손하늘', '2021/09/25');

ALTER SESSION SET nls_date_format='YYYY/MM/DD';
INSERT INTO emp (eno, ename, hdate)
VALUES ('0201', '안영숙', '2021/09/25:03:07:15');
INSERT INTO emp (eno, ename, hdate)
VALUES ('0201', '안영숙', TO_DATE('2021/09/25:03:07:15',
'YYYY/MM/DD:HH24:MI:SS'));

INSERT INTO emp (eno,hdate)
VALUES ('01', TO_DATE('2000', 'YYYY'));
INSERT INTO emp (eno,hdate)
VALUES ('02', TO_DATE('99', 'YY'));
INSERT INTO emp (eno,hdate)
VALUES ('03', TO_DATE('99', 'RR'));
INSERT INTO emp (eno,hdate)
VALUES ('04', sysdate);
SELECT * FROM emp
WHERE eno IN ('01','02','03','04','05');













"""