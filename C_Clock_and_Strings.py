number_of = int(input())
for _ in range(number_of):
    a,b,c,d = list(map(int, input().split()))
    w = (b - a) % 12
    k = (c - a) % 12
    m = (d - a) % 12
    
    if (0 < k < w) != (0 < m < w):
        print("YES")
    else:
        print("NO")



