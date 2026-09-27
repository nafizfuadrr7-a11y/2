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

msg = input("Enter a message: ")
enc = caesar_encrypt(msg, 4)
dec = caesar_decrypt(enc, 4)
print("Original:", msg)
print("Encrypted:", enc)
print("Decrypted:", dec)