# VERY SIMPLE DES DECRYPTION DEMO (Keys reversed)

shifts = [1,1,2,2,2,2,2,2, 1,2,2,2,2,2,2,1]

def left_shift(s, n):
    return s[n:] + s[:n]

def gen_keys(key):
    C, D = key[:28], key[28:]
    keys = []
    for s in shifts:
        C = left_shift(C, s)
        D = left_shift(D, s)
        keys.append(C + D)      # simplified PC2
    return keys

def F(r, k):
    return ''.join('1' if r[i] != k[i] else '0' for i in range(32))  # simple XOR

def des_decrypt(cipher, key):
    keys = gen_keys(key)[::-1]   # REVERSE ORDER for decryption
    L, R = cipher[:32], cipher[32:]
    for k in keys:
        L, R = R, ''.join('1' if L[i] != F(R, k)[i] else '0' for i in range(32))
    return R + L                 # final swap

cipher = "1100110011001100110011001100110011001100110011001100110011001100"
key    = "0"*56  # simple 56-bit key

plain = des_decrypt(cipher, key)
print("Decrypted plaintext:", plain)
