from collections import Counter
a = list(map(int, input().split()))
b = list(map(int, input().split()))
first = dict(Counter(a))
second = dict(Counter(b))
print(all(second[char] <= first[char] for char in second))