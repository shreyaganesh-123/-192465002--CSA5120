# DES Key Scheduling Demo
# Each subkey = 24 bits from C + 24 bits from D (disjoint halves)

shifts = [1,1,2,2,2,2,2,2, 1,2,2,2,2,2,2,1]

def left_shift(b, n):
    return b[n:] + b[:n]

def generate_subkeys(key56):
    C = key56[:28]     # first 28 bits
    D = key56[28:]     # last 28 bits
    subkeys = []

    for s in shifts:
        C = left_shift(C, s)
        D = left_shift(D, s)

        # FIRST 24 bits from C (subset of its 28 bits)
        # SECOND 24 bits from D (subset of its 28 bits)
        K = C[:24] + D[:24]

        subkeys.append(K)
    return subkeys

# Example 56-bit key
key = "01100011011000110110001101100011011000110110001101100011"

keys = generate_subkeys(key)
for i, k in enumerate(keys, 1):
    print(f"K{i:02d} = {k}")
