
import random
import string

def generate_key(length):
    """Generate a random key: list of integers 0-26"""
    return [random.randint(0, 26) for _ in range(length)]

def encrypt(plaintext, key):
    """Encrypt plaintext using one-time pad Vigenère cipher"""
    plaintext = plaintext.upper()
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char in string.ascii_uppercase:
            shift = key[i]
            cipher_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += cipher_char
        else:
            ciphertext += char  # keep non-letter as is
    return ciphertext

def decrypt(ciphertext, key):
    """Decrypt ciphertext using one-time pad Vigenère cipher"""
    plaintext = ""
    for i, char in enumerate(ciphertext):
        if char in string.ascii_uppercase:
            shift = key[i]
            plain_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += plain_char
        else:
            plaintext += char
    return plaintext

# --------------------------
# Example usage
# --------------------------
plaintext = "MEET ME AT NOON"
key = generate_key(len(plaintext))

ciphertext = encrypt(plaintext, key)
decrypted = decrypt(ciphertext, key)

print("Plaintext :", plaintext)
print("Random Key:", key)
print("Ciphertext:", ciphertext)
print("Decrypted :", decrypted)

