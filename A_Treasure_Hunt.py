t = int(input())  
for _ in range(t):
    x, y, a = map(int, input().split())


    full_cycles = a // (x + y)

    remaining = a - full_cycles * (x + y)
  

    
    if remaining < x:
        print("NO")
    else:
        print("YES")

 