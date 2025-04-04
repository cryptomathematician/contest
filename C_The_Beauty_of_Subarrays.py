t = int(input())
for _ in range(t):
    n= int(input())
    numbers = list(map(int, input().split()))

    k = [0] * (n+1)

    for i in range(n):
        k[numbers[i]] = i


    result = []

    r = j = k[1]

    for m in range(1,n+1):
        r= min(r, k[m])
        j= max(j, k[m])

        if j-r+1 == m:
            result.append('1')
        else:
            result.append('0')
    print("".join(result))
