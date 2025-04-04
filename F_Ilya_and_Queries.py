
s = input().strip()
n = len(s)


p = [0] * n  
for i in range(1, n):
    p[i] = p[i - 1] + (1 if s[i] == s[i - 1] else 0)

m = int(input().strip())
for _ in range(m):
    l, r = map(int, input().split())
    print(p[r - 1] - p[l - 1])
