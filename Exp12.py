import string

ALPHABET = string.ascii_lowercase
char_to_num = {ch: i for i, ch in enumerate(ALPHABET)}
num_to_char = {i: ch for i, ch in enumerate(ALPHABET)}

def clean(text):
    return ''.join(ch for ch in text.lower() if ch in ALPHABET)

def pad_even(text):
    return text if len(text) % 2 == 0 else text + 'x'

def mat_mul_2x2_vec(K, v):
    return [(K[0][0]*v[0] + K[0][1]*v[1]) % 26,
            (K[1][0]*v[0] + K[1][1]*v[1]) % 26]

def text_to_pairs_nums(text):
    nums = [char_to_num[ch] for ch in text]
    return [(nums[i], nums[i+1]) for i in range(0, len(nums), 2)]

def nums_pairs_to_text(pairs):
    return ''.join(num_to_char[a] + num_to_char[b] for a, b in pairs)

def encrypt(plain, K):
    pairs = text_to_pairs_nums(plain)
    c_pairs = [tuple(mat_mul_2x2_vec(K, list(p))) for p in pairs]
    return nums_pairs_to_text(c_pairs)

def decrypt(cipher, K_inv):
    pairs = text_to_pairs_nums(cipher)
    p_pairs = [tuple(mat_mul_2x2_vec(K_inv, list(p))) for p in pairs]
    return nums_pairs_to_text(p_pairs)

# Given key
K = [[9, 4],
     [5, 7]]

# Precomputed inverse modulo 26: [[5,12],[15,25]]
K_inv = [[5, 12],
         [15, 25]]

plaintext = "meet me at the usual place at ten rather than eight oclock"
pt = pad_even(clean(plaintext))

ciphertext = encrypt(pt, K)
recovered = decrypt(ciphertext, K_inv)

print("Sanitized plaintext:", pt)
print("Ciphertext:", ciphertext)
print("Decrypted:", recovered)
