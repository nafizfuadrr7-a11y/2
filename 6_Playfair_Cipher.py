import string
def playfair_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix = []
    for c in key + string.ascii_uppercase:
        if c not in seen and c != 'J':
            seen.add(c)
            matrix.append(c)
    return [matrix[i*5:i*5+5] for i in range(5)]

def find_pos(matrix, c):
    for i, row in enumerate(matrix):
        if c in row:
            return i, row.index(c)

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs

def playfair_encrypt(text, key):
    matrix = playfair_matrix(key)
    pairs = prepare_text(text)
    result = ""
    for pair in pairs:
        r1, c1 = find_pos(matrix, pair[0])
        r2, c2 = find_pos(matrix, pair[1])
        if r1 == r2:
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

def playfair_decrypt(cipher, key):
    matrix = playfair_matrix(key)
    result = ""
    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)
        if r1 == r2:
            result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

key = "MONARCHY"
msg = "INSTRUMENTS"
enc = playfair_encrypt(msg, key)
dec = playfair_decrypt(enc, key)
print("Key:", key)
print("Encrypted:", enc)
print("Decrypted:", dec)
