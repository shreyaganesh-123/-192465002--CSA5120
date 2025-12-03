matrix = [
    ['M','F','H','I','K'],
    ['U','N','O','P','Q'],
    ['Z','V','W','X','Y'],
    ['E','L','A','R','G'],
    ['D','S','T','B','C']
]

def pos(c):
    for i,row in enumerate(matrix):
        if c in row: return i,row.index(c)

def playfair_encrypt(text):
    text = [c for c in text.upper().replace("J","I") if c.isalpha()]
    # create digraphs
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1<len(text) and text[i+1]!=a else 'X'
        i += 2 if b!= 'X' else 1
        pairs.append((a,b))
    # encrypt
    cipher = ""
    for a,b in pairs:
        r1,c1 = pos(a); r2,c2 = pos(b)
        if r1==r2: cipher += matrix[r1][(c1+1)%5]+matrix[r2][(c2+1)%5]
        elif c1==c2: cipher += matrix[(r1+1)%5][c1]+matrix[(r2+1)%5][c2]
        else: cipher += matrix[r1][c2]+matrix[r2][c1]
    return cipher

msg = "Must see you over Cadogan West. Coming at once."
print("Plain Text:", msg)
print("Cipher Text:", playfair_encrypt(msg))
