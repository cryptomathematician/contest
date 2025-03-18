numbers = list(map(int, input().split()))

k= numbers[0]
n= numbers[1]
w= numbers[2]

m= (w*(k+w*k)//2) - n

if m <= 0:
    print(0)
else:
    print(m)
