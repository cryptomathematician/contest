
t = int(input())
results = []
for _ in range(t):
    k= int(input())
    n = list(map(int, input().split()))
    r= sorted(n)
    if n == r :
        print('NO')
    else:
        print('YES')