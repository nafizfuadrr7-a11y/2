def caesar_encrypt(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = 65 if c.isupper() else 97
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

message=input("Enter a message to encrypt: ")
cipher = caesar_encrypt(message, 9)

def caesar_bruteforce(cipher):
    for shift in range(26):
        print(shift, ":", caesar_decrypt(cipher, shift))

print("Original Message: ", message)
print("Ciphertext:", cipher)
print()
caesar_bruteforce(cipher)
