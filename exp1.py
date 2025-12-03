def caesar(text, k):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = 'a' if ch.islower() else 'A'
            result += chr((ord(ch) - ord(base) + k) % 26 + ord(base))
        else:
            result += ch
    return result

text = input("\nEnter text: ")
k = int(input("Enter shift (1–25): "))
print("Encrypted:", caesar(text, k))
