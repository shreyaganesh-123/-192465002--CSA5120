def affine_decrypt(cipher, a, b):
    a_inv = next(x for x in range(26) if (a*x)%26 == 1)
    return "".join(
        chr((a_inv*(ord(ch)-97 - b)) % 26 + 97) if ch.isalpha() else ch
        for ch in cipher.lower()
    )

cipher = "puupvt pu fcvb"
print("Cipher Text:", cipher)
print("Plaintext =", affine_decrypt(cipher, 3, 15))
