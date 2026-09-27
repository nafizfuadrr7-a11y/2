import math

# --- Helper Functions ---

def gcd(a, b):
    """
    Calculates the Greatest Common Divisor (GCD) of two numbers.
    This is needed to select 'e'.
    """
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """
    Finds the modular multiplicative inverse of e mod phi.
    This is needed to calculate 'd' (the private key). (d = e^-1 mod phi)
    """
    # In Python 3.8+, this can be done in one line: pow(e, -1, phi)
    # We are using a basic algorithm here for clarity.
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("Modular inverse does not exist.")


# --- Main RSA Algorithm ---

# Step 1: Key Generation (for Alice)
def generate_keys(p, q):
    """
    Generates a public and private key pair based on the steps in the image.
    """
    # 'p' and 'q' must be prime and not equal to each other.
    if p == q:
        raise ValueError("p and q must be distinct prime numbers.")

    # Calculate n = p * q
    n = p * q
    
    # Calculate φ(n) = (p-1) * (q-1) (phi of n)
    phi_n = (p - 1) * (q - 1)
    
    # Select an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1.
    e = 2
    while e < phi_n:
        if gcd(e, phi_n) == 1:
            break
        e += 1
    
    # Calculate d where d = e^-1 mod φ(n)
    d = mod_inverse(e, phi_n)
    
    # Public key (PU) = {e, n}
    # Private key (PR) = {d, n}
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key, phi_n


# Step 2: Encryption (by Bob with Alice's Public Key)
def encrypt(public_key, plaintext_message):
    """
    Encrypts a plaintext message into a ciphertext.
    Formula: C = M^e mod n
    """
    e, n = public_key
    
    # Apply the encryption formula
    ciphertext = pow(plaintext_message, e, n)
    
    return ciphertext


# Step 3: Decryption (by Alice with her Private Key)
def decrypt(private_key, ciphertext):
    """
    Decrypts a ciphertext back into the original plaintext message.
    Formula: M = C^d mod n
    """
    d, n = private_key
    
    # Apply the decryption formula
    plaintext_message = pow(ciphertext, d, n)
    
    return plaintext_message


# --- Main Program Execution ---
if __name__ == "__main__":
    # --- Key Generation ---
    # Select two prime numbers (in a real scenario, these would be very large)
    p = 17
    q = 11
    
    print(f"Selected prime numbers: p = {p}, q = {q}")
    
    public_key, private_key, phi = generate_keys(p, q)
    
    e, n = public_key
    d, _ = private_key # n is the same, so we ignore it with _
    
    print(f"Calculated n (p*q) = {n}")
    print(f"Calculated φ(n) = {phi}")
    print(f"Selected e = {e}")
    print(f"Calculated d = {d}")
    print("-" * 30)
    print(f"Public Key (PU): {{e, n}} = {public_key}")
    print(f"Private Key (PR): {{d, n}} = {private_key}")
    print("-" * 30)

    # --- Encryption and Decryption ---
    # The message to be encrypted (as a number).
    # Condition: The message (M) must be less than n.
    message = 123
    
    print(f"Original Message (M): {message}")
    
    # Encryption: Bob uses Alice's public key
    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted Message (C): {encrypted_message}")
    
    # Decryption: Alice uses her private key
    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Decrypted Message (M): {decrypted_message}")
    
    # Verification
    if message == decrypted_message:
        print("\nSuccess: Encryption and decryption were completed successfully!")
    else:
        print("\nError: Something went wrong!")