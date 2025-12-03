def monoalphabetic(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            pos = ord(ch.lower()) - ord('a')
            new = key[pos]
            result += new if ch.islower() else new.upper()
        else:
            result += ch
    return result

key = "qwertyuiopasdfghjklzxcvbnm"   # define your substitution alphabet

text = input("Enter text: ")
print("Encrypted:", monoalphabetic(text, key))
