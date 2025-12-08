import random
import string

# Function to generate random key for OTP
def generate_key(length):
    return [random.randint(0, 25) for _ in range(length)]

# Function to encrypt using One-Time Pad Vigenere
def otp_encrypt(plaintext, key):
    plaintext = plaintext.lower().replace(" ", "")
    ciphertext = ""

    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('a')
        c = (p + key[i]) % 26
        ciphertext += chr(c + ord('a'))
    return ciphertext

# Function to decrypt
def otp_decrypt(ciphertext, key):
    plaintext = ""

    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('a')
        p = (c - key[i]) % 26
        plaintext += chr(p + ord('a'))
    return plaintext

# ----------- MAIN PROGRAM -----------

plaintext = "attack at once"

# Remove spaces
pt = plaintext.replace(" ", "")

# Generate key (same length as plaintext)
key = generate_key(len(pt))

cipher = otp_encrypt(pt, key)
decrypted = otp_decrypt(cipher, key)

print("Plaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", cipher)
print("Decrypted :", decrypted)

