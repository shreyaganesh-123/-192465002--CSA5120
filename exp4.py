def vigenere_encrypt(pt, key):
    pt, key = pt.lower(), key.lower()
    c, k = "", 0
    for ch in pt:
        if ch.isalpha():
            c += chr((ord(ch)-97 + ord(key[k % len(key)])-97) % 26 + 97)
            k += 1
        else:
            c += ch
    return c

# ---- MAIN ----
pt = input("Enter plaintext: ")
key = input("Enter key: ")
print("Encrypted:", vigenere_encrypt(pt, key))
