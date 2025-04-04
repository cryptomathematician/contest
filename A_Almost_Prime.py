import math

def is_prime(w):
    if w < 2:
        return False
    if w == 2:
        return True
    if w % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(w)) + 1, 2):
        if w % i == 0:
            return False
    return True

print(is_prime(w= 2 ))




