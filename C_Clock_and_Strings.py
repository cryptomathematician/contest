number_of = int(input())
for _ in range(number_of):
    numbers = list(map(int, input().split()))
    a= int(numbers[0]) 
    b=int(numbers[1])
    c= int(numbers[2])
    d= int(numbers[3])


   
    w = (b - a) % 12
    k = (c - a) % 12
    m = (d - a) % 12
    
    if (0 < k < w) != (0 < m < w):
        print("YES")
    else:
        print("NO")


print((0 < k < w))

