# 사각형 행렬 전치 암호

def encrypt(plaintext, key):
    # 공백 제거 및 소문자 변환
    plaintext = plaintext.replace(" ", "").lower()

    # 키를 숫자 리스트로 변환
    key = list(map(int, key.split()))

    # 키의 가장 큰 값 = 열의 개수
    cols = max(key)

    # 열의 개수에 맞게 x로 패딩
    while len(plaintext) % cols != 0:
        plaintext += "x"

    # 행렬 생성
    matrix = []

    for i in range(0, len(plaintext), cols):
        row = list(plaintext[i:i + cols])
        matrix.append(row)

    ciphertext = ""

    # 키 숫자 1부터 순서대로 해당 열을 읽음
    for number in range(1, cols + 1):

        # 현재 숫자가 있는 열 찾기
        col = key.index(number)

        # 해당 열을 위에서 아래로 읽기
        for row in matrix:
            ciphertext += row[col]

    return ciphertext


def decrypt(ciphertext, key):
    # 공백 제거 및 소문자 변환
    ciphertext = ciphertext.replace(" ", "").lower()

    # 키를 숫자 리스트로 변환
    key = list(map(int, key.split()))

    # 키의 가장 큰 값 = 열의 개수
    cols = max(key)

    # 행 개수 계산
    rows = len(ciphertext) // cols

    # 빈 행렬 생성
    matrix = [[""] * cols for _ in range(rows)]

    index = 0

    # 암호화와 같은 순서로 열에 암호문 채우기
    for number in range(1, cols + 1):

        # 현재 숫자가 있는 열 찾기
        col = key.index(number)

        # 위에서 아래로 채우기
        for row in range(rows):
            matrix[row][col] = ciphertext[index]
            index += 1

    plaintext = ""

    # 행 단위로 읽기
    for row in matrix:
        plaintext += "".join(row)

    # 패딩용 x 제거
    plaintext = plaintext.rstrip("x")

    return plaintext


# =========================
# 실행
# =========================

mode = input("암호화(E) / 복호화(D): ").upper()

if mode == "E":

    plaintext = input("평문 입력: ")
    key = input("키 입력: ")

    result = encrypt(plaintext, key)

    print("암호문:", result)


elif mode == "D":

    ciphertext = input("암호문 입력: ")
    key = input("키 입력: ")

    result = decrypt(ciphertext, key)

    print("평문:", result)


else:
    print("잘못된 입력입니다.")