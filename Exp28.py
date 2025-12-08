def wrong_dh(a, q, x, y):
    # Alice sends x^a mod q
    A = pow(x, a, q)
    # Bob sends y^a mod q
    B = pow(y, a, q)

    # Alice computes supposed key
    KA = pow(B, x, q)
    # Bob computes supposed key
    KB = pow(A, y, q)

    return A, B, KA, KB

a = 5
q = 23
x = 6  # Alice's secret
y = 15 # Bob's secret

A, B, KA, KB = wrong_dh(a, q, x, y)

print("Alice sends:", A)
print("Bob sends:", B)
print("Alice computes key:", KA)
print("Bob computes key:", KB)
print("Do keys match?", KA == KB)
