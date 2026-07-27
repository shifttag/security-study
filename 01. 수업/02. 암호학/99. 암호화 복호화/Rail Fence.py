import math


def encrypt(plain_text, depth):
    plain_text = plain_text.replace(" ", "").lower()

    columns = math.ceil(len(plain_text) / depth)

    padding = depth * columns - len(plain_text)

    plain_text += "x" * padding

    matrix = []

    index = 0

    for row in range(depth):
        current_row = []

        for col in range(columns):
            current_row.append(plain_text[index])
            index += 1

        matrix.append(current_row)

    cipher_text = ""

    for col in range(columns):
        for row in range(depth):
            cipher_text += matrix[row][col]

    return cipher_text


def decrypt(cipher_text, depth):
    length = len(cipher_text)

    columns = length // depth

    matrix = [[""] * columns for _ in range(depth)]

    index = 0

    for col in range(columns):
        for row in range(depth):
            matrix[row][col] = cipher_text[index]
            index += 1

    plain_text = ""

    for row in range(depth):
        for col in range(columns):
            plain_text += matrix[row][col]

    return plain_text.rstrip("x")


# -------------------------
# 실행
# -------------------------

depth = int(input("깊이 입력: "))

mode = input("암호화(e) / 복호화(d): ")

if mode == "e":
    plain_text = input("평문 입력: ")
    print("암호문:", encrypt(plain_text, depth))

elif mode == "d":
    cipher_text = input("암호문 입력: ")
    print("복호문:", decrypt(cipher_text, depth))

else:
    print("잘못된 입력입니다.")