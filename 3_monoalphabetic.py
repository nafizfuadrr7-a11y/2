import random, string

alphabet = list(string.ascii_uppercase)
shuffled = alphabet.copy()
random.shuffle(shuffled)
enc_map = dict(zip(alphabet, shuffled))
dec_map = dict(zip(shuffled, alphabet))

def mono_encrypt(text):
    return ''.join(enc_map.get(c, c) for c in text.upper())

def mono_decrypt(text):
    return ''.join(dec_map.get(c, c) for c in text.upper())

msg = "HELLO WORLD"
enc = mono_encrypt(msg)
dec = mono_decrypt(enc)

print("Key map:", enc_map)
print("Original:", msg)
print("\nEncrypted:", enc)
print("\nDecrypted:", dec)

