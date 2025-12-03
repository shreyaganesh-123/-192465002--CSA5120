# Playfair Cipher
def generate_matrix(keyword):
    keyword = keyword.lower().replace("j","i")
    used = set()
    matrix = [ch for ch in keyword if ch.isalpha() and ch not in used and not used.add(ch)]
    matrix += [ch for ch in "abcdefghiklmnopqrstuvwxyz" if ch not in used]
    return [matrix[i:i+5] for i in range(0,25,5)]

def find_pos(matrix,ch):
    for i,row in enumerate(matrix):
        if ch in row: return i,row.index(ch)

def playfair_encrypt(pt, key):
    m = generate_matrix(key)
    pt = pt.lower().replace("j","i")
    digraphs, i = "", 0
    while i < len(pt):
        a = pt[i]; b = pt[i+1] if i+1<len(pt) else "x"
        if a==b: b="x"; i+=1
        else: i+=2
        digraphs += a+b
    c = ""
    for i in range(0,len(digraphs),2):
        a,b = digraphs[i],digraphs[i+1]
        r1,c1 = find_pos(m,a); r2,c2 = find_pos(m,b)
        if r1==r2: c+=m[r1][(c1+1)%5]+m[r2][(c2+1)%5]
        elif c1==c2: c+=m[(r1+1)%5][c1]+m[(r2+1)%5][c2]
        else: c+=m[r1][c2]+m[r2][c1]
    return c

# Vigenere Cipher
def vigenere_encrypt(pt,key):
    pt,key = pt.lower(), key.lower()
    c,k = "",0
    for ch in pt:
        if ch.isalpha():
            shift = ord(key[k%len(key)])-ord('a')
            c += chr((ord(ch)-ord('a')+shift)%26 + ord('a')); k+=1
        else: c+=ch
    return c

# ---- MAIN ----
pt = input("Enter plaintext: ")
key = input("Enter keyword/key: ")
print("Playfair Encrypted:", playfair_encrypt(pt,key))
print("Vigenere Encrypted:", vigenere_encrypt(pt,key))
