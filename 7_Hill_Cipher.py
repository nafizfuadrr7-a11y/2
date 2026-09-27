import numpy as np

def mod_inverse(a, m):
    """Find modular inverse of a under modulo m (used for decryption)."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"
    text_vector = [ord(c) - 65 for c in text]
    cipher = ""
    for i in range(0, len(text_vector), 2):
        pair = np.dot(key, text_vector[i:i + 2]) % 26
        cipher += "".join(chr(num + 65) for num in pair)
    return cipher

def hill_decrypt(ciphertext, key):
    det = int(round(np.linalg.det(key))) % 26
    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        raise ValueError("Key matrix is not invertible under modulo 26.")
    
    # Compute inverse key matrix under mod 26
    key_inv = (
        det_inv * np.round(det * np.linalg.inv(key)).astype(int)
    ) % 26

    cipher_vector = [ord(c) - 65 for c in ciphertext]
    plain = ""
    for i in range(0, len(cipher_vector), 2):
        pair = np.dot(key_inv, cipher_vector[i:i + 2]) % 26
        plain += "".join(chr(int(num) + 65) for num in pair)
    return plain

# User input
text = input("Enter plaintext: ")

print("Enter 2x2 key matrix:")
a = int(input("Enter key[0][0]: "))
b = int(input("Enter key[0][1]: "))
c = int(input("Enter key[1][0]: "))
d = int(input("Enter key[1][1]: "))
key = np.array([[a, b], [c, d]])

# Encrypt and decrypt
encrypted = hill_encrypt(text, key)
decrypted = hill_decrypt(encrypted, key)

print("\nKey Matrix:\n", key)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
