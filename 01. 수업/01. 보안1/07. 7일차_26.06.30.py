"""
NOS
: 라우터나 스위치에 들어있는 OS

Cisco Packet Tracer 사용
GUI만들다 포기 웹 통합해서 만들다보면 괜찮음
명령어 직접 입력하는 CLI 방식 사용
단점 - 명령어 다 외우거나 정리해서 써둬야함

리눅스 명령어
tar를 이용한 증분 백업
# tar [옵션] [압축파일명] -g [백업정보 파일] [대상]
ex) tar cvfz home_full.gz -g /backup/home_backup /home
ex) tar cvfz home_l1.gz -g /backup/home_backup /home
ex) tar cvfz home_.gz -g /backup/home_backup /home
: 파일의 상태정보를 저장
: 파일이 바뀌면 다시 백업을 해야하는데 해시코드의 차이를 보고 
  파일이 바꼇다를 인식

cat /etc/shadow
root:$6$jiFAnDjW66KGNyoa$3cQgKYzeFcCfX7/dFWOFIak5yaNjyYFR6t13TRiuD9rckHVUOloAmju5erpjegNI1bVGIcLfDzZqDhxvfl1XR/::0:99999:7:::

해시함수로 인해 바뀐 password이다
해시함수는 복호화가 불가능하다

vi 에디터
# vi [파일명]

자주쓰는 명령

명령모드에서 삽입모드로 변경
- i : 커서 위치부터 입력
- o : 커서 아래 새로운 라인을 삽입하고 입력

명령모드
- gg : 문서 맨 처음으로 이동
- G : 문서 맨 아래로 이동
- Ctrl + f, Ctrl + b, Ctrl + d, Ctrl + u : 화면단위 이동
- x : 글자 삭제
- dd : 라인 삭제

실행모드
- :wq : 저장 후 종료
- :q! : 저장하지 않고 종료

cmd창에서 
scp [보낼파일 경로] 계정@주소:[받을 경로]








"""