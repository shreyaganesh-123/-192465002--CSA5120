# Letter-frequency attack for additive (Caesar) cipher

# English letter frequency order (most to least common)
freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQ"

def score(text):
    text = text.upper()
    count = {c: text.count(c) for c in freq_order}
    # Score = sum of rank weights for frequent letters
    return sum((26-i) * count[c] for i, c in enumerate(freq_order))

def decrypt(cipher, shift):
    res = ""
    for ch in cipher:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            res += chr((ord(ch) - base - shift) % 26 + base)
        else:
            res += ch
    return res

ciphertext = input("Enter ciphertext: ")
top_n = int(input("How many top plaintexts? "))

candidates = []
for s in range(26):
    p = decrypt(ciphertext, s)
    candidates.append((score(p), s, p))

# Sort by score (best first)
candidates.sort(reverse=True)

print("\nTop results:\n")
for i in range(top_n):
    print(f"Shift {candidates[i][1]:2d}: {candidates[i][2]}")
