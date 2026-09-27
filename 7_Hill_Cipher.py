import numpy as np

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def hill_encrypt(text, key_matrix):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    result = ""
    for i in range(0, len(text), 2):
        pair = np.array([ord(text[i])-65, ord(text[i+1])-65])
        enc = np.dot(key_matrix, pair) % 26
        result += chr(enc[0]+65) + chr(enc[1]+65)
    return result

def hill_decrypt(cipher, key_matrix):
    det = int(round(np.linalg.det(key_matrix)))
    det_inv = mod_inverse(det, 26)
    adj = np.array([[key_matrix[1][1], -key_matrix[0][1]],
                     [-key_matrix[1][0], key_matrix[0][0]]])
    inv_matrix = (det_inv * adj) % 26
    result = ""
    for i in range(0, len(cipher), 2):
        pair = np.array([ord(cipher[i])-65, ord(cipher[i+1])-65])
        dec = np.dot(inv_matrix, pair) % 26
        result += chr(int(dec[0])+65) + chr(int(dec[1])+65)
    return result

key_matrix = np.array([[3, 3], [2, 5]])
msg = "HELP"
enc = hill_encrypt(msg, key_matrix)
dec = hill_decrypt(enc, key_matrix)
print("Encrypted:", enc)
print("Decrypted:", dec)
