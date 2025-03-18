from fractions import Fraction
numbers = list(map(int, input().split()))
def mod_inverse(a, mod):
    """Returns the modular inverse of a under modulo mod using Fermat's theorem."""
    return pow(a, mod - 2, mod)

n= numbers[0]
q= numbers[1]

p = (10**-4) * q
frac = Fraction(p).limit_denominator()
w = frac.denominator
m = frac.numerator

inv_w = mod_inverse(w, 998244353)  # w^(-1) mod 998244353
k = (m * inv_w) % 998244353  # Find k using modular multiplication

print(k)