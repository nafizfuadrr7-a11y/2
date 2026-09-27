import random, string

def generate_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
def otp_encrypt(text, key):
    return''.join(chr((ord(t)-65+ord(k)-65)%26+65) for t,k in zip(text.upper(),key))
def otp_decrypt(cipher, key):
    return''.join(chr((ord(c)-ord(k))%26+65) for c,k in zip(cipher,key))

msg = input("Enter a message for OTP encryption: ")
key = generate_key(len(msg))
enc = otp_encrypt(msg, key)
dec = otp_decrypt(enc, key)
print("Key:", key)
print("Encrypted:", enc)
print("Decrypted:", dec)

