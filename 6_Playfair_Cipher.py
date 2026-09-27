import numpy as np

def generate_key_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = "".join(dict.fromkeys(key + alphabet))
    return np.array(list(matrix)).reshape(5, 5)

def find_position(matrix, char):
    result = np.where(matrix == char)
    return result[0][0], result[1][0]

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    i = 0
    new_text = ""
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        if a == b:
            new_text += a + "X"
            i += 1
        else:
            new_text += a + b
            i += 2
    if len(new_text) % 2 != 0:
        new_text += "X"
    return new_text

def encrypt_playfair(text, matrix):
    text = prepare_text(text)
    ciphertext = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            ciphertext += matrix[r1, (c1+1)%5] + matrix[r2, (c2+1)%5]
        elif c1 == c2:
            ciphertext += matrix[(r1+1)%5, c1] + matrix[(r2+1)%5, c2]
        else:
            ciphertext += matrix[r1, c2] + matrix[r2, c1]
    return ciphertext

def decrypt_playfair(ciphertext, matrix):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            plaintext += matrix[r1, (c1-1)%5] + matrix[r2, (c2-1)%5]
        elif c1 == c2:
            plaintext += matrix[(r1-1)%5, c1] + matrix[(r2-1)%5, c2]
        else:
            plaintext += matrix[r1, c2] + matrix[r2, c1]
    return plaintext

# User input
key = input("Enter the key: ")
text = input("Enter the plaintext: ")

matrix = generate_key_matrix(key)
encrypted = encrypt_playfair(text, matrix)
decrypted = decrypt_playfair(encrypted, matrix)

print("\nKey Matrix:\n", matrix)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
