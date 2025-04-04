from math import ceil
from collections import Counter

n= int(input())
numbers = list(map(int, input().split()))

e = Counter(numbers)
u = max(e.values())

r = set(numbers)

j = list(r)


print(f"{u} {len(j)}")