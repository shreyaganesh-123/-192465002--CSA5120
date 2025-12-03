def keyword_cipher_encrypt(plain, keyword="CIPHER"):
    keyword = "".join(dict.fromkeys(keyword.lower()))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = keyword + "".join(c for c in alphabet if c not in keyword)
    table = {a:c for a,c in zip(alphabet, cipher)}
    return "".join(table.get(ch, ch) for ch in plain.lower())

print("Cipher Text:", keyword_cipher_encrypt("attack at dawn"))
