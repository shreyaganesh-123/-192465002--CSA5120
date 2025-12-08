
# -------------------------------
# ECB, CBC, and CFB modes demo
# Block size = 8 bytes (64 bits) for simplicity
# -------------------------------

def pad(plaintext, block_size):
    """
    Pad plaintext to a multiple of block_size using 1-bit + zeros
    """
    n = len(plaintext)
    pad_len = block_size - (n % block_size)
    if pad_len == 0:
        pad_len = block_size  # always add padding even if exact multiple
    return plaintext + bytes([0x80] + [0]*(pad_len-1))

def split_blocks(data, block_size):
    return [data[i:i+block_size] for i in range(0, len(data), block_size)]

# --- Simple XOR block cipher for demonstration ---
def simple_encrypt_block(block, key):
    return bytes([b ^ k for b, k in zip(block, key)])

def simple_decrypt_block(block, key):
    return bytes([b ^ k for b, k in zip(block, key)])

# --- ECB Mode ---
def ecb_encrypt(plaintext, key):
    blocks = split_blocks(plaintext, len(key))
    return b''.join([simple_encrypt_block(b, key) for b in blocks])

def ecb_decrypt(ciphertext, key):
    blocks = split_blocks(ciphertext, len(key))
    return b''.join([simple_decrypt_block(b, key) for b in blocks])

# --- CBC Mode ---
def cbc_encrypt(plaintext, key, iv):
    blocks = split_blocks(plaintext, len(key))
    ciphertext = []
    prev = iv
    for b in blocks:
        x = bytes([a ^ b for a, b in zip(b, prev)])
        c = simple_encrypt_block(x, key)
        ciphertext.append(c)
        prev = c
    return b''.join(ciphertext)

def cbc_decrypt(ciphertext, key, iv):
    blocks = split_blocks(ciphertext, len(key))
    plaintext = []
    prev = iv
    for c in blocks:
        x = simple_decrypt_block(c, key)
        p = bytes([a ^ b for a, b in zip(x, prev)])
        plaintext.append(p)
        prev = c
    return b''.join(plaintext)

# --- CFB Mode ---
def cfb_encrypt(plaintext, key, iv):
    blocks = split_blocks(plaintext, len(key))
    ciphertext = []
    prev = iv
    for b in blocks:
        s = simple_encrypt_block(prev, key)
        c = bytes([a ^ b for a, b in zip(s, b)])
        ciphertext.append(c)
        prev = c
    return b''.join(ciphertext)

def cfb_decrypt(ciphertext, key, iv):
    blocks = split_blocks(ciphertext, len(key))
    plaintext = []
    prev = iv
    for c in blocks:
        s = simple_encrypt_block(prev, key)
        p = bytes([a ^ b for a, b in zip(s, c)])
        plaintext.append(p)
        prev = c
    return b''.join(plaintext)

# ---------------------------
# Example Usage
# ---------------------------
plaintext = b"HELLO ECB CBC CFB MODES"
block_size = 8  # bytes
key = b"KEYBLOCK"  # 8 bytes key
iv = b"\x00"*8     # simple IV

# Pad plaintext
padded = pad(plaintext, block_size)

# Encrypt & Decrypt
ecb_ct = ecb_encrypt(padded, key)
ecb_pt = ecb_decrypt(ecb_ct, key)

cbc_ct = cbc_encrypt(padded, key, iv)
cbc_pt = cbc_decrypt(cbc_ct, key, iv)

cfb_ct = cfb_encrypt(padded, key, iv)
cfb_pt = cfb_decrypt(cfb_ct, key, iv)

print("Original plaintext:", plaintext)
print("Padded plaintext  :", padded)
print("\n--- ECB ---")
print("Ciphertext:", ecb_ct)
print("Decrypted :", ecb_pt)
print("\n--- CBC ---")
print("Ciphertext:", cbc_ct)
print("Decrypted :", cbc_pt)
print("\n--- CFB ---")
print("Ciphertext:", cfb_ct)
print("Decrypted :", cfb_pt)
