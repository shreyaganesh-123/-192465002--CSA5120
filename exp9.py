import re

def playfair_matrix(key):
    key = key.upper().replace("J","I")
    seen = set()
    seq = [ch for ch in key if ch.isalpha() and ch not in seen and not seen.add(ch)]
    seq += [ch for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ" if ch not in seen]
    return [seq[i:i+5] for i in range(0,25,5)]

def pos(matrix,ch):
    for r,row in enumerate(matrix):
        if ch in row: return r,row.index(ch)

def clean_text(text):
    return [ch.upper().replace("J","I") if ch.isalpha() else ch for ch in text]

def remove_filler_x(text):
    text = re.sub(r'([A-Z])X([A-Z])', r'\1\2', text)
    text = re.sub(r'X(\s|$)', r'\1', text)
    return text

def playfair_decrypt(cipher,key):
    arr = clean_text(cipher)
    M = playfair_matrix(key)
    pt,i = "",0

    while i < len(arr):
        if not arr[i].isalpha():
            pt += arr[i]; i+=1; continue
        a = arr[i]
        j = i+1
        while j < len(arr) and not arr[j].isalpha():
            pt += arr[j]; j+=1
        if j>=len(arr): break
        b = arr[j]
        r1,c1 = pos(M,a); r2,c2 = pos(M,b)

        if r1==r2:
            pt += M[r1][(c1-1)%5] + M[r2][(c2-1)%5]
        elif c1==c2:
            pt += M[(r1-1)%5][c1] + M[(r2-1)%5][c2]
        else:
            pt += M[r1][c2] + M[r2][c1]
        i = j+1

    return remove_filler_x(pt)

cipher = """KX IEYU REB EZW EHEW RYTU HE YFSKR EH EGOYFIWU QUTQYO MUQ YCAIP OBOOEXUKN BOUKNO BOTF RBWB ONEYCU ZWRGNON SSZ TURZOKZVYOUZSKRE"""
print(playfair_decrypt(cipher, "royal new zealand navy"))
