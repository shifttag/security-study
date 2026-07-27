# 알파벳 기준 Vigenere 암호
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def extend_key(text, key):
    key = key.upper()
    return (key * ((len(text) // len(key)) + 1))[:len(text)]


def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = extend_key(plaintext, key)

    ciphertext = ""

    for p, k in zip(plaintext, key):
        # 평문 문자 위치 + 키 문자 위치
        p_index = ALPHABET.index(p)
        k_index = ALPHABET.index(k)

        c_index = (p_index + k_index) % 26
        ciphertext += ALPHABET[c_index]

    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = extend_key(ciphertext, key)

    plaintext = ""

    for c, k in zip(ciphertext, key):
        # 암호문 문자 위치 - 키 문자 위치
        c_index = ALPHABET.index(c)
        k_index = ALPHABET.index(k)

        p_index = (c_index - k_index) % 26
        plaintext += ALPHABET[p_index]

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