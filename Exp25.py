import math

# Suppose RSA modulus (unknown factors)
n = 3599    # = 59 * 61
e = 31

# Attacker receives ciphertext blocks, but also learns that
# one plaintext block has a common factor with n.
# Let's simulate such a plaintext:
m_bad = 59     # shares a factor with n

# Attacker computes gcd(m_bad, n)
g = math.gcd(m_bad, n)

print("gcd =", g)

if 1 < g < n:
    print("Non-trivial factor of n found:", g)
    p = g
    q = n // g
    print("p =", p)
    print("q =", q)

    # Compute phi(n)
    phi = (p - 1) * (q - 1)
    print("phi(n) =", phi)

    # Compute private key using modular inverse
    def egcd(a, b):
        if b == 0:
            return (a, 1, 0)
        g, x1, y1 = egcd(b, a % b)
        return (g, y1, x1 - (a // b) * y1)

    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise ValueError("Inverse does not exist")
        return x % m

    d = modinv(e, phi)
    print("Recovered private key d =", d)

else:
    print("No help; gcd=1, plaintext is normal.")
