def affine_encrypt(pt, a, b):
    c = ""
    for ch in pt.lower():
        if ch.isalpha():
            c += chr((a*(ord(ch)-97) + b) % 26 + 97)
        else:
            c += ch
    return c

def affine_decrypt(cipher, a, b):
    # modular inverse of a mod 26
    a_inv = next(x for x in range(26) if (a*x)%26==1)
    return "".join(
        chr((a_inv*(ord(ch)-97 - b)) % 26 + 97) if ch.isalpha() else ch
        for ch in cipher
    )

enc = affine_encrypt("hello", 5, 8)
print("Encrypted:", enc)
print("Decrypted:", affine_decrypt(enc, 5, 8))
