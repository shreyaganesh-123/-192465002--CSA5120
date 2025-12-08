def generate_matrix(keyword):
    keyword = keyword.lower().replace("j", "i")
    matrix = []
    used = set()

    for ch in keyword:
        if ch not in used and ch.isalpha():
            used.add(ch)
            matrix.append(ch)

    for ch in "abcdefghiklmnopqrstuvwxyz":  # j removed
        if ch not in used:
            used.add(ch)
            matrix.append(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return None


def playfair_encrypt(plaintext, keyword):
    matrix = generate_matrix(keyword)
    plaintext = plaintext.lower().replace("j", "i")
    new_text = ""

    # Prepare digraphs
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i+1] if i+1 < len(plaintext) else 'x'
        if a == b:
            b = 'x'
            i += 1
        else:
            i += 2
        new_text += a + b

    cipher = ""
    for i in range(0, len(new_text), 2):
        a, b = new_text[i], new_text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # same row
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:  # same column
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]
        else:  # rectangle
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


# ---- MAIN ----
plaintext = input("Enter plaintext: ")
keyword = input("Enter keyword: ")

cipher = playfair_encrypt(plaintext, keyword)
print("Encrypted:", cipher)

